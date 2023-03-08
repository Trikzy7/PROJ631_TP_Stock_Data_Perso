
from .Data import Data


class Node:

    def __init__(self, id:int, capacity:int, list_data_stock:list[Data], list_node_access:list, list_arc_ongoing:list, list_arc_outgoing:list)-> None:
        self.id = id
        self.capacity = capacity
        self.list_data_stock = list_data_stock
        self.list_node_access = list_node_access
        self.list_arc_ongoing = list_arc_ongoing
        self.list_arc_outgoing = list_arc_outgoing

    def add_all_nodes(self, list_nodes:list) -> None:
        for node in list_nodes:
            if node != self:
                self.list_node_access.append(node)

    def add_arcs_ongoing(self, list_arcs_ongoing:list) -> None:
        self.list_arc_ongoing += list_arcs_ongoing

    def add_arcs_outgoing(self, list_arcs_outgoing:list) -> None:
        self.list_arc_outgoing += list_arcs_outgoing

    def get_current_arc_ongoing(self, currentUser):
        """
        Permet de renvoyer l'arc auquel est lié le node et le user en parametre
        :param currentNode: User
        :return: type Arc
        """
        for arc in self.list_arc_ongoing:
            if arc.start == currentUser:
                return arc

        return False

    def add_data(self, data) -> None:
        self.list_data_stock.append(data)

    def remove_data(self, data) -> None:
        self.list_data_stock.remove(data)

    def get_list_arc_outgoing_sorted(self, order) -> list:
        """
        Permet de renvoyer le liste des arcs sortants triés selon le parametre order
        :param order: str : asc | desc
        :return: list of arc outgoing sorted
        """

        list_sorted = sorted(self.list_arc_outgoing)

        if order != "asc":
            list_sorted.reverse()

        return list_sorted

    def get_capacity_remaining(self) -> int:
        """
        Calcul la capacité restant d'un node en fonction des data qu'il stocke
        :return: int : capacity remaining
        """
        return self.capacity - sum([
            data.value for data in self.list_data_stock
        ])

    def has_data(self, data):
        """
        Permet de savoir si un node contient la data en paramètre
        :param data: Data
        :return: Bool
        """
        return data in self.list_data_stock

    def get_arc_node(self, node):
        """
        Permet de renvoyer l'arc qui a comme destination le node en paramètre parmi les arc sortants
        :param node: Node
        :return: Arc
        """
        for arc in self.list_arc_outgoing:
            node_destination_arc = arc.get_node_destination(self)

            if node_destination_arc == node:
                return arc

    def __str__(self):
        return f'Node id: {self.id}'
