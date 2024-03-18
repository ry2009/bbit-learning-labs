import os
import pika
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Establish a connection to the RabbitMQ server
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=self.con_params)
        self.channel = self.connection.channel()

        # Declare an exchange
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')

    def publishOrder(self, message: str) -> None:
        # Publish a message to the exchange with the specified routing key
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message
        )
        print(f"Message published to exchange '{self.exchange_name}': {message}")

        # Closing channel and connection
        self.channel.close()
        self.connection.close()
