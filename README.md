# python-behave

## Setup:

#### Clone the repo

`$ git clone https://github.com/emmodunne/python-behave.git`

`$ cd python-behave`

#### Project Requirements
- Google Chrome
- Python 3
- selenium (https://pypi.org/project/selenium/)
- behave (https://behave.readthedocs.io/en/stable/install.html)

#### Configure the project

Edit `$ features/browser.py` 

to point to 

`$ home/full/path/to/python-behave/drivers/chromedriver`

You may have to download a different version and replace the above chromedriver depending on what version of Google Chrome you have installed on your machine.
Find appropriate chromedriver for your version of Google Chrome here: https://chromedriver.chromium.org/downloads

#### To run all tests

Run

`$ behave`

from project root.

#### To run an individual test by feature tag

`$ behave --tags=tag_name`

For example, 

`$ behave --tags=login`

### About the Behave Framework

Behave is a Gherkin-based Behavior-Driven Development (BDD) tool developed especially for Python. Read more about it [here](https://behave.readthedocs.io/en/latest/).



