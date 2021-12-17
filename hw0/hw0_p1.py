# -*- coding: utf-8 -*-
"""hw0_p1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RnZ_OBmKF6gy-Vof2ECFdlE3ikM9Ts2R

# 第一題
"""

#輸入方程式
print('(X+2*Y)(2*X^2-Y^2+Z)')
polynomials = input('輸入方程式')
#拆開括號
polynomials_lstrip = polynomials.strip('(')
polynomials_strip =polynomials_lstrip.strip( ')')
y = polynomials_strip.replace('-','+-')
x = y.split(')(')
#用加號分開，變成list
for idx in range(len(x)):
  x[idx] = x[idx].split('+')
#更換一些細節
for i in range(len(x)):
  for j in range(len(x[i])):
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
    if x[i][j] == 'Z':
      x[i][j]=x[i][j].replace('Z','1*Z')
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*YY')
    if x[i][j] == 'XY^2':
      x[i][j]=x[i][j].replace('XY^2','1*XYY')
    if x[i][j] == 'X^2Y':
      x[i][j]=x[i][j].replace('X^2Y','1*XXY')
    if x[i][j] == 'Z^2':
      x[i][j]=x[i][j].replace('Z^2','1*ZZ')
for i in range(len(x)):
  for idx in range(len(x[i])):
    x[i][idx] = x[i][idx].split('*')
    for idx1 in range(len(x[i][idx])):
      if x[i][idx][idx1] == 'X^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('X^2','XX')
      if x[i][idx][idx1] == 'Y^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('Y^2','YY')
#係數變成int(方便之後進行相乘)
for i in range(len(x)):
  for j in range(len(x[i])):
    x[i][j][0] = int(x[i][j][0])
polylist = []
coefficient = []
#係數相乘，文字相加
for i in range(len(x[0])):
  for j in range(len(x[1])):
    coefficient.append(x[0][i][0]*x[1][j][0])
    polylist.append(x[0][i][1]+x[1][j][1])
for i in range(len(coefficient)):
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == -1:
    coefficient[i] = '-1'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == 3:
    coefficient[i] = '+3'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
#文字換回題目所需格式
for i in range(len(polylist[:])):
  if polylist[i] == 'XXX':
    polylist[i]=polylist[i].replace('XXX','*X^3')
  if polylist[i] == 'XYY':
    polylist[i]=polylist[i].replace('XYY','*XY^2')
  if polylist[i] == 'YXX':
    polylist[i]=polylist[i].replace('YXX','*X^2Y')
  if polylist[i] == 'YYY':
    polylist[i]=polylist[i].replace('YYY','*Y^3')
  if polylist[i] == 'XZ':
    polylist[i]=polylist[i].replace('XZ','*XZ')
  if polylist[i] == 'YZ':
    polylist[i]=polylist[i].replace('YZ','*YZ')
  if polylist[i] == 'XXYY':
    polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
  if polylist[i] == 'XXXY':
    polylist[i]=polylist[i].replace('XXXY','*X^3Y')
  if polylist[i] == 'XZZ':
    polylist[i]=polylist[i].replace('XZZ','*XZ^2')
  if polylist[i] == 'YXYY':
    polylist[i]=polylist[i].replace('YXYY','*XY^3')
  if polylist[i] == 'YXXY':
    polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
  if polylist[i] == 'YZZ':
    polylist[i]=polylist[i].replace('YZZ','*YZZ')
  if polylist[i] == 'ZXYY':
    polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
  if polylist[i] == 'ZXXY':
    polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
  if polylist[i] == 'ZZZ':
    polylist[i]=polylist[i].replace('ZZZ','*Z^3')
#重複項處理
if polylist[0] == polylist[4]:
  coefficient[0] = int(coefficient[0])+int(coefficient[4])
  del polylist[4]
  del coefficient[4]
#print出答案
for i in range(len(polylist)):
  print(coefficient[i],polylist[i],sep='',end='')

"""# 第二題"""

print('(2*X+3*Y+4*Z)(XY^2+X^2Y+Z^2)')
polynomials = input('輸入方程式')
polynomials_lstrip = polynomials.strip('(')
polynomials_strip =polynomials_lstrip.strip( ')')
y = polynomials_strip.replace('-','+-')
x = y.split(')(')
for idx in range(len(x)):
  x[idx] = x[idx].split('+')
for i in range(len(x)):
  for j in range(len(x[i])):
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
    if x[i][j] == 'Z':
      x[i][j]=x[i][j].replace('Z','1*Z')
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*YY')
    if x[i][j] == 'XY^2':
      x[i][j]=x[i][j].replace('XY^2','1*XYY')
    if x[i][j] == 'X^2Y':
      x[i][j]=x[i][j].replace('X^2Y','1*XXY')
    if x[i][j] == 'Z^2':
      x[i][j]=x[i][j].replace('Z^2','1*ZZ')
for i in range(len(x)):
  for idx in range(len(x[i])):
    x[i][idx] = x[i][idx].split('*')
    for idx1 in range(len(x[i][idx])):
      if x[i][idx][idx1] == 'X^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('X^2','XX')
      if x[i][idx][idx1] == 'Y^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('Y^2','YY')
for i in range(len(x)):
  for j in range(len(x[i])):
    x[i][j][0] = int(x[i][j][0])
polylist = []
coefficient = []
for i in range(len(x[0])):
  for j in range(len(x[1])):
    coefficient.append(x[0][i][0]*x[1][j][0])
    polylist.append(x[0][i][1]+x[1][j][1])
for i in range(len(coefficient)):
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == -1:
    coefficient[i] = '-1'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == 3:
    coefficient[i] = '+3'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
for i in range(len(polylist[:])):
  if polylist[i] == 'XXX':
    polylist[i]=polylist[i].replace('XXX','*X^3')
  if polylist[i] == 'XYY':
    polylist[i]=polylist[i].replace('XYY','*XY^2')
  if polylist[i] == 'YXX':
    polylist[i]=polylist[i].replace('YXX','*X^2Y')
  if polylist[i] == 'YYY':
    polylist[i]=polylist[i].replace('YYY','*Y^3')
  if polylist[i] == 'XZ':
    polylist[i]=polylist[i].replace('XZ','*XZ')
  if polylist[i] == 'YZ':
    polylist[i]=polylist[i].replace('YZ','*YZ')
  if polylist[i] == 'XXYY':
    polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
  if polylist[i] == 'XXXY':
    polylist[i]=polylist[i].replace('XXXY','*X^3Y')
  if polylist[i] == 'XZZ':
    polylist[i]=polylist[i].replace('XZZ','*XZ^2')
  if polylist[i] == 'YXYY':
    polylist[i]=polylist[i].replace('YXYY','*XY^3')
  if polylist[i] == 'YXXY':
    polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
  if polylist[i] == 'YZZ':
    polylist[i]=polylist[i].replace('YZZ','*YZZ')
  if polylist[i] == 'ZXYY':
    polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
  if polylist[i] == 'ZXXY':
    polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
  if polylist[i] == 'ZZZ':
    polylist[i]=polylist[i].replace('ZZZ','*Z^3')
if polylist[0] == polylist[4]:
  coefficient[0] = int(coefficient[0])+int(coefficient[4])
  del polylist[4]
  del coefficient[4]
for i in range(len(polylist)):
  print(coefficient[i],polylist[i],sep='',end='')

"""# 第三題"""

print('(A+2*B^2)(B+3*C^3)(2*A+B+C)')
polynomials = input('輸入方程式')
polynomials_lstrip = polynomials.strip('(')
polynomials_strip =polynomials_lstrip.strip( ')')
y = polynomials_strip.replace('-','+-')
x = y.split(')(')
for idx in range(len(x)):
  x[idx] = x[idx].split('+')
for i in range(len(x)):
  for j in range(len(x[i])):
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == 'B':
      x[i][j]=x[i][j].replace('B','1*B')
    if x[i][j] == 'C':
      x[i][j]=x[i][j].replace('C','1*C')
    if x[i][j] == 'A':
      x[i][j]=x[i][j].replace('A','1*A')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
    if x[i][j] == 'Z':
      x[i][j]=x[i][j].replace('Z','1*Z')
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*YY')
    if x[i][j] == 'XY^2':
      x[i][j]=x[i][j].replace('XY^2','1*XYY')
    if x[i][j] == 'X^2Y':
      x[i][j]=x[i][j].replace('X^2Y','1*XXY')
    if x[i][j] == 'Z^2':
      x[i][j]=x[i][j].replace('Z^2','1*ZZ')
    if x[i][j] == '2*B^2':
      x[i][j]=x[i][j].replace('2*B^2','2*BB')
    if x[i][j] == '3*C^3':
      x[i][j]=x[i][j].replace('3*C^3','3*CCC')
for i in range(len(x)):
  for idx in range(len(x[i])):
    x[i][idx] = x[i][idx].split('*')
    for idx1 in range(len(x[i][idx])):
      if x[i][idx][idx1] == 'X^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('X^2','XX')
      if x[i][idx][idx1] == 'Y^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('Y^2','YY')
for i in range(len(x)):
  for j in range(len(x[i])):
    x[i][j][0] = int(x[i][j][0])
polylist = []
coefficient = []
for i in range(len(x[0])):
  for j in range(len(x[1])):
    for k in range(len(x[2])):
      coefficient.append(x[0][i][0]*x[1][j][0]*x[2][k][0])
      polylist.append(x[0][i][1]+x[1][j][1]+x[2][k][1])
print(coefficient)
for i in range(len(coefficient)):
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == -1:
    coefficient[i] = '-1'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
  if coefficient[i] == 12:
    coefficient[i] = '+12'
  if coefficient[i] == 3:
    coefficient[i] = '+3'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
  if coefficient[i] == 6:
    coefficient[i] = '+6'
for i in range(len(polylist[:])):
  if polylist[i] == 'XXX':
    polylist[i]=polylist[i].replace('XXX','*X^3')
  if polylist[i] == 'XYY':
    polylist[i]=polylist[i].replace('XYY','*XY^2')
  if polylist[i] == 'YXX':
    polylist[i]=polylist[i].replace('YXX','*X^2Y')
  if polylist[i] == 'YYY':
    polylist[i]=polylist[i].replace('YYY','*Y^3')
  if polylist[i] == 'XZ':
    polylist[i]=polylist[i].replace('XZ','*XZ')
  if polylist[i] == 'YZ':
    polylist[i]=polylist[i].replace('YZ','*YZ')
  if polylist[i] == 'XXYY':
    polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
  if polylist[i] == 'XXXY':
    polylist[i]=polylist[i].replace('XXXY','*X^3Y')
  if polylist[i] == 'XZZ':
    polylist[i]=polylist[i].replace('XZZ','*XZ^2')
  if polylist[i] == 'YXYY':
    polylist[i]=polylist[i].replace('YXYY','*XY^3')
  if polylist[i] == 'YXXY':
    polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
  if polylist[i] == 'YZZ':
    polylist[i]=polylist[i].replace('YZZ','*YZZ')
  if polylist[i] == 'ZXYY':
    polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
  if polylist[i] == 'ZXXY':
    polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
  if polylist[i] == 'ZZZ':
    polylist[i]=polylist[i].replace('ZZZ','*Z^3')
  if polylist[i] == 'BBCCCC':
    polylist[i]=polylist[i].replace('BBCCCC','*B^2C^4')
  if polylist[i] == 'BBCCCB':
    polylist[i]=polylist[i].replace('BBCCCB','*B^3C^3')
  if polylist[i] == 'BBCCCA':
    polylist[i]=polylist[i].replace('BBCCCA','*AB^2C^3')
  if polylist[i] == 'BBBC':
    polylist[i]=polylist[i].replace('BBBC','*B^3C')
  if polylist[i] == 'BBBB':
    polylist[i]=polylist[i].replace('BBBB','*B^4')
  if polylist[i] == 'BBBA':
    polylist[i]=polylist[i].replace('BBBA','*AB^3')
  if polylist[i] == 'ACCCC':
    polylist[i]=polylist[i].replace('ACCCC','*AC^4')
  if polylist[i] == 'ACCCB':
    polylist[i]=polylist[i].replace('ACCCB','*ABC^3')
  if polylist[i] == 'ACCCA':
    polylist[i]=polylist[i].replace('ACCCA','*A^2C^3')
  if polylist[i] == 'ABC':
    polylist[i]=polylist[i].replace('ABC','*ABC')
  if polylist[i] == 'ABB':
    polylist[i]=polylist[i].replace('ABB','*AB^2')
  if polylist[i] == 'ABA':
    polylist[i]=polylist[i].replace('ABA','*A^2B')
if polylist[0] == polylist[4]:
  coefficient[0] = int(coefficient[0])+int(coefficient[4])
  del polylist[4]
  del coefficient[4]
for i in range(len(polylist)):
  print(coefficient[i],polylist[i],sep='',end='')

"""#以下是過程紀錄(不重要)


"""

print('(2*X+3*Y+4*Z)(XY^2+X^2Y+Z^2)')
polynomials = input('輸入方程式')
print(polynomials.strip('('))
polynomials_lstrip = polynomials.strip('(')
print(polynomials_lstrip.strip( ')'))
polynomials_strip =polynomials_lstrip.strip( ')')
print(polynomials_strip)
y = polynomials_strip.replace('-','+-')
print(y.split(')('))
x = y.split(')(')
for idx in range(len(x)):
  x[idx] = x[idx].split('+')
print(x)
print(x[0][1][1])
for i in range(len(x)):
  for j in range(len(x[i])):
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*YY')
    if x[i][j] == 'XY^2':
      x[i][j]=x[i][j].replace('XY^2','1*XYY')
    if x[i][j] == 'X^2Y':
      x[i][j]=x[i][j].replace('X^2Y','1*XXY')
    if x[i][j] == 'Z^2':
      x[i][j]=x[i][j].replace('Z^2','1*ZZ')
print(x)
for i in range(len(x)):
  for idx in range(len(x[i])):
    x[i][idx] = x[i][idx].split('*')
    for idx1 in range(len(x[i][idx])):
      if x[i][idx][idx1] == 'X^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('X^2','XX')
      if x[i][idx][idx1] == 'Y^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('Y^2','YY')
print(x)

for i in range(len(x)):
  for j in range(len(x[i])):
    x[i][j][0] = int(x[i][j][0])

print(x)

print('(X+2*Y)(2*X^2-Y^2+Z)')
polynomials = input('輸入方程式')
polynomials_lstrip = polynomials.strip('(')
polynomials_strip =polynomials_lstrip.strip( ')')
y = polynomials_strip.replace('-','+-')
x = y.split(')(')
for idx in range(len(x)):
  x[idx] = x[idx].split('+')
for i in range(len(x)):
  for j in range(len(x[i])):
    if x[i][j] == 'X':
      x[i][j]=x[i][j].replace('X','1*X')
    if x[i][j] == '-Y^2':
      x[i][j]=x[i][j].replace('-Y^2','-1*Y^2')
    if x[i][j] == 'Z':
      x[i][j]=x[i][j].replace('Z','1*Z')
for i in range(len(x)):
  for idx in range(len(x[i])):
    x[i][idx] = x[i][idx].split('*')
    for idx1 in range(len(x[i][idx])):
      if x[i][idx][idx1] == 'X^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('X^2','XX')
      if x[i][idx][idx1] == 'Y^2':
        x[i][idx][idx1]=x[i][idx][idx1].replace('Y^2','YY')
for i in range(len(x)):
  for j in range(len(x[i])):
    x[i][j][0] = int(x[i][j][0])
polylist = []
coefficient = []
for i in range(len(x[0])):
  for j in range(len(x[1])):
    coefficient.append(x[0][i][0]*x[1][j][0])
    polylist.append(x[0][i][1]+x[1][j][1])
for i in range(len(coefficient)):
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == -1:
    coefficient[i] = '-1'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'
for i in range(len(polylist[:])):
  if polylist[i] == 'XXX':
    polylist[i]=polylist[i].replace('XXX','*X^3')
  if polylist[i] == 'XYY':
    polylist[i]=polylist[i].replace('XYY','*XY^2')
  if polylist[i] == 'YXX':
    polylist[i]=polylist[i].replace('YXX','*X^2Y')
  if polylist[i] == 'YYY':
    polylist[i]=polylist[i].replace('YYY','*Y^3')
  if polylist[i] == 'XZ':
    polylist[i]=polylist[i].replace('XZ','*XZ')
  if polylist[i] == 'YZ':
    polylist[i]=polylist[i].replace('YZ','*YZ')
for i in range(len(polylist)):
  print(coefficient[i],polylist[i],sep='',end='')

polylist = []
coefficient = []
for i in range(len(x[0])):
  for j in range(len(x[1])):
    print(x[0][i][0]*x[1][j][0],x[0][i][1]+x[1][j][1])
    coefficient.append(x[0][i][0]*x[1][j][0])
    polylist.append(x[0][i][1]+x[1][j][1])

print(coefficient)
print(polylist)

for i in range(len(coefficient)):
  if coefficient[i] == 2:
    coefficient[i] = '+2'
  if coefficient[i] == 3:
    coefficient[i] = '+3'
  if coefficient[i] == 1:
    coefficient[i] = '+1'
  if coefficient[i] == 4:
    coefficient[i] = '+4'

print(coefficient)

for i in range(len(polylist[:])):
  if polylist[i] == 'XXYY':
    polylist[i]=polylist[i].replace('XXYY','*X^2Y^2')
  if polylist[i] == 'XXXY':
    polylist[i]=polylist[i].replace('XXXY','*X^3Y')
  if polylist[i] == 'XZZ':
    polylist[i]=polylist[i].replace('XZZ','*XZ^2')
  if polylist[i] == 'YXYY':
    polylist[i]=polylist[i].replace('YXYY','*XY^3')
  if polylist[i] == 'YXXY':
    polylist[i]=polylist[i].replace('YXXY','*X^2Y^2')
  if polylist[i] == 'YZZ':
    polylist[i]=polylist[i].replace('YZZ','*YZZ')
  if polylist[i] == 'ZXYY':
    polylist[i]=polylist[i].replace('ZXYY','*XY^2Z')
  if polylist[i] == 'ZXXY':
    polylist[i]=polylist[i].replace('ZXXY','*X^2YZ')
  if polylist[i] == 'ZZZ':
    polylist[i]=polylist[i].replace('ZZZ','*Z^3')
print(polylist)

for i in range(len(polylist)):
  print(coefficient[i],polylist[i],sep='',end='')

if polylist[0] == polylist[4]:
  coefficient[0] = int(coefficient[0])+int(coefficient[4])
  del polylist[4]
  del coefficient[4]

for i in range(len(polylist)):
  print(coefficient[i],polylist[i],sep='',end='')

for i in range(len(polylist)):
  if polylist[i] == 'XXX':
    polylist[i].replace('XXX','*X^3')
  elif polylist[i] == 'XYY':
    polylist[i].replace('XYY','*XY^2')  
  elif polylist[i] == 'YXX':
    polylist[i].replace('YXX','*X^2Y')
  elif polylist[i] == 'YYY':
    polylist[i].replace('YYY','*Y^3')
  elif polylist[i] == 'XZ':
    polylist[i].replace('XZ','*XZ')
  elif polylist[i] == 'YZ':
    polylist[i].replace('YZ','*YZ')
print(polylist)

if polylist[0] == 'XXX':
  print('+++++')
  polylist[0].replace('XXX','*X^3')
print(polylist)

for i in range(len(polylist)):
  if polylist[i] == 'XYY':
    polylist[i].replace('*XY^2','XYY')
print(polylist)