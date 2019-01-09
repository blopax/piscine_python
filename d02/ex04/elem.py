class Text(str):
    def __init__(self, text_input=''):
        super().__init__()
        if text_input is None:
            self.text = ''
        else:
            self.text = str(text_input)

    def text_replace(self):
        clean_text = self.text
        clean_text = clean_text.replace("<", "&lt;")
        clean_text = clean_text.replace(">", "&gt;")
        clean_text = clean_text.replace('"', "&quot;")
        clean_text = clean_text.replace("\n", "\n<br />\n")
        return clean_text

    def __str__(self):
        return self.text_replace()


class Elem:
    class ValidationError(Exception):
        def __str__(self):
            return "ValidationError"

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        self.tag = tag
        if attr is None:
            attr = {}
        self.attribute = attr
        self.content_list = self._content_to_list(content)
        self.tag_type = tag_type
        self.string_content = self._parse_content()

    @staticmethod
    def _content_to_list(content):
        content_list = []
        if content is None:
            content_list = [Text("")]
        elif type(content) != list:
            content_list.append(content)
        else:
            content_list = content
        return content_list

    def _parse_content(self):
        content_string = ""
        for content_item in self.content_list:
            if type(content_item) not in [Elem, Text]:
                raise self.ValidationError()
            if str(content_item) != '':
                content_string += str("\n" + str(content_item))
        if content_string != "":
            content_string = content_string.replace("\n", "\n  ")
            content_string += "\n"
        return content_string

    def add_content(self, new_content):
        new_content_list = self._content_to_list(new_content)
        self.content_list += new_content_list
        self.string_content = self._parse_content()

    def __str__(self):
        attribute_str = ''
        for k, v in self.attribute.items():
            attribute_str += " {}={}".format(k, v)
        if self.tag_type == 'double':
            html = "<{}{}>{}</{}>".format(self.tag, attribute_str, self.string_content, self.tag)
        else:
            html = "<{}{}/>".format(self.tag, attribute_str)
        return html


if __name__ == "__main__":
    title = Elem(tag='title', content=Text('"Hello ground!"'))
    h1 = Elem(tag='h1', content=Text('"Oh no, not again!"'))
    img = Elem(tag='img', attr={'src': "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')
    html_page = Elem(tag='html', content=Elem(tag='head', content=title))
    html_page.add_content(Elem(tag='body', content=[h1, img]))
    print(html_page)
