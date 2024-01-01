
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

#### - Run PostgresSQL service

```
sudo service postgresql start
```

#### - Show PostgreSQL status

```
sudo service postgresql status
```

### Step 2. Set PostgresSQL Admin Account

#### - Connect PostgresSQL Server

```
sudo -i -u postgres
psql
```

#### - Set Passwords of PostgresSQL Admin Account

  - 'postgres' is default admin account of PostgresSQL
    
```
ALTER USER postgres WITH PASSWORD '{passwords}';
```

#### - Show PostgresSQL Accounts

```
\du
```

### Step 3. Create PostgresSQL Database

#### - Create PostgresSQL Database

  - Set Owner as 'postgres'

```
CREATE DATABASE {db_name} OWNER postgres;
```

#### - Show PostgresSQL Database

```
\list
```

#### - Disconnect PostgresSQL Server

```
exit
```

### Step 4. Allow Remote Access 

#### - Move to path of PostgresSQL configs file

```
cd /etc/postgresql/{version_of_PostgresSQL}/main
```

#### - Edit 'postgresql.conf' file

  - Set 'listen_addresses' as '0.0.0.0' for listening to all IPs
  - Set 'port' to the port you want to connect to
    
<img src="https://github.com/qbxlvnf11/postgresql-server/assets/52263269/42799844-d67e-493e-adf5-556ae0ac3eb2" width="60%"></img>
    
```
sudo nano postgresql.conf
```

#### - Restart PostgresSQL service 

  - For applying modified configs file

```
sudo service postgresql restart
```

#### - Edit 'pg_hba.conf' file

  - Add line as follow for allowing to connect all IPs
    
<img src="https://github.com/qbxlvnf11/postgresql-server/assets/52263269/80f23735-dcde-43cc-a412-9bc1d583ddd3" width="60%"></img>

```
sudo nano pg_hba.conf
```

#### - Restart PostgresSQL service 

  - For applying modified configs file

```
sudo service postgresql restart
```

### Step 5. Test Remote Access

#### - Test remote access to PostgresSQL server and running query

  - Custom python PostgresSQL server class
    - Connect PostgreSQL server, Create table, Insert data, Select data etc.

```
python db_test --host '{server_ip}' --port {port} --db_name '{db_name}' --user 'postgres' --password '{password}' --table_name '{table_name}'
```
