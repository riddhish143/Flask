from flask import Flask , render_template

#create a flask instance
app = Flask(__name__)

#create a app decorator
@app.route('/')

# def index():
#     return "<h1>This is first program of flask</h1>"

def index():
    name = 'Riddhish is the handsome guy'
    return render_template(template_name_or_list="index.html" , guy = name)

#localhost:5000/user/riddhish
@app.route('/user/<name>') 
def user(name):
    return render_template(template_name_or_list="user.html" , name = name)

@app.route('/riddhish')
def result():
    python_list = ['Riddhish','Ganesh','Mahajan']
    do_this = "bold this <strong> Riddhish </strong>"
    return render_template(template_name_or_list="index.html", do_this = do_this , python_list = python_list)   

# Custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#Internal server error
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html")