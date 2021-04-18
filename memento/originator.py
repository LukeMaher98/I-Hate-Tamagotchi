import copy
from memento import memento

class Originator:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def save_state(self):
        return memento.Memento(copy.deepcopy(self.state))

    def load_state(self, memento):
        self.state = memento.rollback_state()