from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        sepal_length = request.form['sl']
        sepal_width = request.form['sw']
        petal_length = request.form['pl']
        petal_width = request.form['pw']
        print(sepal_length)
        return render_template('name.html', firstname=sepal_length)
    else:
        return render_template('name.html')
    


if __name__ =='__main__':
    app.run()