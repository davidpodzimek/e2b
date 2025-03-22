# E2B Data Analysis Crew

This project uses a crew of AI agents powered by CrewAI and E2B's code interpreter to analyze unknown datasets. The system automatically processes, analyzes, and generates meaningful insights without requiring prior knowledge of the data structure.

## Features

- Automatically detect and load various data formats (CSV, JSON, Excel, etc.)
- Perform comprehensive data cleaning and preparation
- Conduct statistical analysis and visualization
- Generate meaningful insights from patterns and correlations
- Identify time series data suitable for ML prediction models
- Suggest appropriate machine learning models for time series forecasting
- Create structured reports with actionable information

## Workflow Agents

The analysis is powered by a crew of specialized AI agents:

1. **Data Reader**: Loads and identifies file formats of unknown datasets
2. **Data Cleanup**: Prepares and cleans raw data for analysis
3. **Data Analyzer**: Performs statistical analysis and creates visualizations
4. **Insight Generator**: Extracts meaningful patterns and actionable insights
5. **Time Series Model Predictor**: Evaluates data for ML model suitability and makes prediction recommendations
6. **Report Creator**: Compiles findings into a comprehensive report

## Prerequisites

- Python 3.9 or higher
- An E2B API key (get one at https://e2b.dev/docs)
- OpenAI API key or equivalent LLM API key

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt