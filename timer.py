
# TODO dodać kalendarz z czasem pracy i czasem przerwy (main_time, break_time)
    # TODO dodawanie do kalendarza po zamknięciu okiennka timer
    # TODO tkcalendar, ale po kliknięciu na dzień otwiera się aktywność
    # TODO oznaczyć na tkcalendarze że jest jakaś aktywnosć danego dnia (mała kropka, zmieniony kolor itp)
    # TODO zrobienie szablonów (aktywność można podpiąć pod jakąś aktywnosć (np programowanie) z unikalnym kolorem, nazwą opisem itp)
# TODO obszar podsumowania zliczający wszystkie aktywności dla każdego szablonu
# TODO w kalendarzu dodać przesyłanie do google calendar (pomyśleć jak połączyc różne sesje, jak je zapisać w lokalnym kalenadarzu, przy dodawaniu podać nazwe, opis itp)
# TODO sprawdzić zapisywanie plików również po nieoczekikwanym zamknięciu aplikacji
# TODO sprawdzić zmiane domyślnego paska
# TODO sprawdzić czy jest możliwość inplementacji animacji

import tkinter as tk
from tkinter import ttk

class TimerApp():
    
    def __init__(self) -> None:
        self.main_time = False
        self.break_time = False
        self.current_break_time = False
        
    def open_timer_window(self):
        
        """
        Shows a window with main timer, button, break timer and currnet break timer.
        Normally main timer counts down the time,but then button is unclicked break timer and currnet break timer starts counts.
        Break timer stores time of sum of all 'breaks' and current break timer stores time of current break.
        """
        
        def update(time: tk.IntVar, timer: tk.StringVar) -> tuple[tk.IntVar, tk.StringVar]:
            """
            Updates given time and return new time value and string timer to display
            """
            time.set(time.get() + 1)
            seconds = time.get()
            timer.set(f"{seconds // 3600}:{seconds // 60 % 60 :02d}:{seconds % 60 :02d}")
            return (time, timer)

        def time_loop():
            """
            Checks if update main timer or stop timer and updates it
            """
            #! loop dont stop after WM_DELETE_WINDOW and rises 
            #? 'invalid command name "loop" while executing "loop" ("after" script)'
            if is_running.get():
                button_text.set("STOP")
                self.current_break_time.set(0)
                self.main_time, self.main_timer = update(self.main_time, self.main_timer)
            else:
                button_text.set("START")
                self.current_break_time, self.current_break_timer = update(self.current_break_time, self.current_break_timer)
                self.break_time, self.break_timer = update(self.break_time, self.break_timer)    
            timer_window.after(1000, time_loop) 

        self.root.destroy()
        timer_window = tk.Tk()
        timer_window.title("Timer")
        icon = tk.PhotoImage(file="timer-icon.png")
        timer_window.iconphoto(True,icon)
        timer_window.geometry("300x150")
        timer_window.config(bg="#011638")
        
        #| main_time stores the time (in sec)
        self.main_time = tk.IntVar(value=0)
        #| main_timer stores formated main_time (H:M:S)
        self.main_timer = tk.StringVar()
        main_label = tk.Label(timer_window, 
            font=("Ariel",40),
            pady=12,
            fg="#E8C1C5",
            bg="#011638",
            textvariable=self.main_timer)
        main_label.pack()

        
        #| stop_button indicates wich time should be updated (main_time or break_time)
        is_running = tk.IntVar(value=1)
        button_text = tk.StringVar(value="STOP")
        stop_button = tk.Checkbutton(timer_window, 
            font=("Ariel",15),
            fg="#D499B9",
            bg="#011638",
            selectcolor="#2E294E", 
            variable=is_running, 
            textvariable=button_text, 
            indicatoron=False)
        stop_button.pack()
        
        #| Freame for breaks timers
        frame = tk.Frame(timer_window)
        frame.pack()

        #| Style for breaks timers
        style = ttk.Style()
        style.configure("BW.TLabel",
            font=("Ariel",15),
            foreground="#E8C1C5", 
            background="#011638"
            )

        #| break_time stores the time (in sec)
        self.break_time = tk.IntVar(value=0)
        #| break_timer stores formated break_time (H:M:S)
        self.break_timer = tk.StringVar()
        break_label = ttk.Label(frame,
            style="BW.TLabel",
            textvariable=self.break_timer)
        break_label.pack(side="left")

        pipe = ttk.Label(frame,
            style="BW.TLabel",
            text="|")
        pipe.pack(side="left")

        #| current_break_time stores the time (in sec)
        self.current_break_time = tk.IntVar(value=0)
        #| current_break_timer stores formated current_break_time (H:M:S)
        self.current_break_timer = tk.StringVar()
        current_break_label = ttk.Label(frame,
            style="BW.TLabel",
            textvariable=self.current_break_timer)
        current_break_label.pack(side="right")

        time_loop()
        
        timer_window.protocol("WM_DELETE_WINDOW", lambda: [timer_window.destroy(), self.open_main_window()])
    
    def open_calendar_window(self):
        
        self.root.destroy()
        cal_window = tk.Tk()
        cal_window.title("Calendar")
        cal_window.geometry("300x150")
        cal_window.config(bg="#011638")
        
        if self.main_time and self.break_time and self.current_break_time:
            txt = f'{self.main_time.get()} | {self.break_time.get()} | {self.current_break_time.get()}'
            t = tk.Label(cal_window,
                text=txt)
            t.pack()
        
        cal_window.protocol("WM_DELETE_WINDOW", lambda: [cal_window.destroy(), self.open_main_window()])
        
    def open_main_window(self):
        """
        MENU
        """
        self.root = tk.Tk()
        self.root.title("TimerApp")
        self.root.config(bg="#011638")
        icon = tk.PhotoImage(file="timer-icon.png")
        self.root.iconphoto(True,icon)
        
        button_to_timer = tk.Button(self.root,
            text="Timer",
            fg="#011638", 
            bg="#E8C1C5",
            activebackground="#D499B9",
            pady= 12,
            padx= 50,
            font=("Ariel", 40 , 'bold'),
            command=self.open_timer_window)
        button_to_timer.pack(fill='x', padx=30, pady=20)
        
        button_to_calendar = tk.Button(self.root,
            text='Calendar',
            fg="#011638", 
            bg="#E8C1C5",
            activebackground="#D499B9",
            pady= 12,
            padx= 50,
            font=("Ariel", 40 , 'bold'),
            command=self.open_calendar_window)
        button_to_calendar.pack(fill='x', padx=30, pady=20)

        self.root.mainloop()
    
if __name__=="__main__":
    t = TimerApp()
    t.open_main_window()