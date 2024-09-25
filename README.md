# FlaskServer
Flask server and locust file

On your local machine, use locust or jmeter to do the following:
a. Start up the flask server flask_api.py.
b. Execute your test case and save your test report.
c. Do the below test automatically: increase the concurrent user number by 50 
for every 10 seconds, until the average response time of the payment API is 
greater than 100ms.
