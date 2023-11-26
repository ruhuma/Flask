import flask from flask, render_template, request

app = Flask(__name__)

@app.route('/')
def