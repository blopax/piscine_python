from elements import *


class Page:
    def __init__(self, page):
        self.page = page
        self.valid_page = self.is_valid()

    def __str__(self):
        if self.valid_page is True:
            string = self.page.__str__()
            if type(self.page) is Html:
                string = "<!DOCTYPE html>\n{}".format(string)
        else:
            string = "There is a problem with the page. It is not valid."
        return string

    def write_to_file(self, filename):
        with open(filename, 'w+') as fd:
            fd.write(self.__str__())

    @staticmethod
    def nodes(node):
        if not Elem.check_type(node.content):
            return False
        for elem in node.content:
            if type(elem) is Elem:
                return False
        return True

    @staticmethod
    def html_check(node):
        if len(node.content) != 2:
            return False
        if (type(node.content[0]), type(node.content[1])) != (Head, Body):
            return False
        return True

    @staticmethod
    def head_check(node):
        if len(node.content) != 1:
            return False
        if type(node.content[0]) != Title:
            return False
        return True

    @staticmethod
    def body_div_check(node):
        for elem in node.content:
            if type(elem) not in [H1, H2, Div, Table, Ul, Ol, Span, Text]:
                return False
        return True

    @staticmethod
    def title_h1_h2_li_th_td_check(node):
        if len(node.content) != 1:
            return False
        if type(node.content[0]) != Text:
            return False
        return True

    @staticmethod
    def p_check(node):
        for elem in node.content:
            if type(elem) != Text:
                return False
        return True

    @staticmethod
    def span_check(node):
        for elem in node.content:
            if type(elem) not in [Text, P]:
                return False
        return True

    @staticmethod
    def ul_ol_check(node):
        if len(node.content) == 0:
            return False
        for elem in node.content:
            if type(elem) is not Li:
                return False
        return True

    @staticmethod
    def tr_check(node):
        if len(node.content) == 0:
            return False
        inner_node = node.content[0]
        for elem in node.content:
            if type(elem) not in [Th, Td] or type(elem) is not type(inner_node):
                return False
        return True

    @staticmethod
    def table_check(node):
        for elem in node.content:
            if type(elem) is not Tr:
                return False
        return True

    @staticmethod
    def _is_node_valid(node):
        for elem in node.content:
            if isinstance(type(elem), Elem):
                if Page._is_node_valid(elem) is False:
                    return False
        if type(node) is Html and not Page.html_check(node):
            return False
        if type(node) is Head and not Page.head_check(node):
            return False
        if type(node) in [Body, Div] and not Page.body_div_check(node):
            return False
        if type(node) in [Title, H1, H2, Li, Th, Td] and not Page.title_h1_h2_li_th_td_check(node):
            return False
        if type(node) is P and not Page.p_check(node):
            return False
        if type(node) is Span and not Page.span_check(node):
            return False
        if type(node) in [Ul, Ol] and not Page.ul_ol_check(node):
            return False
        if type(node) is Tr and not Page.tr_check(node):
            return False
        if type(node) is Table and not Page.table_check(node):
            return False
        return True

    def is_valid(self):
        if not(Page.nodes(self.page) or isinstance(self.page, Elem)):
            return False
        return Page._is_node_valid(self.page)

    @staticmethod
    def page_tests():
        # Tests Html
        assert(Page.html_check(Html([Head(), Body()])))
        assert (Page.html_check(Html([Body(), Head()])) is False)
        assert (Page.html_check(Html([Head(), Body(), Head()])) is False)

        # Tests Head
        assert(Page.head_check(Head(Title())))
        assert(Page.head_check(Head()) is False)
        assert(Page.head_check(Head([Title(), P()])) is False)

        # Tests body div
        assert(Page.body_div_check(Body()))
        assert(Page.body_div_check(Body(Div())))
        assert(Page.body_div_check(Body(Tr())) is False)
        assert (Page.body_div_check(Div([H1(), H2(), Div(), Table(), Ul(), Ol(), Span(), Text()])))

        # Tests title, h1, h2, li, th, td
        assert (Page.title_h1_h2_li_th_td_check(Title()))
        assert (Page.title_h1_h2_li_th_td_check(H1(Text("Bob"))))
        assert (Page.title_h1_h2_li_th_td_check(H2()))
        assert (Page.title_h1_h2_li_th_td_check(Li(Text())))
        assert (Page.title_h1_h2_li_th_td_check(Li(Text("yo"))))
        assert (Page.title_h1_h2_li_th_td_check(Th(Text("yo"))))
        assert (Page.title_h1_h2_li_th_td_check(Td([Text("yo"), Text()])) is False)
        assert (Page.title_h1_h2_li_th_td_check(H1(Div())) is False)

        # Tests p
        assert (Page.p_check(P()))
        assert (Page.p_check(P([Text(), Text(""), Text("Bob")])))
        assert (Page.p_check(P(Div())) is False)

        # Tests span
        assert(Page.span_check(Span()))
        assert(Page.span_check(Span(Text())))
        assert(Page.span_check(Span(P())))
        assert(Page.span_check(Span(Text())))
        assert(Page.span_check(Span([P(), Text()])))
        assert(Page.span_check(Span([P(), Text(), Div()])) is False)
        assert(Page.span_check(Span(Div())) is False)

        # Tests Ul Ol
        assert(Page.ul_ol_check(Ul(Li())))
        assert(Page.ul_ol_check(Ul([Li(), Li()])))
        assert(Page.ul_ol_check(Ol(Li())))
        assert(Page.ul_ol_check(Ol([Li(), Li()])))
        assert(Page.ul_ol_check(Ul()) is False)
        assert(Page.ul_ol_check(Ul([Li(), Div()])) is False)

        # Tests Tr
        assert(Page.tr_check(Tr(Th())))
        assert(Page.tr_check(Tr(Td())))
        assert(Page.tr_check(Tr([Td(), Td(), Td()])))
        assert(Page.tr_check(Tr([Th(), Th(), Th()])))
        assert(Page.tr_check(Tr([Td(), Div()])) is False)
        assert(Page.tr_check(Tr([Td(), Th()])) is False)

        # Tests Table
        assert(Page.table_check(Table(Tr())))
        assert(Page.table_check(Table([Tr(), Tr(), Tr()])))
        assert(Page.table_check(Table([Td()])) is False)

        print("Page tests: OK")


if __name__ == "__main__":
    Page.page_tests()
    html_page = example()
    test = Page(html_page)
    print(test.is_valid())
    print(test)
    test.write_to_file("test.html")
