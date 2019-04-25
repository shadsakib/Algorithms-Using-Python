import operator

class Activity:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

n = int(input("Enter number of activity: "))

activities = []
print("Enter starting and ending times: ")
for i in range(n):
    #x, y = input().split(" ")
    x, y = [int(z) for z in input().split(" ")]
    activities.append(Activity(x, y))

sortedActivities = sorted(activities, key=operator.attrgetter('endTime'))

curr = sortedActivities[0]
print("{0} {1}".format(curr.startTime, curr.endTime))

for a in sortedActivities:
    if a.startTime > curr.endTime :
        print("{0} {1}".format(a.startTime, a.endTime))
        curr = a




