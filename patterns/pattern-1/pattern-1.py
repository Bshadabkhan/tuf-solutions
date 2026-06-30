// Problem: Pattern 1
// Category: Patterns
// Difficulty: Easy
// Link: https://takeuforward.org/plus/dsa/problems/pattern-1?subject=dsa&sidebar=open&tab=submissions
// Solved: 2026-06-30
//
// Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:*************************Print the pattern in the function given to you.

class Solution:
    def pattern1(self, n):
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(n):
                print("*", end="")
                
            """ As soon as N stars are printed, move
            to the next row and give a line break."""
            print()