import flask

from . import app
from . import cel_app


@app.route('/post', methods=['POST'])
def sendMessage():
    username = flask.request.values.get('user')
    message = flask.request.values.get('message')
    r = cel_app.send_task('tasks.Send_Message', kwargs={'user': username, 'mess': message})
    return str(cel_app.AsyncResult(str(r.id)).result)


@app.route('/get', methods=['GET'])
def getChat():
    r = cel_app.send_task('tasks.Get_Message')
    return str(cel_app.AsyncResult(str(r.id)).result)
