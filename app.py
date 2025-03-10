from flask import Flask
from routes.livrosRoutes import livros_blueprint

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<p>Hello World!</p>"

app.register_blueprint(livros_blueprint)

if __name__ == "__main__":
    app.run(debug=True)