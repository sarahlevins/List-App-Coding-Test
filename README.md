# Tennis Player List App

A Django Web Framework application which displays a list of tennis players. Built in 1.5 hours as a coding test

## Getting Started

Set up the virtual environment and install requirements

```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
cd List-App-Coding-Test
pip install -r requirements.txt
```

This application uses a postgreSQL database.
Create your database

```sql
psql
CREATE DATABASE yourdbname;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;
\q
```

Set your database credentials as environment variables

```bash
export DATABASE_NAME=yourdbname;
export DATABASE_USER=youruser;
export DATABASE_PASSWORD=yourpass;
```

Migrate the database and create a superuser for the admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

Load data fixtures using the following command
```bash
python manage.py loaddata player_data.json
```

Application will be on http://localhost:8000/
