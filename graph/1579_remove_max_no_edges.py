class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        sorted_edges = []
        for edge in edges:
            if edge[0] == 3:
                sorted_edges.insert(0, edge)
                continue
            sorted_edges.append(edge)
        
        class node:
            def __init__(self, value, rank, parent = None):
                self.value = value
                self.parent = parent
                self.rank = rank
        
        def find_node(node):
            if node.parent == None:
                return node
            node.parent = find_node(node.parent)
            return node.parent

        def link_nodes(node1, node2):
            if node1.rank > node2.rank:
                node2.parent = node1
            else:
                node1.parent = node2
                if node1.rank == node2.rank:
                    node2.rank += 1
        
        def make_node(value):
            return node(value, 0, None)
        
        def union(node1, node2):
            link_nodes(find_node(node1), find_node(node2))

        def mst(edges, nodes):
            g1 = {}
            g2 = {}
            g1_count = 0
            g2_count = 0
            skip_edges = []
            for node in range(1, nodes+1):
                g1[node] = make_node(node)
                g2[node] = make_node(node)
            for edge in edges:
                n1 = edge[1]
                n2 = edge[2]
                if edge[0] == 3:
                    if find_node(g1[n1]) == find_node(g1[n2]) and find_node(g2[n1]) == find_node(g2[n2]):
                        skip_edges.append(edge)
                        continue
                    if find_node(g1[n1]) != find_node(g1[n2]):
                        g1_count += 1
                        union(g1[n1], g1[n2])
                    if find_node(g2[n1]) != find_node(g2[n2]):
                        g2_count += 1
                        union(g2[n1], g2[n2])
                elif edge[0] == 1:
                    if find_node(g1[n1]) == find_node(g1[n2]):
                        skip_edges.append(edge)
                        continue
                    g1_count += 1
                    union(g1[n1], g1[n2])
                else:
                    if find_node(g2[n1]) == find_node(g2[n2]):
                        skip_edges.append(edge)
                        continue
                    g2_count += 1
                    union(g2[n1], g2[n2])
            if nodes - 1 > g1_count or nodes - 1 > g2_count:
                return -1
            return len(skip_edges)
        
        return mst(sorted_edges, n)
        
        

s = Solution()
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
n = 4
s.maxNumEdgesToRemove(n, edges)