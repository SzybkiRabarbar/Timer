import tkinter as tk

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from timer_app import TimerApp

class CreateMenu:
    """
    Creates buttons that open other classes.
    """
    def __init__(self, App: 'TimerApp') -> None:
        self.App = App
        self.main()
    
    def main(self):
        self.App.clear_window()
        if self.App.was_fullscreen:
            self.App.root.geometry(self.App.default_window_shift)
            self.App.was_fullscreen = False
        self.App.root.geometry('446x719')
        self.App.window.config(bg=self.App.BGCOLOR)
        
        button_to_timer = tk.Button(
            self.App.window,
            text = "Timer",
            bg = self.App.MIDCOLOR,
            fg = self.App.FGCOLOR,
            activebackground = self.App.MIDCOLOR,
            activeforeground = self.App.BGCOLOR,
            pady = 12,
            padx = 50,
            font = (self.App.FONTF, 40 , 'bold'),
            command = self.App.open_timer
        )
        button_to_timer.pack(fill='x', padx=30, pady=20)
        
        button_to_calendar = tk.Button(
            self.App.window,
            text = 'Calendar',
            bg = self.App.MIDCOLOR,
            fg = self.App.FGCOLOR,
            activebackground = self.App.MIDCOLOR,
            activeforeground = self.App.BGCOLOR,
            pady = 12,
            padx = 50,
            font = (self.App.FONTF, 40 , 'bold'),
            command = self.App.open_calendar
        )
        button_to_calendar.pack(fill='x', padx=30, pady=20)
        
        button_to_summary = tk.Button(
            self.App.window,
            text = 'Summary',
            bg = self.App.MIDCOLOR,
            fg = self.App.FGCOLOR,
            activebackground = self.App.MIDCOLOR,
            activeforeground = self.App.BGCOLOR,
            pady = 12,
            padx = 50,
            font = (self.App.FONTF, 40 , 'bold'),
            command = self.App.open_summary
        )
        button_to_summary.pack(fill='x', padx=30, pady=20)

        lowest_button = tk.Frame(self.App.window)
        lowest_button.pack(fill='x', padx=30, pady=20)
                
        button_change_mode = tk.Button(
            lowest_button,
            text = self.App.MODESIGN,
            bg = self.App.MIDCOLOR,
            fg = self.App.FGCOLOR,
            activebackground = self.App.MIDCOLOR,
            activeforeground = self.App.BGCOLOR,
            pady = 12,
            padx = 25,
            font = (self.App.FONTF, 40 , 'bold'),
            command=self.App.change_color
        )
        button_change_mode.pack(side='left')
        
        button_to_google = tk.Button(
            lowest_button,
            text = 'Settings',
            bg = self.App.MIDCOLOR,
            fg = self.App.FGCOLOR,
            activebackground = self.App.MIDCOLOR,
            activeforeground = self.App.BGCOLOR,
            pady = 12,
            font = (self.App.FONTF, 40 , 'bold'),
            command = self.App.open_settings
        )
        button_to_google.pack(side='right', fill='x', expand=True)