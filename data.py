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
    def write(self, df, table_name, if_exists = "replace"):
        df.to_sql(table_name, con = self.__engine, if_exists = if_exists)

    # fetch data
    def fetch(self, table_name, index_col = None, filter_column = None, filter_values = None):
        # read table from SQL
        df = self.read(table_name, index_col = index_col)

        # filter table with list of given filter
        if filter_column and filter_values and type(filter_values) == list:
            df = df[df[filter_column].isin(filter_values)]

        # clean dataframe
        df.drop(columns = ["index"], inplace = True)
        df.reset_index(drop = True, inplace = True)

        return df