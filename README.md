# Functions and generator practice

### **Exercise 1**

Create a generator `fact_gen()` that generates factorials. For a number n, n factorial is denoted by n!, and it is the product of all positive integers less than or equal to n. For example,

> 5! = 5 * 4 * 3 * 2 * 1 = 120

Define `prod(a, b)` which returns the product of numbers a and b. You will also define `fact_gen()` which yields the next factorial number.


### **Exercise 2**
In the next exercise, you will write a function that checks sudoku squares for correctness.

Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. For this question we will generalize and simplify the game.

Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

A valid sudoku square satisfies these two properties:

Each column of the square contains each of the whole numbers from 1 to n exactly once.

Each row of the square contains each of the whole numbers from 1 to n exactly once.

You may assume that the input is square and contains at least one row and column.

