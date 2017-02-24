from flask import Flask
from flask import make_response
import io
import matplotlib.pyplot as plt

from starfighter.simple_page import simple_page
from starfighter import data_access
from starfighter import models


app = Flask(__name__)
app.register_blueprint(simple_page)


def render_page():
    my_title = "Show me the databases:"

    my_text = ""
    for row in models.read_rows():
        my_text += row[0] + "<br/>"

    my_html = my_title + "<br/>" + my_text

    return my_html


@app.route("/db")
def db_page():
    return render_page()


@app.route("/map")
def simple():

    output = io.BytesIO()

    plt.plot([1, 23, 2, 4])
    plt.ylabel('some numbers')

    output = io.BytesIO()
    plt.savefig(output)

    response = make_response(output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    app.run()
