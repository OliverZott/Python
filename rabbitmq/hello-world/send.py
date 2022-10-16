import pika

# Connection to broker
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create queue (idempotent)
channel.queue_declare(queue='hellp_python')

# Send message tp queue through an exchange
# Queue name is specified in routing_key !!!
channel.basic_publish(exchange='',
                      routing_key='hellp_python',
                      body='Hello World!')
print("Python-Publisher sent 'Hello World!'")

# Flush network buffers
connection.close()
