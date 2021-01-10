from flask import Flask , redirect, render_template, request, make_response, session
from flask_session import Session

# create an instance form the Flask class
# this object will pass all the requests from the clinet and hangle them using Web Server Gateway Interface (WSGI)
app = Flask(__name__)
app.config["SESSION_PREMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# define a route 
# a route is just assciation or mapping between the URL requests and the function that handle it
@app.route("/user/<name>") # this is a decorator , a standard pyhton feature to link a function to be invoked when certain events occur
def tasks(name): # this is called view funciton 
    if "todos" not in session:
        session["todos"] = []
    response = make_response(render_template("task.html", todos=session["todos"], name=name), 200)
    return response

# other way to define a route 
# def tasks():
#     return render_template("task.html", todos=todos)

# app.add_url_rule('/', 'tasks', tasks)

@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template("new.html")
    else:
        todo = request.form.get("task")
        session["todos"].append(todo)
        return redirect('/user/<name>')