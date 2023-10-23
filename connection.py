import mysql.connector 

config = {
    'user': 'root',
    'password': 'k0rn82...',
    'database': 'ucorrespondencia',
    'host': 'localhost',
    'autocommit': True,
}

def getConnection():
    try:
        cnx = mysql.connector.connect(**config)
        if cnx and cnx.is_connected():
            return cnx
    except mysql.connector.Error as e:
        return e