import mysql.connector
from mysql.connector import Error
import pandas as pd


def serverConnect(host_name, user_name, password):
    connection = None
    try:
        connection = mysql.connector.connect(host= host_name, user= user_name, password= password)
        print('MySQL server connection successfull')
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def dbConnect(host_name, user_name, password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(host = host_name,
                                            user= user_name,
                                            passwd = password,
                                            database = db_name)
        print('Database connection Sucessful')
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def executeQuery(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Query succesfully executed')
    except Error as err:
        print(f"Error: '{err}'")


def readQuery(connection, query):
    cursor = connection.cursor()
    result = None
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print('Successfully  retrieved results')
        return result
    except Error as err:
        print(f"Error: '{err}'")
    return result
    

# password = '10041225'
# connection = serverConnect('localhost', 'root', password)

# create new database
# db_query = "Create database Projects"  # query to create database
# executeQuery(connection, db_query)

# # create a new table with values
# query = '''Create table products(
#                         SN int primary key,
#                         product  varchar(20) not null,
#                         serial_code varchar(13) not null,
#                         mnfg_date date,
#                         exp_date date,
#                         price float,
#                         used varchar(6) not null);
#            '''
# connection = dbConnect('localhost', 'root', password, 'projects')
# execute_query(connection, query)


# # insert data into created table
# query = """insert into products values
#            (1, 'LaFaire', '109673462846', '2019-01-12', '2021-07-20', 12500, 'false'),
#            (2, 'LaFaire', '119873452946', '2017-01-12', '2019-07-20', 12500, 'true'),
#            (3, 'LaFaire', '139773482866', '2019-12-12', '2021-12-20', 12500, 'false'),
#            (4, 'LaFaire', '159633452846', '2017-05-12', '2019-12-20', 12500, 'false'),
#            (5, 'LaFaire', '129643566866', '2019-01-12', '2021-07-20', 12500, 'false');
#           """
# execute_query(connection, query)


# execute_query(connection, 'drop table products')


# query = """
#          select * from products;
#         """
# data = []
# results = readQuery(connection, query)
# for result in results:
#     data.append(result)
# columns = ['S/N', 'product', 'serial code','mnfg_data', 'exp_date', 'price', 'used']
# df = pd.DataFrame(data, columns= columns)
# df

# # test data availability in dataframe
# str(109673462846) in df['serial code'].values

# get serial code column from database
# query = """
#          select serial_code from products;
#         """
# results = readQuery(connection, query)
# for result in results:
#     print(result)

# get data from database table
# query = """
#          select exp_date from products;
#         """
# results = readQuery(connection, query)
# for result in results:
#     print(result)


# # update table in database
# query = """
#             update products
#             set used = 'true'
#             where SN =3
#           """
# execute_query(connection, query)


# # get data from dataframe
# query = """
#          select * from products;
#         """
# data = []
# results = readQuery(connection, query)
# for result in results:
#     data.append(result)
# columns = ['S/N', 'product', 'serial code','mnfg_data', 'exp_date', 'price', 'used']
# df = pd.DataFrame(data, columns= columns)
# df

