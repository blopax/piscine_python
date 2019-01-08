class Text(str):
    def __init__(self, input=''):
        if input is None:
            self.text = ''
        else:
            self.text = str(input)

    def text_replace(self):
        clean_text = self.text
        #clean_text = clean_text.replace("<", "&lt;")
        #clean_text = clean_text.replace(">", "&gt;")
        #clean_text = clean_text.replace('"', "&quot;")
        clean_text = clean_text.replace("\n", "\n<br />\n")
        return clean_text

    def __str__(self):
        return self.text_replace()


class Elem:
    def __init__(self, tag='div', attr={}, content='', tag_type='double'):
        # name = str, attribute = dict, content = string, type =string)
        self.tag = tag
        self.attribute = attr
        self.content = str(Text(content)) #=self.parse_content(content) ou ger si nul ou pas et si liste ou pas on peut faire un liste append pour ajouter a liste vide
        if self.content != '':
            self.content = "\n  " + self.content + "\n"
        self.tag_type = tag_type

    def __str__(self):
        attribute_str = ''
        for k, v in self.attribute.items():
            attribute_str += " {}={}".format(k, v)
        if self.tag_type == 'double':
            html = "<{}{}>{}</{}>".format(self.tag, attribute_str, self.content, self.tag)
        else:
            html = "<{}{}/>".format(self.tag, attribute_str)
        print(html)
        return html



def test_text():
    # What is Text?
    assert isinstance(Text(), str)
    # Default behaviour :
    assert str(Text()) == ''
    # With an argument :
    assert str(Text('')) == ''
    assert str(Text('foo')) == 'foo'
    # Pattern replacing :
    assert str(Text('\n')) == '\n<br />\n'
    assert str(Text('foo\nbar')) == 'foo\n<br />\nbar'
    # Escaping <, >, "...
    assert str(Text('<')) == '&lt;'
    assert str(Text('>')) == '&gt;'
    assert str(Text('"')) == '&quot;'
    print('Text behaviour : OK.')

def test_elem_basics():
    # Default behaviour :
    assert str(Elem()) == '<div></div>'
    # Arguments order :
    assert str(Elem('div', {}, None, 'double')) == '<div></div>'
    # Argument names :
    assert str(Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double')) == '<body>\n  <div></div>\n</body>'
    # With elem as content :
    assert str(Elem(content=Elem())) == '<div>\n  <div></div>\n</div>'
    # With list as content :
    assert str(Elem(content=[Text('foo'), Text('bar'), Elem()])) == '<div>\n  foo\n  bar\n \
 <div></div>\n</div>'
    print('Basic Elem behaviour : OK.')


def test_empty_texts():
    assert str(Elem(content=Text(''))) == '<div></div>'
    assert str(Elem(content=[Text(''), Text('')])) == '<div></div>'
    assert str(Elem(content=[Text('foo'), Text(''), Elem()])) == '<div>\n  foo\
\n  <div></div>\n</div>'
    print('Elem with empty texts : OK.')


def test_errors():
    # Type error if the content isn't made of Text or Elem.
    try:
        Elem(content=1)
    except Exception as e:
        assert type(e) == Elem.ValidationError
    # The right way :
    assert str(Elem(content=Text(1))) == '<div>\n  1\n</div>'

    # Type error if the elements of the list aren't Text or Elem instances.
    try:
        Elem(content=['foo', Elem(), 1])
    except Exception as e:
        assert type(e) == Elem.ValidationError
    # The right way :
    assert (str(Elem(content=[Text('foo'), Elem(), Text(1)]))
            == '<div>\n  foo\n  <div></div>\n  1\n</div>')

    # Same with add_method()
    try:
        elem = Elem()
        elem.add_content(1)
        raise (Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)

    # Or with lists :
    try:
        elem = Elem()
        elem.add_content([1, ])
        raise (Exception('incorrect behaviour'))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)

    # str can't be used :
    try:
        elem = Elem()
        elem.add_content(['', ])
        raise (Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)

    try:
        elem = Elem(content='')
        raise (Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    print('Error cases : OK.')


def test_embedding():
    assert (str(Elem(content=Elem(content=Elem(content=Elem()))))
            == """<div>
  <div>
    <div>
      <div></div>
    </div>
  </div>
</div>""")
    print('Element embedding : OK.')


import traceback

if __name__ == "__main__":
    try:
        test_elem_basics()
        print('Tests succeeded!')
    except AssertionError as e:
        traceback.print_exc()
        print(e)
        print('Tests failed!')