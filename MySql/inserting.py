import mysql.connector


def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com",
                                         user="root",
                                         password="'\"-LhCB'.%k[4S]z",
                                         database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın adı: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:", err)
    finally:
        connection.close()
        print("dataabase bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host="db-technostudy.ckr1jisflxpv.us-east-1.rds.amazonaws.com",
                                         user="root",
                                         password="'\"-LhCB'.%k[4S]z",
                                         database="node_app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın adı: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:", err)
    finally:
        connection.close()
        print("dataabase bağlantısı kapandı.")


list = []
while True:
    name = input("ürün adı:")
    price = float(input("ürün fiyatı:"))
    imageUrl = input("ürün resim adı:")
    description = input("ürün açıklaması:")

    list.append((name, price, imageUrl, description))

    result = input("devam etmek istiyormusunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız veritabanına ekleniyor...")
        print(list)
        insertProducts(list)
        break

# insertProduct(name,price,imageUrl,description)
