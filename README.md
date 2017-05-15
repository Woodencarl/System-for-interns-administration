# System-for-interns-administration
Bakalářská práce Jana Máry na FIT ČVUT vypracována v roce 2017. Licence podobná GPL

Pro užití musíte mít nainstalované Django verzi 1.11.
Po naklonování repozitáře spusťe následující příkazy:

```
<clone_dir>/isbackend/>python manage.py migrate
<clone_dir>/isbackend/>python manage.py createsuperuser
<clone_dir>/isbackend/>python manage.py runserver
```
now you can visit page [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log-in with credentials you used during "createsuperuser" command

