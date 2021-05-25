class Scene():
    def __init__(self):
        self.started = False

    def start(self):
        self.started = True
        return self.started

    def update(self, delta):
        pass

    def render(self, target):
        pass
