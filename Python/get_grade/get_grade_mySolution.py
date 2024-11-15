def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')


print(get_grade(95, 90, 93))
print(get_grade(60, 82, 76))
print(get_grade(58, 59, 60))