from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    custom_width = 1600
    custom_height = 900
    custom_angle = 30
    data_list = []
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    for k in data:
        data_list.append({'word': k, 'size': data[k] + 13})
    return render_template('home.html', data=data_list, custom_width=custom_width, custom_height=custom_height,
                           custom_angle=custom_angle)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
