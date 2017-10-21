import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



extensions_map = {
    'doc': {'pdf'},
    'video': {'mp4'},
    'audio': {'mp3'}
}

supported_extensions = set()
for key in extensions_map:
    supported_extensions |= extensions_map[key]


RESOURCES_PATH = 'resources'

bibleVersion = ['BBE','ESV','KJV','NIV']
