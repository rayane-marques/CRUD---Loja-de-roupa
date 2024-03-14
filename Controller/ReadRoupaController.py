from flask import jsonify
from model.db import cursor
import transformJSON

class ReadRoupaController:
    def execute():      
        try:      
            sql = "SELECT * FROM roupa"
                      
            cursor.execute(sql)
        
            results = cursor.fetchall()
            print(results)

            list = transformJSON.transformJSON(results)
            
            return jsonify(
                list
            )
            
        except Exception as err:
            return jsonify(
                {"message": "Error >>>"+ str(err)}
            )