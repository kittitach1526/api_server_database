import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_tables(conn):
    """Create tables in the SQLite database."""
    try:
        sql_create_tables = """
        CREATE TABLE IF NOT EXISTS tb_railway_type (
            id_railway_type INTEGER PRIMARY KEY,
            railway_type TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tb_station (
            id_station INTEGER PRIMARY KEY,
            station_name TEXT NOT NULL,
            id_railway_type INTEGER NOT NULL,
            FOREIGN KEY (id_railway_type) REFERENCES tb_railway_type (id_railway_type)
        );

        CREATE TABLE IF NOT EXISTS tb_evaluation (
            id_evaluation INTEGER PRIMARY KEY,
            event TEXT NOT NULL,
            gyro_x TEXT NOT NULL,
            gyro_y TEXT NOT NULL,
            gyro_z TEXT NOT NULL,
            station_start INTEGER NOT NULL,
            station_end INTEGER NOT NULL,
            evaluation_date TEXT NOT NULL,
            evaluation_score TEXT NOT NULL,
            FOREIGN KEY (station_start) REFERENCES tb_station (id_station),
            FOREIGN KEY (station_end) REFERENCES tb_station (id_station)
        );

        CREATE TABLE IF NOT EXISTS tb_account (
            id_account INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS tb_model_testing (
            id_model_testing INTEGER PRIMARY KEY,
            gyro_x TEXT NOT NULL,
            gyro_y TEXT NOT NULL,
            gyro_z TEXT NOT NULL,
            test_result TEXT NOT NULL,
            is_correct TEXT NOT NULL,
            correct_result TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.executescript(sql_create_tables)  # Use executescript for multiple statements
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def main():
    database = r"D:/RMUTT/_Project/code/_wab/api_server_database/railway.db"

    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

        

if __name__ == '__main__':
    main()
