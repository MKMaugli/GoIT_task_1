import tkinter as tk
from tkinter import ttk
import threading
import time
import pystray
from pynput import keyboard
import pyautogui
from PIL import Image
import atexit
import sys
import os
import psutil
import pickle

class KeyPressEmulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Эмулятор нажатия клавиши")

        # Восстановление местоположения окна, если оно было сохранено
        try:
            with open("window_position.pkl", "rb") as file:
                window_position = pickle.load(file)
                self.root.geometry(window_position)
        except FileNotFoundError:
            self.root.geometry("400x220")  # Устанавливаем размер окна по умолчанию

        self.direction_label = tk.Label(root, text="Выберите направление:")
        self.direction_label.grid(row=0, column=0, sticky="w", padx=10)

        self.direction_var = tk.StringVar()
        self.direction_var.set("Влево")

        self.left_radio = tk.Radiobutton(root, text="Влево", variable=self.direction_var, value="Влево")
        self.left_radio.grid(row=0, column=1, sticky="w")

        self.right_radio = tk.Radiobutton(root, text="Вправо", variable=self.direction_var, value="Вправо")
        self.right_radio.grid(row=1, column=1, sticky="w")

        self.speed_label = tk.Label(root, text="Скорость нажатия (мс):")
        self.speed_label.grid(row=2, column=0, sticky="w", padx=10)

        self.speed_var = tk.IntVar()
        self.speed_var.set(100)
        self.speed_entry = ttk.Entry(root, textvariable=self.speed_var)
        self.speed_entry.grid(row=2, column=1)

        self.repeat_label = tk.Label(root, text="Количество нажатий:")
        self.repeat_label.grid(row=3, column=0, sticky="w", padx=10)

        self.repeat_var = tk.IntVar()
        self.repeat_var.set(50)
        self.repeat_entry = ttk.Entry(root, textvariable=self.repeat_var)
        self.repeat_entry.grid(row=3, column=1)

        self.infinite_repeat_var = tk.IntVar()
        self.infinite_repeat_checkbox = tk.Checkbutton(root, text="Бесконечное повторение", variable=self.infinite_repeat_var)
        self.infinite_repeat_checkbox.grid(row=4, columnspan=2, padx=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=5, columnspan=2, pady=10)

        self.start_button = tk.Button(self.button_frame, text="Старт (F8)", command=self.start_emulation)
        self.start_button.pack(side="left", padx=60)

        self.stop_button = tk.Button(self.button_frame, text="Стоп (F8)", command=self.stop_emulation, state=tk.DISABLED)
        self.stop_button.pack(side="right", padx=60)

        self.running = False
        self.emulation_thread = None
        self.hotkey_listener = None

    def start_emulation(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            direction = self.direction_var.get()
            speed = self.speed_var.get() / 1000.0  # Конвертируем в секунды
            repeat = self.repeat_var.get()
            infinite_repeat = self.infinite_repeat_var.get()
            self.emulation_thread = threading.Thread(target=self.emulate_key_press, args=(direction, speed, repeat, infinite_repeat))
            self.emulation_thread.start()

    def stop_emulation(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def emulate_key_press(self, direction, speed, repeat, infinite_repeat):
        while self.running:
            if direction == "Влево":
                pyautogui.press("left")
            elif direction == "Вправо":
                pyautogui.press("right")
            repeat -= 1
            if repeat == 0 and not infinite_repeat:
                self.stop_emulation()
            time.sleep(speed)

def on_hotkey(key):
    if key == keyboard.Key.f8:
        if app.running:
            app.stop_emulation()
        else:
            app.start_emulation()

def exit_program():
    app.stop_emulation()
    root.quit()

def create_system_tray_icon():
    # Загружаем иконку из файла icon.ico
    icon = Image.open("icon.ico")
    
    menu = (
        pystray.MenuItem('Выход', lambda: exit_program()),
    )
    # Передаем иконку при создании системного значка
    icon = pystray.Icon("name", icon, "Меню", menu)
    icon.run()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyPressEmulator(root)
    threading.Thread(target=create_system_tray_icon).start()
    
    atexit.register(exit_program)  # Завершение приложения при выходе

    try:
        with keyboard.Listener(on_press=on_hotkey) as listener:
            root.mainloop()
    except KeyboardInterrupt:
        pass

# Завершаем все дочерние процессы при выходе из программы
for proc in psutil.process_iter():
    try:
        if os.path.basename(sys.argv[0]) in ' '.join(proc.cmdline()):
            proc.terminate()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass