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
reps = 0
timer = None
window = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    global window
    window.lift()
    window.attributes('-topmost',True)
    window.after_idle(window.attributes,'-topmost',False)

    if reps % 8 == 0:
        window.after_cancel(timer)
        count_down(LONG_BREAK_MIN * 60)
        timer_title_label.config(text="Long", fg=RED)
    elif reps % 2 == 0:
        window.after_cancel(timer)
        count_down(SHORT_BREAK_MIN * 60)
        timer_title_label.config(text="Short", fg=PINK)
    else:
        if reps != 1 : window.after_cancel(timer)
        count_down(WORK_MIN * 60)
        timer_title_label.config(text="Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_sec = int(count % 60)
    count_min = int((count - count_sec) / 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps/2)):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


window.mainloop()