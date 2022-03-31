class Solution:
    def sortSentence(self, s: str) -> str:
        s1 = s.split()
        for i in range(len(s1)):
            for j in range(len(s1)-1):
                if int(s1[j][-1]) > int(s1[j+1][-1]):
                    temp = s1[j]
                    s1[j] = s1[j+1]
                    s1[j+1] = temp
        sentence = ''
        for i in range(len(s1)-1):
            sentence = sentence + s1[i][:-1] + ' '
        sentence = sentence + s1[-1][:-1]
        return sentence