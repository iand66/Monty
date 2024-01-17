import csv, logging

def csvRead(filename:str) -> list:
    '''
    Read CSV file
    :param filename - Fully qualified path to filename
    :return list or exception
    :example - csvRead('MyFileName.csv')
    '''
    applog = logging.getLogger('AppLog')
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(', '.join(row))
        return data
    except Exception as e:
        applog.error(e)
        return e

def csvWrite(filename:str, data:list) -> bool:
    '''
    Write CSV file
    :param filename - Fully qualified path to OS directory
    :parma data - Data to write
    :return bool - True or exception
    :example - csvWrite('MyFileName.csv', data)
    '''
    applog = logging.getLogger('AppLog')
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
    '''
    Read CSV file as dictionary
    :param filename - Fully qualified path to filename
    :return list or exception
    :example - csvDictReader('MyFileName.csv')
    '''
    applog = logging.getLogger('AppLog')
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        applog.error(e)
        return e

def csvDictWriter(filename:str, data:dict) -> bool:
    '''
    Write CSV file from dictionary
    :param filename - Fully qualified path to OS directory
    :parma data - Data to write
    :return bool - True or exception
    :example - csvDictWriter('MyFileName.csv', data)
    '''
    applog = logging.getLogger('AppLog')
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