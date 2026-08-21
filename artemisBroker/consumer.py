import stomp
from brokerConfig import brokerConfig as artemis
from services.emailService import sendEmail

class consumer(stomp.ConnectionListener):
    def on_message(self , frame):
        # print("Message recived")
        # print(frame.body)
        email = frame.body
        sendEmail(email)


connection = stomp.Connection12([artemis.artemisHost, artemis.artemisPort])
connection.set_listener("",consumer())

connection.connect(artemis.artemisUserName,artemis.artemisPassword, wait=True)
connection.subscribe(destination=artemis.queueName, id =1 , ack= "auto")

try:
    while True:
        pass
except KeyboardInterrupt:
    connection.disconnect()