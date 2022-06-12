from mongoengine import *
from celery import Celery
from redis import Redis

redis = Redis(host='redis', port=6379, db=0)


class Message(Document):
    name = StringField()
    message = StringField()


app = Celery('tasks',
             broker='amqp://user:pass@rabbit:5672',
             backend='mongodb://mongodb:27017/backdb')


@app.task()
def Send_Message(user, mess):
    try:
        connect('messages', host='mongodb', port=27017)
        Message(name=user, message=mess).save()
    except:
        pass
    print(user, mess)
    if redis.get("cache") is not None:
        redis.delete("cache")

    return "Send message"


@app.task()
def Get_Message():
    res = ""

    if redis.get("cache") is not None:
        res = (str(redis.get("cache")))[2:]
        print("From Redis")
    else:
        try:
            connect('messages', host='mongodb', port=27017)
            res = ""
            for obj in Message.objects():
                res += str(obj.name + ": " + obj.message + " <br>")
        except:
            pass
        redis.set("cache", res)
        print("From BD")
    return res


if __name__ == '__main__':
    app.start(["worker"])
