import sqlite3

class Database:
    def __init__(self, db_path=r"D:/server_app_project/railway.db"):
        self.database = db_path

    def get_connection(self):
        """Create and return a new database connection."""
        try:
            return sqlite3.connect(self.database)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def fetch_all_railway_types(self):
        """Fetch all records from tb_railway_type."""
        sql = '''SELECT * FROM tb_railway_type'''
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [{"id_railway_type": row[0], "railway_type": row[1]} for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def fetch_all_stations(self):
        """Fetch all records from tb_station."""
        sql = '''SELECT * FROM tb_station'''
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [{"id_station": row[0], "station_name": row[1], "id_railway_type": row[2]} for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def fetch_all_evaluations(self):
        """Fetch all records from tb_evaluation."""
        sql = '''SELECT * FROM tb_evaluation'''
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [{
                    "id_evaluation": row[0],
                    "event": row[1],
                    "gyro_x": row[2],
                    "gyro_y": row[3],
                    "gyro_z": row[4],
                    "station_start": row[5],
                    "station_end": row[6],
                    "evaluation_date": row[7],
                    "evaluation_score": row[8]
                } for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def fetch_all_accounts(self):
        """Fetch all records from tb_account."""
        sql = '''SELECT * FROM tb_account'''
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [{
                    "id_account": row[0],
                    "email": row[1],
                    "username": row[2],
                    "password": row[3],
                    "firstname": row[4],
                    "lastname": row[5]
                } for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def fetch_all_model_testings(self):
        """Fetch all records from tb_model_testing."""
        sql = '''SELECT * FROM tb_model_testing'''
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [{
                    "id_model_testing": row[0],
                    "gyro_x": row[1],
                    "gyro_y": row[2],
                    "gyro_z": row[3],
                    "test_result": row[4],
                    "is_correct": row[5],
                    "correct_result": row[6]
                } for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

#------------------------------------INSERT------------------------------------#
    def insert_railway_type(self, railway_type):
        """Insert a new record into tb_railway_type."""
        sql = '''INSERT INTO tb_railway_type(railway_type) VALUES(?)'''
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (railway_type,))
            conn.commit()
            return cursor.lastrowid

    def insert_station(self, station_name, id_railway_type):
        """Insert a new record into tb_station."""
        sql = '''INSERT INTO tb_station(station_name, id_railway_type) VALUES(?, ?)'''
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (station_name, id_railway_type))
            conn.commit()
            return cursor.lastrowid

    def insert_evaluation(self, event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score):
        """Insert a new record into tb_evaluation."""
        sql = '''INSERT INTO tb_evaluation(
                    event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score
                ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (event, gyro_x, gyro_y, gyro_z, station_start, station_end, evaluation_date, evaluation_score))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

    def insert_account(self, email, username, password, firstname, lastname):
        """Insert a new record into tb_account."""
        sql = '''INSERT INTO tb_account(email, username, password, firstname, lastname) VALUES(?, ?, ?, ?, ?)'''
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (email, username, password, firstname, lastname))
            conn.commit()
            return cursor.lastrowid

    def insert_model_testing(self, gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result):
        """Insert a new record into tb_model_testing."""
        sql = '''INSERT INTO tb_model_testing(gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result) 
                VALUES(?, ?, ?, ?, ?, ?)'''
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, (gyro_x, gyro_y, gyro_z, test_result, is_correct, correct_result))
            conn.commit()
            return cursor.lastrowid
