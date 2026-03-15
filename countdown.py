import time

def countdown():
    """
    简易倒计时工具
    功能：用户输入秒数，程序进行倒计时并在结束时提示
    """
    
    # 获取用户输入
    user_input = input("请输入倒计时秒数（正整数）：")
    
    try:
        # 尝试将输入转换为整数
        seconds = int(user_input)
        
        # 检查是否为正整数
        if seconds <= 0:
            print("请输入大于0的正整数！")
            return
        
        # 开始倒计时
        while seconds > 0:
            # 显示剩余时间（\r 让光标回到行首实现原地刷新）
            print(f"剩余时间：{seconds} 秒", end="\r")
            time.sleep(1)  # 暂停1秒
            seconds -= 1
        
        # 倒计时结束
        print(" " * 20, end="\r")  # 清除上一行显示
        print("时间到！")
        
    except ValueError:
        # 处理非数字输入
        print("输入无效，请输入一个正整数！")

# 程序入口
if __name__ == "__main__":
    countdown()