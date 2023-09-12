import json
import tkinter as tk
import queue
from tkinter import messagebox
import pyttsx3

TIMES = 0


def get_word_pronunciation(word):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 设置语速，可根据需要进行调整
    engine.setProperty('volume', 0.8)  # 设置音量，可根据需要进行调整
    engine.say(word)
    engine.runAndWait()


def load_data():
    global TIMES
    # 读配置文件
    config = []
    with open('./myfile/config.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            config.append(int(line.strip().split(':')[1]))
    if config[0] == 0:
        words = read_unfamiliar(config[1])
    else:
        words = read_familiar(config[0])
        TIMES = config[0]
    return words


def read_unfamiliar(form=1):
    words = {}
    lines = []
    word = []
    if form==1:
        with open('./myfile/unfamiliar.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line != '\n':
                    word.append(line.strip())
                if len(word) == 5:
                    lines.append(word)
                    word = []
        for w in lines:
            wo, tra = w[0].split(': ')
            words[wo] = {}
            words[wo]['translate'] = tra
            words[wo]['right_time'] = 0
            words[wo]['sentences'] = []
            words[wo]['sentences'].append([w[1], w[2]])
            words[wo]['sentences'].append([w[3], w[4]])
    elif form==2:
        with open('./myfile/unfamiliar1.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line != '\n':
                    word.append(line.strip())
                if len(word) == 5:
                    lines.append(word)
                    word = []
        for w in lines:
            wo= w[0].split(':')[0]
            words[wo] = {}
            words[wo]['translate'] = w[1].split(': ')[1]
            words[wo]['right_time'] = 0
            words[wo]['sentences'] = []
            words[wo]['sentences'].append([w[3], '暂无中文翻译'])
            words[wo]['sentences'].append([w[4], '暂无中文翻译'])
    return words


def read_familiar(times):
    with open("./myfile/time_{}.json".format(times), "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def generate_sent(words):
    torem = []
    for k, v in words.items():
        sent = words[k]['sentences']
        for s in sent:
            s.append(k)
            torem.append(s)

    my_queue = queue.Queue()

    # 使用列表初始化队列
    for item in torem:
        my_queue.put(item)
    return my_queue


def on_entry_focus_in1(event):
    if input_box1.get() == '请输入单词':
        input_box1.delete(0, tk.END)
        input_box1.configure(foreground='black')


def on_entry_focus_out1(event):
    if input_box1.get() == '':
        input_box1.insert(0, '请输入单词')
        input_box1.configure(foreground='gray')


def on_entry_focus_in2(event):
    if input_box2.get() == '请输入翻译':
        input_box2.delete(0, tk.END)
        input_box2.configure(foreground='black')


def on_entry_focus_out2(event):
    if input_box2.get() == '':
        input_box2.insert(0, '请输入翻译')
        input_box2.configure(foreground='gray')


def button1_clicked():
    global WORD
    global sent
    # 获取输入框中的内容
    input_text = input_box1.get()
    # 判断输入框是否为空
    if input_text.strip() == "":
        messagebox.showinfo("提示", "输入框为空")
    else:
        words[WORD]['right_time'] += 1
        try:
            sent = torem.get(block=False)
            WORD = sent[2]
            text_area.config(state=tk.NORMAL)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, sent[0] + "\n")
            text_area.config(state=tk.DISABLED)
        except queue.Empty:
            text_area.config(state=tk.NORMAL)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, '已完成本部分全部内容的复习' + "\n")
            text_area.config(state=tk.DISABLED)
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")

    # 清空输入框
    input_box1.delete(0, tk.END)


def button2_clicked():
    global WORD
    global sent
    # 获取输入框中的内容
    input_text = input_box1.get()
    # 判断输入框是否为空
    if input_text.strip() == "":
        messagebox.showinfo("提示", "输入框为空")
    else:
        try:
            sent = torem.get(block=False)
            WORD = sent[2]
            text_area.config(state=tk.NORMAL)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, sent[0] + "\n")
            text_area.config(state=tk.DISABLED)
        except queue.Empty:
            text_area.config(state=tk.NORMAL)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, '已完成本部分全部内容的复习' + "\n")
            text_area.config(state=tk.DISABLED)
            button1.config(state="disabled")
            button2.config(state="disabled")
            button3.config(state="disabled")
            button4.config(state="disabled")

    # 清空输入框
    input_box1.delete(0, tk.END)


def button3_clicked():
    get_word_pronunciation(sent[0])


def button4_clicked():
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, sent[1] + "\n")
    text_area.insert(tk.END, WORD + ':' + words[WORD]['translate'] + "\n")
    text_area.config(state=tk.DISABLED)


def close():
    global words
    dict1 = {k: v for k, v in words.items() if v['right_time'] == TIMES}
    dict2 = {k: v for k, v in words.items() if v['right_time'] == TIMES + 1}
    dict3 = {k: v for k, v in words.items() if v['right_time'] == TIMES + 2}

    print(dict1)
    print(dict2)

    with open("./myfile/time_{}.json".format(TIMES), "w", encoding='utf-8') as f1:
        d1=json.dumps(dict1, ensure_ascii=False)
        f1.write(d1)
    with open("./myfile/time_{}.json".format(TIMES + 1), "w", encoding='utf-8') as f2:
        d2 = json.dumps(dict2, ensure_ascii=False)
        f2.write(d2)
    with open("./myfile/time_{}.json".format(TIMES + 2), "w", encoding='utf-8') as f3:
        d3 = json.dumps(dict3, ensure_ascii=False)
        f3.write(d3)



    window.destroy()


if __name__ == '__main__':
    words = load_data()
    torem = generate_sent(words)

    # 创建主窗口
    window = tk.Tk()
    window.title("Text Display")

    # 创建文本显示区域
    text_area = tk.Text(window, font=("Arial", 18), height=10, state=tk.DISABLED)
    text_area.pack()

    sent = torem.get()
    WORD = sent[2]
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, sent[0] + "\n")  # 在文本显示区域末尾插入文本
    text_area.config(state=tk.DISABLED)

    # 创建下方部分的容器
    bottom_frame = tk.Frame(window)
    bottom_frame.pack()

    # 创建两个输入框
    input_box1 = tk.Entry(bottom_frame, width=30)
    input_box1.pack(side=tk.LEFT, padx=10, pady=10)
    input_box1.insert(0, '请输入单词')
    input_box1.bind('<FocusIn>', on_entry_focus_in1)
    input_box1.bind('<FocusOut>', on_entry_focus_out1)

    input_box2 = tk.Entry(bottom_frame, width=30)
    input_box2.pack(side=tk.LEFT, padx=10, pady=10)
    input_box2.insert(0, '请输入翻译')
    input_box2.bind('<FocusIn>', on_entry_focus_in2)
    input_box2.bind('<FocusOut>', on_entry_focus_out2)

    # 创建两个按钮
    button4 = tk.Button(bottom_frame, text="显示", command=button4_clicked)
    button4.pack(side=tk.LEFT, padx=10)
    button3 = tk.Button(bottom_frame, text="读音", command=button3_clicked)
    button3.pack(side=tk.LEFT, padx=10)
    button1 = tk.Button(bottom_frame, text="认识", command=button1_clicked)
    button1.pack(side=tk.LEFT, padx=10)
    button2 = tk.Button(bottom_frame, text="不认识", command=button2_clicked)
    button2.pack(side=tk.LEFT, padx=10)

    window.protocol("WM_DELETE_WINDOW", close)

    # 运行主循环
    window.mainloop()
