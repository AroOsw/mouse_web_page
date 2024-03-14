from flask import Flask, render_template, redirect, url_for, send_from_directory


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/download')
def download():
    return redirect("https://youtube.com/clip/Ugkxl0jWzQSdMoxlDB9xwD5652OEKyJ0RYRp?si=GYJ0Q8fGvk2JLxIk")
    #return send_from_directory('static', 'files/test.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
