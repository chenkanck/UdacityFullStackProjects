## Preparation
1. Install Virtual Box.

   You can download it from this [Link](https://www.virtualbox.org/wiki/Downloads), and install platform package.
2. Install Vagrant

   Download and install it from this [Link](https://www.vagrantup.com/downloads.html),
   run `vagrant --version` in terminal to see if it is installed.
3. Download VM configuration

   Download it from this [Link](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
   Move into `vagrant` directory, and run `vagrant up` and `vagrant ssh` to log into virtual machine.

4. Run `cd /vagrant` to move into working directory.
5. Download database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and put it in vagrant folder.

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