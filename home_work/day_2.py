def max_num(a, b, c):
    return max[a, b, c]

print(max_num(19, 420, 777))

def mult_list(n):
    total = 1
    for x in n:
        total *= x
    return total
Lst= [2, 5, 4]
print (mult_list(Lst))

def rev_string(string):
    return string[::-1]

print(rev_string('hello'))

def num_within(a, b, c):
    if a in range(b, c+1):
        return True
    else:
        return False
print(num_within(3, 4, 6))

def pascal(n):
  triangle = [[1],[1,1]]
  if n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
    
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    for row in triangle:
      print(row)

print(pascal(6))

