
from flask import jsonify


class CreateRoupaController:
    def execute(valuesResponse):
        
        try:
            id, preco, tamanho, peca, descricao = valuesResponse["id"], valuesResponse["preco"], valuesResponse["tamanho"], valuesResponse["peca"], valuesResponse["descricao"]
            print(id, preco, tamanho, peca, descricao)
            return jsonify(
                {"message": "Roupa criada - 201"}
            )
            
        except Exception as err:
            return jsonify(
                {"message": "Error >>> "+ str(err)}
            )