import numpy as np
import matplotlib.pyplot as plt

pic = plt.imread("84.png")
arr = np.array(pic)

block_size = 100
num_blocks_wide = 30
num_blocks_high = 10

result = np.zeros((num_blocks_high, num_blocks_wide))

for i in range(num_blocks_high):
    for j in range(num_blocks_wide):
        block = arr[
            i * block_size : (i + 1) * block_size,
            j
            * block_size : (j + 1)
            * block_size,  # i is starting row for block, i + 1 ending row for the block, j is starting column for block, j + 1 is ending column for the block.
            # We multiply times block_size to jump to next block (e.g. first block is 100:100, 100:100, second block is 200:200, 200:200, so we skip 100 pixels to get to the next block.)
        ]
        mean_value = np.mean(block)
        result[i, j] = mean_value

plt.imshow(result)
plt.show()
