
# serving files with listing directory
# simple bottle application

from bottle import default_app, route, static_file
import os, os.path

ROOT = "/home/vysoky/chess"

@route('<filepath:path>')
def server_static(filepath):
    ipath = ROOT + filepath
    if os.path.isdir(ipath):
        list_dir = os.listdir(ipath)
        html_template = """
<html>
    <head>
        <title>List of {path}</title>
        <style>
            li.file {{
                list-style-type: circle;
            }}
            li.folder {{
                list-style-type: square;
            }}
        </style>
    </head>
    <body>
        <h2>Content of {path}</h2>
        <ul>
{items}
        </ul>
    </body>
</html>
"""
        list_isfile = []
        # list of (<isfile>, <name>)
        for i in list_dir:
        	list_isfile.append((os.path.isfile(os.path.join(ipath,i)),i))
        # sort - folders first then sorted by names
        list_isfile.sort(key = lambda x: str(x[0]) + x[1])
        items = ""
        for item in list_isfile:
            iclass = "file" if item[0] else "folder"
            line = '<li class="{}"><a href="{}">{}</a></li>\n'
            items += line.format(iclass, os.path.join(filepath, item[1]), item[1])
        return html_template.format(path=filepath, items=items)
    else:
        return static_file(filepath, root=ROOT)



application = default_app()

