import unittest
from graphs import Graphs


class GraphsTest(unittest.TestCase):
    def testbasics(self):
        test_graph = Graphs()
        self.assertFalse(test_graph.addEdge("A","B"))

        test_graph.addVertex("A")
        self.assertFalse(test_graph.addEdge("A","B"))

        test_graph.addVertex("B")
        
        checkgrpah = {"A":["B"],"B":["A"]}

        test_graph.addEdge("A", "B")

        self.assertEqual(checkgrpah,test_graph.returnGraph())

        test_graph.addVertex("C")
        test_graph.addVertex("D")

        test_graph.addEdge("A","C")
        test_graph.addEdge("A","D")

        test_graph.addEdge("B","C")
        test_graph.addEdge("B","D")
        test_graph.addEdge("C","D")

        test_graph.addEdge("C","C")

        test_graph.removeVertex("D")
        checkgrpah = {"A":["B","C"], "B":["A","C"], "C":["A","B"]}
        
        self.assertEqual(checkgrpah,test_graph.returnGraph())
        #test_graph.printGraph()

if __name__ == "__main__":
    unittest.main()

