# E2B Data Analysis Crew

This project uses a crew of AI agents powered by CrewAI and E2B's code interpreter to analyze unknown datasets. The system automatically processes, analyzes, and generates meaningful insights without requiring prior knowledge of the data structure.

## Features

- Automatically detect and load various data formats (CSV, JSON, Excel, etc.)
- Perform comprehensive statistical analysis
- Generate visualizations to understand patterns
- Extract meaningful insights from patterns and correlations
- Create structured reports with actionable information

## Prerequisites

- Python 3.9 or higher
- An E2B API key (get one at https://e2b.dev/docs)
- OpenAI API key or equivalent LLM API key

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -e .
   ```
3. Create a `.env` file with your API keys:
   ```
   E2B_API_KEY=your_e2b_api_key
   OPENAI_API_KEY=your_openai_api_key
   LLM_MODEL=gpt-4o-mini  # or your preferred model
   ```

## Usage

Analyze a dataset with:

```bash
python main.py --dataset path/to/your/dataset.csv --output results.md
```

Options:
- `--dataset`, `-d`: Path to the dataset file to analyze (required)
- `--output`, `-o`: Path to save the output report (default: output.md)
- `--format`, `-f`: Output format (markdown, json, html) (default: markdown)

## How It Works

1. **Data Reader Agent**: Loads the dataset, detects its format, and prepares it for analysis
2. **Data Analyzer Agent**: Performs statistical analysis, identifies patterns, and creates visualizations
3. **Insight Generator Agent**: Interprets the analysis results and extracts meaningful insights
4. **Report Creator Agent**: Organizes the findings into a comprehensive, clear report

The agents work together in a sequential workflow, passing their results to the next agent in the pipeline.

## Example

```bash
python main.py --dataset customer_data.csv --output customer_insights.md
```

This will analyze the customer data, generate insights, and save a comprehensive report to `customer_insights.md`.

## Development

For development, install the dev dependencies:

```bash
pip install -e ".[dev]"
```

Run linting and type checking:

```bash
black .
ruff check .
mypy .
```