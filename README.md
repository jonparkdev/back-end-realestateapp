***A coding challenge I had to do for an interview.  This is the backend written using django.  Only one endpoint is defined.  In the view of the endpoint, I randomly generated map coordinates of the Toronto area and did a linear transformation to fit them along the Toronto lakeshore.  This data is served using Django's restful api.  The link to the front end is:***

https://github.com/jonparkdev/front-end-realestateapp

## To execute

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

***Note: I was having trouble dealing with the Cross-Origin Resource Sharing mechanism so
I just turned it off in my browser***
