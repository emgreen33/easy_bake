from flask import Flask, render_template
import datetime
app = Flask(__name__)

# @app.route("/")
# def hello():
#    now = datetime.datetime.now()
#    timeString = now.strftime("%Y-%m-%d %H:%M")
#    templateData = {
#       'title' : 'HELLO!',
#       'time': timeString
#       }
#    return render_template('form_submit.html', **templateData)


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
    return render_template('form_action.html', **page_data)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)