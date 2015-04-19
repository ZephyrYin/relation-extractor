__author__ = 'zephyrYin'
from manual import RelationExtractor
from evaluate import evaluate
from DependencyExtractor import DependencyExtractor
from kitchenSink import kitchenSink

# R = RelationExtractor()
# file = open('test.tsv')
# lines = file.readlines()
# tags = map(lambda l: 'Yes' if len(R.extractor(l)) > 0 else 'No', lines)
# testTags = [line.split(' ')[-1] for line in lines]
# R.genFeature()
# E = evaluate(tags, testTags)
# print E.getEvaluation()


def getConnection(graph, name, institution):
    token = []
    for g in graph:
        if g[2] == name or g[2] == institution:
            if g[1] not in token:
                token.append(g[1])
    return token

# D = DependencyExtractor()
# #D.writeTofile('test.tsv','testDependency.txt')
# result = D.readFromFile('trainDependency.txt')
# cnt = 0
# for r in result:
#     cnt = cnt + 1
#     print cnt
#     temp = []
#     for tree in r:
#         if len(tree) < 1:
#             continue
#         temp = temp + tree
#     print tempt i
#     print D.getRoot(temp)

#D.writeTofile('train.tsv','trainDependency.txt')
trainFileList = ['features/trainManual.arff', 'features/trainBow.arff', 'features/trainCluster.arff', 'features/trainDependency.arff']
testFileList = ['features/testManual.arff', 'features/testBow.arff', 'features/testCluster.arff', 'features/testDependency.arff']

trainFeaPath = 'features/trainKitchen.arff'
testFeaPath = 'features/testKitchen.arff'
# K = kitchenSink(trainFileList, trainFeaPath)
# K.genKitchenFeature()
KT =  kitchenSink(testFileList, testFeaPath)
KT.genKitchenFeature()