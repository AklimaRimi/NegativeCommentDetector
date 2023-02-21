from flask import Flask
from flask import request
from flask import render_template
import requests
import random


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    lists =['https://people.com/thmb/1klCt1aRd8CSvdSofnh5NNdFb4Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(721x0:723x2)/gettyimages-643473902-2000-35bce4551c754affa6fe4283bca2eda6.jpg',
           'https://e1.pxfuel.com/desktop-wallpaper/251/366/desktop-wallpaper-little-brown-baby-girl-cute-black-baby-girl-thumbnail.jpg',
           'https://cdn.britannica.com/71/234471-050-093F4211/shiba-inu-dog-in-the-snow.jpg']
    img = random.choice(lists)
    print(img)
    if request.method == "POST":
        text = request.form['text']
        outputs = call_model(text)['confidences']
        value = [label['label'] for label in outputs if label['confidence']> .4]
        print(value)
        return render_template('home.html',text = text , value = value,image=img)
    else:
        return render_template('home.html',text = '' , value = '',image=img)


def call_model(text):

    response = requests.post("https://rimi98-negativecommentclassifier.hf.space/run/predict", json={
        "data": [
            text
        ]
    }).json()

    data = response["data"]

    return data[0]
if __name__ == '__main__':
    app.run()