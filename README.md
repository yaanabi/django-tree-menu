1) Clone this project.
2) Create virtual env from cloned project: python -m venv myvenv
3) install requirements: pip install -r requirements.txt
4) rename .env.template to .env
5) type: python manage.py runserver

 DB data for menu and superuser are included in project folder.
 Superuser:
   username: admin
   password: admin 
go to 127.0.0.1/ to see 'Home' tree menu. 

To see how many queries made run test: python manage.py test

Uncomment {% draw_menu 'Catalog'%} in home.html to load 'Home' and 'Catalog' on the same page (total queries=2, 1 for each menu)

To add new menu or menu_items go to /admin and use superuser credentials.


