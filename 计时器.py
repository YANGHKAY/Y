import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")
        self.master.geometry("300x100")
        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")
        self.time_label = tk.Label(self.master, font=("Arial", 30), textvariable=self.time_var)
        self.time_label.pack(fill=tk.BOTH, expand=1)
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10)
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT)

        self.timer_running = False
        self.start_time = None

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = int(time.time())
            self.update_time()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.timer_running = False
        self.start_time = None
        self.time_var.set("00:00:00")

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_time(self):
        if self.timer_running:
            elapsed_time = int(time.time()) - self.start_time
            minutes, seconds = divmod(elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_var.set(time_string)
            self.master.after(1000, self.update_time)

if __name__ == "__main__":
    import time
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()





