import winreg
from datetime import datetime

def get_current_date():
    """
    获取当前日期并格式化为月/日/年的格式，无前导零。
    返回格式：月/日/年
    """
    current_date = datetime.now()
    month = current_date.month  # 月份，无前导零
    day = current_date.day      # 日期，无前导零
    year = current_date.year    # 年份，四位数
    return f"{month}/{day}/{year}"

def modify_registry(key_path, value_name, value_data, value_type):
    """
    修改注册表键值
    :param key_path: 注册表键的路径，例如 r"SOFTWARE\MyApp"
    :param value_name: 要修改的值的名称
    :param value_data: 要设置的值
    :param value_type: 值的类型，例如 winreg.REG_SZ (字符串), winreg.REG_DWORD (整数) 等
    """
    try:
        # 打开注册表键（如果不存在则会报错）
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as registry:
            with winreg.OpenKey(registry, key_path, 0, winreg.KEY_SET_VALUE) as key:
                # 修改键值
                winreg.SetValueEx(key, value_name, 0, value_type, value_data)
                return
                print(f"成功修改注册表键值：{key_path}\\{value_name}")
    except PermissionError:
        return
        print("权限不足，无法修改注册表。")
    except FileNotFoundError:
        return
        print("指定的注册表键或路径不存在。")
    except Exception as e:
        return
        print(f"发生错误：{e}")

# 示例：修改注册表
modify_registry("SOFTWARE\\Typora", "IDate", get_current_date(), winreg.REG_SZ)