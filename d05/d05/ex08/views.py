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


def add_file(file, table, columns):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
        cursor = conn.cursor()
        with open(file, 'r') as fd:
            cursor.copy_from(file=fd, table=table, sep='\t', columns=columns, null='NULL')
        conn.commit()
        conn.close()
        print_value = "OK<br/>"
    except Exception as err:
        print_value = "{}<br/>".format(err)
    return print_value


def init(request):
    query = """        
        CREATE TABLE IF NOT EXISTS ex08_planets(
        id SERIAL PRIMARY KEY,
        name VARCHAR (64) UNIQUE NOT NULL,
        climate TEXT,
        diameter INTEGER,
        orbital_period INTEGER,
        population BIGINT,
        rotation_period INTEGER,
        surface_water REAL,
        terrain VARCHAR (128)
        );
        
        CREATE TABLE IF NOT EXISTS ex08_people(
        id SERIAL PRIMARY KEY,
        name VARCHAR (64) UNIQUE NOT NULL,
        birth_year VARCHAR(32),
        gender VARCHAR(32),
        eye_color VARCHAR(32),
        hair_color VARCHAR(32),
        height INTEGER,
        mass REAL,
        homeworld VARCHAR(64) REFERENCES ex08_planets(name)
        );
    """

    try:
        print_value = "OK"
        sql_execute(query)
    except Exception as err:
        print_value = str(err)

    return HttpResponse(print_value)


def populate(request):
    print_value = add_file('ex08/planets.csv', 'ex08_planets', ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'))
    print_value += add_file('ex08/people.csv', 'ex08_people', ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'))
    return HttpResponse(print_value)


def display(request):
    query = """SELECT people.name, people.homeworld, planets.climate  
    FROM ex08_people AS people
    JOIN ex08_planets AS planets ON (people.homeworld = planets.name)
    WHERE planets.CLIMATE LIKE '%windy'
    ORDER BY people.name
    """
    table = None
    length = None
    try:
        table = sql_fetch(query)
        if table:
            length = list(range(len(table[0])))
    except Exception as err:
        print(err)

    return render(request, 'ex08/display.html', {'table': table, "length": length})

