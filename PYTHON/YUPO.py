def sum_numbers(aa, bb):
    print('aa inside sum='+str(aa))
    return aa+bb






a=30
b=True

print(type(b))

if b:
    print('b is True')
    c=60
    print('a='+str(a))
    print('c='+str(c))

print(c)

print(sum_numbers(58,90))
print('a='+str(a))


if a>=40 and b:
    print('a>=40 and b is True')

d=100 if a>40 else -100
print(d)

b1=True
b2=True

if b1^b2:
    print('xor on b1 and b2 is true')
else:
    print('xor is not true')
#komentarz
#praca domowa: in assigmnets , przez teamsa normalnie, how to check is divide, for loop and if statement
#rest of the division-if a number divides fe by three, or two
c=10 %3
print(c)