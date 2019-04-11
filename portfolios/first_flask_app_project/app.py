# class always starts with a capital letter
# package always starts with lowercase characters
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello Flask!'

app.run(port = 5000)