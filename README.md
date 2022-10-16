# News_blog

## Description

On the site you can meet (there is a filtering of news by tag), implements pagination. Model view analytics is available, without the possibility of cheating.
In the admin panel, in addition to the standard set of features, you can delete, add, significantly. By API, you can request, always and add news.
Permissions are not installed, so every user can carry the update.

---

### Technologies:
* Python
* Django
* Pytest
* Git
* html
* Bootstrap
* DRF

---

### Installation
Clone the repository on the local machine:

```$ git clone https://github.com/vkletkin/Market```

 Create a virtual environment:
 
 ```$ python -m venv venv```
 
 Install dependencies:

```$ pip install -r requirements.txt```

Creating and applying migrations:

```$ python manage.py makemigrations``` and  ```$ python manage.py migrate```

Starting the django server:

```$ python manage.py runserver```

---

### URL examples

 [Список всех новостей ```http://127.0.0.1:8000```](http://127.0.0.1:8000)
 
 ```news/<int:pk>```         Новости по индентефикатору. [Пример ```http://127.0.0.1:8000/news/4```](http://127.0.0.1:8000/news/4)
 
 ```tag/<slug:slug>```       Использование тега.         [Пример   ```http://127.0.0.1:8000/tag/weather```](http://127.0.0.1:8000/tag/weather)
 
 ```analytics```             Аналитика просмотров.       [Пример```http://127.0.0.1:8000/analytics```](http://127.0.0.1:8000/analytics)

### API examples

```bash
GET [api/v1/news/](http://127.0.0.1:8000/api/v1/news/) - Получить список всех новостей.
При указании параметров limit и offset выдача должна работать с пагинацией
GET [api/v1/news/{id}](http://127.0.0.1:8000/api/v1/news/1/) - Получение новостей по id
DELETE [api/v1/news/{id}](http://127.0.0.1:8000/api/v1/news/1/) - Удаление новости по id
PATCH  [api/v1/news/{id}](http://127.0.0.1:8000/api/v1/news/1/) - Обновление новости по id
в body :
{
    "tags": null,
    "title": "",
    "text": "",
    "image": null,
    "slug": "",
    "author": null,
    "views": []
 }
```
