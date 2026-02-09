from report_management.report_manager import BaseReport
from tabulate import tabulate
from collections import defaultdict


class AverageGDPReport(BaseReport):
    def __init__(self):
        super().__init__(required_columns=['country', 'gdp'])
    
    def process_data(self, data: list[str]):
        country_gdp = defaultdict(list)
        
        for row in data:
            country = row['country']
            try:
                gdp = float(row['gdp'].replace(',', ''))
                country_gdp[country].append(gdp)
            except (ValueError, KeyError):
                continue
        
        result = []
        for country, values in country_gdp.items():
            if values:
                avg = sum(values) / len(values)
                result.append((country, avg))
        
        result.sort(key=lambda x: x[1], reverse=True)
        return result
    
    def display(self, result: list[str]):
        if not result:
            print("Нет данных")
            return
        
        table_data = [[country, f"{gdp:,.2f}"] for country, gdp in result]
        print(tabulate(table_data, headers=["Страна", "Средний ВВП"], tablefmt="grid"))