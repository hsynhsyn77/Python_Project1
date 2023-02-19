import mysql.connector


def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com", user="root",
                                         password="'\"-LhCB'.%k[4S]z", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)

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
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com", user="root",
                                         password="'\"-LhCB'.%k[4S]z", database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql, values)

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
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com", user="root",
                                         password="'\"-LhCB'.%k[4S]z", database="node_app")
    cursor = connection.cursor()

    #sql = "Select * From products"
    #sql = "Select * From categories"
    #sql = "Select * From products inner join categories on categories.id=products.categoryid"
    #sql = "Select products.name,products.price,categories.name From products inner join categories on categories.id=products.categoryid"
    #sql = "Select products.name,products.price,categories.name From products inner join categories on categories.id=products.categoryid where categories.name='Telefon'"
    sql = "Select p.name,p.price,c.name From products as p inner join categories as c on c.id=p.categoryid where p.name='Iphone x'"

    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for product in result:
            print(product)

    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


def getProductById(id):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com", user="root",
                                         password="'\"-LhCB'.%k[4S]z", database="node_app")
    cursor = connection.cursor()

    sql = "Select * From products Where id=%s"
    params = (id,)

    cursor.execute(sql, params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')


def updateProduct(id, name, price):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com", user="root",
                                         password="'\"-LhCB'.%k[4S]z", database="node_app")
    cursor = connection.cursor()

    sql = "Update products Set name= %s, price= %s where id= %s"
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt güncellendi')
    except mysql.connector.Error as err:
        print('hata:', err)
    finally:
        connection.close()
        print('database bağlantısı kapandı.')


getProducts()
