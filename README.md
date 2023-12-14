Prerequisite:
        * Python 3.8.0+
        * psql(PostgreSQL) 11.5
System Setup:
        Installing Required tools
        
        (option 1 - local) :
        
        Install database
        Ubuntu:-
        
        Client:- sudo apt-get install -y postgresql-11 postgresql-contrib-11
        Server:- sudo apt-get install -y postgresql-doc-11 postgresql-server-dev-11
        OSX:- brew install postgresql@11.5

Environment setup:

          Install pip and virtualenv:
          
          sudo apt-get install python3-pip
          pip install --upgrade pip
          sudo pip3 install virtualenv or sudo pip install virtualenv
          Create virtual environment:

        virtualenv venv
OPTIONAL:- In case finding difficulty in creating virtual environment by above command , you can use the following commands too.

  *   Create virtualenv using Python3:-
          - virtualenv -p python3.8 venv
Activate environment:

source venv/bin/activate
Clone project: git clone https://github.com/KiwiTechLLC/Rockstar-Backend.git

cd ecommrece/
for local system follow below command
  pip3 install -r requirements.txt
Database Setup

Create database with proper permissions to the db-user:

create user user_name;
password user_name;
create database db_name;
grant all privileges on database db_name to user_name;
Add following information in .env file,to get the actual values, please contact to project owner.

DB_ENGINE="******"
DB_NAME="****"
DB_USERNAME="*******"
DB_PASSWORD="*******"
DB_HOST="*******"
DB_PORT=*******
DJANGO_SECRET_KEY="*******"

DB migrations:

$ python manage.py migrate
Run servers:

 $ python manage.py runserver
App Create:

 
 $ mkdir apps
 $ cd apps/
 
 ```
 python ../manage.py startapp customer
 python ../manage.py startapp product
 python ../manage.py startapp order
