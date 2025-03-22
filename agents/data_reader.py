import os

from crewai import Agent
from crewai_tools import FileReadTool

from tools.code_interpreter_tool import E2BCodeInterpreterTool


def create_data_reader_agent(
    file_read_tool: FileReadTool, code_interpreter: E2BCodeInterpreterTool
) -> Agent:
    """
    Creates a Data Reader agent specialized in loading and parsing unknown datasets.

    This agent is responsible for:
    1. Identifying file formats
    2. Loading data from various sources
    """
    return Agent(
        role="Data Reader",
        goal="Efficiently load datasets from various sources and formats",
        backstory="""You are an expert data engineer specializing in data ingestion. 
        You can handle various file formats (CSV, JSON, Excel, parquet, etc.) and 
        understand how to properly load data from different sources. You're skilled
        at detecting file formats and correctly parsing different types of data files.""",
        tools=[file_read_tool, code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True,
    )
