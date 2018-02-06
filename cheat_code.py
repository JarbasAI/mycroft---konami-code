from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
from threading import Thread
from time import sleep


# connect to message bus to interact with mycroft

client = WebsocketClient()


def connect():
    global client
    client.run_forever()


event_thread = Thread(target=connect)
event_thread.setDaemon(True)
event_thread.start()

# wait for thread to connect
sleep(1)


# helper functions
def execute_intent(intent_name, params_dict=None):
    if params_dict is None:
        params_dict = {}
    client.emit(Message(intent_name, params_dict))


def speak(utterance):
    client.emit(Message("speak", {"utterance": utterance}))


def utterance(utterance):
    client.emit(Message("recognizer_loop:utterance",
                        {"utterances": [utterance]}))


# cheat code script
speak("God Mode Activated")

# no skill id, wait for https://github.com/MycroftAI/mycroft-core/pull/1351
# execute_intent("WikipediaSkill:WikipediaIntent",{"ArticleTitle":"Konami Code"})

utterance("tell me about konami code")