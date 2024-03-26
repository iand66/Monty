import csv
from dateutil.parser import parse

def is_date(d: str):
    if '/' in d:
        try:
            parsed_date = parse(d)
            return parsed_date.strftime("%Y-%m-%d")
        except Exception:
            return d
    else:
        return d

from src.helper import applog

def csvRead(filename:str) -> list:
    """
    READ CSV file
    :param filename (str): Fully qualified path to filename
    :return list: List of read lines
    """
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [is_date(value) for value in row]
                data.append(', '.join(row))
        return data
    except Exception as e:
        applog.error(e)
        return e

def csvWrite(filename:str, data:list) -> bool:
    """
    WRITE CSV file
    :param filename (str): Fully qualified path to OS directory
    :parma data (list): Data to write
    :return bool: True or exception
    """
    try:
        with open(filename,'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for i in range(len(data)):
                writer.writerow([data[i]])
        return True
    except Exception as e:
        applog.error(e)
        return e

def csvDictReader(filename:str) -> list:
    """
    READ CSV file as dictionary
    :param filename (str): Fully qualified path to filename
    :return list: List of read lines 
    """
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row = {k: is_date(v) for k, v in row.items()}
                data.append(row)
        return data
    except Exception as e:
        applog.error(e)
        return e

def csvDictWriter(filename:str, data:dict) -> bool:
    """
    WRITE CSV file from dictionary
    :param filename (str): Fully qualified path to OS directory
    :parma data (dict): Data to write
    :return bool (bool): True or exception
    """
    try:
        with open(filename, 'w', newline='', encoding='utf8') as f:
            fieldnames = data[0]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        applog.error(e)
        return e