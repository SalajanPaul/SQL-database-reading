import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='salajan_paul_sebastian_ebib',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `ebib_carte`"
        cursor.execute(sql)

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found in the `ebib_carte` table.")
finally:
    conn.close()