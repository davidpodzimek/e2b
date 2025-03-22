from crewai import Task, Agent
from typing import Dict, Any

def create_data_reading_task(agent: Agent, dataset_path: str) -> Task:
    """
    Creates a task for reading and preparing an unknown dataset.
    
    Args:
        agent: The Data Reader agent
        dataset_path: Path to the dataset file
        
    Returns:
        Task for loading and preparing the dataset
    """
    return Task(
        description=f"""
        Analyze and load the dataset at path: {dataset_path}
        
        Your responsibilities:
        1. Identify the file format and appropriate method to load it
        2. Load the dataset using appropriate libraries
        3. Perform initial data exploration (shape, columns, data types)
        4. Handle basic data cleaning (missing values, duplicates)
        5. Provide summary statistics about the dataset
        6. Return the cleaned dataset as a variable and a summary of its contents
        
        If you encounter any issues with loading the data, try multiple approaches and libraries.
        """,
        expected_output="""
        A dictionary containing:
        1. The cleaned dataset (stored in a variable that can be passed to the next agent)
        2. A summary of the dataset including its structure, key statistics, and any issues found
        3. Suggestions for how to proceed with analysis
        
        Example output format:
        {
            "data_variable": "df",  # The variable name containing the dataset
            "summary": {
                "shape": [rows, columns],
                "columns": [...],
                "dtypes": {...},
                "missing_values": {...},
                "key_statistics": {...}
            },
            "suggestions": [...]
        }
        """,
        agent=agent
    )

def create_data_analysis_task(agent: Agent) -> Task:
    """
    Creates a task for analyzing the prepared dataset.
    
    Args:
        agent: The Data Analyzer agent
        data_info: Information about the dataset from the previous task
        
    Returns:
        Task for analyzing the dataset
    """
    return Task(
        description=f"""
        Analyze the dataset provided by the Data Reader agent.
        
        Your responsibilities:
        1. Explore relationships between variables
        2. Identify correlations and patterns
        3. Create visualizations to highlight key findings
        4. Perform statistical tests where appropriate
        5. Engineer features if needed for better analysis
        6. Identify outliers and anomalies
        
        Focus on finding meaningful patterns rather than just generating statistics.
        """,
        expected_output="""
        A dictionary containing:
        1. Key findings from the analysis
        2. Important correlations and patterns
        3. Visualizations (stored in variables or saved to files)
        4. Statistical test results
        5. Engineered features (if any)
        
        Example output format:
        {
            "findings": [...],
            "correlations": {...},
            "visualizations": [...],
            "statistical_tests": {...},
            "engineered_features": {...}
        }
        """,
        agent=agent
    )

def create_insight_generation_task(agent: Agent) -> Task:
    """
    Creates a task for generating insights from the analysis.
    
    Args:
        agent: The Insight Generator agent
        analysis_results: Results from the data analysis task
        data_info: Information about the dataset from the first task
        
    Returns:
        Task for generating insights
    """
    return Task(
        description=f"""
        Generate meaningful insights based on the data analysis.
                
        Your responsibilities:
        1. Interpret the statistical findings and correlations
        2. Identify the most significant patterns and what they mean
        3. Generate actionable insights based on the data
        4. Prioritize insights based on their importance/impact
        5. Explain complex findings in simple terms
        
        Focus on quality over quantity - identify the most meaningful insights.
        """,
        expected_output="""
        A dictionary containing:
        1. Key insights derived from the analysis
        2. Explanation of why these insights matter
        3. Potential actions or decisions that could be made based on these insights
        4. Areas that require further investigation
        
        Example output format:
        {
            "insights": [
                {
                    "title": "Insight title",
                    "description": "Detailed explanation",
                    "supporting_evidence": "Data points that support this",
                    "potential_actions": [...]
                },
                ...
            ],
            "further_investigation": [...]
        }
        """,
        agent=agent
    )

def create_report_creation_task(agent: Agent) -> Task:
    """
    Creates a task for creating the final report.
    
    Args:
        agent: The Report Creator agent
        insights: Insights generated from the previous task
        analysis_results: Results from the data analysis task
        data_info: Information about the dataset from the first task
        
    Returns:
        Task for creating the final report
    """
    return Task(
        description=f"""
        Create a comprehensive report based on the dataset analysis and insights.
                
        Your responsibilities:
        1. Structure the report in a logical, easy-to-follow format
        2. Create clear visualizations that highlight key findings
        3. Write explanations in accessible language
        4. Include an executive summary of the most important findings
        5. Format the report as specified (default to markdown if not specified)
        
        The report should tell a coherent story about the data.
        """,
        expected_output="""
        A complete report including:
        1. Executive summary
        2. Introduction to the dataset
        3. Methodology used for analysis
        4. Key findings with supporting visualizations
        5. Detailed insights with explanations
        6. Conclusions and recommendations
        7. Appendix with additional details (if needed)
        
        The report should be formatted as markdown by default, or in the specified format.
        """,
        agent=agent
    )