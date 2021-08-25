import pika



credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host="localhost",credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


channel.queue_declare(queue="hello") 
# Creates a queue


channel.exchange_declare(exchange ="hello-exchange") 
# Creates an exchange



channel.queue_bind(queue="hello", exchange="hello-exchange", 
	routing_key="hello-binding-key") 
# binds the exchange and the queue



channel.basic_publish(
	exchange="hello-exchange", routing_key="hello-binding-key", 
	body="Waaaasssss Sup?")

#channel.basic_publish(
#	exchange="hello-exchange", routing_key="hello-binding-key", body= "Wa sup!")

connection.close()


