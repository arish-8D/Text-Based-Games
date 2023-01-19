from tkinter import Tk, Label, Frame, Canvas, Button, IntVar, PhotoImage, Entry, messagebox, Text
from itertools import cycle
from random import choice, randint
from PIL import Image, ImageTk, ImageSequence

root = Tk()
root.state('zoomed')
root.iconbitmap('black_dice.ico')
root.title('Three silly Games')
root.resizable(width=False, height=False)

win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()


def show_frame(frame_):
    frame_.tkraise()


startpage = Frame(root, width=win_width, height=win_height)
hl_frame = Frame(root, width=win_width, height=win_height)
se_frame = Frame(root, width=win_width, height=win_height)
gg_frame = Frame(root, width=win_width, height=win_height)

for frame in (startpage, hl_frame, se_frame, gg_frame):
    frame.place(relx=0, rely=0)

# ----------------------playing bg-gif startpage-----------------------------------------------------------
lbl = Label(startpage, width=win_width, height=win_height)
lbl.pack(fill='both', expand=True)

img = Image.open('bg_gif.gif')
img_iterator = cycle(ImageTk.PhotoImage(image.resize((win_width, win_height), Image.ANTIALIAS)) for image in ImageSequence.Iterator(img))


def gif_():
    lbl.config(image=next(img_iterator))
    root.after(50, gif_)


gif_()
# universal things------------------------------------------------------------------------------
bars = PhotoImage(file='3_bars.png')
streak = 0
text_box_num = 0
btns_displayed = False


def rules_box(box_name, text):
    global text_box_num
    text_box_num += 1

    if text_box_num % 2 == 1:

        if box_name == hl_text_box:
            box_name.place(relx=0.5, rely=0.3, width = 300, height=200, anchor='center')
            box_name.config(font=('gill sans mt condensed', 20))
        else:
            box_name.place(relx=0.5, rely=0.5, width = 600, height=325, anchor='center')

        box_name.insert('end', text)
        box_name.config(state='disabled')
        box_name.tag_config('center', justify='center')
        box_name.tag_add("center", 1.0, "end")
    else:
        box_name.place_forget()


def show_btns(button1, button2, button3, button4, menu_btn):

    def drop_btns():
        global btns_displayed

        def btn1_place():
            global btns_displayed

            if btns_displayed == True:
                button1.place(relx=0.1, rely=0.2, anchor='center')

            else:
                button1.place_forget()


        def btn2_place():
            global btns_displayed

            if btns_displayed == True:
                button2.place(relx=0.1, rely=0.4, anchor='center')

            else:
                button2.place_forget()


        def btn3_place():
            global btns_displayed

            if btns_displayed == True:
                button3.place(relx=0.1, rely=0.6, anchor='center')

            else:
                button3.place_forget()


        def btn4_place():
            global btns_displayed

            if btns_displayed == True:
                button4.place(relx=0.1, rely=0.8, anchor='center')

            else:
                button4.place_forget()


        if btns_displayed == False:
            menu_btn.after(150, btn1_place)
            menu_btn.after(300, btn2_place)
            menu_btn.after(450, btn3_place)
            menu_btn.after(600, btn4_place)
            btns_displayed = True
        else:
            menu_btn.after(150, btn4_place)
            menu_btn.after(300, btn3_place)
            menu_btn.after(450, btn2_place)
            menu_btn.after(600, btn1_place)
            btns_displayed = False


    menu_btn.after(200, drop_btns)



# ===============================startpage==============================================================================

Label(startpage, text='Choose Your Game', font=('gill sans mt condensed', 50), fg='#d924dc', bg='#fad54f').place(
    relx=0.5, rely=0.08, anchor='center')

btn1 = Button(startpage, text='Higher-Lower', bg='#fad54f', fg='#d924dc', font=('gill sans mt condensed', 35),
              command=lambda: show_frame(hl_frame))
btn1.place(relx=0.2, rely=0.7, anchor='center')

btn2 = Button(startpage, text='Guess-Game', bg='#fad54f', fg='#d924dc', font=('gill sans mt condensed', 35),
              command=lambda: show_frame(gg_frame))
btn2.place(relx=0.5, rely=0.7, anchor='center')

btn3 = Button(startpage, text='Snake-Eyes', bg='#fad54f', fg='#d924dc', font=('gill sans mt condensed', 35),
              command=lambda: show_frame(se_frame))
btn3.place(relx=0.8, rely=0.7, anchor='center')

# ==================================hl frame============================================================================
# other things---------------------------
hint_num = randint(1, 99)

# functions---------------------------------


def lower_():
    global streak
    higher.config(state='disabled')
    lower.config(state='disabled')
    equal.config(state='disabled')
    if hidden_num < hint_num:
        hl_always_changing_lbl.config(text=choice(lower_dict['correct']))
        streak += 1
        streak_lbl_hl.config(text=f'Streak - {streak}')
    else:
        hl_always_changing_lbl.config(text=choice(lower_dict['wrong']))
        streak = 0
        streak_lbl_hl.config(text=f'Streak - {streak}')


def higher_():
    higher.config(state='disabled')
    lower.config(state='disabled')
    equal.config(state='disabled')
    global streak
    if hidden_num > hint_num:
        hl_always_changing_lbl.config(text=choice(higher_dict['correct']))
        streak += 1
        streak_lbl_hl.config(text=f'Streak - {streak}')
    else:
        hl_always_changing_lbl.config(text=choice(higher_dict['wrong']))
        streak = 0
        streak_lbl_hl.config(text=f'Streak - {streak}')


def equal_():
    higher.config(state='disabled')
    lower.config(state='disabled')
    equal.config(state='disabled')
    global streak
    if hidden_num == hint_num:
        hl_always_changing_lbl.config(text=choice(equal_dict['correct']))
        streak += 1
        streak_lbl_hl.config(text=f'Streak - {streak}')
    else:
        hl_always_changing_lbl.config(text=choice(equal_dict['wrong']))
        streak = 0
        streak_lbl_hl.config(text=f'Streak - {streak}')


def start_the_thing():
    global hint_num, hidden_num, higher_dict, lower_dict, equal_dict

    hint_num = randint(1, 99)
    hidden_num = randint(1, 100)

    higher_dict = {'correct': [f"You never fail to amuse me\nIt was indeed higher\nThe hidden number was {hidden_num}",
                               f'Noice!! :) You got that right\nIt is {hidden_num}',
                               f"At least god has given you something\nThe hidden number was {hidden_num}"],

                   'wrong': [f"Don't you get tired from losing\nThe hidden number was {hidden_num}",
                             f"No sir, that's not the right choice\nThe hidden number is {hidden_num}",
                             f"Congratulations it was not higher :)\nThe hidden number was {hidden_num} "]}

    lower_dict = {'correct': [f'Good Job!! It is actually smaller\nthan the hidden number\nwhich is {hidden_num}',
                              f"That's my boi\nThe hidden number was {hidden_num}",
                              f"Well Done\nThe hidden number was {hidden_num}"],

                  'wrong': [f'Ooooops... wrong choice :(\nThe hidden number was\n{hidden_num}',
                            f'Well that was kinda expected\nThe hidden number was {hidden_num}',
                            f'Ever hated yourself bcoz of your luck?\nIf not then now is the right time\nIt was {hidden_num}']}

    equal_dict = {'correct': [
        f"Ohhhh Myyyyy Dawwwwwwg.....\nWhat you just did is\nunbelililievable :O\n The hidden number was {hidden_num}",
        f"Whoa whoa whoa whoa * infinity\nHow is that even possible\nThe hidden number {hidden_num} was equal",
        f"We salute you\nwhat you just did has shook the entire planet\nThe hidden number was indeed {hidden_num}"],

        'wrong': [
            f"Whhhat you actually did that\nCan't bleeb dis\nJust for ur information\nthe hidden number was {hidden_num}",
            f"Well, no comments\nThe hidden number was {hidden_num}",
            f"Feeling proud? You should Lmao\nThe hidden number was {hidden_num}"]}

    if just_click_it.winfo_ismapped():
        just_click_it.place_forget()
        advice.place(relx=.5, rely=0.4, anchor='center')
        ur_hint_label.place(relx=0.5, rely=0.1, anchor='center')
        hint.place(relx=0.5, rely=0.275, anchor='center')
        hl_always_changing_lbl.place(relx=0.5, rely=0.85, anchor='center')
        lower.place(relx=0.3, rely=0.6, height=80, anchor='center')
        equal.place(relx=0.5, rely=0.6, height=80, anchor='center')
        higher.place(relx=0.7, rely=0.6, height=80, anchor='center')
        play_btn.config(text='Play Again')
        streak_lbl_hl.place(relx=0.8, rely=0.1)
    else:

        hl_always_changing_lbl.config(text='')
        higher.config(state='normal')
        lower.config(state='normal')
        equal.config(state='normal')
        hint.config(text=hint_num)


# --------------hl photoimage---------------
# --------------hl widgets------------------
hl_frame_a = Frame(hl_frame, bg='#00203F', width=1280, height=720)
hl_frame_b = Frame(hl_frame, bg='#ADEFD1', width=250, height=600)
hl_frame_c = Frame(hl_frame, bg='#ADEFD1', width=500, height=100)
hl_frame_d = Frame(hl_frame, bg='#ADEFD1', width=900, height=500)

# labels------------------------------------
hl_main_label = Label(hl_frame_c, text='Higher - Lower', fg='#ADEFD1', bg='#00203F', width=19, font=('', 50, 'bold'))
just_click_it = Label(hl_frame_d, text='What are you waiting for??\n Just click the PLAY button', fg='#00203f',
                      bg='#adefd1', font=('helvetica', 30))
ur_hint_label = Label(hl_frame_d, text='Your hint is', font=('gill sans mt condensed', 50), fg='#00203f', bg='#adefd1')
advice = Label(hl_frame_d,
               text='click the lower button if you think the hidden number is lesser\n than the number in hint and other buttons accordingly.',
               font=15, bg='#ADEFD1', fg='#00203F')
hl_always_changing_lbl = Label(hl_frame_d, text='', font=('helvetica', 25), bg='#adefd1', fg='#00203f', width=30,
                               height=5)
streak_lbl_hl = Label(hl_frame_d, text=f'Streak = {streak}', bg='#ADEFD1', fg='#00203F', font=20)
hint = Label(hl_frame_d, text=hint_num, font=100, fg='#adefd1', bg='#00203f', padx=5, pady=3)

#text box stuff-----------------------------
hl_text_box = Text(hl_frame_d, font=('gill sans mt condensed', 30), bg='#00203F', fg='#adefd1')  #, width=40, height=7
hl_rules = '\nSimple, just guess if the number\n given in the hint is higher\n or lower than the hidden number'

# buttons-----------------------------------
hl_rules_btn = Button(hl_frame_b, text='Rules', bg='#00203F', fg='#ADEFD1', padx=5, pady=3, font=('helvetica', 20), command=lambda:rules_box(hl_text_box, hl_rules))
play_btn = Button(hl_frame_b, text='Play', fg='#ADEFD1', bg='#00203F', activebackground='#ADEFD1',
                  activeforeground='#00203F', width=10, height=1, font=('gill sans mt condensed', 25),
                  command=start_the_thing)
start_page_btn = Button(hl_frame_b, text='Home Page', font=('gill sans mt condensed', 25),
                        command=lambda: show_frame(startpage))
se_btn = Button(hl_frame_b, text='Snake-Eyes', font=('gill sans mt condensed', 25),
                command=lambda: show_frame(se_frame))
gg_btn = Button(hl_frame_b, text='Guess-Game', font=('gill sans mt condensed', 25),
                command=lambda: show_frame(gg_frame))
lower = Button(hl_frame_d, text='Lower', font=('gill sans mt condensed', 30), width=6, bg='#00203f', fg='#adefd1',
               command=lower_)
equal = Button(hl_frame_d, text='Equal', font=('gill sans mt condensed', 30), width=6, bg='#00203f', fg='#adefd1',
               command=equal_)
higher = Button(hl_frame_d, text='Higher', font=('gill sans mt condensed', 30), width=6, bg='#00203f', fg='#adefd1',
                command=higher_)

# placing-----------------------------------
hl_frame_a.place(relx=0, rely=0)
hl_frame_b.place(relx=0.12, rely=0.5, anchor='center')
hl_frame_c.place(relx=0.4125, rely=0.025)
hl_frame_d.place(relx=0.6125, rely=0.55, anchor='center')
hl_rules_btn.place(relx=.5, rely=0.125, anchor='center')
start_page_btn.place(relx=0.5, rely=0.5, anchor='center')
se_btn.place(relx=0.5, rely=0.7, anchor='center')
gg_btn.place(relx=0.5, rely=0.9, anchor='center')
play_btn.place(relx=0.5, rely=0.3, anchor='center')
hl_main_label.place(relx=0.5, y=50, anchor='center')
just_click_it.place(relx=0.5, rely=0.5, anchor='center')

# ===================================se frame===========================================================================
# photoimage--------------------------------
sedice = PhotoImage(file='se_dice.png')
face1 = PhotoImage(file='face_1.png')
face2 = PhotoImage(file='face_2.png')
face3 = PhotoImage(file='face_3.png')
face4 = PhotoImage(file='face_4.png')
face5 = PhotoImage(file='face_5.png')
face6 = PhotoImage(file='face_6.png')

# frames------------------------------------
se_frame_a = Frame(se_frame, width=win_width, height=win_height, bg='#f4b41a')

# canvas------------------------------------
se_biggest_canvas = Canvas(se_frame, width=win_width, height=win_height, bg='#f4b41a')
se_canvas = Canvas(se_biggest_canvas, width=600, height=325, bg='#143d59', bd=0, highlightthickness=0)
se_canvas_2 = Canvas(se_biggest_canvas, width=175, height=175, bg='#f4b41a', bd=0, highlightthickness=0)
# text box----------------------------------
se_rules_box = Text(se_biggest_canvas, font=('gill sans mt condensed', 25), bg='#143d59', fg='#f4b41a')
se_rules = "Enter a bet which is in whole numbers,\nclick the button and two dices will \nbe rolled if you get two 1's on both\ndices you get 10 times your bet\nif you get 1 on one of the two dices\nyou get 2 times your bet\notherwise you get nothing."

# labels------------------------------------
place_bet = Label(se_canvas, text='Place your bet here -', font=('gill sans mt condensed', 30), bg='#143d59',
                  fg='#f4b41a')

result_label = Label(se_biggest_canvas, text='', font=('gill sans mt condensed', 30, 'bold'), width=45, height=3,
                     bg='#f4b41a', fg='#143d59')

# buttons-----------------------------------
se_rules_button = Button(se_biggest_canvas, text='Rules', bg='#143d59', fg='#f4b41a',
                         font=('gill sans mt condensed', 20),
                         width=10, height=1, command=lambda: rules_box(se_rules_box, se_rules))
high_low = Button(se_biggest_canvas, text='High-Low', width=15, bg='#143d59', fg='#f4b41a',
                  font=('gill sans mt condensed', 25), height=1, command=lambda: show_frame(hl_frame))
home_page = Button(se_biggest_canvas, text='Home-Page', width=15, bg='#143d59', fg='#f4b41a',
                   font=('gill sans mt condensed', 25), height=1, command=lambda: show_frame(startpage))
guess_g = Button(se_biggest_canvas, text='Guess-Game', width=15, bg='#143d59', fg='#f4b41a',
                 font=('gill sans mt condensed', 25), height=1, command=lambda: show_frame(gg_frame))
quit_btn = Button(se_biggest_canvas, text='QUIT', width=15, bg='#143d59', fg='#f4b41a',
                  font=('gill sans mt condensed', 25), height=1, command=lambda: root.quit())
# canvas.create_something()-----------------
se_canvas_2.create_image(75, 100, image=sedice)
se_biggest_canvas.create_text(750, 90, text='Snake-Eyes', font=('pristina', 60, 'bold'))

# others------------------------------------

var = IntVar()
bet_entry = Entry(se_canvas, font=18, textvariable=var)
first_dice_num = randint(1, 6)
second_dice_num = randint(1, 6)
dice_1 = Label(se_canvas, image=None, bd=0, bg='#143d59')
dice_2 = Label(se_canvas, image=None, bd=0, bg='#143d59')
menu_btn_se = Button(se_biggest_canvas, image=bars,
                     command=lambda: show_btns(home_page, guess_g, high_low, quit_btn, menu_btn_se))


# functions----------------------------------


def popup():
    global first_dice_num, second_dice_num
    first_dice_num = randint(1, 6)
    second_dice_num = randint(1, 6)

    question = messagebox.askyesno('Play again ?', 'Do you want to play again??')

    if question == 1:
        result_label.place_forget()
        dice_1.place_forget()
        dice_2.place_forget()
        bet_entry.delete(0, 'end')

    else:
        show_frame(startpage)


def roll_dice():
    wait_pls = ['Hold your BREATH', 'Rolling dices...',
                f'Do you know\nProbability of getting both\nsnake eyes is 2.8% XD',
                "You can only write\n WHOLE NUMBERS\notherwise it won't work."]
    waiting_lbl = Label(se_canvas, text=choice(wait_pls), font=('gill sans mt condensed', 25), width=50, fg='#f4b41a',
                        bg='#143d59')
    waiting_lbl.place(relx=0.5, rely=0.75, anchor='center')

    def now_u_c_me():
        global dice_1, dice_2
        waiting_lbl.place_forget()

        dice_1.place(relx=0.4, rely=0.8, anchor='center')
        dice_2.place(relx=0.6, rely=0.8, anchor='center')
        result_label.place(relx=0.5, rely=0.85, anchor='center')
        try:
            if type(var.get()) == int and var.get() >= 1 and int(bet_entry.get()) % 1 == 0:

                if first_dice_num == 1:
                    dice_1.config(image=face1)
                elif first_dice_num == 2:
                    dice_1.config(image=face2)
                elif first_dice_num == 3:
                    dice_1.config(image=face3)
                elif first_dice_num == 4:
                    dice_1.config(image=face4)
                elif first_dice_num == 5:
                    dice_1.config(image=face5)
                else:
                    dice_1.config(image=face6)

                if second_dice_num == 1:
                    dice_2.config(image=face1)
                elif second_dice_num == 2:
                    dice_2.config(image=face2)
                elif second_dice_num == 3:
                    dice_2.config(image=face3)
                elif second_dice_num == 4:
                    dice_2.config(image=face4)
                elif second_dice_num == 5:
                    dice_2.config(image=face5)
                else:
                    dice_2.config(image=face6)

                if first_dice_num == 1 and second_dice_num == 1:
                    result_label.config(
                        text=f"OP Dude!!! You got both snake's eyes\nSo, now you get 10 times your bet\n{int(var.get()) * 10}")

                elif first_dice_num == 1 or second_dice_num == 1:
                    result_label.config(
                        text=f"Congrats!! You got one snake's eye\nSo, now you get double your bet\n{int(var.get()) * 2}")


                else:
                    result_label.config(text="Awwww, don't be sad\nYou'll get them next time")

        except Exception:
            dice_1.config(text='')
            dice_2.config(text='')
            result_label.config(text="You dumb dumb\nTry whole numbers next time")
            if len(bet_entry.get()) == 0:
                result_label.config(
                    text='So now you want me to\nread your mind. Let me tell you\nThat is never going to happen.')

    waiting_lbl.after(3000, now_u_c_me)
    waiting_lbl.after(5000, popup)


# placing-----------------------------------
se_frame_a.place(relx=0, rely=0)
se_biggest_canvas.place(relx=0, rely=0)
se_canvas.place(relx=0.5, rely=0.5, anchor='center')
se_canvas_2.place(relx=0.35, rely=0.1, anchor='center')
bet_entry.place(relx=0.75, rely=0.2, anchor='center', height=30)
bet_entry.delete(0)
place_bet.place(relx=0.3, rely=0.2, anchor='center')
menu_btn_se.place(relx=0.075, rely=0.1, anchor='center')
#uhhh.......
se_submit_btn = Button(se_canvas, text='Rock and Roll', font=('gill sans mt condensed', 25), command=roll_dice)
se_submit_btn.place(relx=0.5, rely=.45, anchor='center')
#-----------
se_rules_button.place(relx=0.875, rely=0.1, anchor='center')

# =============================================gg frame=================================================================
# -----------frames/canvases-----------------
shadywidth = 600
shadyheight = 450
gg_biggest_canvas = Canvas(gg_frame, width=win_width, height=win_height, bg='#f7c5cc', highlightthickness=0)
gg_shady_canvas = Canvas(gg_biggest_canvas, bg='#f7b0b6', width=shadywidth, height=shadyheight, highlightthickness=0)
gg_redish_frame = Frame(gg_biggest_canvas, bg='#cc313d', width=650, height=450)

# -----------buttons------------------------
gg_high_low = Button(gg_biggest_canvas, text='High-Low', width=15, bg='#cc313d', fg='#f7c5cc',
                     font=('gill sans mt condensed', 25), height=1, command=lambda: show_frame(hl_frame))
gg_homepage = Button(gg_biggest_canvas, text='Home-Page', width=15, bg='#cc313d', fg='#f7c5cc',
                     font=('gill sans mt condensed', 25), height=1, command=lambda: show_frame(startpage))
gg_se_btn = Button(gg_biggest_canvas, text='Snake-Eyes', width=15, bg='#cc313d', fg='#f7c5cc',
                   font=('gill sans mt condensed', 25), height=1, command=lambda: show_frame(se_frame))
gg_quit_btn = Button(gg_biggest_canvas, text='QUIT', width=15, bg='#cc313d', fg='#f7c5cc',
                     font=('gill sans mt condensed', 25), height=1, command=lambda: root.quit())
gg_rules_btn = Button(gg_biggest_canvas, text='Rules', font=('gill sans mt condensed', 20), width=7, height=1, fg='#cc313d', bg='#f7b0b6', command=lambda:rules_box(gg_text_box, gg_rules))
# -----------labels/create_text-------------------------
gg_biggest_canvas.create_text(win_width / 2, win_height / 8, text='Guess - Game',
                              font=('gill sans mt condensed', 75, 'bold'), fill='#f7b0b6')
gg_biggest_canvas.create_text(win_width / 1.96, win_height / 8.75, text='Guess - Game',
                              font=('gill sans mt condensed', 75, 'bold'), fill='#cc313d')
guess_it_lbl = Label(gg_redish_frame, text='Guess the number -', font=('gill sans mt condensed', 30), fg='#f7c5cc',
                     bg='#cc313d')
gg_result_lbl = Label(gg_redish_frame, text='', bg='#cc313d', fg='#f7b0b6', font=('gill sans mt condensed', 30),
                      width=500)
retry_text = gg_shady_canvas.create_text(18, shadyheight / 2, text='', font=('gill sans mt condensed', 22),
                                         fill='#cc313d', angle=90)

#text box stuff------------------------------------------
gg_text_box = Text(gg_biggest_canvas, bg='#f7c5cc', fg='#cc313d', font=('gill sans mt condensed', 25))  # width=35, height=8,
gg_rules = "\n\nThis game is simple, you may have played it.\nSo, there will be a random number in the range of 1 and 20,\nAnd you will be given 5 tries and in those 5 tries \nyou have to guess what that random number is."

#it shouldn't be here but it is--------------------------
retry = 1
#functions--------------------------------------------------------


def play_again():
    global retry, guess_num, retry_text
    gg_play_again_btn.place_forget()
    gg_result_lbl.config(text='')
    retry = 1
    guess_num = randint(1, 20)
    gg_entry.delete(0, 'end')
    gg_shady_canvas.itemconfig(retry_text, state='hidden')


def guessing():
    global retry, guess_num, retry_text
    try:
        guess = gg_var.get()
        if retry < 5:
            gg_shady_canvas.itemconfig(retry_text, text=f'Guess #{retry}', state='normal')
            if 1 <= guess <= 20:
                retry += 1
                if guess_num < guess:
                    gg_result_lbl.config(text=f'You guessed it way toooo HIGH\nSo just slow down a bit.')
                elif guess_num > guess:
                    gg_result_lbl.config(
                        text=f'You guessed it way toooo LOW\nSo just let your imagination touch the skies.')
                else:
                    gg_result_lbl.config(
                        text=f"So that is how you pass your exams Lmao\nGood job btw, {guess_num} was the number ")
                    gg_play_again_btn.place(relx=0.5, rely=0.9, anchor='center')

            else:
                gg_result_lbl.config(
                    text="Don't you understand you have to\nenter whole numbers in the range of 1 and 20")
        else:
            gg_result_lbl.config(text=f'You have ran out of retries.\nIt was {guess_num}')
            gg_shady_canvas.itemconfig(retry_text, text=f'Guess #5')
            gg_play_again_btn.place(relx=0.5, rely=0.9, anchor='center')
    except Exception:
        gg_result_lbl.config(text=f'Whole Numbers only!\nAnd that also in the range of\n1 and 20')


# other things------------------------------
gg_menu = Button(gg_biggest_canvas, image=bars,
                 command=lambda: show_btns(gg_homepage, gg_high_low, gg_se_btn, gg_quit_btn, gg_menu))
guess_num = randint(1, 20)
gg_play_again_btn = Button(gg_redish_frame, text='Play Again', font=('gill sans mt condensed', 18), fg='#cc313d',
                           bg='#f7c5cc', command=play_again)
# entry widget stuff------------------------
gg_var = IntVar()
gg_entry = Entry(gg_redish_frame, textvariable=gg_var, font=25)
guess_btn = Button(gg_redish_frame, text='Guess', font=('gill sans mt condensed', 25), bg='#f7b0b6', fg='#cc313d',
                   command=guessing)
gg_instructions = Label(gg_redish_frame, text='Click the submit button after writing your guess.\nThe range is 1-20',
                        font=('gill sans mt condensed', 15), width=100, fg='#f7b0b6', bg='#cc313d')

gg_entry.delete(0)

# -----------placing------------------------
gg_biggest_canvas.place(relx=0, rely=0)
gg_shady_canvas.place(relx=0.45, rely=0.595, anchor='center')
gg_redish_frame.place(relx=0.5, rely=0.55, anchor='center')
guess_it_lbl.place(relx=0.3, rely=0.1, anchor='center')
gg_entry.place(relx=0.75, rely=0.1, anchor='center')
gg_instructions.place(relx=0.5, rely=0.3, anchor='center')
guess_btn.place(relx=0.5, rely=0.45, anchor='center', width=100, height=50)
gg_result_lbl.place(relx=0.5, rely=0.7, anchor='center')
gg_rules_btn.place(relx=0.925, rely=0.1, anchor='center')
gg_menu.place(relx=0.1, rely=0.1, anchor='center')

# =x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==

show_frame(startpage)
root.mainloop()