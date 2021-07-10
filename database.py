import mysql.connector
from mysql.connector import Error
import pandas as pd


class Database:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def serverConnect(self):
        connection = None
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 user=self.user,
                                                 password=self.password)
            print('Server connection successful')
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def dbConnect(self, dbname):
        connection = None
        try:
            connection = mysql.connector.connect(host=self.host,
                                                 user=self.user,
                                                 passwd=self.password,
                                                 database=dbname)
            print('Database connection Sucessful')
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def executeQuery(self, query, server=False,  dbname=''):
        if server:
            connection = self.serverConnect()
        else:
            connection = self.dbConnect(dbname)

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print('Query succesfully executed')
        except Error as err:
            print(f"Error: '{err}'")

    def readQuery(self, query, dbname):
        connection = self.dbConnect(dbname)
        cursor = connection.cursor()

        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print('Successfully  retrieved results')
            return result
        except Error as err:
            print(f"Error: '{err}'")


    @staticmethod
    def t0DataFrame(data, columns):
        result = []
        for line in data:
            result.append(line)
        dataframe = pd.DataFrame(result, columns= columns)
        return dataframe

