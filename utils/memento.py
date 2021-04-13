import copy


class Memento:
    def __init__(self, mem_state):
        self.mem_state = mem_state

    def rollback_state(self):
        return self.mem_state


class Originator:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def save_state(self):
        return Memento(copy.deepcopy(self.state))

    def load_state(self, memento):
        self.state = memento.rollback_state()


class Caretaker:
    def __init__(self, originator):
        self.state_index = 0
        self.memory = [originator.save_state()]
        self.originator = originator

    def current_state(self):
        return self.originator.get_state()

    def add_state(self, next_state):
        self.state_index += 1
        self.memory = self.memory[:self.state_index]
        self.memory.append(self.originator.save_state())
        self.originator.set_state(next_state)
        for obj in self.memory:
            print(obj.rollback_state())
        print("\n")

    def redo_state(self):
        if self.state_index < len(self.memory) - 1:
            self.state_index += 1
        self.originator.load_state(self.memory[self.state_index])
        for obj in self.memory:
            print(obj.rollback_state())
        print("\n")

    def undo_state(self):
        if self.state_index > 0:
            self.state_index -= 1
        self.originator.load_state(self.memory[self.state_index])
        for obj in self.memory:
            print(obj.rollback_state())
        print("\n")
