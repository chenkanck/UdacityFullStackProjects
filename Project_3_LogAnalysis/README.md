## How to run code
1. setup and log in to datebase using `psql -d news -f newsdata.sql`
2. run commands to create views
3. using `\q` to exit database
4. run `python AnylyzeLog.py`

## Output

```
1. What are the most popular three articles of all time?
['Candidate is jerk, alleges rival', 'Bears love berries, alleges bear', 'Bad things gone, say good people']
2. Who are the most popular article authors of all time?
['Ursula La Multa', 'Rudolf von Treppenwitz', 'Anonymous Contributor']
3. On which days did more than 1% of requests lead to errors?
2016-07-17
```

## Commands to create view

view article_reads
```
create view article_reads as 
select path,count(*) as views from log
where path like '%article%' group by path;
```

view date_request
```
create view date_request as 
select time::date, count(*) as total
from log 
group by time::date;
```

view date_error
```
create view date_error as 
select time::date, count(*) as error_count
from log where status not like '%200%'
group by time::date;
```