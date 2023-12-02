def f(x):
    return (x**4 / 500) - (x**2 / 200) - (3 / 250)

def g(x):
    return -(x**3 / 30) + (x / 20) + (1 / 6)


top = 19 + (61 / 125)
bottom = -32 - (2 / 3)
left = 2
max_right = 10


total_area = (top - bottom) * (max_right - left)
cut_out = total_area
left_area = 0

precision = 1 / 100000


i = left
while i <= max_right:
    strip_h = f(i) - g(i)
    strip_area = strip_h * precision

    cut_out -= strip_area
    left_area += strip_area

    i += precision


print(total_area, cut_out, left_area)
