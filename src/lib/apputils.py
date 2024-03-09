import configparser, logging, os, sys, inspect
from datetime import date
from logging.config import fileConfig

# Call stack used in debug mode
def whoami():
    return inspect.stack()[1][3]

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

def logSetup(cfg: str, loc: str, echo: bool, trace: bool, sec: bool) -> logging.Logger:
    """
    Setup logging environment
    :param cfg (str): Fully qualified location of logging config file
    :param loc (str): Directory to store log files
    :param echo (bool): Update application logger object
    :param trace (bool): Update database logger object
    :param sec (bool): Update security logger object
    :return logging.Logger: Logger object
    """
    today = date.today()
    appfile = loc + f"{today.year}-{today.month:02d}-{today.day:02d}.app"
    datfile = loc + f"{today.year}-{today.month:02d}-{today.day:02d}.dat"
    secfile = loc + f"{today.year}-{today.month:02d}-{today.day:02d}.sec"

    try:
        os.path.exists(cfg)
    except Exception as e:
        print(f"Could not find {cfg} file")
        sys.exit()

    try:
        # TODO Update to dictConfig - json.load(filename)
        fileConfig(cfg, defaults={"logfilename": appfile, "datfilename": datfile, "secfilename": secfile })
        logger = logging.getLogger("AppLog")
        logger.propagate = echo
        logger = logging.getLogger("DatLog")
        logger.propagate = trace
        logger = logging.getLogger("SecLog")
        logger.propagate = sec
    except Exception as e:
        print(f"Could not parse {cfg} file")
        sys.exit()
    return logger