import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title("Text Display")

# 创建文本显示区域
text_area = tk.Text(window, height=10)
text_area.pack()

# 创建下方部分的容器
bottom_frame = tk.Frame(window)
bottom_frame.pack()

# 创建三个输入框
input_box1 = tk.Text(bottom_frame, height=5)
input_box1.pack(side=tk.LEFT, padx=10, pady=10)

input_box2 = tk.Text(bottom_frame, height=5)
input_box2.pack(side=tk.LEFT, padx=10, pady=10)

input_box3 = tk.Text(bottom_frame, height=5)
input_box3.pack(side=tk.LEFT, padx=10, pady=10)

# 创建三个按钮
def button1_clicked():
    text = input_box1.get("1.0", tk.END)
    text_area.insert(tk.END, f"Button 1 Clicked: {text}\n")

button1 = tk.Button(bottom_frame, text="Button 1", command=button1_clicked)
button1.pack(side=tk.LEFT, padx=10)

def button2_clicked():
    text = input_box2.get("1.0", tk.END)
    text_area.insert(tk.END, f"Button 2 Clicked: {text}\n")

button2 = tk.Button(bottom_frame, text="Button 2", command=button2_clicked)
button2.pack(side=tk.LEFT, padx=10)

def button3_clicked():
    text = input_box3.get("1.0", tk.END)
    text_area.insert(tk.END, f"Button 3 Clicked: {text}\n")

button3 = tk.Button(bottom_frame, text="Button 3", command=button3_clicked)
button3.pack(side=tk.LEFT, padx=10)

# 运行主循环
window.mainloop()