# CLT-demo
---
**CLT_simple_demo.py** demonstrates the Central Limit Theorem (CLT) and visualizes probability distributions using random number generation and matplotlib. It includes two main functions:

**animate_clt(func):** This function simulates the Central Limit Theorem. It generates random samples of 10 numbers using the provided func (a random number generation function) and calculates the average of each sample. It repeats this process 200 times, storing the averages in a list y. The script then plots a histogram of the averages, updating the plot for each iteration, demonstrating the convergence to a normal distribution as per the Central Limit Theorem.

**animate_dist(func):** This function simulates a probability distribution. It generates random numbers using the provided func and stores them in the list y. It repeats this process 100 times, updating a histogram of the generated values on each iteration. This function is used to visualize a specific probability distribution.

**Usage**
To use this code, you can follow these steps:

Import the required libraries at the beginning of your script, including numpy, random, and matplotlib.

Define your custom random number generation functions. In this code, diceroll, and coinflip simulate dice rolls and coin flips, while time_to_exam simulates a Poisson distribution for the time until an event (e.g., time until an exam).

Call either animate_clt or animate_dist, passing one of your custom random number generation functions as an argument. These functions will simulate the experiment and update the visualization accordingly.

Run your script to observe the animated histograms that show the behavior of the chosen experiment.

---
