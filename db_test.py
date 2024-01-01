import psycopg2
import argparse

def get_parser():

    parser = argparse.ArgumentParser(description='A simple script with command-line arguments.')

    parser.add_argument('--host', type=str)
    parser.add_argument('--port', type=int)
    parser.add_argument('--db_name', type=str)
    parser.add_argument('--user', type=str)
    parser.add_argument('--password', type=str)

    args = parser.parse_args()

    return args

class PostgreSQL_DB():
    
    def __init__(self, host, port, db_name, user, password):

        self.host = host
        self.port = port
        self.db_name = db_name
        self.user = user
        self.password = password

        print(' ==== DB Init! ====')
        print(' ==> Host:', self.host)
        print(' ==> Port:', self.port)
        print(' ==> DB name:', self.db_name)
        print(' ==> User:', self.user)
        print(' ==> Password:', self.password)
        print(' ================')

        self.__connect_db()
        self.__create_cursor()

    # Establish a connection to the PostgreSQL database
    def __connect_db(self):
        self.conn = psycopg2.connect(
            host = self.host,
            port = self.port,
            database = self.db_name,
            user = self.user,
            password = self.password
        )
        print(' ==> Connect to PostgreSQL!')

    # Create a cursor object to interact with the database
    def __create_cursor(self):
        self.cursor = self.conn.cursor()
        print(' ==> Create cursor!')

    # Fetch data from the table
    def run_selects(self, select_data_query, verbose=False):
        print(' ==> Select query:', select_data_query)

        self.cursor.execute(select_data_query)
        data = self.cursor.fetchall()

        if verbose:
            for row in data:
                print(row)
        
        return data

    # Run query
    def run_query(self, query):
        print(' ==> Run query:', query)
        self.cursor.execute(query)

    # Commit the changes
    def commit_db(self):
        self.conn.commit()

    # Rollback
    def rollback_db(self):
        self.conn.rollback()      

    # Close the cursor and connection
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print(' ==> Close DB!')

if __name__ == '__main__':
    
    # Params
    args = get_parser()

    # Connect PostgreSQL server
    DB = PostgreSQL_DB(args.host, args.port, args.db_name, args.user, args.password)

    # Create table
    table_name = args.table_name
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            user_id serial PRIMARY KEY,
            name VARCHAR (100) NOT NULL,
            email VARCHAR (100) UNIQUE NOT NULL,
            password VARCHAR (100) UNIQUE NOT NULL
        );
    '''
    DB.run_query(create_table_query)

    # Insert data
    user_id = 1
    name = 't'
    email = 'test@gmail.com'
    password = 'test'
    insert_query = f'''
        INSERT INTO {table_name}
            (user_id, name, email, password)
            VALUES ('{user_id}', '{name}', '{email}', '{password}'
        );
    '''
    # Insert error
    try:
        DB.run_query(insert_query)
        DB.commit_db()
    except Exception as e:
        print("Error:", e)
        DB.rollback_db()

    # Select data
    select_data_query = f'SELECT * FROM {table_name}'
    selects_data = DB.run_selects(select_data_query)
    print(' ==> Show all data:', selects_data)
