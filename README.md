
Contents
=============

#### - Install PostgresSQL server on Ubuntu and remote access with Python

PostgresSQL Server Buildup
=============

### Step 1. Install PostgresSQL Server

#### - Check which version of PostgreSQL to install on Ubuntu

```
apt show postgresql
```

#### - PostgreSQL Package Setting

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list. d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
```

#### - Install PostgreSQL on Ubuntu

```
sudo apt-get -y install postgresql
sudo apt install postgresql postgresql-contrib
```

### Step 2. Run PostgresSQL Service

#### - Run PostgresSQL service

```
sudo service postgresql start
```

#### - Show PostgreSQL status

```
sudo service postgresql status
```

### Step 3. Connect PostgresSQL Server on Ubuntu

#### - Connect PostgresSQL Server

```
sudo -i -u postgres
psql
```

### Step 4. Set PostgresSQL Admin Account

#### - Set Passwords of PostgresSQL Admin Account

  - 'postgres' is default admin account of PostgresSQL
    
```
ALTER USER postgres WITH PASSWORD '{passwords}';
```

#### - Show PostgresSQL Accounts

```
\du
```

### Step 5. Create PostgresSQL Database

#### - Create PostgresSQL Database

  - We set Owner as 'postgres'

```
CREATE DATABASE {db_name} OWNER postgres;
```

#### - Show PostgresSQL Database

```
\list
```
