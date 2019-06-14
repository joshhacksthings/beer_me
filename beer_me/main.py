import os

from flask import Flask, jsonify, render_template, request,\
    url_for, redirect
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
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
        return render_template("bio_form.html")

    @app.route('/ratebeer', methods=['GET'])
    def showbio():
        username = request.args.get('username')
        beer = request.args.get('beer')
        rating = request.args.get('rating')
        location = request.args.get('location')
        return render_template("show_bio.html",
                               username=username,
                               beer=beer,
                               rating=rating,
                               location=location
                               )

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)