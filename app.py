from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/downloads")
def downloads():
    return render_template("downloads.html")

@app.route("/V1.0.0patchnotes")
def v100patchnotes():
    return render_template("V1.0.0patchnotes.html")

@app.route("/V1.0.1patchnotes")
def v101patchnotes():
    return render_template("V1.0.1patchnotes.html")

@app.route("/V1.0.2patchnotes")
def v102patchnotes():
    return render_template("V1.0.2patchnotes.html")

@app.route("/V1.0.11patchnotes")
def v1011patchnotes():
    return render_template("V1.0.11patchnotes.html")

@app.route("/V1.1.0patchnotes")
def v110patchnotes():
    return render_template("V1.1.0patchnotes.html")

@app.route("/V1.2.0patchnotes")
def v120patchnotes():
    return render_template("V1.2.0patchnotes.html")

if __name__ == "__main__":
    app.run(debug=True)