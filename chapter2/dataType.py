import fractions

print(type(5))
print(12 + 30000000000000)
print(type(1.5))
print(type(1 + 1j))
print(7 / 3 * 3)
print(type(1 / 3))

# coerce int to float
int_num = 45
float_num = float(int_num)
print(float_num)

# coerce float to int
float_num2 = 78.8
int_num2 = int(float_num2)
print(int_num2)
# int() will truncate float not round

# Floating point numbers's accuracy is finite
float_num3 = 0.123456789123456789123
print(float_num3)

# Python isn’t limited to integers and floating point numbers.
# It can also do all the fancy math you learned in high school
# to use fraction ne
x = fractions.Fraction(1, 3)  # 结果1/3
y = x * 2 + x * 2  # 结果1/4
print(y)


def is_it_true(anything):
    if anything:
        print("Yes I'm true")
    else:
        print("Yes I'm false")


is_it_true(fractions.Fraction(4 / 5))
is_it_true(fractions.Fraction(0 / 5))

# List in python can contain items of the different type

# create a list
s_list = ['a', 'b', 'shen', 'example']
for i in s_list:
    print(i, end=' ')
print()

# slice a list
print(s_list[0:-1])
print(s_list[0:4])
print(s_list[-1:])

# add item to list
a_list = ['a']
a_list = a_list + ['4', '8', '78']
print(a_list)
a_list.append('14')
print(a_list)
a_list.insert(0, '145')
print(a_list)
a_list.extend(['four', 'one'])
print(a_list)
