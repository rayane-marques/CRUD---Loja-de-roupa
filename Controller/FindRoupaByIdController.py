from flask import jsonify
from model.db import cursor
import transformJSON

class FindRoupaByIdController:
    def execute(id):    
        try:
            sql = "SELECT * FROM roupa WHERE id = %s"
            cursor.execute(sql, (id,))
            
            results = cursor.fetchall()

            list = transformJSON.transformJSON(results)
            
            if list:
                return jsonify(list)
            
            else:
                return {"message": "Não existe"}
            
        except Exception as err:
            return jsonify({"message": "Error >>>"+ str(err)})
