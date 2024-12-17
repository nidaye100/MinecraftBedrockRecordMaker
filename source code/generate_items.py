import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import json

# 询问基岩版版本并显示警告
def ask_version_warning():
    version = simpledialog.askstring("警告", "请输入你的基岩版 Minecraft 版本号（例如：1.16.100）。\n此程序仅适用于基岩版。")
    if version:
        messagebox.showwarning("警告", "程序将为基岩版生成配置，请确保你输入了完整的版本号。\n如若输入错误请关掉程序并尝试重新启动。")
    else:
        messagebox.showerror("错误", "未输入有效的版本号，程序将退出。")
        exit()

# 获取歌曲数量和歌曲数据
def get_song_data():
    songs = []
    # 询问用户输入歌曲的数量
    num_songs = simpledialog.askinteger("输入", "你想添加多少首歌？", minvalue=1, maxvalue=10)
    if not num_songs:
        return songs  # 用户取消或输入无效时，返回空列表
    
    for i in range(num_songs):
        song_name = simpledialog.askstring("输入", f"歌曲 {i + 1} 的标识符 (可以随便写，只要确保与其他歌曲标识符不重复。\n这个标识符在程序内部是用来区分不同的歌曲，因此它必须是唯一的。\n例如：my_song_{i + 1})：")
        if not song_name:
            break  # 如果用户取消输入，则停止
        # 提示用户输入歌曲的声音事件标识符
        sound_event = simpledialog.askstring("输入", f"歌曲 {i + 1} 的声音事件 (声音事件指的是在 Minecraft 资源包中用来播放声音的文件名。\n它通常对应于资源包中的音频文件和游戏中的音效事件。\n声音事件通常是以 custom. 开头的字符串，后面跟随自定义的名称。\n例如，你可以定义一个声音事件custom.{song_name}，然后在资源包的 sounds.json 文件中为这个事件指定音频文件。)：")
        record_id = simpledialog.askstring("输入", f"歌曲 {i + 1} 的物品标识符 (物品标识符 就是物品的 ID，是 Minecraft 内部用于识别和引用物品的标识符。\n你可以根据需要自定义物品 ID，但要确保每个物品的 ID 唯一。\n例如：custom:my_record_{i + 1})：")
        
        # 保存每首歌的信息
        songs.append({
            "song_name": song_name,
            "sound_event": sound_event,
            "record_id": record_id
        })
    
    return songs

# 生成 JSON 数据
def generate_json(songs):
    items = []
    for song in songs:
        item = {
            "format_version": "1.16.100",  # Minecraft JSON格式版本
            "minecraft:item": {
                "description": {
                    "identifier": song["record_id"],  # 唯一标识符
                    "category": "items"  # 物品类别
                },
                "components": {
                    "minecraft:max_stack_size": 1,  # 堆叠数量限制
                    "minecraft:record": {
                        "sound_event": song["sound_event"]  # 对应的声音事件
                    }
                }
            }
        }
        items.append(item)
    return items

# 保存 JSON 文件
def save_json_file(data):
    # 弹出保存文件对话框
    save_path = filedialog.asksaveasfilename(
        title="选择保存路径",
        filetypes=[("JSON 文件", "*.json")],
        defaultextension=".json"
    )
    if save_path:
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("成功", f"JSON 配置已保存为:\n{save_path}")
        except Exception as e:
            messagebox.showerror("错误", f"保存文件时发生错误: {e}")
    else:
        messagebox.showwarning("取消", "未选择保存路径，操作已取消。")

# 主程序
def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 提示用户基岩版版本和警告
    ask_version_warning()

    # 获取歌曲数据
    songs = get_song_data()
    if songs:
        # 生成 JSON 数据
        json_data = generate_json(songs)
        
        # 弹出保存文件对话框
        save_json_file(json_data)
    else:
        messagebox.showwarning("警告", "没有输入任何歌曲信息，程序结束。")

if __name__ == "__main__":
    main()
