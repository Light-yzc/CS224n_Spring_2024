# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0
    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    with open(r"D:\Code\CS244n\a4\student\vanilla.nopretrain.test.predictions", 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'London' in line:
                accuracy += 1 / len(lines)

    pass
    ### END YOUR CODE ###

    return accuracy * 100

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
