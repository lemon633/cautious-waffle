import random
import time

CAT_STEPS = [
    ["梳毛去浮毛", "剪指甲", "温水打湿", "宠物香波按摩", "彻底冲洗", "擦干吹毛"],
    ["检查耳朵眼睛", "梳理打结毛发", "全身打湿", "使用猫用沐浴露", "冲洗干净", "低温吹干", "奖励零食"],
    ["安抚情绪", "修剪脚毛", "温水浸泡", "温和清洁", "多次冲洗", "毛巾擦干", "自然风干"]
]

DOG_STEPS = [
    ["梳毛检查", "修剪爪毛", "打湿全身", "香波清洁", "冲洗泡沫", "吹毛梳理"],
    ["挤肛门腺", "修剪指甲", "温水打湿", "深层清洁", "彻底冲洗", "吹干造型", "奖励互动"],
    ["检查皮肤", "梳理毛发", "打湿身体", "宠物沐浴露", "冲洗干净", "吹干梳毛", "耳朵清洁"]
]

SMALL_PET_STEPS = [
    ["轻轻抱起", "温水擦拭", "专用清洁棉", "擦干身体", "放回笼子"],
    ["检查身体", "局部清洁", "专用洗剂", "擦干保暖", "安抚情绪"],
    ["温柔安抚", "温水清洗", "彻底擦干", "保暖放置", "观察状态"]
]

DURATIONS = {
    "cat": ["15-20分钟", "20-25分钟", "25-30分钟"],
    "dog": ["30-40分钟", "40-50分钟", "50-60分钟"],
    "small": ["10-15分钟", "15-20分钟", "20-25分钟"]
}

TIPS = {
    "cat": [
        "猫咪怕水，请温柔安抚，避免应激反应",
        "使用猫咪专用香波，避免刺激皮肤",
        "注意保护耳朵和眼睛，不要进水",
        "低温吹风，猫咪对噪音敏感"
    ],
    "dog": [
        "狗狗爱动，注意安全固定",
        "彻底冲洗香波，避免残留引起皮肤问题",
        "注意挤肛门腺（新手建议请专业人士）",
        "吹干时注意脚趾缝等死角"
    ],
    "small": [
        "小型宠物体温调节差，注意保暖",
        "动作要轻，避免惊吓",
        "使用小型宠物专用清洁产品",
        "洗完后尽快放回温暖环境"
    ]
}

def get_clean_scheme(pet_type):
    """获取宠物清洗方案"""
    pet_type = pet_type.lower()
    
    if pet_type in ["猫咪", "猫", "cat"]:
        key = "cat"
        steps_list = CAT_STEPS
        name = "猫咪"
    elif pet_type in ["狗狗", "狗", "dog"]:
        key = "dog"
        steps_list = DOG_STEPS
        name = "狗狗"
    elif pet_type in ["小型宠物", "小宠", "small"]:
        key = "small"
        steps_list = SMALL_PET_STEPS
        name = "小型宠物"
    else:
        return None
    
    steps = random.choice(steps_list)
    duration = random.choice(DURATIONS[key])
    tip = random.choice(TIPS[key])
    
    return {
        "name": name,
        "steps": steps,
        "duration": duration,
        "tip": tip
    }

def display_scheme(scheme):
    """显示清洗方案"""
    print("\n" + "="*50)
    print(f"🐾 {scheme['name']} 清洗方案 🐾")
    print("="*50)
    
    print(f"\n⏱️ 预计时长：{scheme['duration']}")
    
    print("\n📋 清洗步骤：")
    for i, step in enumerate(scheme['steps'], 1):
        time.sleep(0.3)
        print(f"   {i}. {step}")
    
    print(f"\n💡 温馨提示：{scheme['tip']}")
    print("="*50 + "\n")

def main():
    """主函数"""
    print("🐶🐱 欢迎使用宠物清洗方案生成器 🐹🐰")
    print("支持宠物类型：猫咪 / 狗狗 / 小型宠物")
    
    while True:
        user_input = input("\n请输入宠物类型（输入'q'退出）：").strip()
        
        if user_input.lower() in ['q', 'quit', '退出']:
            print("感谢使用！再见 👋")
            break
        
        scheme = get_clean_scheme(user_input)
        
        if scheme:
            display_scheme(scheme)
        else:
            print("❌ 无效的宠物类型！")
            print("请输入：猫咪 / 狗狗 / 小型宠物")
            print("也可以输入英文：cat / dog / small")

if __name__ == "__main__":
    main()
