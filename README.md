# CLT-demo
---
**Overview**

This repository contains materials and information related to a classroom demonstration of the Central Limit Theorem (CLT) using a simple M&M experiment. The purpose of this presentation is to illustrate how the CLT works and why it's important in statistics. This README will provide an overview of the experiment and its objective.

---
**Presentation Objective**

The primary objective of this presentation is to demonstrate the Central Limit Theorem, a fundamental concept in statistics. The CLT states that, regardless of the shape of the original population distribution, the distribution of the sample means approaches a normal distribution as the sample size increases. This experiment uses M&M candies to visually show this concept.

---
**Experiment Details**

**Materials Needed**

A large jar or bag of M&M candies (with a variety of colors).
A classroom or group of participants.
Writing materials (markers, whiteboard, or paper) for data collection.

**Experiment Procedure**

Start by introducing the Central Limit Theorem and its significance in statistics. Explain that the CLT allows us to make inferences about a population by examining the distribution of sample means.

Distribute a handful of M&M candies to each participant in the class. The number of candies in each sample can vary, but it's important to ensure that each sample is randomly selected and that the sample sizes are not too large.

Ask each participant to count the number of blue M&M candies in their sample and calculate the proportion of blue M&Ms to the total number of candies in their sample.

Collect and record the proportions of blue M&Ms for each participant. This data will represent your sample means.

Plot the sample means in a histogram or bar chart. As the number of samples increases, you should observe that the distribution of sample means approximates a normal distribution.

Discuss the results with the class, emphasizing how the CLT works and how it allows us to draw conclusions about the population even if the original distribution of M&M colors is not normal.

You can calculate and display key statistics of the sample means, such as the mean and standard deviation, to highlight how they align with a normal distribution.

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

**CLT_real_data.py** demonstrated the Central Limit Theorem on a real-life dataset.
