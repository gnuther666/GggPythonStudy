import pika

userx = pika.PlainCredentials('ruroot', 'ruroot')
conn = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1", "9001", "/", credentials=userx))

channelx = conn.channel()

channelx.queue_declare(queue="xxx")

def dongcallbackfun(v1, v2, v3, bodyx):
    print('得到的数据为:',  bodyx)

channelx.basic_consume(queue='xxx', on_message_callback=dongcallbackfun, auto_ack=True)

print('----------- 接受数据 ----------')

channelx.stop_consuming()