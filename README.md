# Online News Report Generator
This Python program runs PostgreSQL queries on a news database
(provided by [Udacity](https://www.udacity.com/)) and prints results to
the terminal window.

## Installation
- Install [Python3](https://www.python.org/downloads/).
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
- Install [Vagrant](https://www.vagrantup.com/downloads.html).
- Download and unzip [this virtual machine configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).
- Download this current repository to the vagrant subdirectory in the
  downloaded VM configuration.
- Download [SQL config file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  and put in /vagrant/news subdirectory.

## Run
From terminal window inside vagrant directory...

```
vagrant up
vagrant ssh
cd /vagrant/news
psql -d news -f newsdata.sql
python newsdb.py
```

## Sample Output
Sample output is available [here](https://github.com/jayrbarr/news-statistics/blob/master/output.txt).
