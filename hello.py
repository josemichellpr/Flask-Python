
from flask import Flask, render_template,request, redirect #Si no declaramos aquí, no funcionará lo que utilicemos como "request" ,"redirect", etcétera#
from flaskext.mysql import MySQL
from datetime import date,time, datetime

app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='comprar_clases'
mysql.init_app(app)


@app.route('/')#Esta probando sin esta línea, pero no funciona sin ella#
@app.route('/formulario')
def formulario ():
    """El archivo HTML debe estar forzosamente dentro de la carpeta "templates"
    porque si no, no sabe donde buscar"""
    conexion=mysql.connect
    print(conexion)
    return render_template('formulario.html')

@app.route('/templates/formulario/guardar',methods=['POST'])#LA RUTA QUE ESTÁ SIGUIENDO ES LA MISMA QUE ESTÁ EN EL MÉTODO "ACTION" DEL FORM QUE ESTÁ EN EL FORMULARIO DE HTML. Si quisieras enviar archivos como imagenes, dentro del <form> debes poner enctype='multipart/form-data'
def templates_formulario_guardar():
    
    _name=request.form['name']#Aquí se le ordena a Python que guarde en la variable "name" lo que RECOLECTE de name=name en el archivo HTML#
    _apellido=request.form['apellido']
    _email=request.form['email']
    _telefono=request.form['telefono']
    _now=datetime.now()
    _fechareg=_now.strftime("%a %b %y")
    sql="INSERT INTO `contacto` (`nombre`, `apellido`, `e-mail`, `telefono`, `fechareg`) VALUES (%s,%s,%s,%s,%s);"
    datos=(_name,_apellido,_email,_telefono,_fechareg)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    print(_name) #Lo que se le dice es pinta por pantalla lo que contenga la variable name (que es el nombre de la persona que se apunta en el formulario). Para ir paso a paso y ver que información es la que se enviará a la base de datos#
    return redirect('/formulario')#Aquí puedes poner la página que quieras. Así como "te has registrado correctamente" o algo así#

    """
    Para correr el programa
    PRIMERO : flask run --app hello
    SEGUNDO : flask --app hello --debug run
    """