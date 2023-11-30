#!/usr/bin/env python
import sys

# The Collatz Conjecture states that for any number n, one will always
# converge on 1 if n is halved when it is even and n is tripled plus one
# (3n+1) when it is odd.  For example, a short example is:
#  10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# Usage: collatz.py n [m]
#        to calculate all collatz sequences from n to m
# Matt Jones, 2010-03-31

# A=65
# Calculate and display a collatz hailstone sequence
def collatz(n):
    order = 0
    while n > 1:
        print(n)
        if n % 2:
            n = 3*n + 1
        else:
            n = n / 2
        order = order + 1
    print(n)
    print('Order: ', order)
    return(order)

# The main method just calls the collatz function with an input number or
# range of inputs, depending on if it is called with one parameter or two
maxorder = 0
m = int(sys.argv[1])
if len(sys.argv) > 2:
    n = int(sys.argv[2]) + 1
    for i in range(m, n):
        order = collatz(i)
        if order > maxorder:
            maxorder = order
            sequence = i
else:
    maxorder = collatz(m)
    sequence = m

print("Highest order: n =", sequence, "took", maxorder, "steps.")

