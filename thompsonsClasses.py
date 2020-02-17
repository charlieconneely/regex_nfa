# Charlie Conneely
# Classes needed for Thompsons Construction

class State:
    edges = []
    # label for arrows - None = epsilon
    label = None
    
    # Constructor
    def __init__(self, label=None, edges=[]):
        self.label = label
        self.edges = edges


class Frag:
    # Start state of NFA fragment
    start = None
    # Accept state of NFA fragment
    accept = None
    
    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

# test instances 
instance1 = State(label='a', edges=[1])
instance2 = State(label='b', edges=[instance1])
frag1 = Frag(instance1, instance2)

print(instance1.label)
print(instance2.edges[0])
print(frag1)


