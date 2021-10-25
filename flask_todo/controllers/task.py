from flask_restful import Resource, reqparse, marshal_with, abort
from models import Todo
from helpers.get_task import get_task
from helpers.resource_fields import task_fields
from helpers.task_put_args import task_put_args
from helpers.app_setup import db

task_patch_args = reqparse.RequestParser()
task_patch_args.add_argument("title", type=str, help="Task title")
task_patch_args.add_argument("description", type=str, help="Task description")
task_patch_args.add_argument("complete", type=bool, help="Task completion")
task_patch_args.add_argument("depends_on", type=int, action="append", help="Task dependencies")

class Task(Resource):
    @marshal_with(task_fields)
    def get(self,task_id):
        todo = get_task(task_id)
        return todo

    @marshal_with(task_fields)
    def put(self, task_id):
        todo = get_task(task_id)
        args = task_put_args.parse_args()
        if not todo:
            abort(404, message="Task does not exist")
        
        todo.title = args['title']
        todo.description = args['description']
        todo.complete = args['complete']
        todo.depends_on = args['depends_on']
        
        db.session.commit()
        return todo, 201

    @marshal_with(task_fields)
    def patch(self, task_id):
        todo = Todo.query.get(task_id)
        args = task_patch_args.parse_args()
        if not todo:
            abort(404, message="Task does not exist")
        
        if args['title']:
            todo.title = args['title']
        if args['description']:
            todo.description = args['description']
        if args['complete']:
            todo.complete = args['complete']
        if args['depends_on']:
            todo.depends_on = args['depends_on']
        
        db.session.commit()
        return todo, 201

    @marshal_with(task_fields)
    def delete(self, task_id):
        task_to_delete = get_task(task_id)
        todo_list = Todo.query.all()
        for todo in todo_list:
           if task_to_delete.depends_on and task_to_delete.id in todo.depends_on:
               todo.depends_on = [x for x in todo.depends_on if x!=task_to_delete.id]
        db.session.delete(task_to_delete)
        db.session.commit()
        return '', 204
        