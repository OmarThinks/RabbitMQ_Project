import pika

parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(parameters)

channel = connection.channel()



def ack_message(channel, method):
    """Note that `channel` must be the same pika channel instance via which
    the message being ACKed was retrieved (AMQP protocol constraint).
    """
    if channel.is_open:
        channel.basic_ack(method.delivery_tag)
    else:
        # Channel is already closed, so we can't ACK this message;
        # log and/or do something that makes sense for your app in this case.
        pass




def callback(channel,method, properties, body):
	ack_message(channel,method)
	print("body",body, flush=True)


channel.basic_consume(
	queue="hello", on_message_callback=callback)

channel.start_consuming()

connection.close()