##Queries

[Chris Pearce](https://github.com/cp0153) will do the odd problems,
[Jason Downing](https://github.com/JasonD94/) will do the even numbers.

1\. List all books' title.

```
SELECT title
FROM Books
```

Output:
```
title
------------------------
But Is It User Friendly?
Computer Phobic AND Non-Phobic Individuals: Behavior Variations
Emotional Security: A New Algorithm
Fifty Years in Buckingham Palace Kitchens
Is Anger the Enemy?
Net Etiquette
"Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean"
Secrets of Silicon Valley
The Busy Executive's Database Guide
You Can Combat Computer Stress!
```

2\. Find the author who wrote the book named But Is It User Friendly.
(Your result should display author's name.)
```
SELECT DISTINCT au_name
FROM Authors
INNER JOIN Writes
ON Authors.au_id = Writes.au_id
WHERE title = "But Is It User Friendly?"
```

Output:
```
au_name
--------------
Cheryl Carson
```

3\. List all books whose price is greater than $20.
List your result in the ascending order of the price.
(Your result should display both book title and price. )

This is the MS Access version:
```
SELECT title, price
FROM Books
WHERE price > 20
ORDER BY price ASC
```

Output:
```
title | price
--------------
"Computer Phobic AND Non-Phobic Individuals: Behavior Variations" "21.59"
"But Is It User Friendly?"  "22.95"
"Net Etiquette" "25.0"
```

4\. Find those pairs of books that have the same price.
(Your result should display book title and each pair of book titles
should only appear once.)
```
SELECT DISTINCT b1.title, b2.title
FROM Books b1, Books b2
WHERE b1.price = b2.price AND b1.title < b2.title
```

Output:
```
title, title
------------
"Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean",
Secrets of Silicon Valley
```

5\. List all books published by New Moon Books.
(Your result should display book titles.)
```
SELECT title
FROM Books, Publishers
WHERE pub_name = 'New Moon Books'
```

Output:
```
title
---------------
"But Is It User Friendly?"
"Computer Phobic AND Non-Phobic Individuals: Behavior Variations"
"Emotional Security: A New Algorithm"
"Fifty Years in Buckingham Palace Kitchens"
"Is Anger the Enemy?"
"Net Etiquette"
"Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean"
"Secrets of Silicon Valley"
"The Busy Executive's Database Guide"
"You Can Combat Computer Stress!"
```

6\. List all authors whose book was published by Binnet & Hardley.
(Your result should display author's name.)
```
SELECT DISTINCT Authors.au_name
FROM ((Authors
  INNER JOIN Writes
    ON Authors.au_id = Writes.au_id)
  INNER JOIN Books
    ON Books.title = Writes.title)
  INNER JOIN Publishers
    ON Books.pub_id = Publishers.pub_id
WHERE Publishers.pub_name = "Binnet & Hardley"
```

Output:
```
au_name
-----------------------
Livia Karsen
Reginald Blotchet-Halls
Sylvia Panteley
```

7\. Find Publishers which publish more than 3 books.
(Your result should display publisher's name.)

This gets count of books:
```
SELECT DISTINCT pub_name, COUNT(*) AS 'number of books'
FROM Publishers, Books
WHERE Publishers.pub_id = Books.pub_id
GROUP BY Publishers.pub_name
```

This is the full query which prints just the publisher with > 3 books:
```
SELECT pub_name
FROM
(
  SELECT DISTINCT pub_name, COUNT(*) AS book_count
  FROM Publishers, Books
  WHERE Publishers.pub_id = Books.pub_id
  GROUP BY Publishers.pub_name
)
WHERE book_count > 3
```

Output:
```
pub_name
---------------------
Algodata Infosystems
```

8\. Insert a new publisher, Ramona Publishers, which is located in Dallas, TX
and id is 1756.
```
INSERT INTO Publishers (pub_id, pub_name, city, state)
VALUES (1756, "Ramona Publishers", "Dallas", "TX")
```

Output
```
Query executed successfully:
INSERT INTO Publishers (pub_id, pub_name, city, state)
VALUES (1756, "Ramona Publishers", "Dallas", "TX") (took 0ms)
```

9\. Increase $2 to those books whose price is lower than $10.
```
UPDATE Books SET price = price + 2
WHERE price < 10
```

Output:
```
Query executed successfully: UPDATE Books SET price = price + 2
WHERE price < 10 (took 0ms)
```

10\. Delete publishers who are located in Chicago.
```
DELETE FROM Publishers
WHERE Publishers.city = "Chicago"
```

Output
```
Query executed successfully: DELETE FROM Publishers
WHERE Publishers.city = "Chicago" (took 0ms)
```
