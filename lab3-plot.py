#!/usr/bin/python

import matplotlib.pyplot as plt

dataDir = "./data/"
xPlots = []
yPlots = []

fileHandles = [dataDir + "lr" + str(x) +".txt" for x in range(1, 4)]
handle2 = [dataDir + "rr" + str(x) +".txt" for x in range(1, 4)]
for h in handle2:
    fileHandles.append(h)

for h in fileHandles:
    x = []
    y = []
    f = open(h)
    for line in f:
        data = line.split()
        x.append(int(data[0]))
        y.append(int(data[1]))
    xPlots.append(x)
    yPlots.append(y)

lAvgX = []
for i in range(len(xPlots[0])):
    avg = sum([x[i] for x in xPlots[:3]]) / 3
    lAvgX.append(avg)

lAvgY = []
for i in range(len(yPlots[0])):
    avg = sum([y[i] for y in yPlots[:3]]) / 3
    lAvgY.append(avg)

rAvgX = []
for i in range(len(xPlots[0])):
    avg = sum([x[i] for x in xPlots[3:]]) / 3
    rAvgX.append(avg)

rAvgY = []
for i in range(len(yPlots[0])):
    avg = sum([y[i] for y in yPlots[3:]]) / 3
    rAvgY.append(avg)

print(len(xPlots))
print(len(xPlots[0]))
fig, axs = plt.subplots(2)
colorCode = ['ro', 'yo', 'bo']
for i in range(3):
    axs[0].plot(xPlots[i], yPlots[i], colorCode[i], label = 'Left Turn Plot' + str(i+1))
    axs[1].plot(xPlots[i+3], yPlots[i+3], colorCode[i], label = 'Right Turn Plot' + str(i+1))

axs[0].plot(lAvgX, lAvgY, 'm^', label = "Corner Avg")
axs[1].plot(rAvgX, rAvgY, 'm^', label = "Corner Avg")


left = True
for a in axs:
    a.set(title = ("Left Turn Calibration"if left else "Right Turn Calibration"),
xlabel = "mm from Start(x)",
ylabel = "mm from Start(y)")
    a.axhline(y = 0)
    a.axvline(x = 0)
    a.legend(loc = 2)
    left = False


plt.show()