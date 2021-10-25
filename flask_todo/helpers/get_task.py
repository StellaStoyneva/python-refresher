from models import Todo

def get_task(task_id):
    print(task_id)
    return Todo.query.filter_by(id=task_id).first()
