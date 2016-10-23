## Requirement

-  Contoso Food Order online system.

## Assumption.

- Solving the challenge in python as visual studio IDE and technology is not open source and available only in windows environment.
-  Restaurant Promos : It refers to Hot Deals.
-  Menu : Refers to items in the menu.
-  Order : Refers to order an item.

## Git Link

-[Foodie](https://github.com/smathilakath/Codename-Foodie.git)

### Prerequisite;
  - Unix
  - Python v2.7.10 
  - MySQL v5.6.27
  - pip v7.1.2
  - Virtual environment v13.11.12
  - Django v1.9
  - wheel v0.24.0
  - Bootstrap v3.3.4
  
### Version
1.0.1

### Installation
- You need to create a database for the project on your localhost, edit as yours;
/Foodie/settings.py
```sh
DATABASES = {
    'default': {
    #it connects localhost serves by default
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'yourdbname',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
    }
}
```

- You need a  to install a stable version python 2 native programming language.
```sh
$ brew install python
```

- Install virtual environment
```sh
$ pip install virtualenv
```
- Activate the virtualenv
```sh
$ source bin/activate
```
- Install the requirement django packages
```sh
 $ pip install -r requirements.txt
```
- Sync the database 
```sh
 $ python manage.py syncdb
```
- Migrate the db

```sh
 $ python manage.py makemigrations
```
- Run the local server 

```sh
 $ python manage.py runserver
```
