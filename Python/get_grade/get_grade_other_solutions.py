def get_grade(s1, s2, s3):
    """Grade book
       Complete the function so that it finds the average of the three scores passed to it and returns
       the letter value associated with that grade."""
    percentage = ((s1 + s2 + s3) / 300) * 100
    if 90 <= percentage <= 100:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    elif 0 <= percentage < 60:
        return "F"

print(get_grade(95, 90, 93))
print(get_grade(60, 82, 76))
print(get_grade(58, 59, 60))