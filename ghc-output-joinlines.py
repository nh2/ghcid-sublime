#!/usr/bin/env python3
import sys

input = sys.stdin.readlines()

output = []

for line in map(str.rstrip, input):
  if line.startswith(' '):
    output[-1].append(line)
  else:
    output.append([line])

sys.stdout.write('\n'.join([' '.join([x.strip() for x in lines]) for lines in output]) + '\n')
