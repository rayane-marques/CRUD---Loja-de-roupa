from flask import jsonify
from model.db import connection, cursor

class DeleteRoupaController:
    def execute(valuesResponse):
        print(valuesResponse)
        
        try:
            sql = "DELETE from roupa WHERE id = %s"

            cursor.execute(sql, (valuesResponse,))
            connection.commit()
            
            return jsonify({"message": "Roupa deletada"})
                 
            
        except Exception as err:
            return jsonify({"message": "Error >>>"+ str(err)})