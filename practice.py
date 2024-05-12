# Import necessary libraries
import time
import RPi.GPIO as GPIO
import requests

# Define GPIO pin for fire sensor input
FIRE_SENSOR_PIN = 14

# Define API endpoint for sending alerts
ALERT_API_ENDPOINT = "https://your_alert_api_endpoint.com"

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(FIRE_SENSOR_PIN, GPIO.IN)

def send_alert():
    payload = {'alert': 'Forest Fire Detected!'}
    try:
        response = requests.post(ALERT_API_ENDPOINT, json=payload)
        if response.status_code == 200:
            print("Alert sent successfully!")
        else:
            print("Failed to send alert.")
    except Exception as e:
        print("Error:", e)

def main():
    print("Forest Fire Detection System Started...")
    try:
        while True:
            # Read fire sensor input
            fire_status = GPIO.input(FIRE_SENSOR_PIN)
            
            if fire_status == GPIO.HIGH:
                print("Fire detected!")
                send_alert()
                # Add code here to activate fire control system (e.g., sprinklers)
            else:
                print("No fire detected.")
            
            # Delay before next iteration
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
