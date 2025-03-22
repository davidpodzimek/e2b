import sys

sys.dont_write_bytecode = True

import os
import json
import argparse
from dotenv import load_dotenv
from workflow.data_analysis_workflow import DataAnalysisWorkflow

# Load environment variables
load_dotenv()

def setup_argparse():
    """Set up command line argument parsing."""
    parser = argparse.ArgumentParser(
        description='Analyze an unknown dataset using a crew of AI agents.'
    )
    parser.add_argument(
        '--dataset', '-d',
        type=str,
        required=True,
        help='Path to the dataset file to analyze'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='output.md',
        help='Path to save the output report (default: output.md)'
    )
    parser.add_argument(
        '--format', '-f',
        type=str,
        choices=['markdown', 'json', 'html'],
        default='markdown',
        help='Output format for the report (default: markdown)'
    )
    return parser

def main():
    """Main entry point for the application."""
    parser = setup_argparse()
    args = parser.parse_args()
    
    # Print welcome message
    BLUE, RESET = '\033[94m', '\033[0m'
    print(f"{BLUE}Starting data analysis with CrewAI...{RESET}")
    print(f"{BLUE}Dataset: {args.dataset}{RESET}")
    print(f"{BLUE}Output will be saved to: {args.output}{RESET}")
    
    try:
        # Create and run the data analysis workflow
        workflow = DataAnalysisWorkflow(
            dataset_path=args.dataset,
            output_format=args.format
        )
        results = workflow.run()
        
        # Save the report to the specified output file
        output_format = args.format
        if output_format == 'json':
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
        else:
            # For markdown and HTML, just save the report text
            with open(args.output, 'w') as f:
                f.write(results["report"])
        
        print(f"{BLUE}Analysis complete! Results saved to {args.output}{RESET}")
        
        # Print a brief summary of findings
        print(f"{BLUE}Summary of key insights:{RESET}")
        try:
            if isinstance(results["insights"], dict) and "insights" in results["insights"]:
                for i, insight in enumerate(results["insights"]["insights"][:3], 1):
                    print(f"{BLUE}{i}. {insight.get('title', f'Insight {i}')}{RESET}")
        except:
            print(f"{BLUE}Insights available in the full report.{RESET}")
            
    except Exception as e:
        print(f"Error during analysis: {e}")
        raise

if __name__ == "__main__":
    main()