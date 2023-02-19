import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com",user="root",password="'\"-LhCB'.%k[4S]z",database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def insertProducts(list):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com",user="root",password="'\"-LhCB'.%k[4S]z",database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')

def getProducts():
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com",user="root",password="'\"-LhCB'.%k[4S]z",database="node_app")
    cursor = connection.cursor()

    cursor.execute("Select * From Products")

    result = cursor.fetchall()

    for product in result:
        print(f'id: {product[0]} name: {product[1]} price: {product[2]}')

def getProductById(id):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com",user="root",password="'\"-LhCB'.%k[4S]z",database="node_app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')