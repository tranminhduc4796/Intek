class Station:
    def __repr__(self):
        return self.name


    def __init__(self, name):
        self.name = name
        self.visited = False
        self.train = None


    def _switch_visit(self):
        self.visited = not self.visited


    def _get_train(self, train):
        self.train = train


    def _remove_train(self):
        self.train = None

    def is_visited(self):
        return self.visited
