# Axes REST
Axes REST is a simple Django app API that provides details on login attempts.
It depends on Django Axes and Django REST framework.

Django Axes: https://github.com/jazzband/django-axes

Django REST framework: https://www.django-rest-framework.org

## Building the reusable app

Run `python setup.py sdist`. This creates a directory called **dist** and builds the package inside. You can then install it with **pip** like this: `pip install dist/django-axes_rest-0.1.tar.gz`

You can download the latest build there: https://github.com/nsb002/django-axes_rest/releases

## Quick start

1. Install axes and rest_framework with pip:

`pip install django-axes==4.5.4 djangorestframework==3.9.2`

2. Add **'axes'**, **'axes_rest'** and **'rest_framework'** to your **INSTALLED_APPS**
   setting like this:

```python
INSTALLED_APPS = [
  # ...
  'axes',
  'axes_rest',
  'rest_framework',
]
```

3. Add axes to your **AUTHENTICATION_BACKENDS** setting like this:

```python
AUTHENTICATION_BACKENDS = [
  'axes.backends.AxesModelBackend',
  # ...
  'django.contrib.auth.backends.ModelBackend',
  # ...
]
```

4. You will probably have to change your **CACHES** setting like this for **axes** to work:

```python
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
  },
  'axes_cache': {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
  }
}

AXES_CACHE = 'axes_cache'
```

5. You may have to configure **axes** like this to be used with a **reverse proxy**:

```python
    AXES_PROXY_COUNT = 1
    AXES_BEHIND_REVERSE_PROXY = True
    AXES_REVERSE_PROXY_HEADER = 'HTTP_X_REAL_IP'
    AXES_META_PRECEDENCE_ORDER = ('HTTP_X_REAL_IP','HTTP_X_FORWARDED_FOR',)
```

6. You can also configure **axes** if you don't want it to lock your IP at failure
   and change its pagination like this:

```python
    AXES_LOCK_OUT_AT_FAILURE = False

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    }
```

7. You may also have to configure your **LOGIN_URL** like this:

```python
    LOGIN_URL = '/api-auth/login/?next=/api/'
```

8. Include the API URLconf in your project **urls.py** like this:

```python
path('api/', include('axes_rest.urls')),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
```

9. Run `python manage.py migrate` to create the **axes** models.

10. Visit http://127.0.0.1:8000/api/ to consume the API locally.
   Note that your user needs to be staff to access the API.

## Some ideas for the future

* Integrate **http://ip-api.com** IP informations and store them using an IP model to limit the number of requests
* Add more complete and advanced tests in **tests.py**
