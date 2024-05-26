target = input('Which positive integer would you like to segment as a sum of distinct Fibs?\n')
target = int(target)
fibs = [0, 1]
while fibs[-1] + fibs[-2] < target:
  fibs.append(fibs[-1] + fibs[-2])
answer = []
while target != 0:
  answer.append(fibs[-1])
  target -= answer[-1]
  fibs = list(filter(lambda x: x <= target, fibs))

print(answer)
