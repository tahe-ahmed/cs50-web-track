from flask import Flask , redirect, render_template, request, make_response

# create an instance form the Flask class
# this object will pass all the requests from the clinet and hangle them using Web Server Gateway Interface (WSGI)
app = Flask(__name__)

todos = []

# define a route 
# a route is just assciation or mapping between the URL requests and the function that handle it
@app.route("/user/<name>") # this is a decorator , a standard pyhton feature to link a function to be invoked when certain events occur
def tasks(name): # this is called view funciton 
    response = make_response(render_template("task.html", todos=todos, name=name), 200)
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
        todos.append(todo)
        return redirect('/user/<name>')