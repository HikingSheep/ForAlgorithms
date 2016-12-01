class Graph(object):
    
    def Display(self):
        print(g.graph)
    
    def _init_(self):
        self.graph = {}

    def AddNode(self,string):
        if string in g.graph:
            print("There")
        else:
            g.graph[string] = []
            g.Display()

    def AddEdge(self,key,NextValue):
        value = []

        if key in g.graph:
            value = g.graph[key]
            if NextValue in value:
                print("Alredy there")
            elif NextValue not in g.graph:
                g.AddNode(NextValue)
                g.AddEdge(key,NextValue)
            else:
                g.graph[key] = value + [NextValue]
                g.AddEdge(NextValue,key)
                g.Display()
        else:
            g.AddNode(key)
            g.AddEdge(key,NextValue)
            g.Display()
            

    def dfs(self,startpoint):
        stack = []
        visited = []
        stack.extend(startpoint)
        while stack:
            edge = stack.pop()
            if edge not in visited:
                visited.extend(edge)
                stack = stack + g.graph[edge]
        return visited

    def bfs(self,startpoint):
        stack = []
        visited = []
        stack.extend(startpoint)
        while stack:
            edge = stack.pop(0)
            if edge not in visited:
                visited.extend(edge)
                stack = stack + g.graph[edge]
        return visited
                
        
if __name__ == '__main__':
     g = Graph()
