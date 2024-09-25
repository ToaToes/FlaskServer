from locust import HttpUser, task, between, events
from locust.runners import STATE_STOPPING, STATE_STOPPED
import time

# Global variable to store response times of the Payment API
payment_response_times = []
stop_test_flag = False

class APIUser(HttpUser):
    #wait_time = between(1, 2)

    @task
    def test_login_order_payment(self):
        global stop_test_flag
        if stop_test_flag:
            self.environment.runner.quit()  # Stop test if stop flag is set
            return

        # 1. Call the Login API to get the session ID
        login_response = self.client.post("/login", json={"username": "user", "password": "pass"})
        if login_response.status_code == 200:
            session_id = login_response.json().get("session_id")

            # 2. Call the Order API to get the order ID
            order_response = self.client.post("/order", json={"session_id": session_id})
            if order_response.status_code == 200:
                order_id = order_response.json().get("order_id")

                # 3. Call the Payment API and track its response time
                start_time = time.time()
                payment_response = self.client.post("/payment", json={"session_id": session_id, "order_id": order_id})
                response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

                # Record the response time of the Payment API
                payment_response_times.append(response_time)

                # Check if the average response time exceeds 100ms
                average_response_time = sum(payment_response_times) / len(payment_response_times)
                print(f"Average Payment API response time: {average_response_time:.2f} ms")

                if average_response_time > 100:
                    print("Average response time exceeded 100ms. Stopping the test.")
                    stop_test_flag = True  # Set the flag to stop the test

                # Handle any potential failure in Payment API
                if payment_response.status_code != 200:
                    self.environment.events.request_failure.fire(
                        request_type="POST",
                        name="/payment",
                        response_time=response_time,
                        response=payment_response
                    )

# Event to stop the test gracefully when average response time condition is met
@events.quitting.add_listener
def on_quitting(environment, **kwargs):
    if environment.runner and environment.runner.state not in [STATE_STOPPED, STATE_STOPPING]:
        print("Test stopped based on custom condition.")
