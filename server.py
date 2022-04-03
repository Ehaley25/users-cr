from socket import create_server
from flask import Flask,render_template,request, redirect
from users import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.show()
    print(users)
    return render_template("index.html", all_users = users)


@app.route('/create' ,methods = ["POST"])
def create():
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'emails':request.form['emails']
    }

    User.insert(data)
    return redirect('/show')

@app.route('/create')
def show():
    return render_template('create.html')

if __name__=="__main__":
    app.run(debug=True)