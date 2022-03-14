from sys import stdin, stdout
N = stdin.readline()
str_n = set(stdin.readline().split())
M = stdin.readline()
str_m = stdin.readline().split()

for i in str_m:
  if i in str_n:
    stdout.write('1\n')
  else:
    stdout.write('0\n')