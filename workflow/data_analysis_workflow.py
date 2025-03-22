import json
from crewai import Crew, Process
from typing import Dict, List, Any

# Using absolute imports for correct package resolution
from agents.data_reader import create_data_reader_agent
from agents.data_analyzer import create_data_analyzer_agent
from agents.insight_generator import create_insight_generator_agent
from agents.report_creator import create_report_creator_agent
from tasks.data_tasks import (
    create_data_reading_task,
    create_data_analysis_task,
    create_insight_generation_task,
    create_report_creation_task
)
from tools.code_interpreter_tool import E2BCodeInterpreterTool
from crewai_tools import FileReadTool
from crewai_tools import FileWriterTool


class DataAnalysisWorkflow:
    """
    Orchestrates the end-to-end process of analyzing an unknown dataset
    using a crew of specialized AI agents.
    """
    
    def __init__(self, dataset_path: str, output_format: str = "markdown"):
        """
        Initialize the data analysis workflow.
        
        Args:
            dataset_path: Path to the dataset file to analyze
            output_format: Format for the final report (markdown, json, html)
        """
        self.dataset_path = dataset_path
        self.output_format = output_format
        
        # Initialize the code interpreter tool
        self.code_interpreter = E2BCodeInterpreterTool(result_as_answer=True)
        self.file_read_tool = FileReadTool()
        
        # Create specialized agents
        self.data_reader = create_data_reader_agent(self.code_interpreter, self.file_read_tool)
        self.data_analyzer = create_data_analyzer_agent(self.code_interpreter)
        self.insight_generator = create_insight_generator_agent(self.code_interpreter)
        self.report_creator = create_report_creator_agent(self.code_interpreter)
        
    def run(self) -> Dict[str, Any]:
        """
        Execute the full data analysis workflow.
        
        Returns:
            The final report and analysis results
        """
        try:
            data_reading_task = create_data_reading_task(
                agent=self.data_reader,
                dataset_path=self.dataset_path
            )
            data_analysis_task = create_data_analysis_task(
                agent=self.data_analyzer
            )
            insight_generation_task = create_insight_generation_task(
                agent=self.insight_generator
            )
            report_creation_task = create_report_creation_task(
                agent=self.report_creator
            )

            # Create the crew
            crew = Crew(
                agents=[
                    self.data_reader,
                    self.data_analyzer,
                    self.insight_generator,
                    self.report_creator
                ],
                tasks=[data_reading_task, data_analysis_task, insight_generation_task, report_creation_task],
                verbose=True,
                process=Process.sequential  # Tasks must be executed in sequence
            )
            return crew.kickoff()
                        
            
            
            
        finally:
            # Make sure to clean up resources
            self.code_interpreter.close()