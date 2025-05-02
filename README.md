# Django 學習日誌

> Output installed packages in requirements format.
> Packages are listed in a case-insensitive sorted order.

```
$ pip freeze
asgiref==3.8.1
Django==5.2
sqlparse==0.5.3
tzdata==2025.2
```

> Generate a requirements file and then install from it in another environment.

```
$ pip freeze > requirements.txt
$ python -m venv env
$ source env/Scripts/activate
(env)
$ pip install -r requirements.txt
(env)
```

---

> Installing `virtualenv`.
> `virtualenv` is a tool to create isolated Python environments.
 
```
$ pip install virtualenv
```

---

> Creating virtual environment (env).

```
$ python -m venv env
```

---

> Activating virtual environment.

```
$ source env/Scripts/activate
(env)
```

---

> Deactivating virtual environment.

```
$ deactivate
```

---

> Installing Django in virtual environment.

```
$ pip install django
Collecting django
  Using cached Django-5.2-py3-none-any.whl.metadata (4.1 kB)
Collecting asgiref>=3.8.1 (from django)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from django)
  Using cached sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Collecting tzdata (from django)
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Using cached Django-5.2-py3-none-any.whl (8.3 MB)
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.8.1 django-5.2 sqlparse-0.5.3 tzdata-2025.2
(env)
```

---

> Bootstrap a new Django project.

```
$ django-admin.exe startproject mysite .
$ cd mysite/
$ ls
__init__.py  asgi.py  settings.py  urls.py  wsgi.py
```

* `__init__.py`: 讓 Python 將目錄視為一個套件(package)。
* `asgi.py`: ASGI(Asynchronous Server Gateway Interface)入口，用於處理非同步通訊協定(例如 WebSocket)。
* `settings.py`: 專案配置中心，包含資料庫設定、已安裝的 App、Middleware、靜態檔案(Static File，例如 images, JavaScript, CSS)設定、安全性設定等。
* `urls.py`: URL 路由配置，將 URL 對應到特定的 view。也就是設定 urlpatterns，將不同的 URL pattern 對應到特定的函式或類別。
* `wsgi.py`: WSGI(Web Server Gateway Interface)入口，用於處理同步 HTTP Request 的標準介面。

---

> Start the development server.

```
python manage.py runserver
```

---

> Creating an admin user

```
$ python manage.py createsuperuser
```

---

> Changing user's password.

```
$ python manage.py changepassword <username>
```

---

> Creating table.

```
$ python manage.py makemigrations
```

---

> Django structure.

![Django structure](https://hackmd.io/_uploads/rkfnRlcyeg.png)

1. User -> Django -> URL -> View -> Model 
2. Model -> View -> Template -> User

* **URLs:** While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.
* **View:** A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates.
* **Models:** Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database.
* **Templates:** A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn't have to be HTML!

---

## Hello World!

1. 配置 `urls.py`。

    ```=
    from . import views
    
    urlpatterns = [
        path('', views.home, name='home'), # ''中不需要有 home/
    ]
    ```

2. 在 mysite 資料夾建立 `views.py`。
3. 配置 `views.py`。

    ```
    from django.shortcuts import render

    def home(request):
        # return HttpResponse('<h1>Hello World!</h1>')
        return render(request, 'home.html')
    ```
4. 在 `templates` 資料夾建立 `home.html`。
    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To Do List and Task Management App | Django To Do</title>

        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7"
              crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq"
                crossorigin="anonymous"></script>
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <!-- Custom CSS -->
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
    <div class="container">
        <h3 class="pt-4 text-center">Django To Do</h3>
        <div class="row">
            <div class="col-md-6 col-lg-6" style="height: 600px; overflow: scroll;">
                <h4>My Day</h4>
                <p class="text-muted">{% now "jS F Y" %}</p>
                <!-- List of all the tasks for the day -->
                <div class="card m-1">
                    <div class="card-body">
                        This is some Task.
                        <span style="position: relative; float: right;">
                                <a class="btn btn-success"><i class="bi bi-check"></i> Complete</a>
                                <a class="btn btn-danger"><i class="bi bi-trash"></i> Delete</a>
                                <a class="btn btn-primary"><i class="bi bi-pencil-square"></i> Edit</a>
                        </span>
                    </div>
                </div>

            </div>
            <div class="col-md-6 col-lg-6" style="height: 600px; overflow: scroll;">
                <div class="col-md-6 mb-4">
                    <h4>Completed Tasks</h4>
                </div>
                <!-- List of all the tasks that have completed -->
                <div class="card m-1">
                    <div class="card-body">
                        This is the completed task.
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 col-lg-6 p-0" style="position: absolute; bottom: 50px;">
                <!-- To Do Form -->
                <form action="">
                    <div class="form-group">
                            <span style="display: flex;">
                                <input type="text" class="form-control" placeholder="Enter a task…">
                                <button class="btn btn-primary" style="width: 100px;"><i class="bi bi-plus"></i> Add</button>
                            </span>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </body>
    </html>
    ```
5. 配置 `settings.py` 的 `TEMPLATES`。
    
    ```
    TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'], # 新增 templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
    ]
    ```

6. 處理 Static file (CSS、圖片、影片等)。
    
    * 在 mysite 資料夾建立 `static` 資料夾，並在裡面建立 `css` 和 `images` 資料夾。
    * 在 `css` 資料夾中建立 `style.css`。
        ```
        body{
            background-color: lightgray;
        }
        ```
    * 在 `home.html` 中引入 `style.css`。
        ```
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
        
        <image src="{% static 'images/ZYXEL LOGO.png' %}" alt="ZYXEL LOGO"></image>
        ```
    * 於 `settings.py` 加入以下程式碼：
        ```
        STATIC_URL = "static/" # http://yourwebsite/static/style.css
        STATIC_ROOT = BASE_DIR / "static"
        STATICFILES_DIRS = [
            "mysite/static",
        ]
        ```
    * 在 `home.html` 中加入以下程式碼：
        ```
        {% load static %}
        ```

## Project 01 - Employee Directory

1. 建立 app，在 Django 中，每一個 app 通常只負責一個功能或一組功能。

    ```
    $ python manage.py startapp employee
    (env)
    ```
    
2. 執行 migration 將「Python 程式裡的 Table 定義」同步到「真正的 Database」。
    
    ```
    $ python manage.py migrate
    ```
    
3. 建立管理員。
    
    ```
    $ python manage.py createsuperuser
    Username (leave blank to use 'yungh'): djangoadmin
    Email address: lc20240328@gmail.com
    Password:rR890101
    Password (again):rR890101
    Superuser created successfully.
    (env)
    ```

4. 編輯 `models.py` 來建立資料庫 table 和 field。

    ```
    from django.db import models

    # Create your models here.
    class Employee(models.Model): # Inheritance models.Model
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        designation = models.CharField(max_length=100)
        email = models.EmailField(max_length=100, unique=True)
        phone = models.CharField(max_length=10, blank=True)
        portrait = models.ImageField(upload_to='images/', null=True, blank=True)
        createdAt = models.DateTimeField(auto_now_add=True) # Automatically set the field to now when the object is first created.
        updatedAt = models.DateTimeField(auto_now=True) # Automatically set the field to now every time the object is saved.

        def __str__(self):
            return self.first_name
    ```

5. 將 `employee` 註冊到 `settings.py`。

    ```
    # Application definition
    # Performing business logic
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "employee",
    ]
    ```

6. 安裝圖片套件

    ```
    $ pip install Pillow
    Collecting Pillow
      Downloading pillow-11.2.1-cp313-cp313-win_amd64.whl.metadata (9.1 kB)
    Downloading pillow-11.2.1-cp313-cp313-win_amd64.whl (2.7 MB)
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 1.6 MB/s eta 0:00:00
    Installing collected packages: Pillow
    Successfully installed Pillow-11.2.1
    (env)
    ```
    
7. 告訴 Django：我要在 Database 建立一張 Employee Table。

    ```
    $ python manage.py makemigrations
    Migrations for 'employee':
      employee\migrations\0001_initial.py
        + Create model Employee
    (env)
    ```
    
8. Django 實際去 Database 建立了對應的 Table。
    
    ```
    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, employee, sessions
    Running migrations:
      Applying employee.0001_initial... OK
    (env)
    ```

9. 在 `employee` app 的 `admin.py` 註冊 employee。

```
    from django.contrib import admin
    from employee.models import Employee

    # Register your models here.
    admin.site.register(Employee)
```

10. 處理上傳到 table 的圖片。

    * 建立 `media` 資料夾並在其中新增 `images` 資料夾。
    * 在 `settings.py` 裡面配置以下程式碼：
    
    ```
    # Media files configuration
    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"
    ```
    
    * 然後於 `urls.py` 配置下列程式碼：

    ```
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', views.home),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    
11. 將員工資料顯示在前端。

* 讓 `views.py` 將 Employee table 中的全部資料查出來，然後將查到的資料放進一個 `context` 字典，再將這個字典傳給 `home.html` 模板，最後在瀏覽器上渲染並顯示出來。

    ```
    # from django.http import HttpResponse
    from django.shortcuts import render
    from employee.models import Employee

    def home(request):
        # Retrieve all Employee records from the database
        employee = Employee.objects.all()

        # Print the retrieved employee queryset to the console
        print(employee)

        # Create a context dictionary to pass data to the template
        context = {
            'employee': employee,
        }

        # return HttpResponse('<h1>Hello World!</h1>')
        # return render(request, 'home.html')
        # Render the 'home.html' template and pass the context dictionary
        return render(request, 'home.html', context)
    ```

* 在模板 `home.html` 接收 QuerySet 資料。

    ```
    {% load static %} <!-- Using the static template tag to build the URL for the given relative path -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- RWD -->
        <meta http-equiv="X-UA-Compatible" content="ie=edge">  <!-- Compatible with Internet Explorer -->

        <!-- Include Bootstrap’s compiled CSS or JS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>

        <!-- <link rel="stylesheet" href="{% static 'css/style.css' %}"> -->

        <title>Django Basic</title>
    </head>
    <body>
        <div class="container pt-1">
            <h1>Employee List</h1>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Full Name</th>
                        <th scope="col">Designation</th>
                        <th scope="col">Phone Number</th>
                    </tr>
                </thead>
                <tbody>
                    {% for emp in employee %}
                    <tr>
                        <th scope="row">{{ forloop.counter }}</th>
                        <td>{{ emp.first_name }} {{ emp.last_name }}</td>
                        <td>{{ emp.designation }}</td>
                        <td>{{ emp.phone }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>

            <!-- <image src="{% static 'images/ZYXEL LOGO.png' %}" alt="ZYXEL LOGO"></image> -->

        </div>
    </body>
    </html>
    ```
    
* 點下員工會顯示個資細節。

    * 將所有 `/employee/` 開頭的 URL，轉交給 employee app 裡的 `urls.py` 處理。

    ```
    from django.conf import settings
    from django.contrib import admin
    from django.urls import path, include
    from . import views

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', views.home),
        path('employee/', include('employee.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

* 在 employee app 中新增 `urls.py` 檔案。

    ```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('<int:pk>/', views.employee_detail), # pk (primary key) is the url parameter
    ]
    ```

* 然後在 `views.py` 中新增下列程式碼：

    ```
    from django.http import Http404, HttpResponse
    from django.shortcuts import render, get_object_or_404

    from employee.models import Employee

    # Create your views here.
    def employee_detail(request, pk):
        employee = get_object_or_404(Employee, pk=pk) # Simplify try/except
        # print(employee)
        context = {
            'employee': employee,
        }
        return render(request, 'employee_detail.html', context)
        """
        try:
            employee = Employee.objects.get(pk=pk) # all: multiple choice
            print(employee)
        except:
            raise Http404
        """
    ```

* 在 `urls.py` 中修改 home 的 path：

    ```
    from django.conf import settings
    from django.contrib import admin
    from django.urls import path, include
    from . import views

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path("admin/", admin.site.urls),
        path('', views.home, name='home'),
        path('employee/', include('employee.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    ```

* 讓使用者點下特定員工就可以連結到 `employee_detail.html`，所以必須修改 employee app中 `url.py` 的程式碼：

```
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.employee_detail, name='employee_detail'), # pk (primary key) is the url parameter
]
```

* 修改 `home.html`。

    ```
    {% load static %} <!-- Using the static template tag to build the URL for the given relative path -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- RWD -->
        <meta http-equiv="X-UA-Compatible" content="ie=edge">  <!-- Compatible with Internet Explorer -->

        <!-- Include Bootstrap’s compiled CSS or JS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>

        <!-- <link rel="stylesheet" href="{% static 'css/style.css' %}"> -->

        <title>Django Basic</title>
    </head>
    <body>
        <div class="container pt-1">
            <h1>Employee List</h1>
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Full Name</th>
                        <th scope="col">Designation</th>
                        <th scope="col">Phone Number</th>
                    </tr>
                </thead>
                <tbody>
                    {% for emp in employee %}
                    <tr>
                        <th scope="row">{{ forloop.counter }}</th>
                        <td><a href="{% url 'employee_detail' emp.id %}">{{ emp.first_name }} {{ emp.last_name }}</td>
                        <td>{{ emp.designation }}</td>
                        <td>{{ emp.phone }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>

            <!-- <image src="{% static 'images/ZYXEL LOGO.png' %}" alt="ZYXEL LOGO"></image> -->

        </div>
    </body>
    </html>
    ```

* 新增 `employee_detail.html`

    ```
    {% load static %} <!-- Using the static template tag to build the URL for the given relative path -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- RWD -->
        <meta http-equiv="X-UA-Compatible" content="ie=edge">  <!-- Compatible with Internet Explorer -->

        <!-- Include Bootstrap’s compiled CSS or JS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js" integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq" crossorigin="anonymous"></script>

        <title>Django Basic</title>
    </head>
    <body>
        <div class="container pt-1">
            <div class="card mx-auto" style="width: 18rem;">
                <img src="{{ employee.portrait.url }}" class="card-img-top" alt="Employee Portrait">
                <div class="card-body">
                    <p class="card-text">{{ employee.first_name }} {{ employee.last_name }}</p>
                    <p class="card-text">{{ employee.designation }}</p>
                    <p class="card-text">{{ employee.email }}</p>
                    <p class="card-text">{{ employee.phone }}</p>
                </div>
                <a href="{% url 'home' %}" class="btn btn-primary">Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    ```

## Project 02 - TODO App

0. 前置作業

    ```
    $ python -m venv env

    $ source env/Scripts/activate

    (env)
    $ pip install django

    (env)
    $ pip freeze
    asgiref==3.8.1
    Django==5.2
    sqlparse==0.5.3
    tzdata==2025.2

    (env)
    $ django-admin startproject mytodo .

    (env)
    $ python manage.py runserver

    (env)
    $ python manage.py migrate

    (env)
    $ python manage.py createsuperuser
    ```

1. 配置 `urls.py`。

    ```=
    from django.contrib import admin
    from django.urls import path

    from . import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", views.home, name='home'),
        path("todo/", views.todo, name='todo'),
    ]
    ```

2. 在 `mysite` 資料夾建立 `views.py`，再配置 `views.py`。

    ```
    # from django.http import HttpResponse
    from django.shortcuts import render

    def home(request):
        # return HttpResponse('<h1>Hello World!</h1>')
        return render(request, 'home.html')
    
    def todo(request):
        return render(request, 'todo.html')
    ```

3. 在 `templates` 資料夾建立 `todo.html`。
    
    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To Do List and Task Management App | Django To Do</title>

        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet"
              integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq"
                crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <!-- Custom CSS -->
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
    <div class="container">
        <h3 class="pt-5 text-center">Django To Do</h3>
        <div class="row">
            <h4>My Day</h4>
            <p class="text-muted">{% now "jS F Y" %}</p>
            <div class="col-md-7 col-lg-7" style="height: 450px; overflow: scroll;">
                <!-- List of all the tasks for the day -->
                <div class="card m-1">
                    <div class="card-body">
                        This is some Task
                        <span style="position: relative; float: right;">
                                <a class="btn btn-success"><i class="bi bi-check"></i> Mark as Done</a>
                                <a class="btn btn-danger"><i class="bi bi-trash"></i></a>
                                <a class="btn btn-primary"><i class="bi bi-pencil-square"></i></a>
                            </span>
                    </div>
                </div>

            </div>
            <div class="col-md-5 col-lg-5">
                <h5>Completed Tasks</h5>
                <!-- List of all the tasks that have completed -->
                <div class="card m-1">
                    <div class="card-body">
                        This is the completed task.
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 col-lg-6 p-0" style="position: absolute; bottom: 50px;">
                <!-- To Do Form -->
                <form action="">
                    <div class="form-group">
                            <span style="display: flex;">
                                <input type="text" class="form-control" placeholder="Add a task">
                                <button class="btn btn-primary" style="width: 200px;"><i class="bi bi-calendar-plus"></i> Add</button>
                            </span>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </body>
    </html>
    ``` 

4. 配置 `settings.py` 的 `TEMPLATES`。
    
    ```
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ['templates'],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]
    ```
5. 處理 Static file (CSS 和 JavaScript 等)。
    
    * 在 `mysite` 資料夾建立 `static` 資料夾，並在裡面建立 `css` 資料夾。
    * 在 `css` 資料夾中建立 `style.css`。
        ```
        .form-control {
            padding: 2rem 1rem !important;
        }
        ```
    * 在 `todo.html` 中引入 `style.css`。
        
        ```
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
        ```
        
    * 於 `settings.py` 加入以下程式碼：
        
        ```
        STATIC_URL = "static/"
        STATIC_ROOT = BASE_DIR / "static"
        STATICFILES_DIRS = [
            "mytodo/static",
        ]
        ```
        
    * 在 `todo.html` 中加入以下程式碼：
        
        ```
        {% load static %}
        ```
    * 然後於 `urls.py` 配置下列程式碼：

    ```
    from django.contrib import admin
    from django.urls import path

    from . import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", views.todo, name='todo'),
    ]
    ```

6. 配置 Git

```
$ git init
Initialized empty Git repository in D:/Programming/Python/Django/DjangoTodo/.git/

(master)
$ git add -A
warning: in the working copy of '.idea/inspectionProfiles/Project_Default.xml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of '.idea/inspectionProfiles/profiles_settings.xml', LF will be replaced by CRLF the next time Git touches it

(master)
$ git status

(master)
$ git branch -M main

(main)
$ git remote add origin https://github.com/whsh99/django-todo.git

(main)
$ git push -u origin main
Enumerating objects: 30, done.
Counting objects: 100% (30/30), done.
Delta compression using up to 16 threads
Compressing objects: 100% (26/26), done.
Writing objects: 100% (30/30), 13.82 KiB | 2.76 MiB/s, done.
Total 30 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/whsh99/django-todo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

7. 建立 app (封裝了特定功能或子系統的 Python 套件(package))。

```
(env)
$ python manage.py startapp todo
```

8. 將 `todo` 註冊到 `settings.py`。

    ```
    # Application definition
    
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "todo",
    ]
    ```

9. 編輯 app 的 `models.py` 來定義資料庫 table 和 field。

    ```
    from django.db import models

    # Create your models here.
    class Task(models.Model):
        task = models.CharField(max_length=200)
        is_complete = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.task
    ```
    
10. 在 app 的 `admin.py` 註冊 todo，讓它出現在後端管理介面中。

    ```
    from django.contrib import admin
    from .models import Task

    # Register your models here.
    admin.site.register(Task)
    ```
    
11. 使 Django 根據 `models.py` 產生一個 migration 檔案(如 `0001_initial.py`)，其中記錄了要對資料庫做哪些變更(如建立 Task model 對應的 Table)。

    ```
    $ python manage.py makemigrations
    Migrations for 'todo':
      todo\migrations\0001_initial.py
        + Create model Task
    ```

12. Django 讀取並執行所有尚未應用的 migration，實際在資料庫中建立 table。

    ```
    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions, todo
    Running migrations:
      Applying todo.0001_initial... OK
    ```

13. 為了將每一筆 Task 顯示在前端，就必須透過 `views.py` (不是 app 目錄中的 `views.py`)將 Task table 中的全部資料查出來，然後將查到的資料放進一個 `context` 字典，再將這個字典傳給 `todo.html` 模板，最後在瀏覽器上渲染並顯示出來。

    ```
    # from django.http import HttpResponse
    from django.shortcuts import render
    from todo.models import Task

    # Create your views here.
    def todo(request):
        tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
        # Print the retrieved task queryset to the console
        print(tasks)

        context = {
            'tasks': tasks,
        }
        return render(request, 'todo.html', context)
    ```
    
    * 在模板 `todo.html` 接收 QuerySet 資料。

    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>To Do List and Task Management App | Django To Do</title>

        <!-- Bootstrap -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7"
              crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq"
                crossorigin="anonymous"></script>
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <!-- Custom CSS -->
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
    <div class="container">
        <h3 class="pt-4 text-center">Django To Do</h3>
        <div class="row">
            <div class="col-md-6 col-lg-6" style="height: 600px; overflow: scroll;">
                <h4>My Day</h4>
                <p class="text-muted">{% now "jS F Y" %}</p>
                <!-- List of all the tasks for the day -->
                {% for task in tasks %} # 注意這裡！
                <div class="card m-1">
                    <div class="card-body">
                        {{ task.task }} # 注意這裡！
                        <span style="position: relative; float: right;">
                                <a class="btn btn-success"><i class="bi bi-check"></i> Complete</a>
                                <a class="btn btn-danger"><i class="bi bi-trash"></i> Delete</a>
                                <a class="btn btn-primary"><i class="bi bi-pencil-square"></i> Edit</a>
                        </span>
                    </div>
                </div>
                {% endfor %}
            </div>
            <div class="col-md-6 col-lg-6" style="height: 600px; overflow: scroll;">
                <div class="col-md-6 mb-4">
                    <h4>Completed Tasks</h4>
                </div>
                <!-- List of all the tasks that have completed -->
                <div class="card m-1">
                    <div class="card-body">
                        This is the completed task.
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 col-lg-6 p-0" style="position: absolute; bottom: 50px;">
                <!-- To Do Form -->
                <form action="">
                    <div class="form-group">
                            <span style="display: flex;">
                                <input type="text" class="form-control" placeholder="Enter a task…">
                                <button class="btn btn-primary" style="width: 100px;"><i class="bi bi-plus"></i> Add</button>
                            </span>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </body>
    </html>
    ```
    
14. 客製化 Django 管理後台來顯示以下欄位：

    ```
    from django.contrib import admin
    from .models import Task

    class TaskAdmin(admin.ModelAdmin):
        list_display = ('task', 'is_completed', 'created_at','updated_at')
        search_fields = ('task',)

    # Register your models here.
    admin.site.register(Task, TaskAdmin)
    ```

15. 將所有以 `/todo/` 開頭的 request，交由 todo app 下的 `urls.py` 處理。

    ```
    from django.contrib import admin
    from django.urls import path, include

    from . import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", views.todo, name='todo'),

        # To Do
        path('todo/', include('todo.urls')),
    ]
    ```

16. 接著必須在 `todo/urls.py` 中設定路由，把 `/addTask/` 路徑指向 `views.addTask` 函式。

```
from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
]
```

17. 在 `views.addTask` 新增以下程式碼：

```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('todo')
```

18. 為了讓 view 可以正確取得使用者輸入的任務內容，就必須在 template 設計好傳送資料用的表單。

```
<form action="{% url 'addTask' %}" method="post">
    {% csrf_token %}
    <div class="form-group">
        <span style="display: flex;">
            <input type="text" name="task" class="form-control" placeholder="Enter a task…">
            <button type="submit" class="btn btn-primary" style="width: 100px;"><i class="bi bi-plus"></i> Add</button>
        </span>
    </div>
</form>
```

19. 顯示出 Completed Tasks

    * 在 `mytodo/views.py` 新增以下程式碼，使其能查詢到已完成的 task。

    ```
    completed_tasks = Task.objects.filter(is_completed=True)
        #print(completed_tasks)

        context = {
            'tasks': tasks,
            'completed_tasks': completed_tasks,
        }
    ```

    * 讓 teplate 可以顯示 completed task。

    ```
    <div class="col-md-6 col-lg-6" style="height: 600px; overflow: scroll;">
        <div class="col-md-6 mb-4">
            <h4>Completed Tasks</h4>
        </div>
        <!-- List of all the tasks that have completed -->
        {% for task in completed_tasks %}
            <div class="card m-1">
                <div class="card-body">
                    {{ task.task }}
                </div>
            </div>
        {% endfor %}
    </div>
    ```
    
20. Mark as Done/Undone

* 在 `todo.html` 中加入以下程式碼，就會發現每一個 task 都有一個 primary key：

    ```
    {{ task.task }} - PK = {{ task.pk }}
    ```

* 呈上，接下來就可以利用這個 primary key 作為依據來找出要標記為完成的 task。首先，在 `todo/urls.py`

    ```
    urlpatterns = [
        ...
        path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    ]
    ```

* 然後就要實際在 `todo/views.py` 新增 `mark_as_done()`。

    ```
    def mark_as_done(request, pk):
        return HttpResponse(pk)
    ```

* 晚一點再來完成 `mark_as_done()`，接著去 `todo.html` 把 Done 按鈕部分完成。

    ```
    <a href="{% url 'mark_as_done' task.pk %}" class="btn btn-success"><i class="bi bi-check"></i> Complete</a>
    ```

* 將 `mark_as_done` 完成。

    ```
    def mark_as_done(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = True
        task.save()
        return redirect('todo')
    ```

21. Edit Task

* 帶出要修改的 Task

    * 利用 primary key 作為依據來找出要標記為完成的 task。首先，在 `todo/urls.py`

        ```
        urlpatterns = [
            ...
            path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
        ]
        ```

    * 然後就要實際在 `todo/views.py` 新增 `edit_task()`。

        ```
        def edit_task(request, pk):
        get_task = get_object_or_404(Task, pk=pk)
        if request.method == 'POST':
            return 
        else:
            context = {
                'get_task': get_task,
            }
        return render(request, 'edit_task.html', context)
        ```

    * 接著新增 `edit_task.html`。

        ```
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Editing To Do Task | Django To Do</title>

            <!-- Bootstrap -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css"
                  rel="stylesheet"
                  integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7"
                  crossorigin="anonymous">
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js"
                    integrity="sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq"
                    crossorigin="anonymous"></script>
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
            <!-- Custom CSS -->
            <link rel="stylesheet" href="{% static 'css/style.css' %}">
        </head>
        <body>
            <div class="container">
                <h3 class="pt-5 pb-5 text-center">Django To Do - Edit Task</h3>
                <form action="" method="post" style="width: 500px; margin: 0 auto;">
                        {% csrf_token %}
                        <div class="form-group">
                                <span style="display: flex;">
                                    <input type="text" name="task" class="form-control" placeholder="Enter a task…" value="{{ get_task.task }}">
                                    <button type="submit" class="btn btn-primary" style="width: 200px;"><i class="bi bi-upload"></i> Update</button>
                                </span>
                        </div>
                    </form>
            </div>
        </body>
        </html>
        ```

    * 記得在 `todo.html` 也要把 Edit 按鈕部分連到 `edit_task.html`。

        ```
        <a href="{% url 'edit_task' task.id %}" class="btn btn-primary"><i class="bi bi-pencil-square"></i> Edit</a>
        ```

* 完成 `POST`。
    
    * 在 `edit_task.html` 加入 form 的 action。
    
    ```
    <form action="{% url 'edit_task' get_task.pk %}" method="post" style="width: 500px; margin: 0 auto;">
    ```

    * 讓 `edit_task` 可以回傳 POST 的表單。
    
    ```
    def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('todo')
    ```

22. 刪除 Task

* `\mytodo\urls.py`

    ```
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    ```

* `\todo\views.py`

    ```
    def delete_task(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('todo')
    ```
    
* `\mytodo\todo.html`

    ```
    <a href="{% url 'delete_task' task.id %}" class="btn btn-danger"><i class="bi bi-trash"></i> Delete</a>
    ```
