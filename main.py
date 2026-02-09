import argparse
import csv
from report_management.report_manager import ReportFactory


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    
    args = parser.parse_args()
    
    filenames = args.files
    

    report_fact = ReportFactory()
    report = report_fact.create_report(args.report)
    raw_data = report.read_data(filenames)
    report_data = report.process_data(raw_data)
    report.display(report_data)

if __name__ == "__main__":
    main()