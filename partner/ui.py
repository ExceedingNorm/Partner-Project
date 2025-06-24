"""Flask-based web UI for Partner app."""
from flask import Flask, render_template, request, redirect, url_for
from .llm import LLMClient


app = Flask(__name__)
llm_client = LLMClient()


@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            response = llm_client.generate(prompt)
    return render_template("index.html", response=response)


def run(host: str = "0.0.0.0", port: int = 5000) -> None:
    app.run(host=host, port=port)

