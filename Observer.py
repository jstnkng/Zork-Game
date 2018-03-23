class Observer(object):
    def update(self):
        pass

class Observable(object):
    def __init__(self):
        self.observers = []

    def add_Observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_Observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def clear_Observers(self):
        self.observers = []
