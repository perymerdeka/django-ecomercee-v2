# Mastering Pytest Using Django

---

In this chapter, we'll cover how to configure and master pytest in Django (best practice way) this chapter discusses how to configure and design test-driven development using pytest for large, scalable projects.

## Kick off

let's see the table of content for this chapter

#### Table of contemt

* Creating Django project
* Configure and Install Pytest
* Install Plugin for Pytest
* Configure `pytest.ini`
* Restructure tests directory for best practice
* Introduction to Pytest fixtures
* writing first test using selenium and Pytest

### Introduction to Pytest

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

before continue on this chapter let me tell you the pattern for writing test, here is the pattern

* Arrage
* Act
* Assert

#### Installing Pytest

Installing pytest using pip

```py
pip install pytest
```

refer the docs here: https://docs.pytest.org/en/latest/

refer here for pypi project https://pypi.org/project/pytest/

**Example Usage**

```py
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```

#### Pytest Plugin

the plugin are used on this project

* Pytest
* Pytest Django
* Pytest selenium
* Faker
* Factoryboy
* coverage

## Writing first Test with Selenium and Pytest

### Using LiveServerTestCase

LiveServerTestCase does basically the same as TransactionTestCase with one extra feature: it launches a live Django server in the background on setup, and shuts it down on teardown. This allows the use of automated test clients other than the Django dummy client such as, for example, the Selenium client, to execute a series of functional tests inside a browser and simulate a real user’s actions.

based on https://docs.djangoproject.com/en/4.0/topics/testing/tools/#django.test.LiveServerTestCase

we can write live test using
* [selenium](https://pypi.org/project/selenium/) 
* [selenium webdriver manager](https://pypi.org/project/webdriver-manager/)

#### Project Structure for Testing

To start the project, we create a project structure like this, so it's easy to maintain

```sh
backend/
├── apps
│   ├── __init__.py
│   └── dashboard
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       └── views.py
├── conftest.py
├── core
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── development.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── pytest.ini
└── tests
    ├── __init__.py
    └── test_dashboard_selenium.py
```


#### Install Required Plugin

for this project on this chapter install required plugin for testing

* [pytest](https://docs.pytest.org/en/latest/)
* [Pytest-django](https://pytest-django.readthedocs.io/en/latest/)
* [pytest-selenium](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html)
* [factoryboy](https://pypi.org/project/pytest-factoryboy/)
* [faker](https://pypi.org/project/pytest-faker/)
* [selenium](https://pypi.org/project/selenium/) 
* [selenium webdriver manager](https://pypi.org/project/webdriver-manager/)

After knowing what plugins will be installed, let's install them using pip

```sh
pip install pytest pytest-django pytest-selenium pytest-factoryboy pytest-faker selenium webdriver-manager
```

then we can proceed to the next step, which is how to best practice pytest in django config

#### Configuring Pytest on Django

for configuring pytest on django, we need to create a file called `pytest.ini`

```sh
[pytest]
DJANGO_SETTINGS_MODULE = core.settings.development
django_find_project = true
python_files = tests.py test_*.py *_tests.py
pythonpath = . backend
addopts = -v --nomigrations --ignore=venv
filterwarnings =
    ignore:.*U.*mode is deprecated:DeprecationWarning
    ignore:.*Django now detects this configuration.*:django.utils.deprecation.RemovedInDjango41Warning
```

refer on this link for more detail

* https://pytest-django.readthedocs.io/en/latest/

#### Writing First Test

in this chapter, we will write first test using selenium and pytest