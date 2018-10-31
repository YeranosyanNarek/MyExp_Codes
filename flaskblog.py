from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3f840c1b8c50c10599a3e94685979b30'

data_temp = [
    {
        'author' : 'author1',
        'title': 'title1',
        'content': 'content1',
        'date_posted': 'April 1st, 2017'
    },

    {
        'author' : 'author2',
        'title': 'title2',
        'content': 'content2',
        'date_posted': 'April 2nd, 2017'
    },

    {
        'author' : 'author3',
        'title': 'title3',
        'content': 'content3',
        'date_posted': 'April 3rd, 2017'
    }


]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = data_temp, my_title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', my_title = "About")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form1 = LoginForm()
    return render_template('login.html', my_title = "Login", form = form1)


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form2 = RegistrationForm()
    return render_template('register.html', my_title = "Register", form = form2)


if __name__ == '__main__':
    app.run(debug=True)