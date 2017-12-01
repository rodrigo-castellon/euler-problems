from __future__ import division
import ast
import math

word_file = open('words.txt','r')

word_contents = word_file.read()

words = ast.literal_eval(word_contents)

def convert_alpha(word_input):
	return [ord(char) - 96 for char in word_input.lower()]

def t(n):
	return (n*(n+1))/2

def tri(word):
	nums = convert_alpha(word)
	return sum(nums)

tri_list = [t(n) for n in range(99999)]

triangle_words = 0
for i, word in enumerate(words):
	if tri(word) in tri_list:
		triangle_words += 1
print(triangle_words)
