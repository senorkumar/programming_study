
#assume there is a graph class
#interface:
#has a list of nodes in g.nodes

#Nodes have two properties:
#n = Node(data)
#n.children is a list of nodes 
#n.data 


def is_route(start, end):

	q = Queue()

	q.add(start)

	visited = set()

	while not q.is_empty():
		node = q.deque()
		if node not in visited:
			visited.add(node)
			if node == end:
				return True
			else:
				for n in node.children:
					q.add(n)

	return False
