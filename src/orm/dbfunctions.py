import logging
from sqlalchemy import text
from sqlalchemy import text, exc
from src.orm.schema import Base

def get_attributes(model) -> dict:
    """
    RETURN all attributes from a SQLAlchemy object.
    :param model (object): SQLAlchemy object instance.
    :return dict: Dictionary containing all attributes.
    """
    # TODO Reverse these items
    data = {}
    for key, value in model.__dict__.items():
        if not key.startswith('_sa_'):
            data[key] = value
    return data

def dbBulkInsert(session, table:str, data:Base, echo:bool, trace:bool) -> int:
    """
    INSERT multiple records into database table
    :param session (session): SQLAlchemy session instance
    :param table (str): Database tablename 
    :param data (Base): SQLALchemy data object(s)
    :param echo (bool): Enable application logging
    :param trace (bool): Enable database logging
    :return int: Number of records inserted
    """
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    if session.bind.name == 'sqlite':
        session.execute(text('pragma foreign_keys=on'))
    try:
        session.bulk_insert_mappings(table, data)
        session.commit()
        if trace:
            datlog.info(f'{table.__tablename__} {data}')
        return len(data)
    except Exception as e:
        session.rollback()
        if echo:
            applog.error(e)
        return 0
    finally:
        session.close()

def dbInsert(session, data:Base, echo:bool, trace:bool) -> int:
    """
    INSERT record into database table
    :param session (session): SQLAlchemy session instance
    :param data (Base): SQLALchemy data object 
    :param echo (bool): Enable application logging
    :param trace (bool): Enable database logging
    :return int: RowId of inserted record
    """
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    if session.bind.name == 'sqlite':
        session.execute(text('pragma foreign_keys=on'))
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
        if trace:
            datlog.info(f'Added {data.Id} to {data.__tablename__}')
        return data.Id
    except exc.SQLAlchemyError as e:
        session.rollback()
        if echo:
            applog.error(e)
        return 0
    finally:
        session.close()

def dbSelect(session, table:Base, echo:bool, trace:bool, **kwargs) -> list:
    """
    SELECT query on the given table with optional filtering
    :param session (session): SQLAlchemy session object
    :param table (Base): Database tablename 
    :param echo (bool): Enable application logging
    :param trace (bool): Enable database logging
    :param kwargs (dict): Key-value pairs representing filter conditions (column_name=value)
    :return list: List of model instances if found, empty list otherwise.
    """
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    data = []
    if session.bind.name == 'sqlite':
        session.execute(text('pragma foreign_keys=on'))
    try:
        query = session.query(table)
        for key, value in kwargs.items():
            if '%' in value:
                query = query.filter(getattr(table, key).like(value))
            else:
                query = query.filter(getattr(table, key) == (value))
            for row in query.all():
                r = (get_attributes(row))
                data.append(r)   
                if trace:
                    datlog.info(f'Selected ... {r}')
        return data
    except exc.SQLAlchemyError as e:
        if echo:
            applog.error(e)
        return []
    finally:
        session.close()
    
def dbUpdate(session, table:Base, filter:dict, update:dict, echo:bool, trace:bool,) -> int:
    """
    UPDATE records in the database based on the given filter condition(s)
    :param session (session): SQLAlchemy session object
    :param table (Base): SQLAlchemy model class
    :param filter_kwargs (dict): Key-value pairs filter conditions (column_name=value)
    :param update_kwargs (dict): Key-value pairs update values (column_name=new_value)
    :return int: Number of updated records
    """
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    if session.bind.name == 'sqlite':
        session.execute(text('pragma foreign_keys=on'))
    try:
        query = session.query(table)
        for key, value in filter.items():
            if '%' in value:
                query = query.filter(getattr(table, key).like(value))
            else:
                query = query.filter(getattr(table, key) == value)
        updated = query.update(update, synchronize_session=False)
        session.commit()
        if trace and updated > 0:
            datlog.info(f'Updated {table.__tablename__} {updated} times')
        return updated
    except exc.SQLAlchemyError as e:
        if echo:
            applog.error(e)
        return 0
    finally:
        session.close()

def dbDelete(session, table:Base, echo:bool, trace:bool, **kwargs) -> int:
    """
    DELETE records from a database table
    :param session (session): SQLAlchemy session object
    :param table (Base): Database tablename 
    :param echo (bool): Enable application logging
    :param trace (bool): Enable database logging
    :param kwargs (dict): Key-value pairs representing filter conditions (column_name=value)
    :return int: Number of records deleted
    """
    applog = logging.getLogger('AppLog')
    datlog = logging.getLogger('DatLog')
    if session.bind.name == 'sqlite':
        session.execute(text('pragma foreign_keys=on'))
    try:
        query = session.query(table)
        for key, value in kwargs.items():
            if '%' in value:
                query = query.filter(getattr(table, key).like(value))
            else:
                query = query.filter(getattr(table, key) == (value))
        deleted = query.delete()
        session.commit()
        if trace and deleted > 0:
            datlog.info(f'Deleted {deleted} from {table.__tablename__}')
        return deleted
    except exc.SQLAlchemyError as e:
        if echo:
            applog.error(e)
        return 0
    finally:
        session.close()