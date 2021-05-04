string = "abbc"

dict = {}

for s in string:
    if s in dict:
        print("repeat")
        break
    dict[s] = 1


print("non repeat")







# def countLevelUpPlayers(cutOffRank, num, scores):     
#     scores.sort(reverse = True)
#     count = 1
#     ranks = []
#     ranks.append(1)
#     currRank = 1
#     maxScore = scores[0]
    
#     if cutOffRank == 0:
#         return 0
#     elif cutOffRank > num:
#         return 0
#     elif num >= 100000:
#         return "Size of input too large"
    
#     for i in range(1,num):
#         if scores[i] > 0:
#             if scores[i] == maxScore:
#                 ranks.append(currRank)
#                 if currRank <= cutOffRank:
#                     count += 1
#             else:
#                 ranks.append(i+1)
#                 currRank = i + 1
#                 maxScore = scores[i]
#                 if currRank <= cutOffRank:
#                     count += 1
#     return count