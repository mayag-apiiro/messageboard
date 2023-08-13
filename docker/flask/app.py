from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import psycopg2


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        try:
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                user="postgres",
                password="1234",
                host="db",  # This corresponds to the service name in Docker Compose
                port="5432",
                database="postgres"
            )
            cursor = connection.cursor()

            # Retrieve all rows from the table
            select_query = "SELECT * FROM messages"
            cursor.execute(select_query)
            rows = cursor.fetchall()

            # Close the database connection
            cursor.close()
            connection.close()

            # Convert rows to a list of dictionaries
            message_list = []
            for row in rows:
                message = {
                    'user': row[0],
                    'title': row[1],
                    'content': row[2]
                }
                message_list.append(message)

            return jsonify({'messages': message_list})

        except:
            app.logger.exception("Something went wrong while fetching messages")
            return jsonify({'error': 'Failed to fetch messages'}), 500

class NewPost(Resource):
    def post(self):
        app.logger.info("HAJABABABEKKKOOO!")
        try:
            app.logger.info("Entire request object:")
            app.logger.info(request.__dict__)
            app.logger.info("Fetching json")
            app.logger.info(request.json)
            app.logger.info(request)
            app.logger.info(request.get_json())
            
        except:
            app.logger.exception("Something went wrong")
        
        app.logger.info("Fetching json after")
        # return jsonify({'message': 'Message added successfully'})
        request.json
        data = request.get_json()
        user = data.get('user')
        title = data.get('title')
        content = data.get('content')
        # app.logger.info(content)
        app.logger.info("V1")


        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="1234",
            host="db",  # This corresponds to the service name in Docker Compose
            port="5432",
            database="postgres"
        )
        cursor = connection.cursor()

        # Insert the new message into the database
        insert_query = "INSERT INTO messages (\"user\", title, content) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (user, title, content))
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Message was added successfully'})

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
