from flask import Flask, jsonify, render_template, request,\
    url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/appdb'
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Model
class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text


# Flask WTF
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post_text = StringField('Post_Text', validators=[DataRequired()])


@app.route('/addpost', methods=['GET', 'POST'])
def add_post():
    postform = PostForm()
    print(request.method)
    # TODO: this block does not get executed...
    if request.method == 'POST':
        print('im in the post request')
        pf = Post(
            postform.title.data,
            postform.post_text.data,
        )
        db.session.add(pf)
        db.session.commit()
        return redirect(url_for('view_posts'))
    return render_template('post_form.html', postform=postform)


@app.route('/posts', methods=['GET', 'POST'])
def view_posts():
    posts = Post.query.all()
    print(posts)
    return render_template('view_posts.html', posts=posts)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route('/greet/<someName>')
def greet(someName):
    user_info = {'username': someName, 'age': 25}
    return render_template(
        'user_greet.html',
        user=user_info['username'],
        age=user_info['age'])


@app.route("/foo/<someId>")
def foo_url_arg(someId):
    return jsonify({"echo": someId})


@app.route('/form', methods=['POST', 'GET'])
def beer_data_form():
    if request.method == "POST":
        username = request.form['username']
        beer = request.form['beer']
        rating = request.form['rating']
        location = request.form['location']
        return redirect(url_for('ratebeer',
                                username=username,
                                beer=beer,
                                rating=rating,
                                location=location))
    return render_template("beer_form.html")


@app.route('/ratebeer', methods=['GET'])
def showbeer():
    username = request.args.get('username')
    beer = request.args.get('beer')
    rating = request.args.get('rating')
    location = request.args.get('location')
    return render_template(
        "show_beer_entry.html",
        username=username,
        beer=beer,
        rating=rating,
        location=location
    )


if __name__ == "__main__":
    manager.run()