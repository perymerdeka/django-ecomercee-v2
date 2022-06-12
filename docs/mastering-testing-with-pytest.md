# Mastering Pytest Using Django

---

In this chapter, we'll cover how to configure and master pytest in Django (best practice way) this chapter discusses how to configure and design test-driven development using pytest for large, scalable projects.

## Kick off

let's see the table of content for this chapter

#### Table of contemt

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

