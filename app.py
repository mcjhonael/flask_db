from flask import Flask,request
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from os import environ

load_dotenv()

app=Flask(__name__)
# CORS(app)

app.config['MYSQL_HOST']=environ.get('MYSQL_HOST')
app.config['MYSQL_USER']=environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD']=environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB']=environ.get('MYSQL_DB')
app.config['MYSQL_PORT']=int(environ.get('MYSQL_PORT'))

mysql=MySQL(app)

# print(app.config)
# print("++++++")
# print(environ)

@app.route("/")
def inicio():
    return "hola desde la pagina de inicio"

@app.route("/departamentos",methods=["GET","POST"])
def gestion_departamentos():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM DEPARTAMENTOS")
        resultados=cur.fetchall()
        departamentos=[]
        for resultado in resultados:
            departamentos.append({
                "id":resultado[0],
                "nombre":resultado[1]
            })
        print(departamentos)

        return{
            "content":departamentos,
            "message":"Todos los departamentos"
        },200
    elif request.method=="POST":
        data=request.get_json()
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO DEPARTAMENTOS(NOMBRE) VALUES('%s')" % data['nombre'])
        mysql.connection.commit()

        print(data)
        return{
            "content":data,
            "message":"Departamento creado exitosamente"
        },201
@app.route("/departamento/<int:id>",methods=["GET","PUT","DELETE"])
def gestion_departamento(id):
    if request.method=="GET":
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM DEP ARTAMENTOS WHERE ID=%d" % id)
        resultado=cur.fetchall()
        print(resultado)

        return{
            "content":"",
            "message":""
        }   
    elif request.method=="PUT":
        return{
            "content":"",
            "message":""
        }
    elif request.method=="DELETE":
        return{
            "content":"",
            "message":""
        }
if __name__=="__main__":
    app.run(debug=True,port=5000)