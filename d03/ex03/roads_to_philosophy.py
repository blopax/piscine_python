import sys
# pas le droit a sys
import requests
from bs4 import BeautifulSoup


def print_path_list(path_list):
    for path in path_list:
        print(path)
    print("{} road(s) from {} to philosophy".format(len(path_list) - 1, path_list[0]))


def has_href_and_parent_p(tag):
    href = tag.has_attr('href')
    parent_p = tag.parent.name == 'p'
    parent_italic = tag.parent.name == 'i' and tag.parent.parent.name == 'p'
    redirect = 'class' in tag.parent.parent.attrs.keys() and tag.parent.parent['class'] == ["redirectText"]
    new_article_in_href = True
    introduction = tag.find_previous("h2") is None
    if href:
        help_in_href = ("Help:" in tag.attrs['href'])
        file_in_href = ("File:" in tag.attrs['href'])
        new_article_in_href = not (help_in_href or file_in_href)
    return href and introduction and (parent_p or parent_italic or redirect) and new_article_in_href


def response_to_next_query(response, path_list):
    html_text = response.text
    soup = BeautifulSoup(html_text, features='html.parser')
    title = soup.h1.string
    if title in path_list:
        print("It leads to an infinite loop !")
        return None
    path_list.append(title)
    if title == "Philosophy":
        print_path_list(path_list)
        return None
    link_tag = soup.body.find(id="mw-content-text").find(has_href_and_parent_p)
    if link_tag is None:
        print("It leads to a dead end !")
        return None
    return link_tag.attrs['href'][6:]


def roads_to_philosophy(query, path_list):
    if path_list is None:
        path_list = []

    try:
        response = requests.get('https://en.wikipedia.org/w/index.php?title={}&redirect=no'.format(query))
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(response)
        next_query = response_to_next_query(response, path_list)
        if next_query is not None:
            roads_to_philosophy(next_query, path_list)

    except requests.exceptions.HTTPError as errh:
        if str(errh) == '<Response [404]>':
            print("Http Error: {}. It is probably due to a bad request. Try another one.".format(errh))
        else:
            print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        roads_to_philosophy(sys.argv[1], None)


# tests "42", "42_(numbers)",  "/dev/null", "Marie antoinette"-->404 "Marie Antoinette", "Accuvio",
# "Veguary", exp ac paragrpahe intro only?, "index.php" "index.php?hack"-->404
