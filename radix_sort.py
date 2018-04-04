import math

array = [2, 65, 34, 145, 6754, 123, 1787, 3498, 6, 476]

def sort(array, radix=10):
  if len(array) == 0:
    return array

  minValue = array[0];
  maxValue = array[0];
  for i in range(1, len(array)):
    if array[i] < minValue:
      minValue = array[i]
    elif array[i] > maxValue:
      maxValue = array[i]

  # Perform counting sort on each exponent/digit, starting at the least
  # significant digit
  exponent = 1
  while (maxValue - minValue) / exponent >= 1:
    array = countingSortByDigit(array, radix, exponent, minValue)
    exponent *= radix

  return array

def countingSortByDigit(array, radix, exponent, minValue):
  bucketIndex = -1
  buckets = [0] * radix
  output = [None] * len(array)

  # Count frequencies
  for i in range(0, len(array)):
    bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
    buckets[bucketIndex] += 1

  # Compute cumulates
  for i in range(1, radix):
    buckets[i] += buckets[i - 1]

  # Move records
  for i in range(len(array) - 1, -1, -1):
    bucketIndex = math.floor(((array[i] - minValue) / exponent) % radix)
    buckets[bucketIndex] -= 1
    output[buckets[bucketIndex]] = array[i]

  return output
print(sort(array))

### http://www.growingwiththeweb.com/sorting/radix-sort-lsd/ was used as a reference for much of this code
