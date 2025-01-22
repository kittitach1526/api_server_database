import sqlite3

def insert_railway_type(conn, railway_type):
    """Insert a new record into tb_railway_type."""
    sql = '''INSERT INTO tb_railway_type(railway_type) VALUES(?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (railway_type,))
    conn.commit()
    return cursor.lastrowid

def insert_station(conn, station_name, id_railway_type):
    """Insert a new record into tb_station."""
    sql = '''INSERT INTO tb_station(station_name, id_railway_type) VALUES(?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (station_name, id_railway_type))
    conn.commit()
    return cursor.lastrowid

def insert_evaluation(conn, event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score):
    """Insert a new record into tb_evaluation."""
    sql = '''INSERT INTO tb_evaluation(
                 event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score
             ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score))
    conn.commit()
    return cursor.lastrowid

def insert_account(conn, email, username, password, firstname, lastname):
    """Insert a new record into tb_account."""
    sql = '''INSERT INTO tb_account(email, username, password, firstname, lastname) VALUES(?, ?, ?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (email, username, password, firstname, lastname))
    conn.commit()
    return cursor.lastrowid

def insert_model_testing(conn, gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result):
    """Insert a new record into tb_model_testing."""
    sql = '''INSERT INTO tb_model_testing(gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result) 
             VALUES(?, ?, ?, ?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result))
    conn.commit()
    return cursor.lastrowid

def main():
    database = r"D:/server_app_project/railway.db"

    # Create a database connection
    conn = sqlite3.connect(database)

    # Example usage
    if conn is not None:
        try:
            # Insert data into tb_railway_type
            railway_type_id = insert_railway_type(conn, "High-Speed Railway")
            print(f"Inserted into tb_railway_type: {railway_type_id}")

            # Insert data into tb_station
            station_id = insert_station(conn, "Central Station", railway_type_id)
            print(f"Inserted into tb_station: {station_id}")

            # Insert data into tb_evaluation
            evaluation_id = insert_evaluation(
                conn, "Train Event A", "0.123", "0.456", "0.789", station_id, station_id, "2025-01-01", "90%"
            )
            print(f"Inserted into tb_evaluation: {evaluation_id}")

            # Insert data into tb_account
            account_id = insert_account(conn, "user@example.com", "username", "password123", "John", "Doe")
            print(f"Inserted into tb_account: {account_id}")

            # Insert data into tb_model_testing
            model_testing_id = insert_model_testing(
                conn, "0.123", "0.456", "0.789", "Test Passed", "True", "Test Passed"
            )
            print(f"Inserted into tb_model_testing: {model_testing_id}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
