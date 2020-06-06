class Digraph:
    """This class implements a directed, weighted graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.children = dict()
        self.parents = dict()
        self.edges = 0

    def add_node(self, node):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""
        if node in self.nodes:
            return 'this node already exist'
        self.nodes.add(node)
        self.children[node] = dict()
        self.parents[node] = dict()

    def add_arc(self, tail, head, weight):
        """Creates a directed arc pointing from 'tail' to 'head' and assigns 'weight' as its weight."""
        if tail not in self.nodes:
            self.add_node(tail)
        if head not in self.nodes:
            self.add_node(head)
        self.children[tail][head] = weight
        self.parents[head][tail] = weight
        self.edges += 1

    def has_arc(self, tail, head):
        return tail in self.nodes and head in self.children[tail]

    def get_weight(self, tail, head):
        if tail not in self.nodes:
            raise Exception("this tail node doesn't exist")
        if head not in self.nodes:
            raise Exception("this head node doesn't exist")
        if head not in self.children[tail]:
            raise Exception(f"The edge {tail} - {head} doesn't exist")
        return self.children[tail][head]

    def delete_arc(self, tail, head):
        """Removes the directed arc from 'tail' to 'head'."""
        if tail not in self.nodes:
            return "this tail doesn't exist"
        if head not in self.nodes:
            return "this head doesn't exist"
        del self.children[tail][head]
        del self.parents[head][tail]
        self.edges -= 1

    def delete_node(self, node):
        """Removes the node from this digraph. Also, removes all arcs incident on the input node."""
        if node not in self.nodes:
            return "this node doesn't exist"
        self.edges -= len(self.children[node]) + len(self.parents[node])
        # Unlink children:
        for child in self.children[node]:
            del self.parents[child][node]
        # Unlink parents:
        for parent in self.parents[node]:
            del self.children[parent][node]
        del self.children[node]
        del self.parents [node]
        self.nodes.remove(node)

    def __len__(self):
        return len(self.nodes)

    def get_parents(self, node):
        """Returns all parents of 'node'."""
        if node not in self.nodes:
            return "this node doesn't exist"
        return self.parents[node]

    def get_children(self, node):
        """Returns all children of 'node'."""
        if node not in self.nodes:
            return "this node doesn't exist"
        return self.children[node]

    def clear(self):
        self.nodes.clear()
        self.children.clear()
        self.parents.clear()
        self.edges = 0