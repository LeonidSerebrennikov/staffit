from report_manager import BaseReport
from tabulate import tabulate


class AverageGDPReport(BaseReport):
    def get_report_data(self, country_data):
        result = []
    
        for country, gdp_values in country_data.items():
            if gdp_values:
                avg_gdp = sum(gdp_values) / len(gdp_values)
                result.append((country, avg_gdp))
        
        result.sort(key=lambda x: x[1], reverse=True)
        return result
    
    def print_report(self, country_data):
        averages = self.get_report_data(country_data)
        table_data = []
        for country, avg in averages:
            formatted_gdp = f"{avg:,.2f}"
            table_data.append([country, formatted_gdp])
        
        headers = ["Страна", "Средний ВВП"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))