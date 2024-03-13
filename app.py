from flask import Flask, request
from Controller import CreateRoupaController, ReadRoupaController, UpdateRoupaController, DeleteRoupaController

app = Flask(__name__);

# CRUD
# CREATE
@app.route("/criar-roupa",methods=['POST'])
def criar_roupa():
    if request.method == 'POST':
        response = request.get_json()
        result = CreateRoupaController.CreateRoupaController.execute(response)
        return result
 
 # READ
@app.route("/listar-roupa",methods=['GET'])
def listar_roupa():
    if request.method == 'GET':
        return ReadRoupaController.ReadRoupaController.execute()

# UPDATE
@app.route("/att-roupa", methods=['PUT'])
def att_roupa():
    if request.method == 'PUT':
        response = request.get_json()
        result = UpdateRoupaController.UpdateRoupaController.execute(response)
        return result

# DELETE  
@app.route("/del-roupa/<id>", methods=['DELETE'])
def del_roupa(id):
    if request.method == 'DELETE':
        result = DeleteRoupaController.DeleteRoupaController.execute(id)
        return result
             

if __name__ == "__main__":
    app.run(debug=True)
    
