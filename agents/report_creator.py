import os
from crewai import Agent
from typing import List
from tools.code_interpreter_tool import E2BCodeInterpreterTool

def create_report_creator_agent(code_interpreter: E2BCodeInterpreterTool) -> Agent:
    """
    Creates a Report Creator agent specialized in generating final outputs.
    
    This agent is responsible for:
    1. Organizing insights into a coherent structure
    2. Creating clear visualizations for the final report
    3. Writing explanations in a clear, accessible way
    4. Formatting the output in the desired format (JSON, HTML, Markdown, etc.)
    """
    return Agent(
        role="Report Creator",
        goal="Create comprehensive, clear reports that effectively communicate data insights",
        backstory="""You are an expert in data storytelling and report creation. With a 
        background in data journalism and technical writing, you know how to present 
        complex findings in a clear, engaging way. You're skilled at creating visualizations
        that highlight key insights and can structure information logically to guide the
        reader through complex analyses to clear conclusions.""",
        tools=[code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True
    )