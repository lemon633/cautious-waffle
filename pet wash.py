import random

# 宠物类型配置
PET_TYPES = {
    "1": "猫咪",
    "2": "狗狗",
    "3": "小型宠物"
}

# 各宠物的清洗步骤库
WASH_STEPS = {
    "猫咪": [
        ["1. 轻柔梳理毛发", "2. 用温水湿润全身", "3. 涂抹猫咪专用沐浴露", "4. 轻轻揉搓起泡", "5. 彻底冲洗干净", "6. 用毛巾包裹吸水", "7. 低温吹干毛发"],
        ["1. 安抚情绪", "2. 剪指甲防抓伤", "3. 温水浸湿毛发", "4. 使用无香沐浴露", "5. 快速清洗避免应激", "6. 毛巾擦干", "7. 自然风干或低温吹干"],
        ["1. 准备防滑垫", "2. 温水淋湿", "3. 涂抹温和洗剂", "4. 顺毛轻揉", "5. 冲净泡沫", "6. 吸水毛巾包裹", "7. 吹风机低档吹干"]
    ],
    "狗狗": [
        ["1. 梳理打结毛发", "2. 棉球塞耳防水", "3. 温水淋湿全身", "4. 涂抹狗狗沐浴露", "5. 全身揉搓清洁", "6. 彻底冲洗", "7. 毛巾擦干后吹干"],
        ["1. 检查皮肤状况", "2. 梳毛去浮毛", "3. 温水湿润", "4. 涂抹洗毛液", "5. 按摩清洁", "6. 冲洗干净", "7. 吹干并梳理"],
        ["1. 戴好项圈牵引", "2. 温水冲洗", "3. 使用狗狗专用香波", "4. 重点清洁四肢", "5. 冲净泡沫", "6. 擦干水分", "7. 完全吹干防感冒"]
    ],
    "小型宠物": [
        ["1. 准备小盆温水", "2. 轻轻放入宠物", "3. 涂抹小宠专用洗剂", "4. 快速轻柔清洗", "5. 温水冲净", "6. 毛巾轻轻包裹", "7. 自然晾干或暖风吹干"],
        ["1. 检查宠物状态", "2. 准备适宜水温", "3. 局部湿润", "4. 少量洗剂轻揉", "5. 快速冲洗", "6. 吸水纸巾擦干", "7. 保暖静置"],
        ["1. 固定好宠物", "2. 温水喷雾湿润", "3. 涂抹温和洗剂", "4. 指腹轻揉", "5. 喷水冲洗", "6. 干毛巾吸水", "7. 低温吹干或晾干"]
    ]
}

# 各宠物的清洗时长库
WASH_DURATION = {
    "猫咪": ["约15-20分钟", "约20-25分钟", "约10-15分钟"],
    "狗狗": ["约30-40分钟", "约25-35分钟", "约35-45分钟"],
    "小型宠物": ["约10-15分钟", "约5-10分钟", "约15-20分钟"]
}

# 各宠物的温馨提示库
TIPS = {
    "猫咪": [
        "猫咪怕水，动作要轻柔快速，避免应激反应",
        "洗前先剪指甲，防止被抓伤",
        "水温控制在37-38度，接近猫咪体温",
        "避免水进入耳朵和眼睛",
        "洗后给予零食奖励，建立正面联想"
    ],
    "狗狗": [
        "洗前先散步排便，避免洗澡时紧张",
        "水温控制在35-38度为宜",
        "注意清洁脚掌和肛门周围",
        "吹干时要彻底，防止皮肤病",
        "大型犬建议两人配合清洗"
    ],
    "小型宠物": [
        "动作要非常轻柔，小型宠物骨骼脆弱",
        "水温不宜过高，30-35度即可",
        "清洗时间不宜过长，避免着凉",
        "洗后注意保暖，放在温暖处",
        "部分小宠（如仓鼠）不建议水洗，可用浴沙"
    ]
}


def show_welcome():
    """显示欢迎界面"""
    print("=" * 50)
    print("       🐾 宠物清洗方案生成器 🐾")
    print("=" * 50)
    print("\n请选择您的宠物类型：")
    for key, name in PET_TYPES.items():
        print(f"  [{key}] {name}")
    print("  [0] 退出程序")
    print("-" * 50)


def get_pet_choice():
    """获取用户选择的宠物类型"""
    while True:
        choice = input("\n请输入选项编号：").strip()
        
        if choice == "0":
            return None
        elif choice in PET_TYPES:
            return PET_TYPES[choice]
        else:
            print("❌ 无效选项，请输入 1-3 或 0 退出")


def generate_wash_plan(pet_type):
    """生成随机清洗方案"""
    # 随机选择清洗步骤
    steps = random.choice(WASH_STEPS[pet_type])
    # 随机选择清洗时长
    duration = random.choice(WASH_DURATION[pet_type])
    # 随机选择2条温馨提示
    tips = random.sample(TIPS[pet_type], 2)
    
    return steps, duration, tips


def display_wash_plan(pet_type, steps, duration, tips):
    """显示清洗方案"""
    print("\n" + "=" * 50)
    print(f"       🛁 {pet_type}清洗方案 🛁")
    print("=" * 50)
    
    print(f"\n【清洗时长】{duration}")
    
    print("\n【清洗步骤】")
    for step in steps:
        print(f"  {step}")
    
    print("\n【温馨提示】")
    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")
    
    print("\n" + "-" * 50)
    print("祝您的宠物洗澡愉快！✨")


def main():
    """主程序"""
    while True:
        show_welcome()
        pet_type = get_pet_choice()
        
        if pet_type is None:
            print("\n感谢使用，再见！👋")
            break
        
        steps, duration, tips = generate_wash_plan(pet_type)
        display_wash_plan(pet_type, steps, duration, tips)
        
        # 询问是否继续
        continue_choice = input("\n是否继续为其他宠物生成方案？(y/n)：").strip().lower()
        if continue_choice != 'y':
            print("\n感谢使用，再见！👋")
            break


if __name__ == "__main__":
    main()