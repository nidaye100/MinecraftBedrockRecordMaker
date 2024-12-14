import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import json

# 获取自定义音效名称
def get_sound_events():
    sound_events = []
    
    # 询问用户输入音效数量
    try:
        num_sounds = simpledialog.askinteger("输入", "请输入需要添加的音效数量（正整数）：", minvalue=1, maxvalue=100)
        if not num_sounds:
            return sound_events  # 用户取消输入时返回空列表
    except ValueError:
        messagebox.showerror("错误", "请输入一个有效的数字！")
        return sound_events

    # 循环输入每个音效的名称
    for i in range(num_sounds):
        while True:
            sound_name = simpledialog.askstring(
                "输入", 
                f"请输入第 {i + 1} 个音效的名称（只能使用英文、小写字母、数字、下划线，例如：my_song_{i + 1}\n注意，items.json 中的 sound_event 字段 和 sounds.json 中的声音事件 必须一致。）："
            )
            if not sound_name:  # 如果用户取消输入，停止
                return sound_events

            # 验证音效名称是否符合规范
            if sound_name.isidentifier() and sound_name.islower():
                sound_events.append(sound_name)
                break
            else:
                messagebox.showerror(
                    "名称不合法", 
                    "请确保名称仅包含英文、小写字母、数字或下划线，且不能包含空格或其他特殊字符。"
                )

    return sound_events

# 构建 sounds.json 的内容
def generate_sounds_json(sound_events):
    sounds_data = {}
    for sound in sound_events:
        sounds_data[f"custom.{sound}"] = {
            "sounds": [
                {
                    "name": f"custom/{sound}",
                    "stream": True
                }
            ]
        }
    return sounds_data

# 保存 sounds.json 文件
def save_sounds_json(sounds_data):
    # 选择保存文件路径
    save_path = filedialog.asksaveasfilename(
        title="选择保存位置",
        filetypes=[("JSON 文件", "*.json")],
        defaultextension=".json",
        initialfile="sounds.json"
    )
    if not save_path:
        messagebox.showwarning("取消", "未选择保存位置，操作已取消。")
        return

    # 保存文件
    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(sounds_data, f, indent=4)
        messagebox.showinfo("成功", f"sounds.json 文件已保存到:\n{save_path}")
    except Exception as e:
        messagebox.showerror("错误", f"保存文件时发生错误：{e}")

# 主程序
def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    messagebox.showinfo("欢迎", "欢迎使用 sounds.json 生成器！")

    # 获取用户输入的音效名称
    sound_events = get_sound_events()
    if not sound_events:
        messagebox.showwarning("警告", "未输入任何音效名称，程序结束。")
        return

    # 生成 sounds.json 数据
    sounds_data = generate_sounds_json(sound_events)

    # 保存 sounds.json 文件
    save_sounds_json(sounds_data)

if __name__ == "__main__":
    main()
