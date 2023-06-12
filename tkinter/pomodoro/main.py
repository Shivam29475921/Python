from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
check_mark = "✔"
clock = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global clock
    window.after_cancel(clock)
    check_marks.config(text="")
    global reps
    reps = 0
    global check_mark
    check_mark = "✔"
    timer_text.config(text="TIMER", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_countdown():
    global reps
    reps += 1
    if reps == 8:
        timer_text.config(text="BREAK", fg=RED, font=(FONT_NAME, 50))
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_text.config(text="BREAK", fg=PINK, font=(FONT_NAME, 50))
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 2 == 1:
        timer_text.config(text="WORK", fg=GREEN, font=(FONT_NAME, 50))
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(s):
    if s > -1:
        minutes = s // 60
        seconds = s % 60
        canvas.itemconfig(timer, text=f"{minutes:02d}:{seconds:02d}")
        global clock
        clock = window.after(1, count_down, s-1)
        if minutes == 0 and seconds == 0:
            start_countdown()
            if reps % 2 == 0 and reps != 8:
                global check_mark
                check_marks.config(text=check_mark)
                check_mark = check_mark + "✔"


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=background)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# labels
timer_text = Label(text="TIMER", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)

check_marks = Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# buttons
start_btn = Button(text="Start", border=0, command=start_countdown)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", border=0, command=reset)
reset_btn.grid(column=2, row=2)

window.mainloop()
