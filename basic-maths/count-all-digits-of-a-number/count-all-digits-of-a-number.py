// Problem: Count all Digits of a Number
// Category: Basic Maths
// Difficulty: Easy
// Link: https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number?category=beginner-problem&subcategory=basic-maths&tab=submissions
// Solved: 2026-06-30
//
// You are given an integer n. You need to return the number of digits in the number.The number will have no leading zeroes, except when the number is 0 itself.

class Solution:
    def countDigit(self, n):
        if n == 0:
            return 1
        
        count = 0

        while n > 0:
            
            count = count + 1
            n = n//10
        return count



