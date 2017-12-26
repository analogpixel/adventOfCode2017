def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   


b = 109300
c = 126300
h=0

for bb in range(b, c + 1, 17):
  if not is_prime(bb):
    h += 1
    print("%d,%d" %(h, bb))

print(h)