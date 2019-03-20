=====
Axes REST
=====

Axes REST is a simple Django app API that provides details on login attempts.
It depends on Django Axes and Django REST framework.

Django Axes : https://github.com/jazzband/django-axes
Django REST framework : https://www.django-rest-framework.org

Quick start
-----------

1. Install axes and rest_framework with pip::
    pip install django-axes==4.5.4 djangorestframework==3.9.2

2. Add "axes", "rest_framework" and "axes_rest" to your INSTALLED_APPS
   setting like this::

    INSTALLED_APPS = [
        ...
        'axes',
        'rest_framework',
        'axes_rest',
    ]

3. Add axes to your AUTHENTICATION_BACKENDS setting like this::

    AUTHENTICATION_BACKENDS = [
        'axes.backends.AxesModelBackend',
	'django.contrib.auth.backends.ModelBackend',
        ...
    ]

4. You will probably have to change your CACHES setting like this
   for axes to work::

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        },
        'axes_cache': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

    AXES_CACHE = 'axes_cache'

5. You can also configure axes if you don't want it to lock your IP at failure
   and change pagination like this::

    AXES_LOCK_OUT_AT_FAILURE = False

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    }

6. Include the API URLconf in your project urls.py like this::

    path('api/', include('axes_rest.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

7. Run `python manage.py migrate` to create the axes models.

8. Visit http://127.0.0.1:8000/api/ to consume the API locally.
   Note that your user needs to be staff to access the API.