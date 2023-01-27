from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    label1["text"] = "Timer"
    checkmark_label.config(text="")
    canvas.itemconfigure(timer_text, text= "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_breake = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        label1.config(text="Break", fg="RED")

    elif reps % 2 == 0:
        countdown(short_breake)
        label1.config(text="Break", fg="PINK")

    else:
        countdown(work_time)
        label1.config(text= 'WORK', fg="GREEN")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"



    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_count()
        marks = ""
        work_sessions = floor(reps/2)
        for n in range(work_sessions):
            marks += "✔"
            checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Alarm")
window.minsize(width=400, height=400)
window["bg"] = YELLOW


canvas = Canvas(width=250, height=224, bg=YELLOW, highlightthickness=0)
domates = PhotoImage(file="tomato.png")
canvas.create_image(125, 112, image=domates)
canvas.place(x=79, y=80)
timer_text = canvas.create_text(125, 130, text="00:00", font=("Arial", 40, "bold"), fill="white")



label1 = Label(text="Timer", font=("Courier", 40, "bold"), fg=GREEN, bg=YELLOW)
label1.place(x=133, y=20)

start_button = Button(text="Start", bg="white", font=("Calibiri", 11, "bold"), highlightthickness=0, command=start_count)
start_button.place(x=75, y=320)

reset_button = Button(text="Reset", bg="white", font=("Calibiri", 11, "bold"), highlightthickness=0, command=reset_timer)
reset_button.place(x=270, y=320)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=("Courier", 15, "bold"))
checkmark_label.place(x=160, y=320)

window.mainloop()


