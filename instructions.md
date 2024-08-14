## GitHub

git clone https://github.com/iago-mansur/locallibrary.git

cd locallibrary

## Installing the virtual environment software

sudo pip3 install virtualenvwrapper

"""
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
"""

source ~/.bashrc

### Creating a virtual environment
mkvirtualenv my_django_environment


    deactivate — Exit out of the current Python virtual environment
    workon — List available virtual environments
    workon name_of_environment — Activate the specified Python virtual environment
    rmvirtualenv name_of_environment — Remove the specified environment.

## Installing Django
python3 -m pip install django~=4.2

django-admin startproject locallibrary .

python3 manage.py startapp catalog

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver

## Defining the LocalLibrary Models
python3 manage.py makemigrations
python3 manage.py migrate

## Django admin site
python3 manage.py createsuperuser

    Username (leave blank to use 'iago'): admin
    Email address: admin@example.com
    Password: admin123

python3 manage.py runserver

## User authentication and permissions

http://127.0.0.1:8000/admin/auth/group/add/
    Name: Library Members
    SAVE

http://127.0.0.1:8000/admin/auth/user/add/
    Username: userone
    Password: User1123
    SAVE

http://127.0.0.1:8000/admin/auth/user/2/change/

    Username: userone
    First name: User
    Last name: One
    Email address: user1@example.com
    Groups: Chosen groups: Library Members
    SAVE

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

## Working with forms

http://127.0.0.1:8000/catalog/book/<uuid:pk>/renew/
http://127.0.0.1:8000/catalog/author/create/


## Testing a Django web application

python3 manage.py test
python3 manage.py test catalog.tests





## New session
pip freeze > requirements.txt
deactivate

sudo pip3 install virtualenvwrapper
"""
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
"""
source ~/.bashrc
mkvirtualenv my_django_environment
pip install --upgrade pip
pip3 install -r requirements.txt