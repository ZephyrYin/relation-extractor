__author__ = 'zephyros'
from parser import  Parser
import copy

class DependencyExtractor:
    def __init__(self):
        self.parser = Parser()

    def createDependency(self, sentence):
        dependencies = self.parser.parseToStanfordDependencies(sentence)
        tupleResult = [(rel, gov.text, dep.text) for rel, gov, dep in dependencies.dependencies]
        return tupleResult

    def writeTofile(self, inPath, outPath):
        inFile = open(inPath)
        lines = inFile.readlines()
        inFile.close()
        outFile = open(outPath, 'w')
        cnt = 0
        for line in lines:
            cnt = cnt + 1
            institution, person, snippet, intermediate_text, judgment = line.split("\t")
            sentences = (person.replace(' ','') + intermediate_text + institution.replace(' ','')).decode('utf-8')
            print cnt
            print sentences
            lineDependency = []
            for sentence in sentences.split('. '):
                if len(sentence) < 4:
                        continue
                dependency = self.createDependency(sentence)
                lineDependency.append(dependency)
            outFile.write(str(lineDependency))
            outFile.write('\n')
        outFile.close()

    def readFromFile(self, path):
        file = open(path)
        lines = file.readlines()
        cnt = 0
        dependencyList = []
        for line in lines:
            cnt = cnt + 1
            print cnt
            dependency = []
            temp = line[2:-3]
            list = temp.split('], [')
            for tt in list:
                de = []
                tupleList = tt.split('), (')
                for t in tupleList:
                    tupleStr = t.strip('(').strip(')')
                    tList = [temp.strip('u').strip('\n')[1:-1] for temp in tupleStr.split(', ')]
                    if len(tList) < 3:
                        continue
                    de.append(tList)

                dependency.append(de)
            dependencyList.append(dependency)
        return dependencyList

    def getDistance(self, name, institution, dependency):
        dict = {}
        root = self.getRoot(dependency)
        for d in dependency:
            if len(d) < 1:
                continue
            if d[1] in dict:
                if d[2] in dict[d[1]]:
                    continue
                dict[d[1]].append(d[2])
            else:
                dict[d[1]] = []

    def getDis(self, root, node, dict):
        level = 0
        queue = [root, '#']
        while len(queue) > 0:
            firstItem = queue[0]
        return level

    def getRoot(self, dependency):
        allNodes = []
        for d in dependency:
            if d[1] not in allNodes:
                allNodes.append(d[1])
            if d[2] not in allNodes:
                allNodes.append(d[2])
        print allNodes
        for d in dependency:
            if d[2] in allNodes:
                allNodes.remove(d[2])
        return allNodes




