from flask import Flask,render_template,request,url_for,flash,redirect
import mysql.connector
cnx=mysql.connector.connect(user='root',host='localhost',database='stud_data')

app = Flask(__name__)
app.secret_key=('Jay Shri Ram')

@app.route('/')
def index():
    cur = cnx.cursor()
    cur.execute('SELECT * FROM students')
    data = cur.fetchall()
    cur.close()
    print(data)
    return render_template('index.html', data=data)

@app.route('/insert' , methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        cur=cnx.cursor()
        cur.execute('insert into stud_data.students (name,email,mobile) values (%s,%s,%s)',(name,email,mobile))
        cnx.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id>' , methods = ['GET'])
def delete(id):
    flash('Record has been deleted successfully')
    cur=cnx.cursor()
    cur.execute('DELETE FROM stud_data.students where id=%s',(id,))
    cnx.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>' , methods = ['POST','GET'])
def update(id):
    if request.method=='POST':
        id=request.form['id']
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']

        cur=cnx.cursor()
        cur.execute('update students set name=%s,email=%s,mobile=%s where id=%s',(name,email,mobile,id))
        cnx.commit()
        flash('Data has been updates')
        return redirect(url_for('index'))
    else:
        cur = cnx.cursor()
        cur.execute('SELECT * FROM students WHERE id=%s', (id,))
        data = cur.fetchone()
        cur.close()
        return render_template('update.html', row=data)
   
if __name__ == '__main__':
    app.run(debug=True)