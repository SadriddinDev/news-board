<h2 align="center">NewsAPI project</h2>

- The project was created using django and djangorestframework.

- PostgreSQL was used for the database.

- API runs in the docker container.

- [django-celery-beat](doc:https://github.com/celery/django-celery-beat) was used to reset the posts upvote_count

- Code is formatted in [black](doc:https://github.com/psf/black)
- Code checked using [Flake8](doc:https://flake8.pycqa.org/en/latest/)
- Postman documentation: **[https://documenter.getpostman.com/view/15718974/UVXqDXuH](doc:https://documenter.getpostman.com/view/15718974/UVXqDXuH)**


- Heroku url: **[https://news-board-project.herokuapp.com/api/v1/](doc:https://news-board-project.herokuapp.com/api/v1/)**

---


## Installation and usage



```sh
git clone https://github.com/SadriddinDev/news-board.git
```

```sh
cd news-board/
```
---

## Docker-compose build and up for `Ubuntu`

```sh
sudo docker-compose build
```

```sh
sudo docker-compose up
```
---

## Docker-compose build and up for `Windows`

```sh
docker-compose build
```

```sh
docker-compose up
```

# Note! 
**Wait for download images from docker hub. It is might bi few seconds.**