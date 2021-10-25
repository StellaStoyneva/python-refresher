from flask_restful import fields

task_fields = {
    'id': fields.Integer,
	'title': fields.String,
	'description': fields.String,
	'complete': fields.Boolean,
	'depends_on': fields.List(fields.Integer)
}
