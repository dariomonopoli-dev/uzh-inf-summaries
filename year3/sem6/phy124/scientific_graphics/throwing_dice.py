import numpy as np
import matplotlib.pyplot as plt

fyle = open("dice.txt", "r")
lines = fyle.readlines()
fyle.close()
sums = []
for line in lines:
    line = line.strip().split(" ")
    for i, el in enumerate(line):
        line[i] = int(el)

    sums.append(sum(line))


repetitions = sums[:100]

x = range(1, len(repetitions) + 1)

plt.plot(x, repetitions)
plt.xlabel("Repetition")
plt.ylabel("Sum of 3 Dice")
plt.title("Sum of 3 Dice vs Repetition")
plt.show()


plt.figure()
plt.hist(sums, edgecolor="black", bins=range(3, 19))
plt.xlabel("Sum of 3 Dice")
plt.ylabel("Frequency")
plt.title("Distribution of Sum of 3 Dice")
plt.show()


bin_values, bin_edges, _ = plt.hist(
    sums, edgecolor="black", bins=range(3, 19)
)  # unpack the return values
bin_centers = (
    bin_edges[:-1] + np.diff(bin_edges) / 2
)  # calculate center points of bins (np.diff calculates the difference between consecutive elements)
bin_entries = np.sqrt(bin_values)

plt.errorbar(bin_centers, bin_values, xerr=0.5, yerr=bin_entries, fmt="o")
plt.xlabel("Sum of 3 Dice")
plt.ylabel("Frequency")
plt.title("Distribution of Sum of 3 Dice")
plt.show()
