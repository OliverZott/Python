"""
Work Queues

https://www.rabbitmq.com/tutorials/tutorial-two-python.html

- Message acknowledgment
- Message durability
- Fair dispatch
"""

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# ...give more than one message to a worker at a time.
# channel.basic_qos(prefetch_count=1)

# Message from sys args
message = ' '.join(sys.argv[1:]) or 'default arg'


# persistent queue and persistent messages
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
print(f"Publisher generated task: {message}")

connection.close()
