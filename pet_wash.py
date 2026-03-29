# 宠物清洗小程序
# 功能：根据宠物类型生成随机清洗方案
# 适合新手学习的 Python 原生代码示例

import random  # 导入随机模块，用于生成随机方案


def get_wash_steps(pet_type):
    """
    获取指定宠物类型的清洗步骤库
    参数：pet_type - 宠物类型（猫咪/狗狗/小型宠物）
    返回：该类型宠物的清洗步骤列表
    """
    steps_database = {
        "猫咪": [
            "1. 安抚情绪，戴上伊丽莎白圈",
            "2. 梳理毛发，去除打结",
            "3. 温水湿润全身（避开头部）",
            "4. 涂抹猫咪专用沐浴露",
            "5. 轻柔按摩后彻底冲洗",
            "6. 用吸水毛巾包裹擦干",
            "7. 低温吹风机吹干（保持安全距离）"
        ],
        "狗狗": [
            "1. 梳理毛发，检查皮肤状况",
            "2. 温水从背部开始冲洗",
            "3. 使用犬用沐浴露清洗全身",
            "4. 重点清洁爪子和腹部",
            "5. 彻底冲洗避免残留",
            "6. 毛巾擦干多余水分",
            "7. 吹风机吹干并梳理造型"
        ],
        "小型宠物": [
            "1. 准备浅盆温水（约35℃）",
            "2. 轻柔放入水中适应",
            "3. 用手或软刷轻洗",
            "4. 快速冲洗避免着凉",
            "5. 柔软毛巾轻轻吸干",
            "6. 保暖环境下自然晾干"
        ]
    }
    return steps_database.get(pet_type, [])


def get_random_duration(pet_type):
    """
    生成随机清洗时长
    参数：pet_type - 宠物类型
    返回：随机时长（分钟）
    """
    duration_ranges = {
        "猫咪": (25, 45),      # 猫咪较难控制，时间波动大
        "狗狗": (30, 60),      # 狗狗根据体型差异
        "小型宠物": (15, 25)   # 小型宠物清洗较快
    }
    min_time, max_time = duration_ranges.get(pet_type, (20, 40))
    return random.randint(min_time, max_time)


def get_random_tips(pet_type):
    """
    获取随机温馨提示
    参数：pet_type - 宠物类型
    返回：随机选择的提示语
    """
    tips_database = {
        "猫咪": [
            "💡 提示：洗前剪指甲可防止被抓伤",
            "💡 提示：选择猫咪放松的时间段进行",
            "💡 提示：水温以手腕内侧试温，38-40℃为宜",
            "💡 提示：洗后给予零食奖励，建立正面联想"
        ],
        "狗狗": [
            "💡 提示：洗前让狗狗排便，避免中途打断",
            "💡 提示：耳内塞棉花球防止进水",
            "💡 提示：选择狗狗运动后较累时更易配合",
            "💡 提示：定期清洗可预防皮肤病"
        ],
        "小型宠物": [
            "💡 提示：水位不宜超过宠物腹部",
            "💡 提示：动作要轻柔，避免惊吓",
            "💡 提示：洗后注意保暖，防止感冒",
            "💡 提示：过于频繁清洗会破坏皮肤油脂"
        ]
    }
    tips_list = tips_database.get(pet_type, ["💡 提示：请温柔对待您的小宠物"])
    return random.choice(tips_list)


def generate_wash_plan(pet_type):
    """
    生成完整的清洗方案
    参数：pet_type - 宠物类型
    返回：包含步骤、时长、提示的字典
    """
    steps = get_wash_steps(pet_type)
    duration = get_random_duration(pet_type)
    tip = get_random_tips(pet_type)
    
    return {
        "type": pet_type,
        "steps": steps,
        "duration": duration,
        "tip": tip
    }


def display_plan(plan):
    """
    格式化输出清洗方案
    参数：plan - 清洗方案字典
    """
    print("\n" + "=" * 40)
    print(f"        🐾 {plan['type']}清洗方案 🐾")
    print("=" * 40)
    
    print(f"\n⏱️  预计时长：{plan['duration']} 分钟")
    print("\n📋 清洗步骤：")
    
    for step in plan['steps']:
        print(f"   {step}")
    
    print(f"\n{plan['tip']}")
    print("=" * 40)


def show_menu():
    """
    显示主菜单
    """
    print("\n" + "=" * 40)
    print("        🛁 宠物清洗小助手 🛁")
    print("=" * 40)
    print("\n请选择宠物类型：")
    print("   1. 猫咪")
    print("   2. 狗狗")
    print("   3. 小型宠物（仓鼠/兔子/龙猫等）")
    print("   0. 退出程序")
    print("-" * 40)


def get_pet_type(choice):
    """
    将用户选择转换为宠物类型
    参数：choice - 用户输入的选项
    返回：对应的宠物类型字符串，无效返回 None
    """
    type_map = {
        "1": "猫咪",
        "2": "狗狗",
        "3": "小型宠物",
        "猫咪": "猫咪",
        "猫": "猫咪",
        "狗狗": "狗狗",
        "狗": "狗狗",
        "小型宠物": "小型宠物",
        "小宠物": "小型宠物"
    }
    return type_map.get(choice.strip(), None)


def main():
    """
    主程序循环
    """
    print("欢迎使用宠物清洗小助手！")
    
    while True:
        show_menu()
        user_input = input("请输入选项（0-3）：").strip()
        
        # 退出程序
        if user_input == "0":
            print("\n感谢使用，祝您的宠物健康快乐！🐾")
            break
        
        # 获取宠物类型
        pet_type = get_pet_type(user_input)
        
        # 输入验证
        if pet_type is None:
            print("\n❌ 无效输入，请输入 0-3 或对应的宠物名称")
            continue
        
        # 生成并显示方案
        plan = generate_wash_plan(pet_type)
        display_plan(plan)
        
        # 询问是否继续
        again = input("\n是否继续生成方案？(y/n)：").strip().lower()
        if again not in ["y", "yes", "是", "1"]:
            print("\n感谢使用，祝您的宠物健康快乐！🐾")
            break


# 程序入口
if __name__ == "__main__":
    main()
