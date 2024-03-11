from flask import Flask, request
from Controller import CreateRoupaController

app = Flask(__name__);

# CRUD
# CREATE
@app.route("/criar-roupa",methods=['POST'])
def criar_roupa():
    response = request.get_json()
    return CreateRoupaController.CreateRoupaController.execute(response)
    
if __name__ == "__main__":
    app.run(debug=True)
    
