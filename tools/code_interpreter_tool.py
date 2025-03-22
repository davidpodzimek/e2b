import json
import os
from typing import Type

from crewai.tools import BaseTool
from e2b_code_interpreter import Sandbox
from pydantic import BaseModel, Field


class E2BCodeInterpreterSchema(BaseModel):
    """Input schema for the CodeInterpreterTool, used by the agent."""

    code: str = Field(
        ...,
        description="Python3 code used to run in the Jupyter notebook cell. Non-standard packages are installed by appending !pip install [packagenames] and the Python code in one single code block.",
    )


class E2BCodeInterpreterTool(BaseTool):
    """
    This is a tool that runs arbitrary code in a Python Jupyter notebook.
    It uses E2B to run the notebook in a secure cloud sandbox.
    It requires an E2B_API_KEY to create a sandbox.

    Provides file management capabilities to upload datasets and other files to the sandbox.
    """

    name: str = "code_interpreter"
    description: str = "Execute Python code in a Jupyter notebook cell and return any rich data (eg charts), stdout, stderr, and errors."
    args_schema: Type[BaseModel] = E2BCodeInterpreterSchema
    _code_interpreter_tool: Sandbox | None = None
    result_as_answer: bool = False
    dataset_path: str | None = None

    def __init__(
        self, *args, result_as_answer=False, dataset_path: str = None, **kwargs
    ):
        # Call the superclass's init method
        super().__init__(*args, **kwargs)

        self.result_as_answer = result_as_answer

        # Ensure that the E2B_API_KEY environment variable is set
        if "E2B_API_KEY" not in os.environ:
            raise Exception(
                "Code Interpreter tool called while E2B_API_KEY environment variable is not set. Please get your E2B API key here https://e2b.dev/docs and set the E2B_API_KEY environment variable."
            )

        # Initialize the code interpreter tool
        self._code_interpreter_tool = Sandbox(timeout=600)
        self.dataset_path = dataset_path
        if self.dataset_path:
            self.upload_file(self.dataset_path)


    def _run(self, code: str) -> str:
        # Execute the code using the code interpreter
        print(code)
        self._code_interpreter_tool.set_timeout(300)
        execution = self._code_interpreter_tool.run_code(code)

        # Extract relevant execution details
        result = {
            "results": [str(item) for item in execution.results],
            "stdout": execution.logs.stdout,
            "stderr": execution.logs.stderr,
            "error": str(execution.error),
        }

        # Convert the result dictionary to a JSON string since CrewAI expects a string output
        content = json.dumps(result, indent=2)

        return content

    def write(self, filename: str, content) -> str:
        """
        Write content to a file in the sandbox.

        Args:
            filename: The name of the file to write to
            content: The content to write (can be a string, bytes, or file-like object)

        Returns:
            Path to the file in the sandbox
        """
        try:
            # If content is a file-like object (has read method)
            if hasattr(content, "read"):
                content_bytes = content.read()
                if isinstance(content_bytes, str):
                    content_bytes = content_bytes.encode("utf-8")
            # If content is a string, convert to bytes
            elif isinstance(content, str):
                content_bytes = content.encode("utf-8")
            # If content is already bytes, use it directly
            elif isinstance(content, bytes):
                content_bytes = content
            else:
                raise ValueError(f"Unsupported content type: {type(content)}")

            # Write the file to the sandbox
            self._code_interpreter_tool.files.write(filename, content_bytes)

            # Return the path to the file in the sandbox
            return filename
        except Exception as e:
            print(f"Error writing file to sandbox: {e}")
            raise

    def upload_files(self, file_paths: list) -> list:
        """
        Upload multiple files to the sandbox.

        Args:
            file_paths: List of file paths to upload

        Returns:
            List of uploaded file paths in the sandbox
        """
        uploaded_files = []
        for file_path in file_paths:
            try:
                with open(file_path, "rb") as f:
                    sandbox_path = self.write(file_path, f)
                    uploaded_files.append(sandbox_path)
            except Exception as e:
                print(f"Error uploading file {file_path}: {e}")
                raise
        return uploaded_files

    def upload_file(self, file_path: str) -> str:
        """
        Upload a single file to the sandbox.

        Args:
            file_path: Path to the file to upload

        Returns:
            Path to the uploaded file in the sandbox
        """
        try:
            with open(file_path, "rb") as f:
                return self.write(file_path, f)
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}")
            raise

    def close(self):
        # Close the interpreter tool when done
        self._code_interpreter_tool.kill()
