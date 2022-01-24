from flask import Flask

app = Flask(__name__)  #экземпляр класса Flask
app.debug = True
app.secret_key = 'cairocoders-ednalan' #ключ для сессии

from app import routes
if __name__ == "main":
    app.run()