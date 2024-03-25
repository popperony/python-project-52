### Hexlet tests and linter status:
[![Actions Status](https://github.com/popperony/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/popperony/python-project-52/actions)
[![Python CI](https://github.com/popperony/python-project-52/actions/workflows/python-ci.yml/badge.svg)](https://github.com/popperony/python-project-52/actions/workflows/python-ci.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/06cade9720606195b4ae/test_coverage)](https://codeclimate.com/github/popperony/python-project-52/test_coverage)

### [Try the application](https://python-project-52-ewi5.onrender.com)

### Requirements
1. Python >=3.10
2. poetry >= 1.2.0
3. django >= 5.0.2
4. django-bootstrap5 >= 23.4
5. postgreSQL >= 16
5. gunicorn >= 21.2.0


### To get started
1. Clone git repo:
  `git@https://github.com/popperony/python-project-52.git`
2. Go to directory python-project-52:
  `cd python-project-52`
3.  Configuring `poetry` to create a virtual environment:
  `poetry config virtualenvs.in-project true`
4.  Create virtual environment and Install dependencies
  `make install`
5. Create `.env` file in the root folder similar to `.env.example`
5. Start app
  `make migrate`
  `make static`
  `make start`
