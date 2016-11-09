################################################################################
#
#   Python Script for creating an SQLite version of the Database I M$ Ace$$ db.
#   Created by: Jason Downing
#         Date: 11/9/2016
#   Project by: Jason Downing and Christoper Pearce
#
################################################################################
import pandas
import sqlite3

# For the CSV file, the first line should be a list of the column names and
# all of the lines after that should be the data
# Examples for each table provided below.

# DB here, name "books" matches the DB given in M$ Ace$$ form.
conn = sqlite3.connect('books.db')

# Table "Authors". Example for authors:
# au_id,au_name,address
# "213-46-8915","Marjorie Green","Oakland"
table = "Authors"  # name table here
df = pandas.read_csv('csv/authors.csv')
df.to_sql(table, conn, if_exists='append', index=False)

# Table "Books". Example for books:
# title,pub_id,price,ytd_sales
# "But Is It User Friendly?","1389",$22.95,8780
table = "Books"  # name table here
df = pandas.read_csv('csv/books.csv')
df.to_sql(table, conn, if_exists='append', index=False)

# Table "Publishers". Example for publishers:
# pub_id,pub_name,city,state
# "0736","New Moon Books","Boston","MA"
table = "Publishers"  # name table here
df = pandas.read_csv('csv/publishers.csv')
df.to_sql(table, conn, if_exists='append', index=False)

# Table "Writes". Example for writes:
# au_id,title,royaltyper
# "213-46-8915","You Can Combat Computer Stress!",100
table = "Writes"  # name table here
df = pandas.read_csv('csv/writes.csv')
df.to_sql(table, conn, if_exists='append', index=False)
