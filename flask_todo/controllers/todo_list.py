from flask.json import jsonify
from flask_restful import Resource, abort, marshal_with
from flask import Flask
from models import Todo
from helpers.app_setup import db
from helpers.resource_fields import task_fields
from helpers.task_put_args import task_put_args


class TodoList(Resource):
    @marshal_with(task_fields)
    def get(self):
        todo_list = Todo.query.all()
        return todo_list
    
    @marshal_with(task_fields)
    def post(self):
        args = task_put_args.parse_args()
        new_title = args['title']
        todo = Todo.query.filter_by(title=new_title).first()
        if todo:
            abort(409, message="Task already exists")

        new_todo = Todo(title=args['title'], description=args['description'], complete=False, depends_on=args['depends_on'])
        
        db.session.add(new_todo)
        db.session.commit()
        return new_todo
        