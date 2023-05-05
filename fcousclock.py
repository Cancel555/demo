import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        # 创建计时器标签和开始/停止按钮
        self.timer_label = tk.Label(master, font=(None, 48), text="25:00")
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)

        # 将组件放置在窗口中
        self.timer_label.pack()
        self.start_button.pack(side=tk.LEFT)
        self.stop_button.pack(side=tk.RIGHT)

        # 初始化计时器状态
        self.is_running = False
        self.time_left = 1500  # 初始25分钟

    def start_timer(self):
        self.is_running = True
        self.tick()

    def stop_timer(self):
        self.is_running = False

    def tick(self):
        if not self.is_running:
            return

        # 更新剩余时间
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_str = "{:02d}:{:02d}".format(minutes, seconds)
        self.timer_label.configure(text=time_str)

        # 计时器减一秒
        self.time_left -= 1

        # 如果时间用完了，则重置计时器
        if self.time_left == 0:
            self.is_running = False
            self.time_left = 1500
            self.timer_label.configure(text="25:00")

        # 延迟1秒后再次调用tick函数
        self.master.after(1000, self.tick)

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
