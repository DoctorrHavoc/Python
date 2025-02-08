def distance(num1, num2, num3):
    close_diff = 1
    far_diff = 2

    if abs(num2-num1) <= close_diff and abs(num3-num1) >= far_diff and abs(num3-num2) >= far_diff:
        return True

    if abs(num3-num1) <= close_diff and abs(num2-num1) >= far_diff and abs(num2-num3) >= far_diff:
        return True

    return False
