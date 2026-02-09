import tempfile
import csv
import os
from report_management.reports.average_gdp import AverageGDPReport
from report_management.report_manager import ReportFactory


def create_test_csv(content):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerows(content)
        return f.name


def test_average_gdp_process():
    report = AverageGDPReport()
    
    data = [
        {'country': 'USA', 'gdp': '1000'},
        {'country': 'USA', 'gdp': '2000'},
        {'country': 'China', 'gdp': '500'},
        {'country': 'China', 'gdp': '1500'}
    ]
    
    result = report.process_data(data)
    
    assert len(result) == 2
    assert result[0][0] == 'USA'
    assert result[0][1] == 1500.0
    assert result[1][0] == 'China'
    assert result[1][1] == 1000.0


def test_read_data():
    report = AverageGDPReport()
    
    csv_content = [
        ['country', 'year', 'gdp'],
        ['USA', '2023', '1000'],
        ['USA', '2022', '2000'],
        ['China', '2023', '500']
    ]
    
    temp_file = None
    try:
        temp_file = create_test_csv(csv_content)
        
        data = report.read_data([temp_file])
        
        assert len(data) == 3
        assert data[0]['country'] == 'USA'
        assert data[0]['gdp'] == '1000'
        assert data[2]['country'] == 'China'
        
    finally:
        if temp_file:
            os.unlink(temp_file)


def test_invalid_columns():
    report = AverageGDPReport()
    
    data = [
        {'country': 'USA', 'wrong_column': '1000'},
        {'country': 'China', 'gdp': '500'}
    ]
    
    result = report.process_data(data)
    
    assert len(result) == 1
    assert result[0][0] == 'China'


def test_empty_data():
    report = AverageGDPReport()
    
    data = []
    result = report.process_data(data)
    
    assert result == []


def test_report_factory():
    report = ReportFactory.create_report('average-gdp')
    assert isinstance(report, AverageGDPReport)
    
    try:
        ReportFactory.create_report('wrong')
        assert False
    except ValueError:
        assert True


def test_multiple_files():
    report = AverageGDPReport()
    
    csv1 = [
        ['country', 'gdp'],
        ['USA', '1000'],
        ['China', '500']
    ]
    
    csv2 = [
        ['country', 'gdp'],
        ['USA', '2000'],
        ['Germany', '400']
    ]
    
    files = []
    try:
        files.append(create_test_csv(csv1))
        files.append(create_test_csv(csv2))
        
        data = report.read_data(files)
        
        assert len(data) == 4
        
        result = report.process_data(data)
        
        assert len(result) == 3
        assert result[0][0] == 'USA'
        assert result[0][1] == 1500.0
        
    finally:
        for f in files:
            if os.path.exists(f):
                os.unlink(f)