from flask import render_template, request, jsonify
from app import app
from app.models import File
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/getContent', methods=['GET'])
def getContent():
    filetype = request.args.get('filetype')
    files = db.session.query(File).filter(File.filetype == filetype).all()
    out = [
        {
            "id": file.id,
            "name": file.name,
            "description": file.description,
            "path": file.path,
            "extension": file.extension
        }
        for file in files
    ]
    return jsonify(out)
