from flask import *
import pymysql

app=Flask(__name__)
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="moulik"

)
cursor= mydb.cursor()

@app.route("/",methods=["post","get"])
def signup():
    msg=""
    if request.method=="POST":
        u=request.form["uname"]
        r=request.form["roll_no"]
        e=request.form["email"]
        p=request.form["password"]
        try:
            cursor.execute("INSERT INTO signup SET username=%s,rollno=%s,email=%s,password=%s",(u,r,e,p))
            mydb.commit()
            msg=1
        except:
            msg=0
    return render_template("index.html",msgg=msg)
@app.route("/user")
def users():
    cursor.execute("SELECT * FROM signup")
    data=cursor.fetchall()
    return render_template("user.html",us=data)
@app.route("/editinfo",methods=["post","get"])
def editdata():
    a=request.args.get('id')
    if request.method=="POST":
        try:
            Username=request.form["username"]
            cursor.execute("UPDATE signup SET username=%s WHERE id=%s",(Username,a,))
            mydb.commit()
            return redirect("/user")
        except:
            return redirect("/user")
    cursor.execute("SELECT * FROM signup where id=%s",(a,))
    b=cursor.fetchone()
    return render_template("edit.html",mou=b)
@app.route("/delete")
def delete():
    userid=request.args.get('id')
    try:
        cursor.execute("DELETE FROM signup WHERE id=%s",(userid,))
        mydb.commit()
        return redirect("/user")
    except Exception as e:
        print(str(e))
        return redirect("/user")
if __name__=="__main__":
    app.run(debug=True)
