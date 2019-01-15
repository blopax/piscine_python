from django.shortcuts import HttpResponse, render
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


def sql_fetch(query):
    conn = psycopg2.connect(
        database='formationdjango',
        host='localhost',
        user='djangouser',
        password='secret'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    response = cursor.fetchall()
    conn.close()
    return response


def init(request):
    query = """        
        CREATE TABLE IF NOT EXISTS ex06_movies(
        title VARCHAR (64) UNIQUE NOT NULL,
        episode_nb INTEGER PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR (128) NOT NULL,
        release_date DATE NOT NULL,
        created TIMESTAMP DEFAULT NOW(),
        updated TIMESTAMP DEFAULT NOW()
        );
        
        CREATE OR REPLACE FUNCTION update_changetimestamp_column()
        RETURNS TRIGGER AS $$
        BEGIN
        NEW.updated = now();
        NEW.created = OLD.created;
        RETURN NEW;
        END;
        $$ language 'plpgsql';
        CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
        ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
        update_changetimestamp_column();
    """

    try:
        print_value = "OK"
        sql_execute(query)
    except Exception as err:
        print_value = str(err)

    return HttpResponse(print_value)


def add_movie(title, episode_nb, director, producer, release_date):
    try:
        query = """
                INSERT INTO ex06_movies (title, episode_nb, director, producer, release_date)VALUES 
                ('{}', '{}' , '{}', '{}', '{}');
                """.format(title, episode_nb, director,producer, release_date)
        sql_execute(query)
        print_value = "OK<br/>"
    except Exception as err:
        print_value = "{}<br/>".format(err)
    return print_value


def populate(request):
    print_value = add_movie('The Phantom Menace', 1 , 'George Lucas', 'Rick McCallum', '1999-05-19')
    print_value += add_movie('Attack of the Clones', 2, 'George Lucas', 'Rick McCallum', '2002-05-16')
    print_value += add_movie('Revenge of the Sith', 3, 'George Lucas', 'Rick McCallum', '2005-05-19')
    print_value += add_movie('A New Hope', 4, 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25')
    print_value += add_movie('The Empire Strikes Back', 5, 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')
    print_value += add_movie('Return of the Jedi', 6, 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')
    print_value += add_movie('The Force Awakens', 7, 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11');

    return HttpResponse(print_value)


def display(request):
    query = """SELECT * FROM ex06_movies ORDER BY episode_nb"""
    table = None
    length = None
    try:
        table = sql_fetch(query)
        if table:
            length = list(range(len(table[0])))
    except Exception as err:
        print(err)

    return render(request, 'ex06/display.html', {'table': table, "length": length})


def update(request):
    title = request.POST.get('title', None)
    opening_crawl = request.POST.get('opening_crawl', None)
    no_data = False
    table = None
    try:
        if title:
            query = """UPDATE ex06_movies SET opening_crawl = '{}' WHERE title = '{}'""".format(opening_crawl, title)
            sql_execute(query)
        query = """SELECT * FROM ex06_movies ORDER BY episode_nb"""
        table = sql_fetch(query)
        if not table:
            no_data = True
    except Exception as err:
        no_data = True
    return render(request, 'ex06/update.html', {'table': table, "no_data": no_data})
