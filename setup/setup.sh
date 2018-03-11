#!/bin/bash

echo
echo --------------------🇨🇳 Database Setup🇨🇳 --------------------
echo 😊 Enter your custom configurations when prompted, otherwise hit 'enter' to use default.

read -p "Database hostname (localhost): " database
read -p "Database user (root): " user
read -s -p "Database password: " pass
echo
echo
LOGWRITE="DEV_DB_HOST=${database:='localhost'}\nDEV_DB_USER=${user:='root'}\nDEV_DB_PASS=lol i ain't showing you shit\n"

echo $LOGWRITE

# Databaset setup
echo "🤔 Running database setup"; 
echo
export MYSQL_PWD=$pass
echo 🚴 Setting up database...
mysql -u $user < setup.sql 
echo 📚 Completed
unset MYSQL_PWD

echo -------------------🇨🇳 Setup completed🇨🇳  --------------------
