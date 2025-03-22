import os
from crewai import Agent
from typing import List
from tools.code_interpreter_tool import E2BCodeInterpreterTool
from crewai_tools import FileReadTool


def create_data_cleanup_agent(file_read_tool: FileReadTool, code_interpreter: E2BCodeInterpreterTool) -> Agent:
    """
    Creates a Data Cleanup agent specialized in initial data preparation and analysis.
    
    This agent is responsible for:
    1. Basic data cleaning and preparation
    2. Handling missing values and outliers
    3. Data type detection and conversion
    4. Providing summary statistics about the dataset
    """
    return Agent(
        role="Data Cleanup",
        goal="Prepare and clean datasets for deeper analysis",
        backstory="""You are an expert data engineer with a focus on data quality and preparation.
        You excel at identifying data quality issues, handling missing values, detecting outliers,
        and transforming data into a clean, analysis-ready format. You're skilled at providing
        initial summary statistics and helping others understand the basic structure and
        characteristics of datasets.""",
        tools=[code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True
    )

def create_data_analyzer_agent(file_read_tool: FileReadTool, code_interpreter: E2BCodeInterpreterTool) -> Agent:
    """
    Creates a Data Analyzer agent specialized in statistical analysis and pattern finding.
    
    This agent is responsible for:
    1. Performing statistical analysis on the dataset
    2. Identifying patterns and correlations
    3. Creating visualizations to better understand the data
    4. Feature engineering and data transformation
    """
    return Agent(
        role="Data Analyzer",
        goal="Uncover meaningful patterns and insights from datasets through statistical analysis",
        backstory="""You are a skilled data scientist with expertise in statistical analysis, 
        machine learning, and data visualization. You excel at finding patterns that others 
        might miss and can translate complex data into clear visualizations. You know how to
        use libraries like pandas, numpy, scipy, matplotlib, seaborn, and scikit-learn to 
        extract valuable insights from any dataset.""",
        tools=[code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True
    )