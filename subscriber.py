from cyclonedds import domain, topic, sub
from cyclonedds.idl import IdlStruct
from dataclasses import dataclass
from time import sleep


@dataclass
class Message(IdlStruct):
    text: str


participant = domain.DomainParticipant()
topic = topic.Topic(
    domain_participant=participant,
    topic_name="messaging",
    data_type=Message
)
reader = sub.DataReader(participant, topic)

while True:
    if sample := reader.read_next():
        print(sample)
        break
    sleep(0.1)
