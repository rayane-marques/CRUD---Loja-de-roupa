from flask import jsonify
from model.db import connection, cursor

class UpdateRoupaController:
    def execute(valuesResponse):
        print(valuesResponse);
        try:
            preco, tamanho, peca, descricao, id = valuesResponse["preco"], valuesResponse["tamanho"], valuesResponse["peca"], valuesResponse["descricao"], valuesResponse["id"]
            
            sql = "UPDATE roupa SET preco = %s, tamanho = %s, peca = %s, descricao = %s WHERE id = %s"
            where = (preco, tamanho, peca, descricao, id)
            
            cursor.execute(sql, where)
            connection.commit()
            
            return jsonify({"message": "Atualização feita"})
        
        except Exception as err:
            return jsonify({"message": "Error >>> "+ str(err)})
    
    