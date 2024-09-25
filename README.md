# FlaskServer

### Performance Test Assignment
performance testing for a service that is deployed on a 
cloud platform and configured for auto-scaling. The service has only 3 APIs: 
1. The get login API returns a session id
2. The order API returns an order id. When the user calls this API, the user needs to 
provide the session id and the order id will be mapped to this session id.
3. the payment API. When the user calls this API, user needs to provide both the 
session id and order id to make the payment. If the session id and order id are 
not matched, the server will return an error.


Flask server and locust file

On your local machine, use locust or jmeter to do the following:
a. Start up the flask server flask_api.py.
b. Execute your test case and save your test report.
c. Do the below test automatically: increase the concurrent user number by 50 
for every 10 seconds, until the average response time of the payment API is 
greater than 100ms.


Flask API: Ensure you have a Flask API running in flask_api.py.
Locust Installation: Install Locust if you haven’t already:

```
pip install locust
```

Step 1: Start Your Flask Server
Run your Flask API in a terminal:

```
python flask_api.py
```

Step 2: Running Locust File

```
locust -f locustfile.py --host=http://localhost:5000  # Adjust host if necessary
```
