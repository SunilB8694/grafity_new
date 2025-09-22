from flask import Flask
from grafityGet import grafity_bp

app = Flask(__name__)

app.register_blueprint(grafity_bp)

if __name__=='__main':app.run()