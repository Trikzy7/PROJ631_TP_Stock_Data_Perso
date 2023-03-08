

class Arc:

    def __init__(self, id, value, start, end):
        self.id = id
        self.value = value
        self.start = start
        self.end = end

    def get_node_destination(self, currentNode):
        """
        Permet de récupérer le node destination de l'arc.
        Le node destination est le node start de l'arc si le node end de l'arc est == currentNode
        :param currentNode: Node qui permet l'inversion s'il est égale au node end de l'arc
        :return: Node destination
        """
        return self.start if self.end == currentNode else self.end

    def __str__(self):
        return f'Arc id: {self.id} | value: {self.value}'

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


