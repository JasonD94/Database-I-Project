##Queries

[Chris Pearce](https://github.com/cp0153) will do the odd problems,
[Jason Downing](https://github.com/JasonD94/) will do the even numbers.

1. List all books' title.

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

2. Find the author who wrote the book named But Is It User Friendly.
(Your result should display author's name.)

```
SELECT DISTINCT au_name
FROM Authors
INNER JOIN Writes
ON Authors.au_id = Writes.au_id
WHERE title = "But Is It User Friendly?"
```

Output
```
au_name
--------------
Cheryl Carson
```

3. List all books whose price is greater than $20.
List your result in the ascending order of the price.
(Your result should display both book title and price. )

```
SELECT title, price
FROM Books
WHERE price > 20
ORDER BY ASCEND
```

Output
```


```

4. Find those pairs of books that have the same price.
(Your result should display book title and each pair of book titles
should only appear once.)

```
SELECT DISTINCT b1.title, b2.title
FROM Books b1, Books b2
WHERE b1.price = b2.price AND b1.title != b2.title
```

Output (need to fix, currently shows pairs twice)
```
"Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean" "Secrets of Silicon Valley"
"Secrets of Silicon Valley" "Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean"
```

5. List all books published by New Moon Books.
(Your result should display book titles.)

```
SELECT title
FROM Books, Publishers
WHERE pub_name = 'New Moon Books'
```

Output
```


```

6. List all authors whose book was published by Binnet & Hardley.
(Your result should display author's name.)

```
SELECT  Authors.au_name
FROM Authors
    JOIN Writes
      ON Authors.au_id = Writes.au_id
    JOIN Books
      ON Books.title = Writes.title
    JOIN Publishers
      ON Books.pub_id = Publishers.pub_id
WHERE Publishers.pub_name = "Binnet & Hardley"
```

Output
```
au_name
-----------------------
Livia Karsen
Reginald Blotchet-Halls
Sylvia Panteley
```

7. Find Publishers which publish more than 3 books.
(Your result should display publisher's name.)

```
SELECT pub_name
FROM Publishers
GROUP BY Having count(Books.pub_id) > 3
```

Output
```


```

8. Insert a new publisher, Ramona Publishers, which is located in Dallas, TX
and id is 1756.

```
code
```

Output
```


```

9. Increase $2 to those books whose price is lower than $10.

```
UPDATE Books SET price = price + 2
WHERE price < 10
```

Output
```


```

10. Delete publishers who are located in Chicago.

```
code
```

Output
```


```
