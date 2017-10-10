import psycopg2

def problem1():
    # most popular article
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    #article_reads is a view
    c.execute("select title, views from article_reads, articles where article_reads.path like '/article/' || articles.slug order by views desc limit 3;")
    rows = c.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    DB.close()
    return result

def problem2():
    # most popular author
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    query = ("select authors.name, sum(views) as t_views "
             "from articles, authors, article_reads "
             "where articles.author = authors.id and path like '/article/' || articles.slug "
             "group by authors.name order by t_views desc limit 3;"
            )
    c.execute(query)
    rows = c.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    return result

def problem3():
    DB = psycopg2.connect("dbname=news")
    c = DB.cursor()
    query = ("select * from "
             "(select date_request.time, (error_count * 100 /total ) as percent "
             "from date_request join date_error "
             "on date_error.time = date_request.time) as temp "
             "where percent > 1;"
    )
    c.execute(query)
    rows = c.fetchall()
    result = rows[0][0]
    DB.close()
    return result

print "1. What are the most popular three articles of all time?"
print problem1()
print "2. Who are the most popular article authors of all time?"
print problem2()
print "3. On which days did more than 1% of requests lead to errors?"
print problem3()