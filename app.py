from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = ''
mysql_db = 'quizzaroo'

db_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)

cursor = db_connection.cursor()

@app.route('/')
def opening():
    return render_template('start.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            if user[3] == password:
                # Password is correct, redirect to home
                return redirect(url_for('home'))
            else:
                # Password is incorrect
                error_message = "Invalid email or password. Please try again."
                return render_template('login.html', error_message=error_message)
        else:
            # User doesn't exist
            error_message = "User does not exist. Please sign up."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, email, password))
        db_connection.commit()

        return redirect(url_for('login'))
    return render_template('regis.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET', 'POST'])  # Allow both GET and POST methods for the '/join' endpoint
def join_quiz():
    if request.method == 'POST':
        nickname = request.form['nickname']  # Get the entered nickname from the form
        code = request.form['code']  # Get the entered code from the form

        # Process the form data and perform any necessary actions, such as validating the code
        # Redirect to the Quizz UI page if the code is valid
        return redirect(url_for('quizz'))

    return render_template('join.html')

@app.route('/quizz')
def quizz():
    return render_template('test.html')

@app.route('/logout')
def logout():
    return redirect(url_for('opening'))

if __name__ == "__main__":
    app.run(debug=True)