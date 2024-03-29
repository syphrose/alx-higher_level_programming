### GENERAL LEARNING OBJECTIVES
-----------------------------------------------------------------
At the end of this task, I sould be able to know and understand:
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

----------------------------------------------------------
### GENERAL REQUIREMENTS
-----------------------------------------------------------------
~ Allowed editors: vi, vim, emacs
~ All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
~ All your files should end with a new line
~ All your SQL queries should have a comment just before (i.e. syntax above)
~ All your files should start by a comment describing the task
~ All SQL keywords should be in uppercase (SELECT, WHERE…)
~ A README.md file, at the root of the folder of the project, is mandatory
~ The length of your files will be tested using wc

You are as well required to installed the MySQL 8.0 on Ubuntu 20.04 LTS using
 this commands on the prompt:
    $ sudo apt update
    $ sudo apt install mysql-server
    ... 
    $ mysql --version
    mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

Then you'll connect to the MySQL server by typing;
    $ sudo mysql
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 11
    Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

    Copyright (c) 2000, 2021, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql>
    mysql> quit
    Bye
    $
-------------------------------------------------------------
### Importing a SQL dump
--------------------------------------------
Use the commands below:
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
--------------------------------------------------------
