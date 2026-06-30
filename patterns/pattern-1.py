// Problem: Pattern 1
// Category: Patterns
// Link: https://takeuforward.org/plus/dsa/problems/pattern-1?subject=dsa&sidebar=open&tab=submissions
// Solved: 2026-06-30

class Solution:
    def pattern1(self, n):
        for i in range(n):
            
            # Inner loop will run for columns.
            for j in range(n):
                print("*", end="")
                
            """ As soon as N stars are printed, move
            to the next row and give a line break."""
            print()