class Caretaker:
    def __init__(self, originator):
        self.state_index = 0
        self.default_state = originator.save_state()
        self.memory = [self.default_state]
        self.originator = originator

    def current_state(self):
        return self.originator.get_state()

    def add_state(self, next_state):
        self.state_index += 1
        self.memory = self.memory[:self.state_index]
        self.memory.append(self.originator.save_state())
        self.originator.set_state(next_state)

        
    def redo_state(self):
        if self.state_index < len(self.memory) - 1:
            self.state_index += 1
        self.originator.load_state(self.memory[self.state_index])


    def undo_state(self):
        if self.state_index > 0:
            self.state_index -= 1
        self.originator.load_state(self.memory[self.state_index])

    
    def clear_state(self):
        self.state_index = 0
        self.memory = [self.default_state]
        self.originator.set_state(self.default_state.rollback_state())