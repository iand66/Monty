import configparser, os, sys, inspect
from datetime import date
from logging.config import fileConfig

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
        print(f"Could not find {filename} file")
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

    try:
        os.path.exists(logcfg)
    except Exception as e:
        print(f"Could not find {logcfg} file")
        sys.exit()

    try:
        fileConfig(logcfg, defaults={"logfilename": appfile, "datfilename": datfile, "secfilename": secfile })
        # TODO Log rotation @ 00:00
    except Exception as e:
        if os.path.exists(logloc):
            print(f"Could not process {logcfg} file")
            sys.exit()
        else:
            os.mkdir(logloc)

