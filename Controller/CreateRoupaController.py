
from flask import jsonify
from model.db import connection, cursor

# insert into tabela (coluna, linha) values ('ana', 'joao');

class CreateRoupaController:
    def execute(valuesResponse):
        
        try:
            preco, tamanho, peca, descricao = valuesResponse["preco"], valuesResponse["tamanho"], valuesResponse["peca"], valuesResponse["descricao"]
            
            sql = "INSERT into roupa (preco, tamanho, peca, descricao) VALUES(%s,%s,%s,%s)"
            values = (preco, tamanho, peca, descricao)
            
            cursor.execute(sql,values)
            connection.commit()
            
            return jsonify(
                {"message": "Roupa criada - 201"}
            )
            
        except Exception as err:
            return jsonify(
                {"message": "Error >>> "+ str(err)}
            )
            