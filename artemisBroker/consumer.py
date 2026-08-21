import stomp
from artemisBroker.producer import producer
from services.emailService import sendEmail

class consumer(stomp.ConnectionListener):
    def on_message(self , frame):
        # print("Message recived")
        # print(frame.body)
        email = frame.body
        sendEmail(email)


connection = stomp.Connection12([producer.artemisHost, producer.artemisPort])
connection.set_listener("",consumer())

connection.connect(producer.artemisUserName,producer.artemisPassword, wait=True)
connection.subscribe(destination=producer.queueName, id =1 , ack= "auto")

try:
    while True:
        pass
except KeyboardInterrupt:
    connection.disconnect()