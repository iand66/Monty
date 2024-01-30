import logging
from sqlalchemy import text
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from orm.schema import *

# Table level functions
def dbInsertAll(engine:Engine, tablename:str, data:Base, echo:bool, trace:bool) -> int:
    '''
    Insert multiple records into database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param data - SQLALchemy data objects
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return int - Number of records inserted or exception
    :example - dbInsertAll(engine, tablename, dataToImport, False)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        if engine.name == 'sqlite':
            session.execute(text('pragma foreign_keys=on'))
        try:
            session.bulk_insert_mappings(tablename, data)
            session.commit()
            if trace:
                datlog.info(f'{tablename.__tablename__} {data}')
            return len(data)
        except Exception as e:
            session.rollback()
            if echo:
                applog.error(e)
            return e

def dbSelectAll(engine:Engine, tablename:Base, echo:bool, trace:bool) -> list:
    #TODO ORM to Dict{} is not elegant
    '''
    Select all records from a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param echo - Enable applocation logging
    :param trace - Enable database logging
    :return data - Query results as list
    :example - x = dbSelectAll(engine, Genre, True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    try:
        with Session(engine) as session:
            data = []
            results = session.query(tablename).all()
            for row in results: 
                rowdict = {col: str(getattr(row,col)) for col in row.__table__.c.keys()}
                if trace:
                    datlog.info(f'Selected ... {rowdict}')
                data.append(rowdict)
            return data
    except SQLAlchemyError as e:
        if echo:
            applog.error(e)
        return e

def dbUpdateAll(engine:Engine, tablename:Base, updAttr:str, updVal:str, echo:bool, trace:bool) -> int:
    '''
    Update records in a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param updAttr - Table column to update
    :param updVal - New value for table column
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return results - Integer of update results processed
    :example - x = dbUpdateAll(engine, Customer, 'City', 'My Town', True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        try:
            results = session.query(tablename).update({updAttr:updVal})
            session.commit()
            if trace:
                datlog.info(f'Updated {tablename.__tablename__} table, {updAttr} column contents, to "{updVal}" {results} times')
            return results
        except Exception as e:
            session.rollback()
            if echo:
                applog.error(e)
            return(e)

def dbDeleteAll(engine:Engine, tablename:Base, echo:bool, trace:bool) -> int:
    '''
    Delete all records from table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary ColumnName Criteria
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return int - Number of records deleted
    :example - dbDeleteAll(engine, Customer, True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog') 
    with Session(engine) as session:
        if engine.name == 'sqlite':
            session.execute('pragma foreign_keys=on')
        try:
            results = session.query(tablename).delete()
            session.commit()
            if trace:
                datlog.info(f'Deleted {tablename.__tablename__} contents ... {results} entries')
            return results
        except Exception as e:
            session.rollback()
            if echo:
                applog.error(e)
            return(e)

# Record level functions
def dbInsert(engine:Engine, data:Base, echo:bool, trace:bool) -> int:
    '''
    Insert record into database table
    :param engine - SQLAlchemy session instance
    :param data - SQLALchemy data object 
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return int - RowId of inserted record
    :example - dbInsert(engine,Genre(GenreName='Screaming'),True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        if engine.name == 'sqlite':
            session.execute('pragma foreign_keys=on')
        try:
            session.add(data)
            session.commit()
            session.refresh(data)
            if trace:
                datlog.info(f'Added record number {data.Id} to {data.__tablename__}')
            return data.Id
        except Exception as e:
            session.rollback()
            if echo:
                applog.error(e)

def dbSelect(engine:Engine, tablename:Base, filters:dict, echo:bool, trace:bool) -> list:
    #TODO ORM to Dict{} is not elegant
    '''
    Select records from a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary {'ColumnName':'Criteria'}
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return data - Query results as list
    :example - x = dbSelect(engine, Customer, {'Country':'Brazil'}, True)
    '''
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        data = []
        results = session.query(tablename).filter_by(**filters).all()
        if len(results) > 0:
            for row in results:
                rowdict = {col: str(getattr(row,col)) for col in row.__table__.c.keys()}
                data.append(rowdict)
                if trace:
                    datlog.info(f'Selected ... {rowdict}')
            return data
        else:
            if trace:
                datlog.info(f'Missing ... {filters}')

def dbUpdate(engine:Engine, tablename:Base, filters:dict, updAttr:str, updVal:str, echo:bool, trace:bool) -> int:
    '''
    Update filtered records in a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary {'ColumnName':'Criteria' [,...]}
    :param updAttr - Table column to update
    :param updVal - New value for table column
    :param echo - Enable application logging
    :parma trace - Enable database logging
    :return results - Integer of update results processed
    :example - x = dbUpdate(engine, Customer, {'Country':'Brazil'}, 'City', 'My Town', True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        try:
            results = session.query(tablename).filter_by(**filters).update({updAttr:updVal})
            session.commit()
            if trace:
                datlog.info(f'Updated {tablename.__tablename__} table, {updAttr} column contents, to "{updVal}" {results} times')
            return results
        except Exception as e:
            session.rollback()
            if echo:
                applog.error(e)
            return e

def dbDelete(engine:Engine, tablename:Base, filters:dict, echo:bool, trace:bool) -> int:
    '''
    Delete records from a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary ColumnName Criteria
    :param echo - Enable application logging
    :param trace - Enable database logging
    :return int - Number of records deleted
    :example - dbDelete(engine, Customer, {'Country':'Brazil'}, True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        if engine.name == 'sqlite':
            session.execute('pragma foreign_keys=on')
        try:
            results = session.query(tablename).filter_by(**filters).delete()
            session.commit()
            if trace:
                datlog.info(f'Deleted {list(filters.keys())[0]} = {list(filters.values())[0]} from {tablename.__tablename__} table {results} times')
            return results
        except Exception as e:
            if echo:
                applog.error(e)
            return e       