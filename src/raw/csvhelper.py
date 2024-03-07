import csv, logging

def csvRead(filename:str, echo:bool) -> list:
    """
    READ CSV file
    :param filename (str): Fully qualified path to filename
    :param echo (bool): Enable application logging
    :return list: List of read lines
    """
    applog = logging.getLogger('AppLog')
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(', '.join(row))
        return data
    except Exception as e:
        if echo:
            applog.error(e)
        return e

def csvWrite(filename:str, data:list, echo:bool) -> bool:
    """
    WRITE CSV file
    :param filename (str): Fully qualified path to OS directory
    :parma data (list): Data to write
    :param echo (bool): Enable application logging
    :return bool: True or exception
    """
    applog = logging.getLogger('AppLog')
    try:
        with open(filename,'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for i in range(len(data)):
                writer.writerow([data[i]])
        return True
    except Exception as e:
        if echo:
            applog.error(e)
        return e

def csvDictReader(filename:str, echo:bool) -> list:
    """
    READ CSV file as dictionary
    :param filename (str): Fully qualified path to filename
    :param echo (bool): Enable application logging
    :return list: List of read lines 
    """
    applog = logging.getLogger('AppLog')
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        if echo:
            applog.error(e)
    return e

def csvDictWriter(filename:str, data:dict, echo:bool) -> bool:
    """
    WRITE CSV file from dictionary
    :param filename (str): Fully qualified path to OS directory
    :parma data (dict): Data to write
    :param echo (bool): Enable application logging
    :return bool (bool): True or exception
    """
    applog = logging.getLogger('AppLog')
    try:
        with open(filename, 'w', newline='', encoding='utf8') as f:
            fieldnames = data[0]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        if echo:
            applog.error(e)
        return e