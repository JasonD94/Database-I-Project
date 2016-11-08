# Database-I-Project
Final Project for the Database I (COMP.3090) course at UMass Lowell.

Project consists of 10 SQL Queries in a Microsoft Access Database.

##Project Description:

In this project, you will work on Books Database which contains information of books, authors and publisers. Download the database Books.accdb from google group. Write the SQL queries in MS access interface and execute them.

##Database tables:

- Authors (au_id, au_name, address)

- Writes (au_id, title, royaltyper)

- Books (title, pub_id, price, ytd_sales)

- Publishers (pub_id, pub_name, city, state)

##Queries

[Chris Pearce](https://github.com/cp0153) will do the odd problems, [Jason Downing](https://github.com/JasonD94/) will do the even numbers.

1. List all books' title.

```
SELECT title
FROM Books
```

2. Find the author who wrote the book named But Is It User Friendly.
(Your result should display author's name.)

```
SELECT au_name
FROM Authors, Writes
WHERE title = 'But Is It User Friendly'
```

3. List all books whose price is greater than $20. List your result in the ascending order of the price.
(Your result should display both book title and price. )

```
SELECT title, price
FROM Books
WHERE price > 20
ORDER BY ASCEND
```

4. Find those pairs of books that have the same price.
(Your result should display book title and each pair of book titles should only appear once.)

```
SELECT DISTINCT title
FROM
WHERE
```

5. List all books published by New Moon Books.
(Your result should display book titles.)

```
SELECT title
FROM Books, Publishers
WHERE pub_name = 'New Moon Books'
```

6. List all authors whose book was published by Binnet & Hardley.
(Your result should display author's name.)

```
code
```

7. Find Publishers which publish more than 3 books.
(Your result should display publisher's name.)

```
SELECT pub_name
from Publishers
GROUP BY Having count(Books.pub_id) > 3
```

8. Insert a new publisher, Ramona Publishers, which is located in Dallas, TX and id is 1756.

```
code
```

9. Increase $2 to those books whose price is lower than $10.

```
UPDATE Books SET price = price + 2
WHERE price < 10
```

10. Delete publishers who are located in Chicago.

```
code
```


Created by [Jason Downing](https://github.com/JasonD94/) and [Chris Pearce](https://github.com/cp0153) during the Fall 2016 semester at UMass Lowell.
