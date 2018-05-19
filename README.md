## Local install guide

You should have python 3.6 installed

1. Git clone from https://github.com/anndoc/milo-django-task
1. Create a virtualenv:
    - `virtualenv env/milo-env`
    - `source env/milo-env/bin/activate`
1. Run `pip install -r requirements/local.txt`
1. Create `.env` file and copy data from `env.example` file
1. Run `python manage.py migrate`
1. Run `python manage.py runserver` and visit `localhost:8000`


## Release notes

- [x] Set up a basic latest Django installation
- [x] Extend the User model to have
    - a birthday field of type date
    - a random number field of type integer that is assigned a value from 1-100 on creation

- [x] Create views for: list of all users, viewing, adding, editing and deleting a single user
- [x] Create two template tags:
    - a tag that will display "allowed" if the user is > 13 years old otherwise display "blocked"
    - a tag that will display the BizzFuzz result of the random number that was generated
    for the user. The BizzFuzz specification is that for multiples of three print "Bizz" instead of the number and for the multiples of five print "Fuzz". For numbers which are multiples of both three and five print "BizzFuzz"
    - add a column to the list view after the birthday column that uses the allowed/blocked
    tag
    - add a column to the list view after the random number column that uses the BizzFuzz tag
- [x] Unit tests
- [ ] Optional task: Create a download link on the list view. The link would return the list of results in Excel's format


## Screenshots

[List View](http://joxi.net/Grqb7pVcNpXMPm)

[Detail View](http://joxi.net/BA0LEoaiBgLjWA)
