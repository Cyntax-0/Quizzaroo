from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
import random

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

@app.route('/register', methods=['GET', 'POST'])
def register():
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
    if 'name' not in session:
        return redirect(url_for('login'))
    
    name = session.get('name')
    random_number = random.randint(10000, 99999)
    session['random_number'] = random_number
    return render_template('home.html', name=name, random_number=random_number)

@app.route('/leaderboard')
def leaderboard():
    if 'name' not in session:
        return redirect(url_for('login'))
    # Retrieve the scores from the SQL database table
    cursor.execute("SELECT * FROM respo ORDER BY score DESC")
    scores = cursor.fetchall()
    
    return render_template('lead.html', scores=scores)

@app.route('/back')
def back():
    return redirect(url_for('home'))

@app.route('/clear')
def clear():
    cursor.execute("TRUNCATE TABLE respo")
    db_connection.commit()
    return redirect(url_for('home'))

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        # Handle form submission
        nickname = request.form['nickname']
        code = request.form['code']
        
        # Check if the random number and code match
        random_number = session.get('random_number')
        if random_number == int(code):
            session['nickname'] = nickname
            return redirect(url_for('quizz'))
        else:
            error_message = "Invalid random number or code. Please try again."
            return render_template('join.html', error_message=error_message)
    else:
        return render_template('join.html')

@app.route('/quizz')
def quizz():
    if 'nickname' in session:
        nickname = session['nickname']
        return render_template('test.html', nickname=nickname)
    else:
        # Handle the case when the nickname is not in the session
        error_message = "Nickname not found in session. Please join the quiz first."
        return render_template('join.html', error_message=error_message)

@app.route('/score', methods=['POST'])
def score():
    if 'nickname' in session and 'score' in request.json:
        nickname = session['nickname']
        score = request.json['score']
        
        try:
            # Store the nickname and score in the database
            insert_query = "INSERT INTO respo (nickname, score) VALUES (%s, %s)"
            cursor.execute(insert_query, (nickname, score))
            db_connection.commit()
            
            return render_template('start.html')
        except mysql.connector.Error as error:
            print("Error inserting data into MySQL database:", error)
            # Handle the error, e.g., display an error message to the user
            error_message = "An error occurred while storing the score."
            return render_template('start.html', error_message=error_message)
    else:
        # Handle the case when the required data is not available
        error_message = "Nickname or score data is missing."
        return render_template('start.html', error_message=error_message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)