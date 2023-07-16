from tkinter import *
import threading

check = False
time_out = 20
count = 0
time_out_check = False

def timed():
    global time_out, time_out_check

    if check and time_out > 0:
        time_out -= 1
        timers.config(text=f'{time_out} sec', fg='white', bg='green')  # Colorful timer
    elif time_out == 0:
        app.destroy()
        result = Tk()
        result.resizable(width=False,height=False)
        result.title("Click test")
        result.geometry('700x400')
        result.config(bg='Black')
        global count
        speed = count / 20
        prit = Label(result, text=f'Your speed is {speed} clicks per second', font=('arial', 30,), justify='center', fg='white', bg='blue')  # Colorful result label
        prit.pack()
        result.mainloop()

    app.after(1000, timed)  # Call the timed() function again after 1000ms (1 second)

def click():
    global check, count
    check = True
    count += 1

if __name__ == '__main__':
    app = Tk()
    app.title("Click test")
    app.resizable(width=False,height=False)
    app.geometry('600x400')
    app.configure(bg='black')  # Background color of the main window

    timers = Label(app, text='20 sec', font=('arial', 30,), justify='center', fg='white', bg='red')  # Colorful timer label
    timers.pack()

    thread_timed = threading.Thread(target=timed)
    thread_timed.start()

    button = Button(app, text='Click me', font=('arial', 30,'bold'), justify='center', command=click, fg='yellow', bg='blue')  # Colorful button
    button.pack()

    app.mainloop()
