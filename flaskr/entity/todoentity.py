from flaskr import db
class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    done = db.Column(db.Boolean)