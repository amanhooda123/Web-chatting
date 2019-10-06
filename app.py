from flask import Flask,jsonify,request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'codingelements'
socketio = SocketIO(app)


@app.route('/')
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handleMsg(data):
	socketio.emit('push',data,broadcast=True,include_self=False)


if __name__=="__main__":
	socketio.run(app)




# 	from flask import Flask,jsonify,request


# app = Flask(__name__)

# users = [
#        {'id':1, 'name':'anne', 'age':20},
#        {'id':2, 'name':'cathy', 'age':21},
#        {'id':3, 'name':'bill', 'age':19}
# ]

# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')


# @app.route('/users')
# def getUsers():
# 	return jsonify(users)

# @app.route('/users/<id>')
# def getUsers(id):
# 	result = list(filter(lambda u:str(u['id'])==id,users))
# 	return jsonify(result)

# if __name__=="__main__":
# 	app.run()