ex00 day09

Quick start
------------

1. Add "ex00" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ex00',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('', include('ex00.urls')),

3. Run `python manage.py migrate` to create the app models.

4. Start the development server

5. Visit http://127.0.0.1:8000/