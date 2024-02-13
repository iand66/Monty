import csv

from icecream import ic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.lib.apputils import config, logSetup
from src.orm.schema import Album, Customer
from src.orm.dbfunctions import dbSelect, dbInsert, dbUpdate, dbDelete

appcfg = config('./ini/globals.ini')
echo = eval(appcfg['LOGCFG']['logecho'])
trace = eval(appcfg['LOGCFG']['trace'])
logger = logSetup(appcfg['LOGCFG']['logcfg'], appcfg['LOGCFG']['logloc'], echo, trace)
engine = create_engine(appcfg['DBTST']['dbType'] + appcfg['DBTST']['dbName'], connect_args={"check_same_thread":False}, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

def csvDictWriter(filename:str, data:dict, echo:bool) -> bool:
    try:
        with open(filename, 'w', newline='', encoding='utf8') as f:
            fieldnames = data[0]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        return e

if __name__ == '__main__':  
    s_album = {'Id':'9999'}
    f_album = {'AlbumTitle':'My New%'}
    t_album = {'AlbumTitle':'My Newer Album','ArtistId':2}
    i_album = {'AlbumTitle':'My New Album','ArtistId':1}
    i_customer = {'Firstname':'Test','Lastname':'User','Email':'test@somewhere.com','SupportRepId':'1'}

    yn = input('(S)earch (I)nsert (U)pdate (D)elete ?')
    match yn.upper():
        case 'S':
            s = dbSelect(session, Album, echo, trace, **s_album)
            ic(f'Found {len(s)} results {s}')
        case 'I':
            i = dbInsert(session, Customer(**i_customer), echo, trace)
            ic(f'Inserted {i}')
        case 'U':
            u = dbUpdate(session, Album, f_album, t_album, echo, trace)
            ic(f'Updated {u}')
        case 'D':
            d = dbDelete(session, Album, echo, trace, **s_album)
            ic(f'Deleted {d}')
        case _:
            ic('Unrecognied input')


