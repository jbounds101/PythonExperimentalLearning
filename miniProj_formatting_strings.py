scoresFile = open('miniProg_unsorted_scores.txt', 'r')
lines = scoresFile.readlines()
scores = dict()

for x in lines:
    person = x.split(',')
    name = person[0]
    score = int(person[1])
    scores[name] = score

averageScore = sum(scores.values()) / len(scores)
print('The highest score was {} with {} points'.format(max(scores, key=scores.get), max(scores.values())))
print('The lowest score was {} with {} points'.format(min(scores, key=scores.get), min(scores.values())))
print('The average scores was {:.2f} points'.format(averageScore))

scoresFile.close()
