#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Correct Winner: Ben")
print("--------------------")

print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Correct Winner: Ben")
print("--------------------")

print("Winner: {}".format(isWinner(0, [4, 3])))
print("Correct Winner: None")
print("--------------------")

print("Winner: {}".format(isWinner(5, [1, 2, 3, 4, 5])))
print("Correct Winner: Ben")
print("--------------------")

print("Winner: {}".format(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2])))
print("Correct Winner: Maria")
print("--------------------")

print("Winner: {}".format(isWinner(4, [11, 30, 1, 7])))
print("Correct Winner: Ben")
print("--------------------")

print("Winner: {}".format(isWinner(6, [1, 1, 0, 0, 1, 8])))
print("Correct Winner: Ben")
print("--------------------")

print("Winner: {}".format(isWinner(1, [1])))
print("Correct Winner: Ben")
print("--------------------")

print("Winner: {}".format(isWinner(0, [0])))
print("Correct Winner: None")
print("--------------------")

print("Winner: {}".format(isWinner(-1, [10])))
print("Correct Winner: None")
print("--------------------")

