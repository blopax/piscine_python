#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        clean_text = super().__str__()
        clean_text = clean_text.replace("<", "&lt;")
        clean_text = clean_text.replace(">", "&gt;")
        clean_text = clean_text.replace('"', "&quot;")
        clean_text = clean_text.replace('\n', '\n<br />\n')
        return clean_text

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    class ValidationError(Exception):
        def __str__(self):
            return "ValidationError"

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if not Elem.check_type(content) and content is not None:
            raise Elem.ValidationError
        if content is None:
            self.content = Text("")
        elif type(content) != list:
            self.content = [content]
        else:
            self.content = content
        self.content = [x for x in self.content if x != Text("")]
        self.tag = tag
        if attr is None:
            attr = {}
        self.attr = attr
        self.tag_type = tag_type


    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            content_str = self.__make_content()
            if content_str != "":
                content_str += "\n"
            result= "<{}{}>{}</{}>".format(self.tag, self.__make_attr(), content_str, self.tag)
        elif self.tag_type == 'simple':
            result = "<{}{} />".format(self.tag, self.__make_attr())
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = ''
        for elem in self.content:
            result += "\n{}".format(elem).replace("\n", "\n  ")
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    title = Elem(tag='title', content=Text('"Hello ground!"'))
    h1 = Elem(tag='h1', content=Text('"Oh no, not again!"'))
    img = Elem(tag='img', attr={'src': "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')
    html_page = Elem(tag='html', content=Elem(tag='head', content=title))
    html_page.add_content(Elem(tag='body', content=[h1, img]))
    print(html_page)
