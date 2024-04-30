import mysql.connector

try:
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="quizzaroo"
    )

    mycursor = mydb.cursor()

    # Define the SQL query to create the table
    sql = "CREATE TABLE respo (id INT AUTO_INCREMENT PRIMARY KEY, nickname VARCHAR(255), score FLOAT)"

    # Execute the SQL query
    mycursor.execute(sql)

    print("Table created successfully!")

    # Check if the table is empty
    mycursor.execute("SELECT COUNT(*) FROM users")
    result = mycursor.fetchone()
    if result[0] == 0:
        # Reset the AUTO_INCREMENT value to 1
        mycursor.execute("ALTER TABLE users AUTO_INCREMENT = 1")

    mycursor.close()
    mydb.close()

except mysql.connector.Error as err:
    print("Error occurred:", err)