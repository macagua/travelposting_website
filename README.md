# TRAVELPOSTING

Travelposting definition

## Installation

You need depends necessary for run the app:
```bash
$ sudo apt install build-essential git curl python3.7.4-dev 
```

Use the package manager [pipenv](https://docs.pipenv.org/en/latest/)



If you use macos use 

```bash
brew install pipenv
```
If you use linux use

```bash
apt install pipenv
```

To install the packages to work with django cms use the following command

```bash
pipenv --python 3.7.4 install 
```
Now you should see the .env-example file and put your data and change name to .env for run the project. Your file have the content neccesary for run your database. 

Install Postgresql for your database:

For mac you should the download the package on the [web site](https://www.postgresql.org/download/macosx/)  or execute ```brew install postgresql ```.

For linux please press on your terminal:
```bash 
$ sudo apt install postgresql postgresql-dev
```

Enjoy 
## Usage

Please clone the project 

``` bash
#clone your project
$ git clone  git@gitlab.com:travelposting/travelposting.git 

#Inside on project
$ cd travelposting/

#this get all requirements for your project and will install 
$ pipenv --python 3.7.4 install 

# now you should enter the next comand
## with pipenv shell you should inside on the env for python container 
$ pipenv shell 
# with pipenv run you should execute other commands for pip for example pipenv run pip freeze 
$ pipenv run 

# now enter 
$ cd travel/

# please execute migrate on your project 
$ python manage.py migrate 

# if you want create a new super user

$ python manage.py createsuperser

# now you can see the page for django cms and visite the [initial page](http://localhost:8000) 

$ python manage.py runserver 0.0.0.0:8000

# add the page with paginates from django cms

for page the page coming soon should be hidden on the menu and the url is coming-soon

 ```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)