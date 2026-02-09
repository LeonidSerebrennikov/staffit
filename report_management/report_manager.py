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
    @staticmethod
    def create_report(report_name):
        match report_name:
            case 'average-gdp':
                from report_management.reports.average_gdp import AverageGDPReport
                return AverageGDPReport()
            case _:
                raise ValueError(f"Неизвестный отчет: {report_name}")
