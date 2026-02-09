Для работы программы нужны библиотеки pytest и tabulate, поэтому перед запуском нужно их установить: pip install -r requirements.txt

Программа запускается в соответствии с заданием: 

    python .\main.py --files economic1.csv dataset1.csv --report average-gdp

Добавление нового отчета:    
Новый отчет должен наследоваться от report_manager.BaseReport с использованием его методов. В __init__ указываются необходимые столбцы, которые будут прочитаны из csv файла.     
Пример:

    def __init__(self):
        super().__init__(required_columns=['country', 'year', 'gdp'])

    
В функции process_data на вход принимается лист с прочитанными строками, на выходе отдается лист с обработанными строками. Сам алгоритм зависит от бизнес-логики отчета. В функции display происходит вывод отчета в виде таблицы.

Для регистрации нового отчета нужно указать его в report_manager.ReportFactory в качестве одного из case.     
Пример:

    case 'new-report':
        from report_management.reports.new_report import NewReport
        return NewReport()

Тестирование стандартно:

    pytest tests/test_main.py
