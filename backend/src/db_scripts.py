from typing import Dict
from sqlalchemy import create_engine, text
from helpers import (
    _reformat_column_name,
    _reformat_table_name
    )

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


def create_db_tables(data: Dict):
    
    for key in data.keys():

        table_name = _reformat_table_name(key)
        stat_categories_dict = data[key].records[0].fields
        
        if not stat_categories_dict:
            raise Exception(f'{key} failed')
        
        column_type = " text,"
        column_name = [_reformat_column_name(key) + column_type for key in stat_categories_dict.keys()]
        column_name[-1] = column_name[-1].replace(',', '')
        columns = "".join(column_name)
        
        create_db_table_sql = f"""CREATE TABLE {table_name} ({columns})"""
        
        try:
            with engine.connect() as conn:
                conn.execute(text(create_db_table_sql))
                conn.commit()
                print(f'Table for {table_name} successfully created')
        except ConnectionError as error:
            print(error)
    
    conn.close()
        
        


def insert_data(data: Dict):
    
    pass
