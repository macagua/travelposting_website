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
for page Magazine you should create a page but dont show that on the menu the page url is magazine

```
for create aditional links on the footer please select the base template
    <li class="list-inline-item pl-3">
        <a class="list-group-item-action font-size-1 text-white-70 " href="/cookies/">{% trans 'Cookies' %}</a>
    </li>
    <li class="list-inline-item pl-3">
        <a class="list-group-item-action font-size-1 text-white-70 " href="/fqa/">{% trans 'FQA' %}</a>
    </li>
    <li class="list-inline-item pl-3">
        <a class="list-group-item-action font-size-1 text-white-70 " href="/policy/">{% trans 'Privacy & policy' %}</a>
    </li>
    <li class="list-inline-item pl-3">
        <a class="list-group-item-action font-size-1 text-white-70 " href="/soft-reg/">{% trans 'Register' %}</a>
    </li>
```

    The urls be: 
    1. policy
    2. fqa
    3. soft-reg
    4. cookies 

    and this url please hidden on the menu.

 ```

 On every hotels you should create a snippet with the next code

<iframe src="https://www.booking.com/country/de.de.html?aid=386452;sid=886b5e2b7d8d93e8663a438e1d9ebf26;breadcrumb=city" name="Hoteles en Alemania" width="100%" height="2500"></iframe>

when you indicate the zone on the name iframe for example: "Hoteles en Alemania" or "Hoteles en USA", etc...


Please create a next url with snippet content with next url
1. hotel-germany
2. hotel-usa
3. hotel-china
4. word-mundo
5. make-pay


## Translations 

For every page on diferent idioms so you should configure every placeholder that you have, and define every url for every idioms

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)