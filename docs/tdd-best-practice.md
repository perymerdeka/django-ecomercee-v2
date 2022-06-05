# Test Driven Development Best Practice

---

this chapter discuss about how to implement TDD methodology on django software development here is the content

* Testing metodology
* The Fundamental
* Introduction to Automation Testing


#### Testing Methodology

In layman’s terms, Test Driven Development (**TDD**) is a software development practice that focuses on creating unit test cases before developing the actual code. It is an iterative approach that combines programming, the creation of unit tests, and refactoring.
 
here is the workflow

[![test-driven-development-workflow-2.png](https://i.postimg.cc/v8jX1jLt/test-driven-development-workflow-2.png)](https://postimg.cc/JtNjvpFs)

for example you need to build login feature, but we don't know the feature is working properly or not, so we need to build tests to test the function.

[![test-driven-development-workflow-1.png](https://i.postimg.cc/g0NHGB2R/test-driven-development-workflow-1.png)](https://postimg.cc/f3S9KCXT)

## The Fundamental

to write the test you should know what framework do you use, there's some python frameworks used for testing

* [Robot](https://robotframework.org/)
* [Pytest](https://docs.pytest.org/en/latest/)
* [Unittest](https://docs.python.org/3/library/unittest.html)
* [Nose2](https://docs.nose2.io/en/latest/)

So which one are we going to use?, the good choice is use Pytest, 

### Why Using Pytest

I will give you some reasons why to use pytest for our testing purposes, in this book we will discuss in detail how to use pytest in a practical and applicable way.

* Pytest is open source
* work with build-in Unittest module
* Easy to start
* simple syntax
* Highly Extensible Plugin
* Support with Large Community
* Support Fixtures


with this pytest we can make slight modifications to run automatically using automation software, this is called Automation Testing.

### Introduction to Automation Testing

**Automation Testing** is a software testing technique that performs using special automated testing software tools to execute a test case suite. On the contrary, Manual Testing is performed by a human sitting in front of a computer carefully executing the test steps.

This testing software is diverse and can be used on various platforms such as desktop, mobile, and web, but in this book we will only discuss testing on web applications.

#### Why Automation Testing

[![bd1a3219623cfc7f3eb57c0d7a42c593.jpg](https://i.postimg.cc/Y9SZLmv3/bd1a3219623cfc7f3eb57c0d7a42c593.jpg)](https://postimg.cc/DWtBt0dJ)

Test Automation is the best way to increase the effectiveness, test coverage, and execution speed in software testing. Automated software testing is important due to the following reasons:

* Manual Testing of all workflows, all fields, all negative scenarios is time and money consuming
It is difficult to test for multilingual sites manually
* Test Automation in software testing does not require Human intervention. You can run automated test unattended (overnight)
* Test Automation increases the speed of test execution
* Automation helps increase Test Coverage
* Manual Testing can become boring and hence error-prone.

#### Which Test Cases to Automate?

test cases can be selected based on the level of complexity or which tests are the most time consuming

* High Risk – Business Critical test cases
* Test cases that are repeatedly executed
* Test Cases that are very tedious or difficult to perform manually
* Test Cases which are time-consuming

**Software that is often used for testing automation**

* [Selenium](https://www.selenium.dev/)
* [Selenium Python](https://selenium-python.readthedocs.io/)
* [Playwright](https://playwright.dev/)

in the next chapter we will learn how to make a testcase using pytest in django

---

[Back to readme](../README.md) <> [Mastering Pytest with Django](mastering-testing-with-pytest.md)