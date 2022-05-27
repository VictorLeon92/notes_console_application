import datetime
import hashlib
import users.connection as conn

connect = conn.connect()
database = connect[0]
cursor = connect[1]

class User:

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def register(self):
        date = datetime.datetime.now()

        hpassword = hashlib.sha256()
        hpassword.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.surname, self.email, hpassword.hexdigest(), date)
        
        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

        
    def identify(self):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        hpassword = hashlib.sha256()
        hpassword.update(self.password.encode('utf8'))

        user = (self.email, hpassword.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result