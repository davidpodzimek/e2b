import os

from crewai import Agent
from crewai_tools import FileReadTool

from tools.code_interpreter_tool import E2BCodeInterpreterTool


def create_time_series_model_predictor_agent(
    file_read_tool: FileReadTool, code_interpreter: E2BCodeInterpreterTool
) -> Agent:
    """
    Creates a Time Series Model Predictor agent specialized in evaluating data for machine learning model suitability.

    This agent is responsible for:
    1. Identifying time series data in the dataset
    2. Evaluating the quality of time series data for ML prediction
    3. Making suggestions about which data could be predicted effectively
    4. Recommending appropriate model types for each time series
    5. Providing example code for implementing the suggested models
    """
    return Agent(
        role="Time Series Model Predictor",
        goal="Identify potential time series variables suitable for prediction models and suggest appropriate ML approaches",
        backstory="""You are an expert data scientist specializing in time series analysis and predictive modeling.
        You excel at evaluating data for its suitability for forecasting and predictive applications.
        You can quickly identify which variables in a dataset would make good candidates for time series prediction,
        and you have deep knowledge of different time series models like ARIMA, Prophet, LSTM, and others.
        You understand seasonality, trends, and other time-dependent patterns in data.""",
        tools=[code_interpreter],
        llm=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        verbose=True,
    )
