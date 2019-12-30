cd .../demo_django
#create project
django-admin startproject demo_site

#start up project ==> http://127.0.0.1:8000/
python manage.py runserver

#create app
python manage.py startapp demo_app1

#update demo_app1/views.py
#update urls.py under demo_app1 and demo_site

#start up project and app ==> http://localhost:8000/app1/
python manage.py runserver

