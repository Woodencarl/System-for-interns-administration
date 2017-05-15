# System-for-interns-administration
Bakalářská práce Jana Máry na FIT ČVUT vypracována v roce 2017. Licence podobná GPL.

Pro užití musíte mít nainstalované Django verzi 1.11.
Po naklonování/rozbalení repozitáře spusťe následující příkazy:

```
<clone_dir>/isbackend/> python manage.py flush
<clone_dir>/isbackend/> python manage.py makemigrations
<clone_dir>/isbackend/> python manage.py migrate
<clone_dir>/isbackend/> python manage.py createsuperuser
<clone_dir>/isbackend/> python manage.py runserver
```
teď můžete navštívit stránky [http://127.0.0.1:8000/](http://127.0.0.1:8000/) nebo pro administraci [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) a přihlásit se údaji vytvořených během příkazu "createsuperuser".

