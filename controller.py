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
    page_data = {
    'name' : request.form['yourname'],
    'number' : request.form['yournumber'],
    'status' : "on"
    }
    # name=request.form['yourname']
    # number=request.form['yournumber']
    return render_template('form_action.html', **page_data)


while True:
  if cookie_submit():
    print oven.status()
    oven.switch_on()
    print oven.status()
    time.sleep(4)
    oven.switch_off()
    print oven.status()
    time.sleep(4)

