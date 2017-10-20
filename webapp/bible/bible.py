from flask import Flask, request
import xml.etree.ElementTree as ET
app = Flask(__name__)

#Paramater
#b - Book
#c - Chapter
#v - Verse
#ver - Version
@app.route('/', methods=['GET'])
def hello_world():
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
        tree = ET.parse(version + '.xml')
        root = tree.getroot()
        if verse is not None:
            return str(verse) + ' ' + root[book-1][chapter-1][verse-1].text
        else:
            return ' '.join([verse.get('n') + ' ' + verse.text for verse in root[book-1][chapter-1]])
    except IOError:
        return 'Version not supported'
    except:
        return 'Missing parameter'
