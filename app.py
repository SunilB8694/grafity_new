from flask import Flask
from grafityGet import grafity_bp
from grafityMain import grafitymain_bp

app = Flask(__name__)

app.register_blueprint(grafity_bp)
app.register_blueprint(grafitymain_bp)

if __name__=='__main__':app.run()