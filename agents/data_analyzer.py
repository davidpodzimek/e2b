import os
from crewai import Agent
from typing import List
from tools.code_interpreter_tool import E2BCodeInterpreterTool

def create_data_analyzer_agent(code_interpreter: E2BCodeInterpreterTool) -> Agent:
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