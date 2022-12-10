# 导入 Tkinter、MoviePy 和 os 库
import tkinter as tk
from moviepy.editor import VideoFileClip
import os

# 创建 Tkinter 窗口
window = tk.Tk()

# 创建一个文本框，用于输入视频文件名
entry = tk.Entry(window)
entry.pack()

# 定义提取音频的函数
def extract_audio():
    # 读取视频文件
    video_file = entry.get()
    clip = VideoFileClip(video_file)

    # 提取视频中的音频
    audio = clip.audio

    # 获取视频文件的名称和扩展名
    video_name, video_ext = os.path.splitext(video_file)

    # 保存音频到本地文件，文件名为视频文件的名称
    audio.write_audiofile(video_name + ".mp3")
    
# 创建一个按钮
button = tk.Button(window, text="Extract Audio", command=extract_audio)
button.pack()



# 运行窗口
window.mainloop()
