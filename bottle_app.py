
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, static_file
import os

ROOT = "/home/jerryfox/chess"

@route('<filepath:path>')
def server_static(filepath):
    ipath = ROOT + filepath
    if os.path.isdir(ipath):
        list_dir = os.listdir(ipath)
        output = []
        output.append('<html>')
        output.append('<head><title>List of %s</title></head>' % filepath)
        output.append('<h2>Content of %s</h2>' % filepath)
        output.append('<ul>')
        for descriptor in list_dir:
            output.append('<li>')
            output.append('<a href="%(full_path)s">%(name)s</a>' % {
                'name': descriptor,
                'full_path': os.path.join(filepath, descriptor)
            })
            output.append('</li>')
        output.append('</ul>')
        output.append('</html>')

        return "\n".join(output)
    else:
        return static_file(filepath, root=ROOT)



application = default_app()

