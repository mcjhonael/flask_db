from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/")
def inicio():
    return "hola desde la pagina de inicio"

if __name__=="__main__":
    app.run(debug=True,port=5000)