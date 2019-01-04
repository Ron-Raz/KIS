#!/usr/bin/env python2.7

from crontab import CronTab
cron = CronTab(user='kaltura')
def set():
	job = cron.new(command='/home/kaltura/cronjobs/testjob.sh')  
	job.minute.every(1)
	cron.write()

def list():
	for job in cron:
		print job

def clear():
	cron.remove_all()
	cron.write()
list()
clear()
list()	
