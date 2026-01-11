from flask import Flask

app = Flask(__name__)

@app.get("teste")
def teste():
    return "ola"

@app.get("teste5")
def teste2():
    return "teste"

app.run()