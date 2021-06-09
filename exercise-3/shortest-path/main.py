from collections import deque

INFINITY = float("inf")


class Graph:
    def __init__(self, filename):
        """Reads graph definition and stores it. Each line of the graph
        definition file defines an edge by specifying the start node,
        end node, and distance, delimited by spaces.

        Stores the graph definition in two properties which are used by
        Dijkstra's algorithm in the shortest_path method:
        self.nodes = set of all unique nodes in the graph
        self.adjacency_list = dict that maps each node to an unordered set of
        (neighbor, distance) tuples.
        """

        # Read the graph definition file and store in graph_edges as a list of
        # lists of [from_node, to_node, distance]. This data structure is not
        # used by Dijkstra's algorithm, it's just an intermediate step in the
        # create of self.nodes and self.adjacency_list.
        graph_edges = []
        with open(filename) as fhandle:
            for line in fhandle:
                node_from, node_to, cost, *_ = line.strip().split("\t")
                graph_edges.append((node_from, node_to, float(cost)))

        self.nodes = set()
        for edge in graph_edges:
            self.nodes.update([edge[0], edge[1]])
        print("self.nodes", self.nodes)

        self.adjacency_list = {node: set() for node in self.nodes}
        for edge in graph_edges:
            self.adjacency_list[edge[0]].add((edge[1], edge[2]))
        print("self.adjacency_list", self.adjacency_list)

    def shortest_path(self, start_node, end_node):
        """Uses Dijkstra's algorithm to determine the shortest path from
        start_node to end_node. Returns (path, distance).
        """

        unvisited_nodes = self.nodes.copy()  # All nodes are initially unvisited.

        # Create a dictionary of each node's distance from start_node. We will
        # update each node's distance whenever we find a shorter path.
        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }
        print("distance_from_start", distance_from_start)

        # Initialize previous_node, the dictionary that maps each node to the
        # node it was visited from when the the shortest path to it was found.
        previous_node = {node: None for node in self.nodes}
        print("previous_node", previous_node)

        print("while unvisited_nodes:")
        while unvisited_nodes:
            print("\tunvisited_nodes", unvisited_nodes)
            # Set current_node to the unvisited node with shortest distance
            # calculated so far.
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            print(f"\tconsider current_node={current_node}")
            unvisited_nodes.remove(current_node)
            print(f"\tunvisited_nodes after remove {current_node}", unvisited_nodes)

            # If current_node's distance is INFINITY, the remaining unvisited
            # nodes are not connected to start_node, so we're done.
            print("\tdistance_from_start[current_node]", distance_from_start[current_node])
            if distance_from_start[current_node] == INFINITY:
                break

            # For each neighbor of current_node, check whether the total distance
            # to the neighbor via current_node is shorter than the distance we
            # currently have for that node. If it is, update the neighbor's values
            # for distance_from_start and previous_node.
            print("\tfor neighbor, distance in self.adjacency_list[current_node]")
            for neighbor, distance in self.adjacency_list[current_node]:
                print(f"\t\tcurrent_node={current_node}, neighbor={neighbor}, distance={distance}")
                new_path = distance_from_start[current_node] + distance
                print("\t\tassume new_path from start", new_path)
                print("\t\tdistance_from_start[neighbor]", distance_from_start[neighbor])
                if new_path < distance_from_start[neighbor]:
                    print("\t\tnew_path < distance_from_start[neighbor]:")
                    distance_from_start[neighbor] = new_path
                    previous_node[neighbor] = current_node
                    print("\t\t\tupdated distance_from_start", distance_from_start)
                    print("\t\t\tupdated previous_node", previous_node)

            if current_node == end_node:
                break  # we've visited the destination node, so we're done
            print("\t================================")

        # To build the path to be returned, we iterate through the nodes from
        # end_node back to start_node. Note the use of a deque, which can
        # appendleft with O(1) performance.
        path = deque()
        current_node = end_node
        print("build the path")
        while previous_node[current_node] is not None:
            print("\tcurrent_node", current_node)
            path.appendleft(current_node)
            print("\tpath", path)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        print("return path", path)
        print("return distance_from_start", distance_from_start)
        return path, distance_from_start[end_node]


def main():
    """Runs a few simple tests to verify the implementation.
    """
    verify_algorithm(
        filename="simple_graph.txt",
        start="A",
        end="F",
        path=["A", "C", "E", "F"],
        distance=11,
    )

    try_algorithm(
        filename="simple_graph.txt",
        start="A",
        end="F",
    )


def verify_algorithm(filename, start, end, path, distance):
    """Helper function to run simple tests and print results to console.

    filename = graph definition file
    start/end = path to be calculated
    path = expected shorted path
    distance = expected distance of path
    """
    graph = Graph(filename)
    returned_path, returned_distance = graph.shortest_path(start, end)
    print("returned_path", returned_path)
    print("returned_distance", returned_distance)

    assert list(returned_path) == path
    assert returned_distance == distance

    print('\ngraph definition file: {0}'.format(filename))
    print('      start/end nodes: {0} -> {1}'.format(start, end))
    print('        shortest path: {0}'.format(path))
    print('       total distance: {0}'.format(distance))


def try_algorithm(filename, start, end):
    graph = Graph(filename)
    returned_path, returned_distance = graph.shortest_path(start, end)
    print("returned_path", returned_path)
    print("returned_distance", returned_distance)

    print('\ngraph definition file: {0}'.format(filename))
    print('      start/end nodes: {0} -> {1}'.format(start, end))
    print('        shortest path: {0}'.format(returned_path))
    print('       total distance: {0}'.format(returned_distance))


if __name__ == "__main__":
    main()
