from sqlalchemy import exc

from src.helper import applog, datlog, trace
from src.orm.schema import Base

# RETURN all attributes from a SQLAlchemy object.
def get_attributes(model) -> dict:
    """
    RETURN all attributes from a SQLAlchemy object.
    :param model (object): SQLAlchemy object instance.
    :return dict: Dictionary containing all attributes.
    """
    data = {}
    for column in model.__table__.columns:
        if not column.key.startswith("_sa_"):
            data[column.key] = getattr(model, column.key)
    return data

# INSERT multiple records into database table
def dbBulkInsert(session, table: str, data: Base) -> int:
    """
    INSERT multiple records into database table
    :param session (session): SQLAlchemy session instance
    :param table (str): Database tablename
    :param data (Base): SQLALchemy data object(s)
    :return int: Number of records inserted
    """
    try:
        session.bulk_insert_mappings(table, data)
        session.commit()
        if trace:
            datlog.info(f"Added {table.__tablename__} {data}")
        return len(data)
    except Exception as e:
        session.rollback()
        applog.error(e)
        return 0
    finally:
        session.close()

# INSERT record into database table
def dbInsert(session, data: Base) -> bool:
    """
    INSERT record into database table
    :param session (session): SQLAlchemy session instance
    :param data (Base): SQLALchemy data object
    :return int: RowId of inserted record
    """
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
        if trace:
            datlog.info(f"Added {data.Id} to {data.__tablename__}")
        return True
    except exc.SQLAlchemyError as e:
        session.rollback()
        applog.error(e)
        return False
    finally:
        session.close()

# SELECT query on the given table with optional filtering
def dbSelect(session, table: Base, **kwargs) -> list:
    """
    SELECT query on the given table with optional filtering
    :param session (session): SQLAlchemy session object
    :param table (object): Database tablename
    :param kwargs (dict): Key-value pairs representing filter conditions (column_name=value)
    :return list: List of model instances if found, empty list otherwise.
    """
    data = []
    try:
        query = session.query(table)
        for key, value in kwargs.items():
            if isinstance(value, str) and "%" in value:
                query = query.filter(getattr(table, key).like(value))
            else:
                query = query.filter(getattr(table, key) == (value))
        result = query.all()
        for row in result:
            r = get_attributes(row)
            data.append(r)
            if trace:
                datlog.info(f"Selected ... {r}")
        return data
    except exc.SQLAlchemyError as e:
        applog.error(e)
        return []
    finally:
        session.close()

# UPDATE records in the database based on the given filter condition(s)
def dbUpdate(session, table: Base, filter: dict, update: dict) -> bool:
    """
    UPDATE records in the database based on the given filter condition(s)
    :param session (session): SQLAlchemy session object
    :param table (object): SQLAlchemy model class
    :param filter_kwargs (dict): Key-value pairs filter conditions (column_name=value)
    :param update_kwargs (dict): Key-value pairs update values (column_name=new_value)
    :return int: Number of updated records
    """
    try:
        query = session.query(table)
        for key, value in filter.items():
            if isinstance(value, str) and "%" in value:
                query = query.filter(getattr(table, key).like(value))
            else:
                query = query.filter(getattr(table, key) == value)
        updated = query.update(update, synchronize_session=False)
        session.commit()
        if trace and updated > 0:
            datlog.info(f"Updated {table.__tablename__} {updated} times")
        return True
    except exc.SQLAlchemyError as e:
        applog.error(e)
        return False
    finally:
        session.close()

# DELETE records from a database table
def dbDelete(session, table: Base, **kwargs) -> bool:
    """
    DELETE records from a database table
    :param session (session): SQLAlchemy session object
    :param table (object): Database tablename
    :param kwargs (dict): Key-value pairs representing filter conditions (column_name=value)
    :return int: Number of records deleted
    """
    try:
        query = session.query(table)
        for key, value in kwargs.items():
            if isinstance(value, str) and "%" in value:
                query = query.filter(getattr(table, key).like(value))
            else:
                query = query.filter(getattr(table, key) == (value))
        deleted = query.delete()
        session.commit()
        if deleted > 0:
            if trace:
                datlog.info(f"Deleted {deleted} from {table.__tablename__}")
            return True
        else:
            return False
    except exc.SQLAlchemyError as e:
        applog.error(e)
        return False
    finally:
        session.close()
