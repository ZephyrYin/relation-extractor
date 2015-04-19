__author__ = 'zephyros'

class evaluate:
    def __init__(self, pre, test):
        self.predictions = [p.strip('\t').strip('\n') for p in pre]
        self.test = [t.strip('\t').strip('\n') for t in test]
        self.evaluation = []

    def getEvaluation(self):
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for i in range(len(self.predictions)):
            if self.predictions[i].lower() == 'yes':
                if self.test[i].lower() == 'yes':
                    TP = TP + 1
                else:
                    FP = FP + 1
            else:
                if self.test[i].lower() == 'yes':
                    FN = FN + 1
                else:
                    TN = TN + 1
        print TP,FP,TN,FN
        if TP == 0:
            precision = 0
            recall = 0
        else:
            precision = float(TP)/(TP + FP)
            recall = float(TP)/(TP + FN)
        if precision == 0 and recall == 0:
            F1 = 0
        else:
            F1 = 2*recall*precision/(recall + precision)

        return [precision, recall, F1]