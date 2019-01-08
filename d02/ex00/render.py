import sys
import os

import settings


def get_dict():
    dict = {}
    for key in [x for x in dir(settings) if x[0:2] != '__']:
        dict[key] = getattr(settings, key)
    return dict


def template_to_html(filename, template):
    try:
        html = template.format_map(get_dict())
        with open(filename.replace('template', 'html'), 'w+')as f:
            f.write(html)
        return None
    except Exception as error:
        return error


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception('This program takes a unique argument.')
        arg = sys.argv[1]
        if os.path.splitext(arg)[1] != ".template":
            raise Exception("Wrong extension. Must be template.")
        if not os.path.exists(arg):
            raise Exception("File doesn't exist.")
        with open(arg, 'r') as fd:
            string = fd.read()
            err = template_to_html(arg, string)
            if err is not None:
                raise Exception(err)
    except Exception as err:
        print(err)
