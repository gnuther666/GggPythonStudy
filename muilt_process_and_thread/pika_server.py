import pika

userx = pika.PlainCredentials('ruroot', 'ruroot')
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", "9001", "/", credentials=userx))

channelx = conn.channel()

channelx.queue_declare(queue="xxx")

channelx.basic_publish(exchange="", routing_key="xxx", body="hello world")

print("----------发送数据----------")

conn.close()
