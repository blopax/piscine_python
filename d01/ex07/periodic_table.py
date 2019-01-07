import sys


def list_from_str(text):
    lines = [line.split(" = ") for line in text.split('\n')]
    periodic_list = []
    for line in lines:
        info = [item for item in line[1].split(", ")]
        info_dict = {}
        for info_item in info:
            info_key_value = [item.strip() for item in info_item.split(':')]
            info_dict[info_key_value[0]] = info_key_value[1]
        periodic_list.append([line[0], info_dict])
    return periodic_list


def make_empty_td(prev_position, position):
    colspan = 1
    if position < 30:
        colspan = position - prev_position
    empty_td = '<td class ="place_holder" colspan="{}"></td>'.format(colspan - 1)
    return empty_td


def make_table(periodic_list):
    prev_postion = -1
    html_table = "<table>\n"
    for element in periodic_list:
        position = int(element[1]['position'])
        if position == 0:
            html_table += "<tr>\n"
        if position - prev_postion != 1:
            html_table += make_empty_td(prev_postion, position)
        html_table += '<td style="border: 1px solid black; padding:10px">\n'
        html_table += '<h4>{}</h4>\n'.format(element[0])
        html_table += '<ul>\n'
        html_table += '<li>No {}</li>\n'.format(element[1]['number'])
        html_table += '<li>{}</li>\n'.format(element[1]['small'])
        html_table += '<li>{}</li>\n'.format(element[1]['molar'])
        html_table += '</ul>\n'
        html_table += '</td\n>'
        prev_postion = position
        if position == 17:
            html_table += "</tr>\n"
            prev_postion = -1
    html_table += '</table>\n'
    return html_table


def make_head():
    head = "<head>\n"
    head += '<meta charset = "utf-8">\n'
    head += '<title>Mendeleiev</title>\n'
    # <link rel = "stylesheet" type = "text/css" href = "responsive.css" />
    head += "</head>\n"
    return head


def make_body(periodic_list):
    body = "<body>\n"
    body += "<header>\n"
    body += "<h1>The periodic table</h1>\n"
    body += "</header>\n"
    body += "<div>\n"
    body += '<img src="http://www.larousse.fr/encyclopedie/data/images/1310399-Dmitri_Ivanovitch_Mendele%C3%AFev.jpg"' \
            ' alt="Dimitri himself"/>\n'
    body += "</div>\n"
    body += "<div>\n"
    body += make_table(periodic_list)
    body += "</div>\n"
    body += "</body>\n"
    return body


def make_html(filename):
    with open(filename, "r") as fd:
        raw_text = fd.read().strip()
    periodic_list = list_from_str(raw_text)
    html = "<!DOCTYPE html>\n<html lang='en'>\n"
    html += make_head()
    html += make_body(periodic_list)
    html += "</html>"
    with open("periodic_table.html", "w+") as fd:
        fd.write(html)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        make_html(sys.argv[1])
