# Steps

1. Create virtual environment: `python3 -m venv ./env`

2. Active virtual environment: `source ./env/bin/activate`

3. Install Django: `pip3 install django`

4. Version check: `python3 -m django --version`

5. Freeze requirements: `pip3 freeze > requirements.txt`

6. Start Django project: `django-admin startproject project1`

7. in settings.py file from project1:
    1. insert `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` above STATIC_URL
    2. insert "template" in "DIRS" from template var

8. `cd project1`

9. Init server: `python3 manage.py runserver`

10. APP crate: `python3 manage.py startapp app1`

11. create "template" directory in app1 directory

12. ADD urls.py file on app1

13. Config urls

14. Create view

15. APP register

16. Make migrations:
    1. `python3 manage.py makemigrations`
    2. `python3 manage.py migrate`

17. Enter shell: `python3 manage.py shell`
    1. `from app1.models import User`
    2. `User.objects.all()`
    3 . `user = User(name= 'Rodrigo', phone=111111, email='brit101o@gmail.com')`
    3 . `user.save()`

18. Create superuser: `python3 manage.py createsuperuser`

19. Register model admin.py
