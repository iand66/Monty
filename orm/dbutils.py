import logging, os 
from sqlalchemy.engine.base import Engine
from raw.csvhelper import csvDictReader, csvRead
from sqlalchemy_utils import database_exists
from orm.dbfunctions import dbInsertAll
from orm.schema import *

def dbInit(engine:Engine, verbose:bool) -> bool:
    '''
    Create database shell
    :param engine - SQLAlchemy session instance
    :param verbose - Enable verbose mode
    :return boolean - True or False
    '''
    applog = logging.getLogger('AppLog')
    if not database_exists(engine.url):
        Base.metadata.create_all(bind=engine)
        if verbose:
            applog.info(f'Database {engine.url.database} created at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
        return True
    else:
        for t in Base.metadata.sorted_tables:
            Base.metadata.create_all(bind=engine, checkfirst=True)
        if verbose:
            applog.info(f'Database {engine.url} updated at at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
        return True
    
def dbFill(engine:Engine, seed:str, database:str, verbose:bool) -> bool:
    '''
    Reload sample data
    :param engine - SQLAlchemy session instance
    :param seed - Fully qualified CSV file of files to import
    :param database - Database name to populate
    :param verbose - Enable verbose mode
    :return boolean - True or False
    '''
    applog = logging.getLogger('AppLog')
    try:
        filesToImport = csvRead(seed)
        if filesToImport is not None:
            for f in enumerate(filesToImport):
                dataToImport = csvDictReader(seed[0:seed.rfind('/')+1] + f[1])
                tblName = f[1][0:f[1].rfind('.')-1]
                dbInsertAll(engine, eval(tblName.title()), dataToImport, verbose)
                if verbose:
                    applog.info(f'{database} {tblName.title()} populated at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
            return True
    except Exception as e:
        if verbose:
            applog.error(f'Seed file of sample files could not be found')
        return e

def dbKill(filename:str, verbose:bool) -> bool:
    '''
    Delete database
    :param filename - Fully qualified path to database name
    :param verbose - Enable verbose mode
    :return boolean - True or False
    '''
    applog = logging.getLogger('AppLog')
    try:
        if os.path.exists(filename):
            os.remove(filename)
            if verbose:
                applog.info(f'File {filename} has been removed at {datetime.today().strftime("%d-%m-%Y %H:%M")}')
            if not os.path.exists(filename):
                return True
        else:
            if verbose:
                applog.warning(f'File {filename} could not be found')
            return False
    except Exception as e:
        return e