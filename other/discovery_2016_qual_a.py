w = int(input())
word = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'

for _ in range(len(word)//w+1):
    if word == '':
        break
    print(word[0:w])
    word = word[w:]
