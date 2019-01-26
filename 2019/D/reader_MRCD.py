vertexs = {}


class Reader:

    def __init__(self):
        fileName = '''excelFile.xlsx'''
        filePath = os.path.dirname(os.path.abspath(__file__))
        print('[tips]请将数据文件'+fileName+"放在目录"+filePath+"下")
        print('[info] Start to load')
        import xlrd
        self.data = xlrd.open_workbook(filePath+'\\'+fileName)
        self.table = self.data.sheets()[0]

    def print(self):
        for i in range(self.table.nrows):
            print(self.table.row_values(i))

    def debug(self):
        print(self.table.ncols, self.table.nrows)

    def getMatrix(self):
        matrix = []
        for i in range(self.table.nrows):
            matrix.append(self.table.row_values(i))
        return matrix

    def getSubMatrix(self, *field):
        matrix = []
        for i in range(self.table.nrows):
            subMat = []
            for x in range(len(field)):
                subMat.append(self.table.cell(i, field[x]).value)
            matrix.append(subMat)
            del(subMat)
        return matrix

    def init(self):
        self.vertexs = {}
        count = 0
        for i in range(self.table.nrows):
            v1 = self.table.row_values(i)[0]
            v2 = self.table.row_values(i)[1]
            if(v1 not in self.vertexs):
                self.vertexs[v1] = count
                count += 1
            if(v2 not in self.vertexs):
                self.vertexs[v2] = count
                count += 1
        self.n = count

    def getGraph(self):
        self.init()
        data = self.getMatrix()
        print(data)
        dic = self.vertexs
        graph = [[] for _ in range(self.n)]
        for edge in data:
            ver1 = dic[edge[0]]
            ver2 = dic[edge[1]]
            graph[ver1].append([ver2, edge[2]])
            graph[ver2].append([ver1, edge[2]])
        # print(data)
        return graph

def dij(start, graph):
    n=len(graph)
    # print(n)
    costs=[99999 for _ in range(n)]
    costs[start]=0
    parents=[-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    t=[]
    while len(t)<n:
        minCost=99999
        minNode=None
        for i in range(n):
            if not visited[i] and costs[i]<minCost:
                minCost=costs[i]
                minNode=i
        t.append(minNode)
        visited[minNode]=True

        for edge in graph[minNode]:
            if not visited[edge[0]] and minCost +edge[1]<costs[edge[0]]:
                costs[edge[0]]=minCost+edge[1]
                parents[edge[0]]=minNode
    return costs,parents



if __name__ == '__main__':
    import os
    print('[path] '+os.path.dirname(os.path.abspath(__file__)))
    reader = Reader()
    #reader.debug()
    # reader.print()
    graph = reader.getGraph()
    # print(reader.n)
    # for edges in graph:
    #     print(edges)
    # 各点到点到1的最短路径
    #print(reader.vertexs['Exit'])
    costs,parents=dij(reader.vertexs['Exit'],graph)
    print(costs)
    print(parents)
