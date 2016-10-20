# Django-Tutorial

Follow along with the slides here: ________________
Adapted from: https://docs.djangoproject.com/en/1.10/intro/tutorial01/

##Step 0: Clone the Repository
If you don't have git, install it here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
Once you have it, clone this repo with the following command: 

```
$ git clone https://github.com/noahpresler/Django-Tutorial.git
```

##Step 1: Install Python/Pip

Django is a web framework that works with Python. If you don't already have python, install it here: https://www.python.org/downloads/

Now, we are going to go ahead and install Django, and VirtualEnv. To do this, simply enter the repository:
```
cd \path\to\Django-Tutorial
```
and checkout the file 'requirements.txt', you'll see:
```
Django==1.9.2
virtualenv==1.11.4
```
Now let's install pip. Simply run
```
sudo python get-pip.py
```
Now you've installed pip!
##Step 2: Enter your Virtual Environment and Install Requirements
First, enter:
```
source venv/bin/activate
```
Then, execute: 
```
pip install -r --user requirements.txt
```
You will install Django version 1.9.2 and virtulenv 1.11.4

##Step 3: Boom, Workshop Done!
Try this: 
```
python manage.py runserver
```
Now, head over to 'localhost:8000' [in your favorite browser (Chrome, of course)](https://gfycat.com/IllustriousPowerfulIlsamochadegu)
Check it out! Your server is working.

Your app works - k bai! 

##Step 4: Jk, jk - let's get to it: Write your First View

Now, you'll see in your directory the following: 
```
Django-Tutorial/
├── db.sqlite3
├── djangoworkshop
├── get-pip.py
├── manage.py
├── polls
├── README.md
├── requirements.txt
└── venv
```
This is because we've setup your app directory for you. In the future you can execute 'python manage.py startapp name_of_your_app' to do this. 

Let's go ahead and write one of those views we talked about earlier. Open the file **polls/views.py**
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Look mom! I made a web app!")
```
When a request is routed to this method, it will respond with HTTP as shown above.

In order to see the result, we need to route a url to call our view! To do this, go ahead and open **polls/urls.py** and include the following code:
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
What this does is map the url matching regex '^$' (which would be localhost:8000 without anything after) to the method named 'index' in our views file. 
