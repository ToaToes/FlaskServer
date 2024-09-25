# FlaskServer
Flask server and locust file

On your local machine, use locust or jmeter to do the following:
a. Start up the flask server flask_api.py.
b. Execute your test case and save your test report.
c. Do the below test automatically: increase the concurrent user number by 50 
for every 10 seconds, until the average response time of the payment API is 
greater than 100ms.


Flask API: Ensure you have a Flask API running in flask_api.py.
Locust Installation: Install Locust if you haven’t already:

'''
pip install locust
'''

Step 1: Start Your Flask Server
Run your Flask API in a terminal:

'''
python flask_api.py
'''

Step 2: Create a Locust File
Step 3: Running Locust File

'''
locust -f locustfile.py --host=http://localhost:5000  # Adjust host if necessary
'''
