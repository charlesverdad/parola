'''
This script populates the database based on files in the resources folder.
This assumes that the file extension is set correctly, and ignores those not 
in config.supported_extensions.

The file description can be specified by adding a .meta file of the same
name as the file itself.

i.e., for a file called `Gospel.mp4`, the description is parsed from the file
`Gospel.meta` if it exists.
'''

from app import db
from config import supported_extensions, basedir, RESOURCES_PATH, extensions_map
from app.models import File
import os


def get_filetype(extension):
    for key in extensions_map:
        if extension in extensions_map[key]:
            return key
    return 'misc'


res_dir = os.path.join(basedir, '..', RESOURCES_PATH)

for root, dirs, fns in os.walk(res_dir):
    for fn in fns:
        filepath = os.path.join(root, fn)
        ext = filepath.split('.')[-1]
        if ext in supported_extensions:
            path = filepath[len(res_dir) + 1:]
            name = fn[0:-len(ext) - 1]
            meta_path = os.path.join(root, name + '.meta')
            desc = None
            if os.path.exists(meta_path):
                with open(meta_path) as f:
                    desc = f.read().strip()

            entry = File(
                name=name,
                extension=ext,
                filetype=get_filetype(ext),
                description=desc,
                path=path
            )
            db.session.add(entry)
db.session.commit()
