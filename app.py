from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from pymysql import cursors

app= Flask(__name__)
# MODIFICAN LO QUE SEA
mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema2123'
mysql.init_app(app)


@app.route('/')
def index():
    sql="INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'santu', 'santu@ciudad.com.ar', 'fotodesantu.jpg');"
    conn=mysql.connect()
    cursors=conn.cursor()
    cursors.execute(sql)
    conn.commit()
    
    return render_template('empleados/index.html')

if __name__=='__main__':
    app.run(debug=True)
