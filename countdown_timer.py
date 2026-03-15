# 简易倒计时工具
# 适合新手学习的 Python 小程序

import time  # 导入时间模块，用于实现倒计时功能


def countdown_timer():
    """
    倒计时工具主函数
    功能：获取用户输入的秒数，进行倒计时显示
    """
    print("=" * 30)
    print("       简易倒计时工具")
    print("=" * 30)
    
    # 获取用户输入
    user_input = input("请输入倒计时秒数（正整数）：")
    
    # 处理输入验证
    try:
        # 尝试将输入转换为整数
        seconds = int(user_input)
        
        # 检查是否为正整数
        if seconds <= 0:
            print("错误：请输入大于0的正整数！")
            return
            
    except ValueError:
        # 捕获非数字输入异常
        print("错误：输入无效，请输入一个正整数！")
        return
    
    print(f"\n倒计时开始：{seconds} 秒")
    print("-" * 30)
    
    # 倒计时循环
    for remaining in range(seconds, 0, -1):
        # 在同一行显示剩余时间，用 \r 实现光标回行首
        print(f"\r剩余时间：{remaining:2d} 秒", end="", flush=True)
        # 暂停 1 秒
        time.sleep(1)
    
    # 倒计时结束
    print("\r" + " " * 20)  # 清除当前行
    print("-" * 30)
    print("🎉 时间到！")
    print("=" * 30)


# 程序入口
if __name__ == "__main__":
    countdown_timer()
