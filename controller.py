import oven
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

import time


if __name__ == '__main__':
    app.run()

@app.route('/')
def cookie_form():
    return render_template('form_submit.html')

@app.route('/cookie_submit/', methods=['POST'])
def cookie_submit():
    name=request.form['yourname']
    number=request.form['yournumber']
    return render_template('form_action.html', name=name, number=number)

while True:
  if cookie_submit():
    print oven.status()
    oven.switch_on()
    print oven.status()
    time.sleep(4)
    oven.switch_off()
    print oven.status()
    time.sleep(4)

