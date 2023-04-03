import mysql.connector #import mysql module
db_connection = mysql.connector.connect(
  host="localhost",
  user="username_of_your_MySQL_server",
  passwd="password_of_your_mysql_server",
  database="your_database_name"
)
my_database = db_connection.cursor()
sql_statement = "SELECT * FROM CODESPEEDY"
my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
  print(x)

# source link: https://www.codespeedy.com/fetch-data-from-mysql-table-in-python-program/