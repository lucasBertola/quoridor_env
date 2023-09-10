import numpy as np
import networkx as nx

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def to_node(self):
        return (self.x, self.y)
        
class Edge():
    def __init__(self, node1:Node, node2:Node):
        self.node1 = node1
        self.node2 = node2
        
    def to_edge(self):
        return (self.node1.to_node(), self.node2.to_node())
    
class BoardGraph():
    
    def __init__(self, size=3):
        self.size = size
        self.graph = nx.Graph()
        self._build_graph()
                    
    def _build_graph(self):
        for i in range(0, self.size,2):
            for j in range(0, self.size,2):
                # Directions: Up, Down, Left, Right
                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                    ni, nj = i + dx, j + dy
                    # Ensure we only add edges once
                    is_valid = 0 <= ni < self.size and 0 <= nj < self.size
                    if is_valid and (i, j) < (ni, nj):
                        self.graph.add_edge((i, j), (ni, nj))
    
    def _dfs(self, node, target_y, visited):
        if node[1] == target_y:
            return True

        visited.add(node)
        for neighbor in self.graph.neighbors(node):
            if neighbor not in visited:
                if self._dfs(neighbor, target_y, visited):
                    return True

        return False
    
    def remove_edges(self,edge1: Edge,edge2: Edge,player1:Node,player2:Node):
        if(not self.graph.has_edge(*edge1.to_edge()) and not self.graph.has_edge(*edge2.to_edge())):
            return
        
        lenComponents = len(list(nx.connected_components(self.graph)))
        
        self.graph.remove_edge(*edge1.to_edge())
        self.graph.remove_edge(*edge2.to_edge())
        
        #todo, on pourrait utiliser le cache pour savoir si la suppression de cet edge rend le graph non connexe

        components = list(nx.connected_components(self.graph))
        if(len(components) == lenComponents):
            # The graph is still connected, we can stop here
            return
        
        # Find which component contains (xPlayer1, yPlayer1) or (xPlayer2, yPlayer2)
        good_component = []
        for component in components:
            if player1.to_node() in component or player2.to_node() in component:
                good_component.append(component)
                break
            
        # Remove all other components
        for component in components:
            if component not in good_component:
                for node in component:
                    self.graph.remove_node(node)
    
    def edges_can_be_removed(self, edge1: Edge, edge2: Edge, player1:Node, player2:Node):
        #todo check dans le cache si c'est un coup autorisé ou pas
        if(not self.graph.has_edge(*edge1.to_edge()) and not self.graph.has_edge(*edge2.to_edge())):
            return True
        
        # Temporarily remove the edges
        self.graph.remove_edge(*edge1.to_edge())
        self.graph.remove_edge(*edge2.to_edge())

        # Check if a path exists for both players using DFS
        player1_can_reach = self._dfs(player1.to_node(), self.size - 1, set())
        player2_can_reach = self._dfs(player2.to_node(), 0, set())

        # Add the edges back since we just wanted to check
        self.graph.add_edge(*edge1.to_edge())
        self.graph.add_edge(*edge2.to_edge())

        # Return True if both players can still reach their respective goals, else False
        return player1_can_reach and player2_can_reach
                
    def clone(self):
        new_board = BoardGraph(self.size)
        new_board.graph = self.graph.copy()
        return new_board
    
    def find_articulation_points(self):
        return nx.articulation_points(self.graph)