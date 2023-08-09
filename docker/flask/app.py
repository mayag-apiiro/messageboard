from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Web server is up'}

class NewPost(Resource):
    def post(self):
        data = request.get_json()
        user = data.get('user')
        content = data.get('content')
        # Process user and content data
        return {'user': user, 'content': content}

class DeleteResource(Resource):
    def delete(self):
        id = request.args.get('id')
        # Delete resource with specified ID
        return {'message': f'Deleted resource with ID {id}'}

api.add_resource(HelloWorld, '/')
api.add_resource(NewPost, '/new-post')
api.add_resource(DeleteResource, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
