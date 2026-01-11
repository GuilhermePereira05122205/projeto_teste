from flask import Flask

app = Flask(__name__)

app.get("teste")
def teste():
    return "ola"

app.run()