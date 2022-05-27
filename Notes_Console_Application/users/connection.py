import mysql.connector

def connect():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="notes_app",
        port=3308
    )
    cursor = database.cursor(buffered=True)

    return [database, cursor]