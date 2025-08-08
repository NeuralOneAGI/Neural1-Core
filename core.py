class Neural1Core:
    def __init__(self, memory, parser, reasoner, responder):
        self.memory = memory
        self.parser = parser
        self.reasoner = reasoner
        self.responder = responder

    def process(self, user_input):
        parsed = self.parser.parse(user_input)
        context = self.memory.retrieve(parsed)
        thought = self.reasoner.think(parsed, context)
        output = self.responder.respond(thought)
        self.memory.store(user_input, output)
        return output
