class Memento:
    def __init__(self, mem_state):
        self.mem_state = mem_state

    def rollback_state(self):
        return self.mem_state