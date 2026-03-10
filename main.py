import argparse
from report_management import reports
from report_management.report_manager import ReportFactory


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    
    args = parser.parse_args()
    
    filenames = args.files
    
    report = ReportFactory.get_report(args.report)
    data = report.read_data(filenames=filenames)
    processed_data = report.process_data(data)
    report.display(processed_data)

if __name__ == "__main__":
    main()