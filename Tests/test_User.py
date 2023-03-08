from unittest import TestCase
from projectClass import Data, User, Node, Arc

class TestUser(TestCase):

    def test_place_data(self):
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

        # -- EXECUTE FUNCTION :
        user0.place_data()


        # -- TEST DES DONNÉES ATTENDUES
        self.assertEqual(node0.list_data_stock, [data0])

    def test_place_data_upgraded(self):
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

        # -- TEST DES DONNÉES ATTENDUES
        self.assertEqual(node1.list_data_stock, [data0])


    def test_place_data_optimised(self):
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

        # -- TEST DES DONNÉES ATTENDUES
        self.assertEqual(node0.list_data_stock, [data1, data2])

