import pymysql

def getData(url, user, password, dbname, sql):
    db = pymysql.connect(url, user, password, dbname)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def flushDB(url, user, password, dbname, sql):
    db = pymysql.connect(url, user, password, dbname)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
