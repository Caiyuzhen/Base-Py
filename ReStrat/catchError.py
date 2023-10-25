try:
    user_weight = float(input("输入您的体重(kg):"))
    user_height = float(input("输入您的身高(kg):"))
    user_BMI = user_weight / user_height ** 2

except ValueError: # 捕捉值的错误
    print("❌输入的数字有误, 请输入正确的数字!")

except ZeroDivisionError: # 除 0 错误
    print("❌身高不能为 0 , 请重新输入正确的数字!")

except:
    print("❌发生了未知错误！")
    
else:
    print("您的 BMI 值为:" + str(user_BMI))
    
finally:
    print("程序结束运行～")