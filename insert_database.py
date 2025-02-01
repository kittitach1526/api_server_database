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
    database = r"D:/RMUTT/_Project/code/_wab/api_server_database/railway.db"

    # Create a database connection
    conn = sqlite3.connect(database)

    bts_sukhumvit_line = [
    "คูคต", "แยก คปอ.", "พิพิธภัณฑ์กองทัพอากาศ", "โรงพยาบาลภูมิพลอดุลยเดช", "สะพานใหม่",
    "สายหยุด", "พหลโยธิน 59", "วัดพระศรีมหาธาตุ", "กรมทหารราบที่ 11", "บางบัว",
    "กรมป่าไม้", "มหาวิทยาลัยเกษตรศาสตร์", "เสนานิคม", "รัชโยธิน", "พหลโยธิน 24",
    "ห้าแยกลาดพร้าว", "หมอชิต", "สะพานควาย", "อารีย์", "สนามเป้า",
    "อนุสาวรีย์ชัยสมรภูมิ", "พญาไท", "ราชเทวี", "สยาม", "ชิดลม",
    "เพลินจิต", "นานา", "อโศก", "พร้อมพงษ์", "ทองหล่อ",
    "เอกมัย", "พระโขนง", "อ่อนนุช", "บางจาก", "ปุณณวิถี",
    "อุดมสุข", "บางนา", "แบริ่ง", "สำโรง", "ปู่เจ้าฯ",
    "ช้างเอราวัณ", "โรงเรียนนายเรือ", "ปากน้ำ", "ศรีนครินทร์",
    "แพรกษา", "สายลวด", "เคหะฯ"
    ]

    MRT_blue = [
    "ท่าพระ","จรัญฯ 13","ไฟฉาย","บางขุนนนท์","บางยี่ขัน","สิรินธร","บางพลัด","บางอ้อ","บางโพ",
    "เตาปูน","บางซื่อ","กำแพงเพชร","สวนจตุจักร","พหลโยธิน","ลาดพร้าว","รัชดาภิเษก","สุทธิสาร",
    "ห้วยขวาง","ศูนย์วัฒนธรรมแห่งประเทศไทย","พระราม 9","เพชรบุรี","สุขุมวิท","ศูนย์การประชุมแห่งชาติสิริกิติ์",
    "คลองเตย","ลุมพินี","สีลม","สามย่าน","หัวลำโพง","วัดมังกร","สามยอด","สนามไชย","อิสรภาพ","บางไผ่",
    "บางหว้า","เพชรเกษม 48","ภาษีเจริญ","บางแค","หลักสอง"
    ]

    MRT_purple = [
    "คลองบางไผ่","ตลาดบางใหญ่","สามแยกบางใหญ่","บางพลู","บางรักใหญ่","บางรักน้อยท่าอิฐ","ไทรม้า","สะพานพระนั่งเกล้า",
    "แยกนนทบุรี 1","บางกระสอ","ศูนย์ราชการนนทบุรี","กระทรวงสาธารณสุข","แยกติวานนท์","วงศ์สว่าง","บางซ่อน","เตาปูน"
    ]

    MRT_pink = [
    "ศูนย์ราชการนนทบุรี","แคราย","สนามบินน้ำ","สามัคคี","กรมชลประทาน","แยกปากเกร็ด","เลี่ยงเมืองปากเกร็ด","แจ้งวัฒนะ-ปากเกร็ด 28","ศรีรัช",
    "เมืองทองธานี","แจ้งวัฒนะ 14","ศูนย์ราชการเฉลิมพระเกียรติ","โทรคมนาคมแห่งชาติ","หลักสี่","ราชภัฏพระนคร","วัดพระศรีมหาธาตุ","รามอินทรา 3",
    "ลาดปลาเค้า","รามอินทรา กม. 4","ไมลาภ","วัชรพล","รามอินทรา กม. 6","คู้บอน","รามอินทรา กม. 9","วงแหวนรามอินทรา","นพรัตน์",
    "บางชัน","เศรษฐบุตรบำเพ็ญ","ตลาดมีนบุรี","มีนบุรี","เมืองทองธานี","อิมแพ็ค เมืองทองธานี","ทะเลสาบเมืองทองธานี"
    ]

    # Example usage
    if conn is not None:
        try:
            # Insert data into tb_railway_type
            # railway_type_id = insert_railway_type(conn, "สายสีเขียว")
            # print(f"Inserted into tb_railway_type: {railway_type_id}")
            # railway_type_id = insert_railway_type(conn, "สายสีน้ำเงิน")
            # print(f"Inserted into tb_railway_type: {railway_type_id}")
            # railway_type_id = insert_railway_type(conn, "สายสีม่วง")
            # print(f"Inserted into tb_railway_type: {railway_type_id}")
            # railway_type_id = insert_railway_type(conn, "สายสีชมพู")
            # print(f"Inserted into tb_railway_type: {railway_type_id}")

            # Insert data into tb_station
            # for station in bts_sukhumvit_line:
            #     station_id = insert_station(conn, "สถานี"+station, 3)
            #     print(f"Inserted into tb_station: {station_id}")
            # for station in MRT_blue:
            #     station_id = insert_station(conn, "สถานี"+station, 3)
            #     print(f"Inserted into tb_station: {station_id}")
            # for station in MRT_purple:
            #     station_id = insert_station(conn, "สถานี"+station, 3)
            #     print(f"Inserted into tb_station: {station_id}")
            # for station in MRT_pink:
            #     station_id = insert_station(conn, "สถานี"+station, 4)
            #     print(f"Inserted into tb_station: {station_id}")    

            # Insert data into tb_evaluation
            evaluation_id = insert_evaluation(
                conn, "ออกตัว", "0.123", "0.456", "0.789", 1, 2, "2025-01-01", "2"
            )
            print(f"Inserted into tb_evaluation: {evaluation_id}")
            evaluation_id = insert_evaluation(
                conn, "เข้าโค้ง", "0.123", "0.456", "0.789", 1, 2, "2025-01-01", "2"
            )
            print(f"Inserted into tb_evaluation: {evaluation_id}")
            evaluation_id = insert_evaluation(
                conn, "เบรก", "0.123", "0.456", "0.789", 1, 2, "2025-01-01", "2"
            )
            print(f"Inserted into tb_evaluation: {evaluation_id}")
            # Insert data into tb_account
            # account_id = insert_account(conn, "admin@gmail.com", "admin", "12345678", "John", "Doe")
            # print(f"Inserted into tb_account: {account_id}")

            # Insert data into tb_model_testing
            # model_testing_id = insert_model_testing(
            #     conn, "0.123", "0.456", "0.789", "Test Passed", "True", "Test Passed"
            # )
            # print(f"Inserted into tb_model_testing: {model_testing_id}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
