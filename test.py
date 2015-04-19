__author__ = 'zephyrYin'
import copy



def getPermutations(list):
    if len(list) <2:
        return list
    result = []
    permutations(list, result, 0)
    return result



def permutations(list, result, cur):
    if cur >= len(list):
        result.append(copy.deepcopy(list))
        return
    for i in range(cur, len(list)):
        list[cur], list[i] = list[i], list[cur]
        permutations(list, result, cur+1)
        list[cur], list[i] = list[i], list[cur]

list = ['1','2','3']

#print getPermutations(list)

# line = 'food(21)'
# left = line.index('(')
# right = line.index(')')
# line = line[0:left+1] + list[0] + line[right:len(line)]
# print line

lines = [[1,2,3],[4,5,6],[7,8,9]]
lines[1] = ['232']
print lines
