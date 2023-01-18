import mysql.connector


def mySqlConn(host, user, pwd):
    return mysql.connector.connect(host=host, user=user, password=pwd)


def mySqlQuery(db, query):
    cursor = db.cursor()
    cursor.execute(query)


def mySqlSelect(db, From):
    mySqlQuery(db, "SELECT * FROM " + From)
