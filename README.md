# Database-I-Project
Final Project for the
[Database I (COMP.3090)](http://www.cs.uml.edu/~cchen/309-F16/index.html)
course at UMass Lowell.

Project consists of 10 SQL Queries in a
[Microsoft Access](https://products.office.com/en-us/access) Database.

## Project Description:

In this project, you will work on Books Database which contains information of
books, authors and publishers. Download the database Books.accdb from the
google group. Write the SQL queries in the M$ Acce$$ interface and execute them.

## Database tables:

- Authors (au_id, au_name, address)

- Writes (au_id, title, royaltyper)

- Books (title, pub_id, price, ytd_sales)

- Publishers (pub_id, pub_name, city, state)

## Relations

- Authors is connected to Writes via **au_id**

- Writes and Books are connected via **title**

- Books and Publishers are connected via **pub_id**

- Should be possible to link all four tables together using these properties.

## Notes

- csv subdirectory has each table in CSV format.

- db subdirectory has accdb, mdb, and SQLite versions of the database

- txt subdirectory has each table in .txt format.

- Queries.txt has the queries to run in a DB viewer.

- Run books.py with python to generate new SQLite DBs

  ```python books.py```

Created by [Jason Downing](https://github.com/JasonD94/) and
[Chris Pearce](https://github.com/cp0153) during the Fall 2016 semester at
[UMass Lowell](https://www.uml.edu/Sciences/computer-science/default.aspx) .
