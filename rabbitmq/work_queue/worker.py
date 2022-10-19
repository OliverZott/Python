"""
Work Queue

Using message acknowledgments and prefetch_count you can set up a work queue. The durability options let the tasks survive even if RabbitMQ is restarted
"""

import os
import sys
import time
import pika


def main():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='task_queue',
                          on_message_callback=callback)

    channel.start_consuming()


def callback(ch, method, properties, body):
    # Receiving message by subscribing callback method
    print(f"Worker received {body} / {body.decode()})")
    time.sleep(body.count(b'.'))
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
