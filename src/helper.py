import configparser
import inspect
import logging
import os
import sys
from datetime import date
from logging.config import fileConfig

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


# Call stack used in debug mode
def whoami():
    return inspect.stack()[1][3]


# Read configurable parameters from INI file
def config(filename: str) -> configparser:
    """
    Read configurable parameters from INI file
    :param filename (str): Fully qualifed path to INI file
    :return configparser: ConfigParser object
    """
    config = configparser.ConfigParser()

    try:
        config.read_file(open(filename, "r"))
    except Exception as e:
        print(f"Could not find {filename} file. Problem {e}")
        sys.exit()
    return config


# Setup logging environment
def logSetup(logcfg: str, logloc: str) -> None:
    """
    Setup logging environment
    :param logcfg (str): Fully qualified location of logging config file
    :param logloc (str): Directory to store log files
    :return None
    """
    today = date.today()
    appfile = logloc + f"{today.year}-{today.month:02d}-{today.day:02d}.app"
    datfile = logloc + f"{today.year}-{today.month:02d}-{today.day:02d}.dat"
    secfile = logloc + f"{today.year}-{today.month:02d}-{today.day:02d}.sec"
    apifile = logloc + f"{today.year}-{today.month:02d}-{today.day:02d}.api"

    try:
        os.path.exists(logcfg)
    except Exception as e:
        print(f"Could not find {logcfg} file. Problem {e}")
        sys.exit()

    try:
        fileConfig(
            logcfg,
            defaults={
                "logfilename": appfile,
                "datfilename": datfile,
                "secfilename": secfile,
                "apifilename": apifile,
            },
        )

    except Exception as e:
        if os.path.exists(logloc):
            print(f"Could not process {logcfg} file {e}")
            sys.exit()
        else:
            os.mkdir(logloc)


# Get current database
def get_db():
    db = session()
    if db.bind.name == "sqlite":
        db.execute(text("pragma foreign_keys=on"))
    try:
        return db
    finally:
        db.close()


# Setup working environment
"""
appcfg (configparser) - Application configuration file to read
mode (bool) - Running in LIVE mode?
trace (bool) - Trace database CRUD events to trace logs
secure (bool) - Trace security events to security logs
engine (object) - SQL Alchemy database to use
session (object) - SQL Alchemy session object
"""
appcfg = config("./ini/globals.ini")
mode = eval(appcfg["MODE"]["live"])
trace = eval(appcfg["LOGCFG"]["trace"])
secure = eval(appcfg["LOGCFG"]["secure"])
dbtype = appcfg.get("DBCFG", "dbtype")
logcfg = appcfg.get("LOGCFG", "logcfg")
logloc = appcfg.get("LOGCFG", "logloc")

if mode:
    dbname = appcfg.get("DBCFG", "dblive")
else:
    dbname = appcfg.get("DBCFG", "dbtest")

# Setup logging environment
logger = logSetup(logcfg, logloc)
applog = logging.getLogger("AppLog")
datlog = logging.getLogger("DatLog")
seclog = logging.getLogger("SecLog")
apilog = logging.getLogger("ApiLog")

# Create database
engine = create_engine(dbtype + dbname, connect_args={"check_same_thread": False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
