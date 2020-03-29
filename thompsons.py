# Charlie Conneely
# Classes to use for Thompson's Construction

class State:
    """A state with 1 or 2 edges, all edges labelled by label."""
    # Constructor for the class
    def __init__(self, label=None, edges=None):
         # Every state has 0, 1 or 2 edges from it
        self.edges = edges if edges else []
         # label for arrows - None = epsilon
        self.label = label
       

class Fragment:
    """An NFA fragment with a start and accept state."""
    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept
