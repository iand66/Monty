import configparser
import logging, sys, os
import datetime as dt
from logging.config import fileConfig

#FIXMELogger cannot handle ł \u0142 character - utf-16? 

def config(filename:str) -> configparser:
    """
    Read configurable parameters from INI file
    :param filename (str): Fully qualifed path to INI file
    :return configparser: ConfigParser object
    """
    config = configparser.ConfigParser()

    try:
        config.read_file(open(filename,'r'))
    except Exception as e:
        print(f'Could not find {filename} file')
        sys.exit()
    return config

def logSetup(logcfg:str, logloc:str, echo:bool, trace:bool) -> logging.Logger:
    """
    Setup logging
    :param logcfg (str): Fully qualified location of logging config file
    :param logloc (str): Directory to store log files app=*.log & db=*.trc
    :param echo (bool): Propagate logs to console
    :param trace (bool): Updated logger object
    :return logging.Logger: Logger object
    """
    today = dt.datetime.today()
    logfile = logloc + f'{today.year}-{today.month:02d}-{today.day:02d}.log'
    datfile = logloc + f'{today.year}-{today.month:02d}-{today.day:02d}.trc'

    try:
        os.path.exists(logcfg)
    except Exception as e:
        print(f'Could not find {logcfg} file')
        sys.exit()

    try:
        fileConfig(logcfg, defaults={'logfilename':logfile,'datfilename':datfile})
        logger = logging.getLogger('AppLog')
        logger.propagate=echo
        logger = logging.getLogger('DatLog')
        logger.propagate=trace
    except Exception as e:
        print(f'Could not parse {logcfg} file')
        sys.exit()
    return logger

