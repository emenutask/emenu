#E-menu

This is a simple app for managing menus in admin panel and displaying them to users

###Setup instructions

To set up the application run the following commands from the root directory
1. `docker-compose build`
2. `docker-compose start db`
3. `docker-compose start`
4. `docker-compose exec web ./manage.py migrate`

To manage menus via admin panel create admin account - it can be done by running:
`docker-compose exec web ./manage.py createsuperuser`
then visit localhost:8000/admin/

To see the default data -- load fixtures by running:
`docker-compose exec web ./manage.py loaddata menu`
and visit localhost:3000/
