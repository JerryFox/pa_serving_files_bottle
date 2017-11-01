
# serving files with listing directory
# simple bottle application

from bottle import default_app, route, static_file
import os

ROOT = "/home/vysoky/chess"

@route('<filepath:path>')
def server_static(filepath):
    ipath = ROOT + filepath
    if os.path.isdir(ipath):
        list_dir = os.listdir(ipath)
        output = []
        output.append('<html>')
        output.append('<head>')
        output.append('<title>List of %s</title>' % filepath)
        output.append("""
        <style>
            li.file {
                list-style-type: circle;
            }
            li.folder {
                list-style-type: square;
            }
        </style>""")
        output.append('</head>')
        output.append('<h2>Content of %s</h2>' % filepath)
        output.append('<ul>')
        list_isfile = []
        # list of (<isfile>, <name>)
        for i in list_dir:
        	list_isfile.append((os.path.isfile(os.path.join(ipath,i)),i))
        # sort - folders first then sorted by names
        list_isfile.sort(key = lambda x: str(x[0]) + x[1])
        for item in list_isfile:
            output.append('<li class="{}">'.format("file" if item[0] else "folder"))
            output.append('<a href="%(full_path)s">%(name)s</a>' % {
                'name': item[1],
                'full_path': os.path.join(filepath, item[1])
            })
            output.append('</li>')
        output.append('</ul>')
        output.append('</html>')

        return "\n".join(output)
    else:
        return static_file(filepath, root=ROOT)



application = default_app()

