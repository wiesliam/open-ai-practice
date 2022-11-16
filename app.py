import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        color = request.form["color"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(color),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(color):
    return """Write a poem using this color.

Color: Blue
Poem: The deep indigo sea waved its sullen goodbye
Color: Crimson
Poem: Bloody skies opened into red shade
Color: {}
Poem:""".format(
        color.capitalize()
    )
