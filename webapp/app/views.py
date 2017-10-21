from flask import render_template, request, jsonify
from app import app
from app.models import File
from app import db
import xml.etree.ElementTree as ET
from config import basedir, bibleVersion
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/getContent', methods=['GET'])
def getContent():
# Sample query: GET /getContent?filetype=video

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


#Paramater
#b - Book
#c - Chapter
#v - Verse
#ver - Version
@app.route('/getVerses', methods=['GET'])
def getVerses():
    print request.args
    try:
        book = None
        if request.args.get('b'):
            book = int(request.args.get('b'))
        chapter = None
        if request.args.get('c'):
            chapter = int(request.args.get('c'))

        verse = None
        if request.args.get('v'):
            verse = int(request.args.get('v'))
        version = request.args.get('ver').upper()
        bible_path = os.path.join(basedir, '..', 'bible', version + '.xml')
        print bible_path
        tree = ET.parse(bible_path)
        root = tree.getroot()
        print book, chapter, verse, version
        if verse is not None:
            return str(verse) + ' ' + root[book - 1][chapter - 1][verse - 1].text
        else:
            return ' '.join([verse.get('n') + ' ' + verse.text for verse in root[book - 1][chapter - 1]])
    except IOError:
        return 'Version not supported'

@app.route('/getAvailableVersions', methods=['GET'])
def getAvailableVersions():
    return jsonify({'versions' : bibleVersion});
