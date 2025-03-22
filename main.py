import argparse

from dotenv import load_dotenv

from workflow.data_analysis_workflow import DataAnalysisWorkflow

# Load environment variables
load_dotenv()


def setup_argparse():
    """Set up command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Analyze an unknown dataset using a crew of AI agents."
    )
    parser.add_argument(
        "--dataset",
        "-d",
        type=str,
        help="Path to the dataset file to analyze",
        default="data/grocery.csv",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Path to save the output report (default: output.md)",
        default="output.md",
    )
    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["markdown", "json", "html"],
        default="markdown",
        help="Output format for the report (default: markdown)",
    )
    return parser


def main():
    """Main entry point for the application."""
    parser = setup_argparse()
    args = parser.parse_args()

    # Print welcome message
    BLUE, RESET = "\033[94m", "\033[0m"
    print(f"{BLUE}Starting data analysis with CrewAI...{RESET}")
    print(f"{BLUE}Dataset: {args.dataset}{RESET}")
    print(f"{BLUE}Output will be saved to: {args.output}{RESET}")

    try:
        # Create and run the data analysis workflow
        workflow = DataAnalysisWorkflow(
            dataset_path=args.dataset, output_format=args.format
        )
        results = workflow.run()
        for result in results.tasks_output:
            if result.agent == "Time Series Model Predictor":
                time_series_results = result
                time_series_json = time_series_results.raw
                with open("time_series_results", 'w') as f:
                    f.write(time_series_results.raw)
            if result.agent == "Report Creator":
                report_results = result
                with open("report_results", 'w') as f:
                    f.write(report_results.raw)
            if result.agent == "Insight Generator":
                insight_results = result
                with open("insight_results", 'w') as f:
                    f.write(insight_results.raw)

        print(f"{BLUE}Analysis complete! Results saved to {args.output}{RESET}")

    except Exception as e:
        print(f"Error during analysis: {e}")
        raise


if __name__ == "__main__":
    main()
