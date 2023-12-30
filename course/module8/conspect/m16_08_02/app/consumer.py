import os
import sys

import pika

from models import Task


def main():
    credentials = pika.PlainCredentials("***", "***")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="***",
            port=5672,
            credentials=credentials,
            virtual_host="***",
        )
    )
    channel = connection.channel()
    queue_name = "web_16 campaign"
    channel.queue_declare(queue=queue_name, durable=True)

    consumer = sys.argv[1] if len(sys.argv) > 1 else "Noname"

    def callback(ch, method, properties, body):
        pk = body.decode()
        task = Task.objects(id=pk, status=False).first()
        if task:
            task.update(set__status=True, set__consumer=consumer)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
