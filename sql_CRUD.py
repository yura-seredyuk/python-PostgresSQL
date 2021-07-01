import psycopg2
from psycopg2 import Error
from settings import *

try:
    connection = psycopg2.connect(user = USER, 
                                password = PASSWORD, 
                                host = HOST, 
                                port = PORT,
                                database = 'py_db')

    cursor = connection.cursor()

    # ---------------------------------
    # print('Server information:')
    # print(connection.get_dsn_parameters())
    # cursor.execute('SELECT version()')
    # # print(cursor.fetchmany(size=2))
    # print(cursor.fetchone())
    # ---------------------------------

    # create_teble_query = '''CREATE TABLE IF NOT EXISTS mobile
    #                     (  id INT PRIMARY KEY NOT NULL,
    #                     model TEXT            NOT NULL,
    #                     price REAL);'''

    # cursor.execute(create_teble_query)
    # connection.commit()
    # print('Table mobile was created!')

    #--------------------------------------

    insert_query = """INSERT INTO mobile (id, model, price) VALUES (1, 'Nokia', 1100)"""
    cursor.execute(insert_query)
    connection.commit()
    print("Table was updated!")

    select_query = """SELECT * FROM mobile"""
    cursor.execute(select_query)
    connection.commit()
    print("Result: ",cursor.fetchone())

    update_query = """UPDATE mobile SET price = 1500 WHERE id = 1"""
    cursor.execute(update_query)
    connection.commit()
    print("Information was updated!")

    delete_query = """DELETE FROM mobile WHERE id = 1"""
    cursor.execute(delete_query)
    connection.commit()
    print("Information was deleted!")


except(Exception, Error) as error:
    print("Error connection", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection was closed!")