#!/usr/bin/env python
# coding: utf-8

# # Task 2:
# a. 70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours. What is the expected number of distinct colours in 20 randomly picked balls?
# ___

# # Solution

# First of all, need to know what is its binomial coefficient:
# \begin{equation}
#    \binom {n}{k} = \frac{n!}{(n - k)!k!}
# \end{equation}
# 
# For this formula I use function binom from scipy

from scipy.special import binom

color = 7 # number of each unique color
num_balls_cl = 10 # number of balls for each unique color
cl_balls = 70 # all balls
picked = 20 # number of randomly picked balls


# First I calculate probability for each color from 7 color
# 
# Let's culculate probability the probability that 20 out of 70 will be pr_a
# 
# the probability that 20 out of 70 are actually taken from a set of only 60 balls will be pr_b

pr_a = binom(cl_balls, picked)
pr_b = binom(cl_balls - num_balls_cl, picked)


# the probability that this color was picked and opposite

pr = (pr_b/pr_a)
probability = 1 - pr


# Now probability for 7 colors

result = 7 * probability
print('Answer =', result)

