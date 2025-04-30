class Message:
    def __init__(self, sender: str, receiver: str, body: dict):
        self.sender = sender
        self.receiver = receiver
        self.body = body

class Agent:
    def __init__(self, name: str, runtime):
        self.name = name
        self.runtime = runtime
        runtime.register(self)

    def send(self, msg: "Message"):
        self.runtime.post(msg)

    def receive(self, msg: "Message"):
        raise NotImplementedError
