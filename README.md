# E-menu

This is a simple app for managing menus in admin panel and displaying them to users

### Setup instructions

To set up the application run the following commands from the root directory
1. `docker-compose build`
2. `docker-compose up db`
3. `docker-compose up`
4. `docker-compose exec web ./manage.py migrate`

To manage menus via admin panel create admin account - it can be done by running

`docker-compose exec web ./manage.py createsuperuser`

then visit [localhost:8000/admin/](http://localhost:8000/admin/)

To load fixture with default menus run

`docker-compose exec web ./manage.py loaddata menu`

The application will be available at [localhost:3000/](http://localhost:3000)

To run the tests use the following command

`docker-compose exec web ./manage.py test`

### To consider later:

* change docker settings to skip starting database separately from other containers, see e.g. [https://docs.docker.com/compose/startup-order/](https://docs.docker.com/compose/startup-order/)
* create separate settings for different environments
* add more features like uploading and displaying dish images
