from flask import Flask, render_template, redirect, url_for, send_from_directory


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/download')
def download():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
    #return send_from_directory('static', 'files/test.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
