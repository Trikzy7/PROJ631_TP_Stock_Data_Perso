

from projectClass import Data, User, Node, Arc, DictionaryCustom


if __name__ == "__main__":
    # -------------------- Q2 : Placer les données dont l'utilisateur est intéressé
    """
    # -- CREATE DATA
    data0 = Data(0, 40)
    data1 = Data(1, 25)
    data2 = Data(2, 25)

    # -- CREATE NODE
    node0 = Node(0, 50, [], [], [], [])
    node1 = Node(1, 40, [], [], [], [])
    node2 = Node(2, 40, [], [], [], [])

    all_nodes = [node0, node1, node2]
    node0.add_all_nodes(all_nodes)
    node1.add_all_nodes(all_nodes)
    node2.add_all_nodes(all_nodes)

    # -- CREATE USER
    user0 = User(0, [data0, data1, data2], node0)

    # -- CREATE ARC
    arc0 = Arc(0, 2, user0, node0)
    arc1 = Arc(1, 1, node0, node1)
    arc2 = Arc(2, 1, node1, node2)
    arc3 = Arc(3, 4, node0, node2)


    # -- NODE : adding arcs
    node0.add_arcs_ongoing([arc0])
    node0.add_arcs_outgoing([arc1, arc3])

    node1.add_arcs_outgoing([arc1, arc2])

    node2.add_arcs_outgoing([arc2, arc3])

    # print(node0.get_current_arc_ongoing(user0))
    #
    # print(node0.get_list_arc_outgoing_sorted("asc"))
    #
    # for node in node0.get_list_arc_outgoing_sorted("asc"):
    #     print(node)
    #
    # node0.add_data(data0)
    # print(node0.get_capacity_remaining())

    # -- EXECUTE FUNCTION :
    user0.place_data()
    
    # -- Capacité restante du node0
    print(node0.get_capacity_remaining())

    # -- Data stockée sur le node 0 : Le node 0 avec comme value: 40
    for data in node0.list_data_stock:
        print(data)
    """


    # -------------------- Q3 : Deux user intéressé par même donnée
    """
    # -- CREATE DATA
    data0 = Data(0, 40)

    # -- CREATE NODE
    node0 = Node(0, 50, [], [], [], [])
    node1 = Node(1, 40, [], [], [], [])
    node2 = Node(2, 40, [], [], [], [])
    node3 = Node(3, 40, [], [], [], [])

    all_nodes = [node0, node1, node2, node3]
    node0.add_all_nodes(all_nodes)
    node1.add_all_nodes(all_nodes)
    node2.add_all_nodes(all_nodes)
    node3.add_all_nodes(all_nodes)

    # -- CREATE USER
    user0 = User(0, [data0], node0)
    user1 = User(1, [data0], node3)

    # -- CREATE ARC
    arc0 = Arc(0, 2, user0, node0)
    arc1 = Arc(1, 1, node0, node1)
    arc2 = Arc(2, 1, node1, node2)
    arc3 = Arc(3, 1, node0, node2)
    arc4 = Arc(4, 1, node1, node3)
    arc5 = Arc(5, 1, node2, node3)
    arc6 = Arc(6, 1, node3, node0)
    arc7 = Arc(7, 2, user1, node3)

    # -- NODE : adding arcs
    node0.add_arcs_ongoing([arc0])
    node0.add_arcs_outgoing([arc1, arc3, arc6])

    node1.add_arcs_outgoing([arc1, arc2, arc4])

    node2.add_arcs_outgoing([arc2, arc3, arc5])

    node3.add_arcs_ongoing([arc7])
    node3.add_arcs_outgoing([arc4, arc5, arc6])



    # -- EXECUTE FUNCTION :
    User.place_data_upgraded(user0, user1, data0)


    # print(node3.get_capacity_remaining())
    # -- Data stockée sur le node 1 : le node1 est à égal distance du user0 et user1
    for data in node1.list_data_stock:
        print(data)

    """

    # -------------------- Q4 : Placement des données optimisé

    # -- CREATE DATA
    data0 = Data(0, 40)
    data1 = Data(1, 25)
    data2 = Data(2, 25)
    data3 = Data(3, 30)
    data4 = Data(4, 10)

    # -- CREATE NODE
    node0 = Node(0, 50, [], [], [], [])
    node1 = Node(1, 40, [], [], [], [])
    node2 = Node(2, 40, [], [], [], [])

    all_nodes = [node0, node1, node2]
    node0.add_all_nodes(all_nodes)
    node1.add_all_nodes(all_nodes)
    node2.add_all_nodes(all_nodes)

    # -- CREATE USER
    user0 = User(0, [data0, data1, data2, data3, data4], node0)

    # -- CREATE ARC
    arc0 = Arc(0, 2, user0, node0)
    arc1 = Arc(1, 1, node0, node1)
    arc2 = Arc(2, 1, node1, node2)
    arc3 = Arc(3, 4, node0, node2)

    # -- NODE : adding arcs
    node0.add_arcs_ongoing([arc0])
    node0.add_arcs_outgoing([arc1, arc3])

    node1.add_arcs_outgoing([arc1, arc2])

    node2.add_arcs_outgoing([arc2, arc3])


    # -- EXECUTE FUNCTION :
    user0.place_data_optimised()

    # -- Data stockée sur le node 0 (50) : Résultat attendu: data1 (25) et data2 (25)
    print("------ DATA dans Node 0 ------")
    for data in node0.list_data_stock:
        print(data)
    print("------------------------------")

    # -- Data stockée sur le node 1 (40) : Résultat attendu: data0 (40)
    print("------ DATA dans Node 1 ------")
    for data in node1.list_data_stock:
        print(data)
    print("------------------------------")

    # -- Data stockée sur le node 2 (40) : Résultat attendu: data3 (30) et data4 (10)
    print("------ DATA dans Node 2 ------")
    for data in node2.list_data_stock:
        print(data)
    print("------------------------------")




















    # -------------------------------------- BROUILLON
    # my_list = [40, 25, 25]
    #
    # value_calculed = []
    #
    # for i in range( len(my_list) ):
    #     for j in range( len(my_list)-1, i, -1 ):
    #         # print(f'{my_list[i]} + {my_list[ j ]}')
    #         value_calculed.append({
    #             my_list[i] + my_list[j]: [
    #                 my_list[i],
    #                 my_list[j]
    #             ]
    #         })