import mysql.connector

def db_table_creation(query, contrasena, db_name=None):
    if db_name is not None:
        cnx = mysql.connector.connect(
            user="root", 
            password=contrasena, 
            host="127.0.0.1"
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
    else:
        cnx = mysql.connector.connect(
            user="root", 
            password=contrasena,
            host="127.0.0.1", 
            database=db_name
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cnx.close()
            
def insert_data(query,contrasena,db_name,tuple_list):
    cnx = mysql.connector.connect(
        user="root", 
        password=contrasena, 
        host="127.0.0.1", database=db_name)

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, tuple_list)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()