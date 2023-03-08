
from .Data import Data
from .Node import Node
from.DictionaryCustom import DictionaryCustom


class User:

    def __init__(self, id:int, list_data_interest:list[Data], node_access:Node):
        self.id = id
        self.list_data_interest = list_data_interest
        self.node_access = node_access

    def place_data(self) -> None:
        """
        Permet de placer les données dont l'utilisateur est intéressé.
        :return: None
        """
        # Pour chaque data in list_data_interest
        for current_data in self.list_data_interest:
            # Si la valeur de la donnée actuelle est <= au node access -> On la place direct sur le node access
            if current_data.value <= self.node_access.get_capacity_remaining():
                self.node_access.add_data(current_data)

            # Si le node access n'a plus assez de capacité pour stocker la donnée actuelle
            else:
                # On prend la liste des arcs qui sortent du node access dans l'ordre croissant pour avoir accés aux autres nodes
                list_arc_outgoing_asc = self.node_access.get_list_arc_outgoing_sorted("asc")

                # Pour chaque arc sortant du node access
                for arc in list_arc_outgoing_asc:

                    # Permet d'avoir le node destination de l'arc
                    node_destination_arc = arc.get_node_destination(self.node_access)

                    # Si la valeur de la donnée actuelle est <= au node sur lequel on est -> On la place sur ce node
                    if current_data.value <= node_destination_arc.get_capacity_remaining():
                        arc.end.add_data(current_data)
                        break

    def get_node_data_placed(self, data) -> Node:
        """
        Permet de renvoyer le node sur lequel est placé la data en paramètre
        :param data: Date
        :return: Node
        """
        # Si la data est sur le node access du user -> On return direct ce node
        if self.node_access.has_data(data):
            return self.node_access

        # Si la data n'est pas direct sur le node access du user
        else:
            list_arc_outgoing = self.node_access.list_arc_outgoing

            # On parcours tous les arcs sortant du node access
            for arc in list_arc_outgoing:

                # Peremet d'avoir le node destination de l'arc
                node_destination_arc = arc.get_node_destination(self.node_access)

                # Si le node destination de l'arc a la data -> On le return
                if node_destination_arc.has_data(data):
                    return node_destination_arc

    def calcul_distance_node(self, node) -> int:
        """
        Permet de return la distance entre le user et le node en paramètre
        :param node: Node
        :return: int
        """
        # On prend la distance entre le user et son node access
        distance = self.node_access.get_current_arc_ongoing(self).value

        # Si le node access n'est pas le node en paramètre
        if self.node_access != node:

            list_arc_outgoing = self.node_access.list_arc_outgoing

            # On parcours tous les arcs sortant du node access
            for arc in list_arc_outgoing:

                # Peremet d'avoir le node destination de l'arc
                node_destination_arc = arc.get_node_destination(self.node_access)

                if node_destination_arc == node:
                    distance += node_destination_arc.get_arc_node(self.node_access).value

        return distance

    def calcul_all_combinaison_data_value(self):
        """
        Permet de retourner un tableau avec toutes les valeurs calculées
        dans la liste list_data_interest avec toutes les combinaisons
        possibles. Ces calculs sont la somme des deux data.value
        :return: Dict |
        exemple : {(Data0, Data2): 65 , (Data0, Data1): 65 , (Data1, Data2): 50 }
        """

        values_calculed = {}

        for i in range( len(self.list_data_interest) ):
            values_calculed[self.list_data_interest[i]] = self.list_data_interest[i].value
            for j in range( len(self.list_data_interest)-1, i, -1 ):
                values_calculed[
                    self.list_data_interest[i],
                    self.list_data_interest[j]
                    ] = self.list_data_interest[i].value + self.list_data_interest[j].value

        return values_calculed

    @staticmethod
    def place_data_upgraded(user0, user1, data) -> None:
        # On place la data en partant du 1er user
        user0.place_data()

        # On recup le node où data a été placée
        node_data_placed = user0.get_node_data_placed(data)
        # print(node_data_placed)

        # On calcul la distance entre user0 et node_place_data
        user0_distance_node = user0.calcul_distance_node(node_data_placed)

        # On calcul la distance entre user1 et node_place_data
        user1_distance_node = user1.calcul_distance_node(node_data_placed)

        # Si la distance user0 - node_data_placed et user1 - node_data_placed est différente:
        if user0_distance_node != user1_distance_node:
            # On remove la data du node ou elle a été placée
            node_data_placed.remove_data(data)

            list_arc_outgoing_asc = node_data_placed.get_list_arc_outgoing_sorted("asc")

            for arc in list_arc_outgoing_asc:
                # Peremet d'avoir le node destination de l'arc
                node_destination_arc = arc.get_node_destination(node_data_placed)

                if data.value <= node_destination_arc.get_capacity_remaining():
                    node_destination_arc.add_data(data)

                    # On calcul la distance entre user0 et node_place_data
                    user0_distance_node = user0.calcul_distance_node(node_destination_arc)

                    # On calcul la distance entre user1 et node_place_data
                    user1_distance_node = user1.calcul_distance_node(node_destination_arc)

                # Si les nouvelles valeurs des distances sont égales entre elle -> On sort de la boucle
                if user0_distance_node == user1_distance_node:
                    break

    def place_data_optimised(self):
        # -- Calcul toutes les bominaisons de sum des key in self.list_data_interest
        dict_calculed = self.calcul_all_combinaison_data_value()

        # -- Trie du dict par ordre croissant
        dict_calculed_sorted = DictionaryCustom.sort_by_values(dict_calculed, 'desc')

        # -- Tableau pour savoir si un élément du dict a déjà été
        # ajouté -> Si un un element de dict_calculed_sorted contient un clé qui contient une data qui
        # a déjà été ajoutée, le data_has_placed[id_element_in_dict_calculed_sorted] = True

        data_has_placed = [False for key in dict_calculed_sorted]

        # -- Pour chaque valeur du dict
        for id, key in enumerate(dict_calculed_sorted):

            # -- Si la valeur peut aller sur le node_access -> On le met direct sur le node_access
            if dict_calculed_sorted[key] <= self.node_access.get_capacity_remaining() and data_has_placed[id] is False:
                # -- Si la key est un tuple -> On itère dessus pour ajouter les data au node
                if type(key) is tuple:
                    for data in key:
                        self.node_access.add_data(data)

                        # -- Get the list of ids where data is in the dict
                        list_id_where_data_in_dict = DictionaryCustom.get_ids_keys_dict(dict_calculed_sorted, data)
                        # print(list_id_where_data_in_dict)
                        for id_data_in_dict_keys in list_id_where_data_in_dict:
                            data_has_placed[id_data_in_dict_keys] = True

                    # print(data_has_placed)

                # Sinon, c'est juste une valeur -> On ajoute direct la valeur
                else:
                    self.node_access.add_data(key)

                    # -- Get the list of ids where data is in the dict
                    list_id_where_data_in_dict = DictionaryCustom.get_ids_keys_dict(dict_calculed_sorted, key)

                    for id_data_in_dict_keys in list_id_where_data_in_dict:
                        data_has_placed[id_data_in_dict_keys] = True

            # Si les ou la data n'a pas encore été palcé et si on ne peut pas direct la mettre sur le node access
            elif data_has_placed[id] is False:
                # On prend la liste des arcs qui sortent du node access dans l'ordre décroissant pour avoir accés aux autres nodes
                list_arc_outgoing_desc = self.node_access.get_list_arc_outgoing_sorted("desc")

                # Pour chaque arc sortant du node access
                for arc in list_arc_outgoing_desc:

                    # Permet d'avoir le node destination de l'arc
                    node_destination_arc = arc.get_node_destination(self.node_access)

                    # -- Si la key est un tuple -> On itère dessus pour ajouter les data au node
                    if dict_calculed_sorted[key] <= node_destination_arc.get_capacity_remaining():
                        if type(key) is tuple:
                            for data in key:
                                node_destination_arc.add_data(data)

                                # -- Get the list of ids where data is in the dict
                                list_id_where_data_in_dict = DictionaryCustom.get_ids_keys_dict(dict_calculed_sorted, data)
                                # print(list_id_where_data_in_dict)
                                for id_data_in_dict_keys in list_id_where_data_in_dict:
                                    data_has_placed[id_data_in_dict_keys] = True

                        # Sinon, c'est juste une valeur -> On ajoute direct la valeur
                        else:
                            node_destination_arc.add_data(key)

                            # -- Get the list of ids where data is in the dict
                            list_id_where_data_in_dict = DictionaryCustom.get_ids_keys_dict(dict_calculed_sorted, key)
                            # print(list_id_where_data_in_dict)
                            for id_data_in_dict_keys in list_id_where_data_in_dict:
                                data_has_placed[id_data_in_dict_keys] = True

                        break


