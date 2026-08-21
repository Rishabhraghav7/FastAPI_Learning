import stomp
from fastapi import HTTPException
from brokerConfig import brokerConfig as artemis
# class producer:
#     artemisUserName = "rishabh"
#     artemisPassword = "rishabh"
#     artemisPort = 61613
#     artemisHost = "localhost"
#     queueName = "newEmailQueue"


def produceMessage(email:str):
   connection = stomp.Connection12([(artemis.artemisHost, artemis.artemisPort)])
#    connection = stomp.Connection12([producer.artemisHost, producer.artemisPort])\
   connection.connect(
       artemis.artemisUserName,
       artemis.artemisPassword,
       wait=True
   )
   try:
        connection.send(
        destination=artemis.queueName,
        body=email
    )
        
   except:
       raise HTTPException(
           status_code=500,
           detail="Error while sending in producer"
       )
   finally:
    connection.disconnect()