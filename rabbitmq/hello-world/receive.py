import os
import sys
import pika


def main():

    # Connection to broker
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Create queue (idempotent)
    channel.queue_declare(queue='hellp_python')

    # Tell RabbitMQ that this particular callback function should receive messages from hellp_python queue (queue exists anywas due to queue_declare)
    channel.basic_consume(queue='hellp_python',
                          auto_ack=True,
                          on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def callback(ch, method, properties, body):
    # Receiving message by subscribing callback method
    print(f"Python-Subscriber received {body}")


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
