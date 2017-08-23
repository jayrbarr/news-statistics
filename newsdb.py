#!/usr/bin/env python3
#
# Report generator for news database

import psycopg2

# connect to database and fetch cursor
db = psycopg2.connect("dbname=news")
c = db.cursor()

# query and print most popular 3 articles of all time
query = ("select title, count(title) as num from articles, log "
         "where log.path like concat('%',articles.slug,'%') "
         "group by title order by num desc limit 3;")
c.execute(query)
rows = c.fetchall()
print("\n\nMost Popular Three Articles of All Time"
      "\n-----------------------------------------")
for row in rows:
    print(row[0] + " --- " + str(row[1]) + " views")

# query and print authors ranked by popularity defined by views
query = ("select name, count(*) as num from articles, authors, log "
         "where (author = authors.id AND path like concat('%',slug,'%')) "
         "group by name order by num desc;")
c.execute(query)
rows = c.fetchall()
print("\n\nMost Popular Authors Ranked by Views"
      "\n-----------------------------------------")
for row in rows:
    print(row[0] + " --- " + str(row[1]) + " views")

# query and print days with http errors over 1%
query = ("select to_char(a.time,'Month DD, YYYY'), b.errors "
         "from (select time::date, round(sum(case when status like '%200%' "
         "then 0 else 1 end)*100::numeric/count(*),1) as errors "
         "from log group by time::date) as b join log as a "
         "on a.time = b.time and b.errors>1;")
c.execute(query)
rows = c.fetchall()
print("\n\nDays with HTTP request errors over 1%"
      "\n-----------------------------------------")
for row in rows:
    print(" ".join(row[0].split()) + " --- " + str(row[1]) + "%")

# close database and provide some white space before prompt
db.close()
print("\n\n")
