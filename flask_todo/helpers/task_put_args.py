from flask_restful import reqparse

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("title", type=str, help="Task title is required", required=True)
task_put_args.add_argument("description", type=str, help="Task description")
task_put_args.add_argument("complete", type=bool, help="Task completion")
task_put_args.add_argument("depends_on", type=int, action="append", help="Task dependencies")