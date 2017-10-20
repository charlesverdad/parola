Setting of environment variables

For Windows
set FLASK_APP=bible.py
For Linux
export FLASK_APP=bible.py

Running the server
flask run

Access the function using:
{hostname}:{port}?b={book}&c={chapter}&v={verse}&ver={version}