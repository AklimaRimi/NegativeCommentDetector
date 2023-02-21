from flask import Flask,render_template,request
import requests


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    x = 10
    return render_template('collect-data-form.html',value = x)


if __name__ == '__main__':
    app.run()