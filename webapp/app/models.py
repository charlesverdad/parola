from app import db

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    filetype = db.Column(db.String(64), index=True)
    name = db.Column(db.String(120), index=True)
    path = db.Column(db.String(120))
    extension = db.Column(db.String(5))
    description = db.Column(db.String(240))

    def __repr__(self):
        return '<File %r>' % (self.name)
