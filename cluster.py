__author__ = 'zephyrYin'

class Cluster:
    def __init__(self):
        pass

    def genCluster(self, fileName):
        file = open('paths')
        lines = file.readlines()
        print len(lines)
        dict = {}
        cnt = 0

        keyList = []
        key = -1
        for line in lines:
            cnt = cnt + 1
            items = line.split('\t')
            if items[0] not in keyList:
                keyList.append(items[0])
                key = key + 1
            name = items[1].lower()
            dict[name] = key

# file = open('paths')
# lines = file.readlines()
# print len(lines)
# dict = {}
# cnt = 0
#
# keyList = []
# key = -1
# for line in lines:
#     cnt = cnt + 1
#     items = line.split('\t')
#     if items[0] not in keyList:
#         keyList.append(items[0])
#         key = key + 1
#     name = items[1].lower()
#     dict[name] = key
