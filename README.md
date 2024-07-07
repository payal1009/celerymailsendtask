# celerymailsendtask
Task is to send email to the user using celery
For this task first I start with basic task of performing addtion, for understanding concepts of celery
First step is to install redis broker, celery
In celery.py file I configured a celery by giving broker url, updated time zone to Asia/Kolkata, etc . also imported crontab for scheduling task at perticular time
In views.py create function which respond to http request
In urls.py give path of html page.
For sendin email it uses SMTP protocol
