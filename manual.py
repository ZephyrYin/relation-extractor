__author__ = 'zephyrYin'
import re

class RelationExtractor:
    def __init__(self):
        self.ruleCnt = 5
        self.rules = [re.compile(r) for r in ['(.*?)\sgraduate.*\sin','(.*?)\sstudy.*\sin','(.*?)\semigrate.*\sto','(.*?)\sborn.*\sin','(.*?)\seducated.*\sin']]
    def extractor(self, str):
        matchList = []
        for i in range(len(self.rules)):
            r = self.rules[i]
            if r.match(str) != None:
               matchList.append(i)
        return matchList

    def genFeature(self):
        file = open('train.tsv')
        lines = file.readlines()
        file.close()
        file = open('test.tsv')
        lines = lines + file.readlines()
        file.close()

        features = []
        for line in lines:
            feature = [0, 0, 0, 0, 0]
            institution, person, snippet, intermediate_text, judgment = line.split("\t")
            judgment = judgment.strip()
            mList = self.extractor(intermediate_text)
            for i in mList:
                feature[i] = feature[i] + 1
            feature.append(judgment)
            features.append(feature)
        trainFeatures = features[:6000]
        testFeatures = features[6000:]
        self.writeFeatureToFile(trainFeatures, 'features/trainManual.arff')
        self.writeFeatureToFile(testFeatures, 'features/testManual.arff')

    def writeFeatureToFile(self, features, path):
        instanceCnt = len(features)
        featureDimension = len(features[0]) - 1
        file = open(path, 'w')
        file.write('@RELATION institutions' + '\n')
        for i in range(featureDimension):
            file.write('@ATTRIBUTE token_' + str(i) + ' INTEGER' + '\n')
        file.write('@ATTRIBUTE class {yes,no}' + '\n\n' + '@DATA' + '\n')
        for i in range(instanceCnt):
            file.write('{')
            for j in range(featureDimension):
                if features[i][j] == 0:
                    continue
                file.write(str(j) + ' ' + str(features[i][j]) + ',')
            file.write(str(featureDimension + 1) + ' ' + features[i][featureDimension])
            file.write('}' + '\n')

    def allZero(self, L):
        for item in L:
            if not item == 0:
                return False
        return True