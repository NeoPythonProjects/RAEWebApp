from flask import Flask, render_template
from wtforms import Form
from flask.views import MethodView

# the app needs a unique name, and __name__ is always unique
app = Flask(__name__)


# # function approach
# @app.route("/")
# def home():
#     return render_template("index.html")

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class Download(MethodView):

    def get(self):
        return render_template('download.html')


# if __name__ == "__main__":

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/download', view_func=Download.as_view('download'))

app.run(debug=True)
