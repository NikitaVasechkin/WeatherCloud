from app import app, db


import flask

from app.jobs import DbPush

@app.route('/index', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        temperature = {'temperature': 20}
        return flask.render_template('index.html', title = 'Current temperature display', temperature = temperature)
    
    if flask.request.form['submit'] == 'Send' and flask.request.method == 'POST':
        DbPush()
        flask.flash('Pushed to database current state')
    else: 
        print('test')
        flask.flash('Nothing happens there')
    return flask.redirect(flask.url_for('index'))



