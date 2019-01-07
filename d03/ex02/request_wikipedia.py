import sys
import json
import requests
import dewiki


# gestion d erreurs
# Requêtes erronées : Si des requêtes erronées sont envoyées à l’API, un entête HTTP sera renvoyé avec la clé « MediaWiki-API-Error ». La valeur de cet entête et le code d’erreur renvoyé prendront la même valeur. Pour plus d’information, voyez API: Errors and warnings.



def put_infile(query, clean_text):
    filename = '_'.join(query.split(' ')) + '.wiki'
    filename = filename.replace('/', '_')
    with open(filename, 'w+') as fd:
        fd.write(clean_text)


def request_wikipedia(query):
    try:
        request_params = {'action': 'query', 'titles': query, 'prop': 'revisions', 'rvprop': 'content', 'redirects': 1,
                      'utf-8': 1, 'format': 'json'}
        response = requests.get('https://fr.wikipedia.org/w/api.php', params=request_params)
        response_json = json.loads(response.text)
        pages_dict = response_json['query']['pages']
        pages_id = (list(pages_dict.keys())[0])
        response_text = response_json['query']['pages'][pages_id]['revisions'][0]['*']
        clean_text = dewiki.from_string(response_text)
        put_infile(query, clean_text)
    except KeyError:
        print("There is no results for this query.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        request_wikipedia(sys.argv[1])
    else:
        print("Program accepts only one argument as the query")
