import pika

parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()



def callback(channel,method, properties, body):
	print("body",body, flush=True)




channel.basic_consume(
	queue="hello", on_message_callback=callback, auto_ack=True)


channel.start_consuming()


connection.close()