import os
from crewai import Agent
from typing import List
from tools.code_interpreter_tool import E2BCodeInterpreterTool

def create_data_reader_agent(code_interpreter: E2BCodeInterpreterTool) -> Agent:
    """
    Creates a Data Reader agent specialized in loading and parsing unknown datasets.
    
    This agent is responsible for:
    1. Identifying file formats
    2. Loading data from various sources
    3. Basic data cleaning and preparation
    4. Providing summary statistics about the dataset
    """
    return Agent(
        role="Data Reader",
        goal="Efficiently load and prepare unknown datasets for analysis",
        backstory="""You are an expert data engineer specializing in data ingestion. 
        You can handle various file formats (CSV, JSON, Excel, parquet, etc.) and 
        understand how to properly load and prepare data for analysis. You're skilled
        at detecting data types, handling missing values, and providing initial data
        summaries.""",
        tools=[code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True
    )