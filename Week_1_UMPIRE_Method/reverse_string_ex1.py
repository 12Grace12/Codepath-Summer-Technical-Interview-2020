'''
Write a function that reverses a string.

Example:
Input: "hello"
Output: "olleh"

'''

def reverse(s):
  string = ""
  for i in s:
    string = i + string
  return string
# Edge case 1 
a = ""
print(a)
print(reverse(a))

#Edge case 2 with space
s = "Hello Grace"
print(s)
print(reverse(s))

#Edge case 3 with number
b = "G438W"
print(b)
print(reverse(b))

