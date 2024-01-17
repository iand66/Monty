import logging
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from orm.schema import *

# Table level functions
def dbInsertAll(engine:Session, tablename:str, data:Base, verbose:bool) -> int:
    #TODO Is this actually a session object?
    '''
    Insert multiple records into database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param data - SQLALchemy data objects
    :parma verbose - Enable verbose mode
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
            if verbose:
                datlog.info(f'{tablename.__tablename__} {data}')
            return len(data)
        except Exception as e:
            session.rollback()
            applog.error(e)
            return e

def dbSelectAll(engine:Session, tablename:Base, verbose:bool) -> list:
    #TODO ORM to Dict{} conversion is not elegant
    '''
    Select all records from a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param verbose - Enable verbose mode
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
                if verbose:
                    datlog.info(f'Selected ... {rowdict}')
                data.append(rowdict)
            return data
    except SQLAlchemyError as e:
        if verbose:
            applog.error(e)
        return e

def dbUpdateAll(engine:Session, tablename:Base, updAttr:str, updVal:str, verbose:bool) -> int:
    #TODO Is this actually a session object?
    '''
    Update records in a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param updAttr - Table column to update
    :param updVal - New value for table column
    :param verbose - Enable verbose mode
    :return results - Integer of update results processed
    :example - x = dbUpdateAll(engine, Customer, 'City', 'My Town', True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        try:
            results = session.query(tablename).update({updAttr:updVal})
            session.commit()
            if verbose:
                datlog.info(f'Updated {tablename.__tablename__} table, {updAttr} column contents, to "{updVal}" {results} times')
            return results
        except Exception as e:
            session.rollback()
            applog.error(e)
            return(e)

def dbDeleteAll(engine:Session, tablename:Base, verbose:bool) -> int:
    #TODO Is this actually a session object?
    '''
    Delete all records from table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary ColumnName Criteria
    :param verbose - Enable verbose mode
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
            if verbose:
                datlog.info(f'Deleted {tablename.__tablename__} contents ... {results} entries')
            return results
        except Exception as e:
            session.rollback()
            applog.error(e)
            return(e)

# Record level functions
def dbInsert(engine:Session, data:Base, verbose:bool) -> int:
    #TODO Is this actually a session object?
    '''
    Insert record into database table
    :param engine - SQLAlchemy session instance
    :param data - SQLALchemy data object 
    :param verbose - Enable verbose mode
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
            if verbose:
                datlog.info(f'Added record number {data.Id} to {data.__tablename__}')
            return data.Id
        except Exception as e:
            session.rollback()
            applog.error(e)

def dbSelect(engine:Session, tablename:Base, filters:dict, verbose:bool) -> list:
    #TODO Is this actually a session object?
    #TODO ORM to Dict{} is not elegant
    '''
    Select records from a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary {'ColumnName':'Criteria'}
    :param verbose - Enable verbose mode
    :return data - Query results as list
    :example - x = dbSelect(engine, Customer, {'Country':'Brazil' [,...]}, True)
    '''
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        data = []
        results = session.query(tablename).filter_by(**filters).all()
        if len(results) > 0:
            for row in results:
                rowdict = {col: str(getattr(row,col)) for col in row.__table__.c.keys()}
                data.append(rowdict)
                if verbose:
                    datlog.info(f'Selected ... {rowdict}')
            return data
        else:
            datlog.info(f'Missing ... {filters}')

def dbUpdate(engine:Session, tablename:Base, filters:dict, updAttr:str, updVal:str, verbose:bool) -> int:
    #TODO Is this actually a session object?
    '''
    Update filtered records in a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary {'ColumnName':'Criteria' [,...]}
    :param updAttr - Table column to update
    :param updVal - New value for table column
    :param verbose - Enable verbose mode
    :return results - Integer of update results processed
    :example - x = dbUpdate(engine, Customer, {'Country':'Brazil'}, 'City', 'My Town', True)
    '''
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    with Session(engine) as session:
        try:
            results = session.query(tablename).filter_by(**filters).update({updAttr:updVal})
            session.commit()
            if verbose:
                datlog.info(f'Updated {tablename.__tablename__} table, {updAttr} column contents, to "{updVal}" {results} times')
            return results
        except Exception as e:
            session.rollback()
            applog.error(e)
            return e

def dbDelete(engine:Session, tablename:Base, filters:dict, verbose:bool) -> int:
    #TODO Is this actually a session object?
    '''
    Delete records from a database table
    :param engine - SQLAlchemy session instance
    :param tablename - Database tablename 
    :param filters - Dictionary ColumnName Criteria
    :param verbose - Enable verbose mode
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
            if verbose:
                datlog.info(f'Deleted {list(filters.keys())[0]} = {list(filters.values())[0]} from {tablename.__tablename__} table {results} times')
            return results
        except Exception as e:
            applog.error(e)
            return e       