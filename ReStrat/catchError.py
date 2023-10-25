try:
    user_weight = float(input("输入您的体重(kg):"))
    user_height = float(input("输入您的身高(kg):"))
    user_BMI = user_weight * user_height ** 2

except ValueError:
    print("❌输入的数字有误, 请输入正确的数字!")