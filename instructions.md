## GitHub

git clone https://github.com/iago-mansur/locallibrary.git

cd locallibrary

## Installing the virtual environment software

sudo pip3 install virtualenvwrapper

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

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