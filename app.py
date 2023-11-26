from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name',methods=['GET','POST'])
def hi():
    return('how are you')


if __name__ =='__main__':
    app.run()