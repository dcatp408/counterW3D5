from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "something "


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def add_one():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    print(session['counter'])
    return redirect('/')


@app.route("/reset", methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
