from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = ''
mysql_db = 'quizzaroo'

try:
    db_connection = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_db
    )
    cursor = db_connection.cursor()
except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)

@app.route('/')
def opening():
    return render_template('start.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (name, email, password))
            db_connection.commit()
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL database:", error)

        return redirect(url_for('login'))
    return render_template('regis.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')

            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user:
                if user[3] == password:
                    # Password is correct, store user's name in session and redirect to home
                    session['name'] = user[1]
                    return redirect(url_for('home'))
                else:
                    # Password is incorrect
                    error_message = "Invalid email or password. Please try again."
                    return render_template('login.html', error_message=error_message)
            else:
                # User doesn't exist
                error_message = "User does not exist. Please sign up."
                return render_template('login.html', error_message=error_message)
        except mysql.connector.Error as error:
            print("Error executing MySQL query:", error)
            error_message = "An error occurred. Please try again later."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    name = session.get('name')
    return render_template('home.html', name=name)

@app.route('/join', methods=['GET', 'POST'])
def join_quiz():
    if request.method == 'POST':
        nickname = request.form['nickname']
        code = request.form['code']

        return redirect(url_for('quizz'))

    return render_template('join.html')

@app.route('/quizz')
def quizz():
    return render_template('test.html')

@app.route("/endQuiz")
def endQuiz():
    return redirect("/endQuiz")

@app.route('/logout')
def logout():
    return redirect(url_for('opening'))

if __name__ == "__main__":
    app.run(debug=True)