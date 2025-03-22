# E2B Project Guidelines

## Build, Test & Run Commands
- Run data analysis: `python main.py --dataset <path> --output <output_file>`
- Install dependencies: `pip install -e .`
- Dev dependencies: `pip install -e ".[dev]"`
- Format code: `black .`
- Lint code: `ruff check .`
- Type checking: `mypy .`

## Code Style Guidelines
- **Imports**: Group standard library, third-party, and local imports (separated by newlines)
- **Formatting**: Follow PEP 8 with 88 character line length
- **Type Hints**: All functions must have type annotations
- **Error Handling**: Use specific exception types with meaningful error messages
- **Naming**: snake_case for variables/functions, CamelCase for classes
- **Documentation**: Docstrings required for all public functions and classes
- **Module Structure**: Keep related functionality in dedicated modules

## Project Architecture
- **Agents**: Specialized AI agents in the `/agents` directory
- **Tasks**: Task definitions in the `/tasks` directory
- **Tools**: Shared tools in the `/tools` directory 
- **Workflow**: Orchestration logic in the `/workflow` directory
- Uses CrewAI and E2B code interpreter for AI agent workflows
- Requires E2B_API_KEY and OPENAI_API_KEY (or equivalent) environment variables