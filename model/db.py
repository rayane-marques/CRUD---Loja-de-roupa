import mysql.connector
from mysql.connector import errorcode


try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="loja"
    )
    print(f"\nConectado ao Banco de dados com sucesso. Aperte CTRL + C para parar o servidor")
    cursor = connection.cursor()

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha incorreto")
    else:
        print(err)
    