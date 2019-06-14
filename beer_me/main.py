from flask import Flask, request, \
    render_template, url_for, redirect
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route('/greet')
def greet():
    user_info = {'username': 'Josh', 'age': "20"}
    return render_template(
        'user_greet.html',
        user=user_info['username'],
        age=user_info['age'])


if __name__ == "__main__":
    app.run(debug=True, port=8080)