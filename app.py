from flask import Flask
from flask_restful import Resource, Api 

app = Flask(__name__) #데코레이터 만드는 문법 
api = Api(app) #api 인스턴스, Api 클래스, () 생성자
# @app.route('/')
# def index():

class Rest(Resource): 
    def get(self):
        return {'rest': 'Good ! '}

api.add_resource(Rest, '/')
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
    