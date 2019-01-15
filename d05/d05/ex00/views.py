from django.shortcuts import HttpResponse
import psycopg2


def sql_execute(query):
    conn = psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def init(request):
    query = """
        CREATE TABLE IF NOT EXISTS ex00_movies(
        title VARCHAR (64) UNIQUE NOT NULL,
        episode_nb INTEGER PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR (128) NOT NULL,
        relase_date DATE NOT NULL
        )
    """

    try:
        print_value = "OK"
        sql_execute(query)
    except Exception as err:
        print_value = str(err)

    return HttpResponse(print_value)
