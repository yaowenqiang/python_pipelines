from celery import Celery

app = Celery('tasks',
             brokers='amqp://celery_user:123456@localhost:5672/celery_vhost',
             backend='rpc://'
             )
