
from flask import *
from appdb import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/reg")
def register():
    return render_template("signup.html")

@app.route("/log")
def login():
    return render_template("login.html")

@app.route("/task")
def t_ask():
    return render_template("task.html")

@app.route('/addUser',methods=['POST'])
def newuser():
    email=request.form['email']
    passw=request.form['passw']
    cpassw=request.form['cpassw']

    t=(email,passw,cpassw)
    addUser(t)
    return redirect("about") #need to redirect somewhere else this is only for demo

@app.route("/validUser",methods=['POST'])
def auth():
    email=request.form['email']
    passw=request.form['passw']
    t=(email,passw)
    authen=validUser()
    if (t in authen):
        return render_template("about.html") #need to redirect somewhere else this is only for demo
    else:
        error="Invalid Credentials.....Please Try Again"
        return render_template("login.html",error=error)

@app.route("/tasklist")
def t_asklist():
    data=allData()
    return render_template("tasklist.html",elist=data)

@app.route("/addTask",methods=['POST'])
def add_task():
    title=request.form['title']
    description=request.form['description']
    t=(title,description)
    addTask(t)
    return redirect("tasklist")

@app.route("/delete")
def dele():
    title=request.args.get("title")
    delData(title)
    return redirect("tasklist")

@app.route("/edit")
def edit_task():
    title=request.args.get("title")
    data=selectTask(title)
    return render_template("updatetask.html",row=data)

@app.route("/updateTask",methods=['POST'])
def update_task():
    title=request.form['title']
    description=request.form['description']
    t=(description,title)
    updateTask(t)
    return redirect("tasklist")

@app.route("/about")
def abouttask():
    return render_template("about.html")






if(__name__=="__main__"):
    app.run(debug=True,port=7000)
