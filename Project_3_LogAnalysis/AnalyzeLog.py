#! /user/bin/env python
import psycopg2


def connect_database(name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to database.")


def problem1():
    # most popular article
    db, c = connect_database()
    # article_reads is a view
    query = ("select title, views from article_reads, articles "
             "where article_reads.path like '/article/' || articles.slug "
             "order by views desc limit 3;")
    c.execute(query)
    rows = c.fetchall()
    print("-" * 60)
    print("Most popular articles:")
    for (title, views) in rows:
        print("    {} - {} views".format(title, views))
    db.close()
    return


def problem2():
    # most popular author
    db, c = connect_database()
    query = ("select authors.name, sum(views) as t_views "
             "from articles, authors, article_reads "
             "where articles.author = authors.id "
             "and path like '/article/' || articles.slug "
             "group by authors.name order by t_views desc;")
    c.execute(query)
    rows = c.fetchall()
    print("-" * 60)
    print("Most popular article authors:")
    for (name, views) in rows:
        print("    {} - {} views".format(name, views))
    db.close()
    return


def problem3():
    db, c = connect_database()
    query = ("select * from "
             "(select date_request.time,"
             " round((error_count*1.00 * 100 /total), 2) as percent "
             "from date_request join date_error "
             "on date_error.time = date_request.time) as temp "
             "where percent > 1;")
    c.execute(query)
    rows = c.fetchall()
    print("-" * 60)
    print("Days with more than 1% errors:")
    for (date, percentage) in rows:
        print("    {} - {}% errors".format(date, percentage))
    db.close()
    return

if __name__ == '__main__':
    problem1()
    problem2()
    problem3()
