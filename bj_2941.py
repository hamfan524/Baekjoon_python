a = ['c=', 'c-', 'dz=', 'd-', 'lj','nj', 's=', 'z=']

scan = input()

for i in a:
  if i in scan:
    scan = scan.replace(i, 'A')

print(len(scan))

