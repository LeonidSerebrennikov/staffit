import csv
from abc import ABC, abstractmethod

class BaseReport(ABC):
    def __init__(self, required_columns):
        self.required_columns = required_columns
    
    def read_data(self, filenames: list[str]):
        all_data = []
        
        for filename in filenames:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if all(col in row for col in self.required_columns):
                            all_data.append(row)
            except Exception as e:
                print(f"Ошибка в файле {filename}: {e}")
        
        return all_data
    
    @abstractmethod
    def process_data(self, data):
        pass
    
    @abstractmethod
    def display(self, result):
        pass

class ReportFactory:
    _reports: dict[str, type[BaseReport]] = {}

    
    @classmethod
    def register(cls, report_name: str):
        def decorator(report_class: BaseReport):
            cls._reports[report_name] = report_class
            return report_class
        return decorator

    @classmethod
    def get_report(cls, report_name: str) -> BaseReport:
        if report_name not in cls._reports:
            raise ValueError(f"report {report_name} does not exist")
        
        report_class = cls._reports[report_name]
        report_instance = report_class()
        return report_instance
