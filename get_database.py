import sqlite3

def fetch_all_railway_types(conn):
    """Fetch all records from tb_railway_type."""
    sql = '''SELECT * FROM tb_railway_type'''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def fetch_all_stations(conn):
    """Fetch all records from tb_station."""
    sql = '''SELECT * FROM tb_station'''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def fetch_all_evaluations(conn):
    """Fetch all records from tb_evaluation."""
    sql = '''SELECT * FROM tb_evaluation'''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def fetch_all_accounts(conn):
    """Fetch all records from tb_account."""
    sql = '''SELECT * FROM tb_account'''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def fetch_all_model_testings(conn):
    """Fetch all records from tb_model_testing."""
    sql = '''SELECT * FROM tb_model_testing'''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def main():
    database = r"D:/server_app_project/railway.db"

    # Create a database connection
    conn = sqlite3.connect(database)

    # Fetch and display all data from each table
    if conn is not None:
        try:
            # Fetch and display tb_railway_type data
            railway_types = fetch_all_railway_types(conn)
            print("tb_railway_type:")
            for row in railway_types:
                print(row)

            # Fetch and display tb_station data
            stations = fetch_all_stations(conn)
            print("\ntb_station:")
            for row in stations:
                print(row)

            # Fetch and display tb_evaluation data
            evaluations = fetch_all_evaluations(conn)
            print("\ntb_evaluation:")
            for row in evaluations:
                print(row)

            # Fetch and display tb_account data
            accounts = fetch_all_accounts(conn)
            print("\ntb_account:")
            for row in accounts:
                print(row)

            # Fetch and display tb_model_testing data
            model_testings = fetch_all_model_testings(conn)
            print("\ntb_model_testing:")
            for row in model_testings:
                print(row)
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
