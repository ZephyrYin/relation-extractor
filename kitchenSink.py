__author__ = 'zephyros'

class kitchenSink:
    def __init__(self, fileList, path = 'kitchen.arff'):
        self.fileList = fileList
        self.outputPath = path

    def genKitchenFeature(self):
        self.combineFiles(self.fileList, self.outputPath)

    def readFromFile(self, path):
        file = open(path)
        lines = file.readlines()
        dataIndex = lines.index('@DATA\n')
        attributeLines = lines[0:dataIndex-1]
        dataLines = lines[dataIndex+1 : len(lines)]
        dataLines = [d.strip('\n') for d in dataLines]
        dataList = []
        for dataLine in dataLines:
            dL = dataLine[1:-1].split(',')
            temp = []
            for d in dL:
                d = d.split(' ')
                tuple = [int(d[0]), d[1]]
                temp.append(tuple)
            dataList.append(temp)
        return len(attributeLines) - 1, dataList
    
    def combineTwoFeatures(self, fA, fB):
        featureDimenA = fA[0]
        featuresA = fA[1]
        featureDimenB = fB[0]
        featuresB = fB[1]
        if not len(featuresA) == len(featuresB):
            print 'instance number do not match'
            return
        featureDimen = featureDimenA + featureDimenB - 1        # eliminate label
        features = []
        for i in range(len(featuresA)):
            features.append(featuresA[i][0:-1] + [[B[0] + featureDimenA-1, B[1]] for B in featuresB[i]])
        return featureDimen, features        

    def combineFiles(self, fileList, outputPath):
        if len(fileList) < 2:
            return
        pass
        featureDimen, features = self.readFromFile(fileList[0])
        for i in range(1,len(fileList)):
            dimen, fea = self.readFromFile(fileList[i])
            print dimen, len(fea)
            featureDimen, features = self.combineTwoFeatures([featureDimen, features], [dimen, fea])
        file = open(outputPath, 'w')
        file.write('@RELATION institutions')
        file.write('\n')
        for i in range(featureDimen -1 ):
            file.write('@ATTRIBUTE token_' + str(i) + ' INTEGER')
            file.write('\n')
        file.write('@ATTRIBUTE class {yes,no}')
        file.write('\n\n')

        file.write('@DATA' + '\n')
        for feature in features:
            file.write('{')
            for j in range(len(feature)):
                file.write(str(feature[j][0]) + ' ')
                file.write(feature[j][1])
                if not j == len(feature) - 1:
                    file.write(',')
            file.write('}')
            file.write('\n')
        print featureDimen,len(features)
        return featureDimen, features

