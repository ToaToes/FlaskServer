import time
import subprocess

def run_locust():
    locust_cmd = ["locust", "-f", "locustfile.py", "--headless", "--users", "0", "--spawn-rate", "50", "--run-time", "10m"]
    process = subprocess.Popen(locust_cmd)

    return process

def adjust_load(process):
    users = 0
    while True:
        users += 50
        subprocess.run(["locust", "--reset", "--users", str(users)])
        time.sleep(10)  # Increase load every 10 seconds
        
        # Check if the average response time is greater than 100ms
        # This part needs integration with your monitoring or results analysis

        # Example (pseudo-code, implement actual checking):
        if average_response_time > 100:
            process.terminate()
            break

if __name__ == "__main__":
    process = run_locust()
    adjust_load(process)
