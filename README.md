# Database-I-Project
Final Project for the Database I (COMP.3090) course at UMass Lowell.

Project consists of 10 SQL Queries in a Microsoft Access Database.

##Project Description:

In this project, you will work on Books Database which contains information of
books, authors and publisers. Download the database Books.accdb from google
group. Write the SQL queries in MS access interface and execute them.

##Database tables:

- Authors (au_id, au_name, address)

- Writes (au_id, title, royaltyper)

- Books (title, pub_id, price, ytd_sales)

- Publishers (pub_id, pub_name, city, state)

## Relations

- Authors is connected to Writes via au_id

- Writes and Books are connected via title

- Books and Publishers are connected via pub_id

## Notes

- csv subdirectory has each table in CSV format.

- db subdirectory has accdb, mdb, and SQLite versions of the database

- txt subdirectory has each table in .txt format.

- Queries.txt has the queries to run in a DB viewer.

- Run books.py with python to generate new SQLite DBs

  ```python books.py```

Created by [Jason Downing](https://github.com/JasonD94/) and
[Chris Pearce](https://github.com/cp0153) during the Fall 2016 semester at
UMass Lowell.
