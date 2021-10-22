from flask import Flask

app = Flask(__name__)
app.secret_key = 'a3927756d9df7b9f3eba4621199f0f14'

from Gerbillus_perpallidus import routes

