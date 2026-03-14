import time
import os

def clear_screen():
    """清屏函数，兼容Windows和Unix系统"""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    """倒计时核心函数"""
    while seconds > 0:
        clear_screen()
        print(f"⏳ 剩余时间: {seconds} 秒")
        time.sleep(1)
        seconds -= 1
    clear_screen()
    print("🎉 时间到！")

def main():
    """主函数：获取用户输入并启动倒计时"""
    while True:
        try:
            user_input = input("请输入倒计时秒数（正整数）：")
            seconds = int(user_input)
            
            if seconds <= 0:
                print("❌ 错误：请输入一个正整数！")
                continue
            
            countdown(seconds)
            break
            
        except ValueError:
            print("❌ 错误：输入无效！请输入数字。")

if __name__ == "__main__":
    main()
