from flask import Flask
from flask_restful import Api
from helpers.app_setup import application, db
from controllers.hello_world import HelloWorld
from controllers.task import Task
from controllers.todo_list import TodoList
from controllers.version import Version

app = application
api = Api(app)


api.add_resource(TodoList, '/todo/v1/tasks')
api.add_resource(Task, '/todo/v1/tasks/<int:task_id>')
api.add_resource(HelloWorld, '/')
api.add_resource(Version, '/todo/v1/version')

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)