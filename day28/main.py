from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DEFAULT_WORK_TIME = f'00:00'
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(worktimer_text, text=DEFAULT_WORK_TIME)
    check_marks.config(text='')
    title_label.config(text='Timer', fg=GREEN)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    if REPS != 0:
        global timer
        window.after_cancel(timer)
    REPS += 1
    SECONDS = 60
    
    if REPS % 8 == 0:
        time = LONG_BREAK_MIN * SECONDS
        title_label.config(text='Break', fg=RED)
    elif REPS % 2 == 1:
        time = WORK_MIN * SECONDS
        title_label.config(text='Work', fg=GREEN)
    elif REPS % 2 == 0:
        time = SHORT_BREAK_MIN * SECONDS
        title_label.config(text='Break', fg=RED)
    countdown(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minute = count // 60
    second = count % 60
    canvas.itemconfig(worktimer_text, text=f'{minute:02d}:{second:02d}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            check_marks.config(text=check_marks.cget('text')+"✔️")
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
worktimer_text = canvas.create_text(103, 130, text=DEFAULT_WORK_TIME, fill='white', font=(FONT_NAME, 36, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='reset', command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text='', bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()