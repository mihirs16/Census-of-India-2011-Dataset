# imports
import pandas as pd
import sqlalchemy

# for handling database queries 
class Database:

    # private variables
    __engine = None
    __conn_str = None

    # initialize parameters
    def __init__(self, database, username, password, hostname, echo = False):
        self.__conn_str = f"mysql+pymysql://{username}:{password}@{hostname}/{database}"
        self.__engine = sqlalchemy.create_engine(self.__conn_str, echo = echo)

    # read DataFrame from SQL
    def read(self, table_name, index_col = None):
        df = pd.read_sql_table(table_name, self.__conn_str, index_col = index_col)
        return df

    # write DataFrame to SQL
    def write(self, df, table_name, if_exists = "replace", pipeline = None):
        if pipeline:
            for process in pipeline:
                df = process(df)
        df.to_sql(table_name, con = self.__engine, if_exists = if_exists)

