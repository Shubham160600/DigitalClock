import tkinter as tk
from tkinter import ttk
import math
import time
from datetime import datetime

class AnalogDigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Digital Clock")
        self.root.geometry("800x900")
        self.root.configure(bg='#1e293b')
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg='#1e293b', padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')
        
        # Title
        self.title_label = tk.Label(
            self.main_frame, 
            text="Analog Clock", 
            font=('Arial', 24, 'bold'),
            fg='white',
            bg='#1e293b'
        )
        self.title_label.pack(pady=(0, 10))
        
        self.subtitle_label = tk.Label(
            self.main_frame,
            text="Live Animated Timepiece",
            font=('Arial', 12),
            fg='#93c5fd',
            bg='#1e293b'
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Digital clock frame
        self.digital_frame = tk.Frame(
            self.main_frame,
            bg='#374151',
            relief='raised',
            bd=2
        )
        self.digital_frame.pack(pady=(0, 20), padx=20, fill='x')
        
        # Digital time display
        self.digital_time_label = tk.Label(
            self.digital_frame,
            text="00:00:00:00",
            font=('Courier', 20, 'bold'),
            fg='#10b981',
            bg='#374151'
        )
        self.digital_time_label.pack(pady=15)
        
        self.digital_format_label = tk.Label(
            self.digital_frame,
            text="HH:MM:SS:MS",
            font=('Arial', 10),
            fg='#9ca3af',
            bg='#374151'
        )
        self.digital_format_label.pack()
        
        # Canvas for analog clock
        self.canvas = tk.Canvas(
            self.main_frame,
            width=400,
            height=400,
            bg='#f8fafc',
            highlightthickness=0
        )
        self.canvas.pack(pady=20)
        
        # Time info frame
        self.info_frame = tk.Frame(self.main_frame, bg='#1e293b')
        self.info_frame.pack(pady=20, fill='x')
        
        # Create info boxes
        self.create_info_boxes()
        
        # Status label
        self.status_label = tk.Label(
            self.main_frame,
            text="Real-time analog and digital clock display",
            font=('Arial', 10),
            fg='#9ca3af',
            bg='#1e293b'
        )
        self.status_label.pack(pady=(20, 0))
        
        # Start the clock
        self.update_clock()
    
    def create_info_boxes(self):
        # Hours box
        hours_frame = tk.Frame(self.info_frame, bg='#374151', relief='raised', bd=1)
        hours_frame.pack(side='left', expand=True, fill='x', padx=5)
        
        tk.Label(hours_frame, text="Hours", font=('Arial', 10), 
                fg='#d1d5db', bg='#374151').pack(pady=(10, 5))
        self.hours_value = tk.Label(hours_frame, text="00", font=('Arial', 16, 'bold'),
                                   fg='white', bg='#374151')
        self.hours_value.pack(pady=(0, 10))
        
        # Minutes box
        minutes_frame = tk.Frame(self.info_frame, bg='#374151', relief='raised', bd=1)
        minutes_frame.pack(side='left', expand=True, fill='x', padx=5)
        
        tk.Label(minutes_frame, text="Minutes", font=('Arial', 10), 
                fg='#d1d5db', bg='#374151').pack(pady=(10, 5))
        self.minutes_value = tk.Label(minutes_frame, text="00", font=('Arial', 16, 'bold'),
                                     fg='white', bg='#374151')
        self.minutes_value.pack(pady=(0, 10))
        
        # Seconds box
        seconds_frame = tk.Frame(self.info_frame, bg='#374151', relief='raised', bd=1)
        seconds_frame.pack(side='left', expand=True, fill='x', padx=5)
        
        tk.Label(seconds_frame, text="Seconds", font=('Arial', 10), 
                fg='#d1d5db', bg='#374151').pack(pady=(10, 5))
        self.seconds_value = tk.Label(seconds_frame, text="00", font=('Arial', 16, 'bold'),
                                     fg='white', bg='#374151')
        self.seconds_value.pack(pady=(0, 10))
    
    def format_time(self, num):
        return str(num).zfill(2)
    
    def get_clock_hand_rotation(self, value, max_val):
        return (value / max_val) * 360
    
    def draw_clock_face(self):
        # Clear canvas
        self.canvas.delete("all")
        
        # Clock center
        center_x, center_y = 200, 200
        radius = 180
        
        # Outer circle (border)
        self.canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline='#3b82f6', width=8, fill='#1e293b'
        )
        
        # Inner circle (face)
        inner_radius = 165
        self.canvas.create_oval(
            center_x - inner_radius, center_y - inner_radius,
            center_x + inner_radius, center_y + inner_radius,
            outline='#cbd5e1', width=2, fill='#f8fafc'
        )
        
        # Draw hour marks
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            start_x = center_x + 160 * math.cos(angle)
            start_y = center_y + 160 * math.sin(angle)
            end_x = center_x + 145 * math.cos(angle)
            end_y = center_y + 145 * math.sin(angle)
            
            self.canvas.create_line(
                start_x, start_y, end_x, end_y,
                fill='#1e40af', width=3
            )
        
        # Draw minute marks
        for i in range(60):
            if i % 5 != 0:  # Skip hour marks
                angle = math.radians(i * 6 - 90)
                start_x = center_x + 160 * math.cos(angle)
                start_y = center_y + 160 * math.sin(angle)
                end_x = center_x + 155 * math.cos(angle)
                end_y = center_y + 155 * math.sin(angle)
                
                self.canvas.create_line(
                    start_x, start_y, end_x, end_y,
                    fill='#64748b', width=1
                )
        
        # Draw numbers
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = center_x + 140 * math.cos(angle)
            y = center_y + 140 * math.sin(angle)
            
            self.canvas.create_text(
                x, y, text=str(i),
                font=('Arial', 14, 'bold'),
                fill='#1e40af'
            )
        
        # Brand name
        self.canvas.create_text(
            center_x, center_y - 60,
            text="CLOCK",
            font=('Arial', 16, 'bold'),
            fill='#1e40af'
        )
    
    def draw_clock_hands(self, hours, minutes, seconds, milliseconds):
        center_x, center_y = 200, 200
        
        # Calculate rotations
        second_rotation = math.radians(self.get_clock_hand_rotation(seconds + milliseconds / 1000, 60) - 90)
        minute_rotation = math.radians(self.get_clock_hand_rotation(minutes + seconds / 60, 60) - 90)
        hour_rotation = math.radians(self.get_clock_hand_rotation((hours % 12) + minutes / 60, 12) - 90)
        
        # Hour hand
        hour_x = center_x + 80 * math.cos(hour_rotation)
        hour_y = center_y + 80 * math.sin(hour_rotation)
        self.canvas.create_line(
            center_x, center_y, hour_x, hour_y,
            fill='#1e40af', width=8, capstyle='round'
        )
        
        # Minute hand
        minute_x = center_x + 120 * math.cos(minute_rotation)
        minute_y = center_y + 120 * math.sin(minute_rotation)
        self.canvas.create_line(
            center_x, center_y, minute_x, minute_y,
            fill='#1e40af', width=4, capstyle='round'
        )
        
        # Second hand
        second_x = center_x + 130 * math.cos(second_rotation)
        second_y = center_y + 130 * math.sin(second_rotation)
        self.canvas.create_line(
            center_x, center_y, second_x, second_y,
            fill='#dc2626', width=2, capstyle='round'
        )
        
        # Center dot
        self.canvas.create_oval(
            center_x - 8, center_y - 8,
            center_x + 8, center_y + 8,
            fill='#1e40af', outline='white', width=2
        )
    
    def update_clock(self):
        # Get current time
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        milliseconds = now.microsecond // 1000
        
        # Update digital display
        digital_time = f"{self.format_time(hours)}:{self.format_time(minutes)}:{self.format_time(seconds)}:{self.format_time(milliseconds // 10)}"
        self.digital_time_label.config(text=digital_time)
        
        # Update info boxes
        self.hours_value.config(text=self.format_time(hours))
        self.minutes_value.config(text=self.format_time(minutes))
        self.seconds_value.config(text=self.format_time(seconds))
        
        # Draw analog clock
        self.draw_clock_face()
        self.draw_clock_hands(hours, minutes, seconds, milliseconds)
        
        # Schedule next update (every 10ms for smooth animation)
        self.root.after(10, self.update_clock)

def main():
    root = tk.Tk()
    clock = AnalogDigitalClock(root)
    
    print("🕐 Analog Digital Clock Started!")
    print("=" * 50)
    print("Features:")
    print("✓ Real-time analog clock with smooth hand movement")
    print("✓ Digital time display with milliseconds")
    print("✓ Hour, minute, and second indicators")
    print("✓ Professional clock face with numbers and marks")
    print("✓ Live updating every 10ms")
    print("=" * 50)
    print("Press Ctrl+C or close window to exit")
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\n🛑 Clock stopped by user")
    
    print("👋 Thanks for using Analog Digital Clock!")

if __name__ == "__main__":
    main()
