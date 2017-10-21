from flask import render_template, request, jsonify
from app import app
from app.models import File
from app import db
import xml.etree.ElementTree as ET
from config import basedir
import os

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/bible')
def bible():
    return render_template('bible.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/audio')
def audio():
    return render_template('audio.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/misc')
def misc():
    return render_template('misc.html')


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
    bibleVersion = ['BBE', 'ESV', 'KJV', 'NIV']
    return jsonify({'versions' : bibleVersion});
