import os

from crewai import Agent
from crewai_tools import FileReadTool

from tools.code_interpreter_tool import E2BCodeInterpreterTool


def create_insight_generator_agent(
    file_read_tool: FileReadTool, code_interpreter: E2BCodeInterpreterTool
) -> Agent:
    """
    Creates an Insight Generator agent specialized in interpreting analysis results.

    This agent is responsible for:
    1. Interpreting statistical results
    2. Extracting business value from patterns
    3. Generating actionable insights
    4. Creating meaningful explanations of findings
    """
    return Agent(
        role="Insight Generator",
        goal="Transform data analysis into meaningful, actionable insights",
        backstory="""You are an expert in data interpretation with a background in 
        business intelligence. You excel at taking complex statistical findings and
        translating them into clear, valuable insights. You can identify what 
        patterns and correlations actually matter in a practical context and can
        explain technical findings to non-technical audiences.""",
        tools=[code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True,
    )
