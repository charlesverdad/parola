import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



supported_extensions = {
	'doc': {'pdf'},
	'video': {'mp4'},
	'audio': {'mp3'}
}


KNOWN_FILETYPES = ['mp4']