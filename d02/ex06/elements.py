from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='html', content=content, attr=attr)


class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='head', content=content, attr=attr)


class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='body', content=content, attr=attr)


class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='title', content=content, attr=attr)


class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='table', content=content, attr=attr)


class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='th', content=content, attr=attr)


class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='tr', content=content, attr=attr)


class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='td', content=content, attr=attr)


class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ul', content=content, attr=attr)


class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='ol', content=content, attr=attr)


class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='li', content=content, attr=attr)


class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h1', content=content, attr=attr)


class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='h2', content=content, attr=attr)


class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='p', content=content, attr=attr)


class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='div', content=content, attr=attr)


class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='span', content=content, attr=attr)


class Meta(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='meta', tag_type='simple', content=content, attr=attr)


class Img(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='img', tag_type='simple', content=content, attr=attr)


class Hr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='hr', tag_type='simple', content=content, attr=attr)


class Br(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag='br', tag_type='simple', content=content, attr=attr)


def simple_tests():
    assert (str(Html(Text("Content")))) == '<html>\n  Content\n</html>'
    assert (str(Html(Text("Content"), {'lang': "en"}))) == '<html lang="en">\n  Content\n</html>'
    assert (str(Head(Text("Content")))) == '<head>\n  Content\n</head>'
    assert (str(Body(Text("Content")))) == '<body>\n  Content\n</body>'
    assert (str(Title(Text("Content")))) == '<title>\n  Content\n</title>'
    assert (str(Table(Text("")))) == '<table></table>'
    assert (str(Th(Text()))) == '<th></th>'
    assert (str(Tr())) == '<tr></tr>'
    assert (str(Td())) == '<td></td>'
    assert (str(Ul())) == '<ul></ul>'
    assert (str(Ol())) == '<ol></ol>'
    assert (str(Li())) == '<li></li>'
    assert (str(H1())) == '<h1></h1>'
    assert (str(H2())) == '<h2></h2>'
    assert (str(P())) == '<p></p>'
    assert (str(Div(attr={'style': "color: blue;"}))) == '<div style="color: blue;"></div>'
    assert (str(Span())) == '<span></span>'
    assert (str(Meta(attr={'charset': 'utf-8'}))) == '<meta charset="utf-8" />'
    assert (str(Img(attr={'src': 'image.png', 'title': 'fake'}))) == '<img src="image.png" title="fake" />'
    assert (str(Hr())) == '<hr />'
    assert (str(Br())) == '<br />'
    print("Simple tests: OK")


def combined_tests():
    assert (str(Div(Div(Div(Div(Text("Bob likes potatoes > tomatoes"), {'style': "color: blue;"})))))
            == """<div>
  <div>
    <div>
      <div style="color: blue;">
        Bob likes potatoes &gt; tomatoes
      </div>
    </div>
  </div>
</div>""")
    print(example())
    assert (str(example()) == """<html>
  <head>
    <title>
      &quot;Hello ground!&quot;
    </title>
  </head>
  <body>
    <h1>
      &quot;Oh no, not again!&quot;
    </h1>
    <img src="http://i.imgur.com/pfp3T.jpg" />
  </body>
</html>""")
    print("Combined tests: OK")


def tests():
    simple_tests()
    combined_tests()
    print("All tests: OK")


def example():
    html_page = Html(Head(Title(Text('"Hello ground!"'))))
    html_page.add_content(Body([H1(Text('"Oh no, not again!"')), Img(attr={'src': "http://i.imgur.com/pfp3T.jpg"})]))
    return html_page


if __name__ == "__main__":
    print(example())
    tests()
