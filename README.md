# Searcher
🕸️ Live preview of website [Searcher](https://app-meta-searcher.herokuapp.com/).



<div align="center">

![Django](https://img.shields.io/badge/django%20versions-%203.0.5-blue)
 [![Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
</div> 


--------
The Searcher lets you find the complete information about Android, Playstore apps. It can also help you to suggest meta-tags based on the website url saved in the ever-growing database.

-----------------------------------------------

## Features

- [x] Get app info from playstore, appstore.
- [x] Get recommended tags and meta-description from the website.
- [x] Added AJAX request.
- [x] Used Bootstrap theme.
- [x] Added Unit testing.
- [x] Register modal to admin to manage the database.
- [x] Added 404 Page.
- [x] Validation for package name, appID, appName and url.
-----------------------------------------------

## Todo
- [ ] NLTK Module to recommend similar words based on meta-tags.

-----------------------------------------------
## Steps to run

- Clone this [repository](https://github.com/Arjun009/search).
- pip install -r ```requirements.txt```.
- open command prompt and type ```python manage.py runserver```
- To run the unit testing type ```python manage.py test app``` for app searcher and ```python manage.py test keywords``` for keyword finder app in CMD.
-----------------------------------------------

## Unit Testing

#### For keywords
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
Ran 5 tests in 2.695s

OK
Destroying test database for alias 'default'...
```
#### For app
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....

Ran 4 tests in 17.546s

OK
Destroying test database for alias 'default'...
```
-----------------------------------------------
## Contributions

 Open to `enhancements` & `bug-fixes` :smile: 

-----------------------------------------------

## Contributors

- [Arjun Mohnot](https://github.com/arjun009)

-----------------------------------------------
