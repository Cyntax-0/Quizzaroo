from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def opening():
    return render_template('start.html')

@app.route('/login')
def log_in():
    return render_template('login.html')

@app.route('/signup')
def sign_up():
    return render_template('regis.html')

@app.route('/join')
def join_quiz():
    return render_template('join.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)