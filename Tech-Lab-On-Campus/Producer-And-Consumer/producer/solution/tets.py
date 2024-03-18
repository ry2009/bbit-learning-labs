import os

# Get the AMQP_URL environment variable value
amqp_url = os.environ.get("AMQP_URL")

if amqp_url:
    print(f"AMQP_URL is set to: {amqp_url}")
else:
    print("AMQP_URL environment variable is not set.")
