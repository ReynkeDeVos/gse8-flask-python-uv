import os

from flask import Flask, render_template, request

from main import create_greeting

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    first_name = ""
    last_name = ""
    errors = {}
    greeting = None

    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()

        if not first_name:
            errors["first_name"] = "Bitte gib einen Vornamen ein."
        if not last_name:
            errors["last_name"] = "Bitte gib einen Nachnamen ein."

        if not errors:
            greeting = create_greeting(first_name, last_name)

    return render_template(
        "index.html",
        errors=errors,
        first_name=first_name,
        greeting=greeting,
        last_name=last_name,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
