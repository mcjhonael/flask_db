from flask import Flask,request
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from os import environ

load_dotenv()

app=Flask(__name__)
CORS(app=app)

app.config['MYSQL_HOST']=environ.get('MYSQL_HOST')
app.config['MYSQL_USER']=environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD']=environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB']=environ.get('MYSQL_DB')
app.config['MYSQL_PORT']=int(environ.get('MYSQL_PORT'))

mysql=MySQL(app)

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
        return{
            "content":departamentos,
            "message":"Todos los departamentos"
        },200
    elif request.method=="POST":
        data=request.get_json()
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO DEPARTAMENTOS(NOMBRE) VALUES('%s')" % data['nombre'])
        mysql.connection.commit()
        return{
            "content":data,
            "message":"Departamento creado exitosamente"
        },201
    
@app.route("/departamento/<int:id>",methods=["GET","PUT","DELETE"])
def gestion_departamento(id):
    if request.method=="GET":
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM DEPARTAMENTOS WHERE ID=%d" % id)
        resultado=cur.fetchone()
        if resultado is None:
            return{
                "content":None,
                "message":"Departamento no encontrado"
            },404
        departamento={
            "id":resultado[0],
            "nombre":resultado[1]
        }
        return{
            "content":departamento,
            "message":"Departamentos actualizado"
        },200
    
    elif request.method=="PUT":
        data=request.get_json()
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM DEPARTAMENTOS WHERE ID=%d' % id)
        resultado=cur.fetchone()
        if resultado is None:
            return{
                "content":None,
                "message":"Departamento no encontrado"
            },404
        cur.execute("UPDATE DEPARTAMENTOS SET NOMBRE='%s' WHERE ID=%d" % (data['nombre'],id))
        mysql.connection.commit()
        print("paso normal")
        return{
            "content":data,
            "message":"Departamento actualizado"
        },201
    elif request.method=="DELETE":
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM DEPARTAMENTOS WHERE ID=%d" % id)
        resultado=cur.fetchone()
        if resultado is None:
            return{
                "content":None,
                "message":"Departamentos no encontrado"
            }
        cur.execute("DELETE FROM DEPARTAMENTO WHERE ID=%d" % id)
        mysql.connection.commit()
        return{
            "content":None,
            "message":"Departamento eliminado"
        },204
if __name__=="__main__":
    app.run(debug=True,port=5000)