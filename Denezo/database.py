import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        if not self.connection:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            except Error as e:
                self.connection = None

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None

    def query(self, sql, params=None):
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(sql, params)
            result = cursor.fetchall()
            return result
        except Error as e:
            return None
        finally:
            cursor.close()

    def execute(self, sql, params=None):
        self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, params)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            self.connection.rollback()
            return None
        finally:
            cursor.close()
    
