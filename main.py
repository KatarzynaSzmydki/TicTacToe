from tkinter import *
import numpy as np
import random

THEME_COLOR = "#375362"

class TicTacToe:

    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.move_nbr = 0
        self.player = None
        self.opponent = None
        self.move = None
        self.v = np.empty(shape=(3,3),dtype='object')
        self.game_end = False
        self.draw_number = 1

# score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
# score_label.grid(row=0, column=1)

        self.label_player = Label(text="Make first move and click 'Move' button",fg="white",bg=THEME_COLOR)
        self.label_player.grid(row=0,column=0,columnspan=2)

        self.entry_text11 = StringVar()
        self.entry_text21 = StringVar()
        self.entry_text31 = StringVar()
        self.entry_text12 = StringVar()
        self.entry_text22 = StringVar()
        self.entry_text32 = StringVar()
        self.entry_text13 = StringVar()
        self.entry_text23 = StringVar()
        self.entry_text33 = StringVar()

        self.entry11 = Entry(textvariable=self.entry_text11)
        self.entry21 = Entry(textvariable=self.entry_text21)
        self.entry31 = Entry(textvariable=self.entry_text31)
        self.entry12 = Entry(textvariable=self.entry_text12)
        self.entry22 = Entry(textvariable=self.entry_text22)
        self.entry32 = Entry(textvariable=self.entry_text32)
        self.entry13 = Entry(textvariable=self.entry_text13)
        self.entry23 = Entry(textvariable=self.entry_text23)
        self.entry33 = Entry(textvariable=self.entry_text33)

        self.entry11.grid(row=2, column=0)
        self.entry21.grid(row=3, column=0)
        self.entry31.grid(row=4, column=0)
        self.entry12.grid(row=2, column=1)
        self.entry22.grid(row=3, column=1)
        self.entry32.grid(row=4, column=1)
        self.entry13.grid(row=2, column=2)
        self.entry23.grid(row=3, column=2)
        self.entry33.grid(row=4, column=2)

        self.button1 = Button(text='Move', command=self.getVal)
        self.button1.grid(row=5, column=1)


        self.window.mainloop()


    def getVal(self):
        self.move_nbr += 1
        self.v[0,0] = self.entry11.get().upper()
        self.v[1,0] = self.entry21.get().upper()
        self.v[2,0] = self.entry31.get().upper()
        self.v[0,1] = self.entry12.get().upper()
        self.v[1,1] = self.entry22.get().upper()
        self.v[2,1] = self.entry32.get().upper()
        self.v[0,2] = self.entry13.get().upper()
        self.v[1,2] = self.entry23.get().upper()
        self.v[2,2] = self.entry33.get().upper()

        self.check_if_won()
        if self.game_end is False:
            self.move="Wait for your opponent's move..."
            self.label_player.config(text=self.move)
            self.opponent_move()



    def opponent_move(self):
        if self.move_nbr == 1:
            if (self.v == 'X').any()==True:
                self.player = 'X'
                self.opponent = "O"
            else:
                self.player = 'O'
                self.opponent = 'X'
        self.draw()
        self.move_nbr += 1



    def draw(self):

        print(self.v)
        row = None
        col = None
        self.draw_number = 1

        if self.draw_number == 1:
            for i in range(0,3):
                # defensive
                if (self.v[i] == self.player).sum() > 1 and (self.v[i] == self.opponent).sum() == 0:
                    row = i
                    print('def1')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(row,i)
                    if self.draw_number == 0:
                        break
                elif (self.v[:, i] == self.player).sum() > 1 and (self.v[:, i] == self.opponent).sum() == 0:
                    col = i
                    print('def2')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(i,col)
                    if self.draw_number == 0:
                        break
                elif (self.v.diagonal() == self.player).sum() > 1 and (self.v.diagonal() == self.opponent).sum() == 0:
                    row=i
                    col=i
                    print('def3')
                    self.draw_check(row,col)
                    if self.draw_number == 0:
                        break
                elif (np.fliplr(self.v).diagonal() == self.player).sum() > 1 and (np.fliplr(self.v).diagonal() == self.opponent).sum() == 0:
                    row=i
                    col=2-i
                    print('def4')
                    self.draw_check(row,col)
                    if self.draw_number == 0:
                        break

        if self.draw_number == 1:
            for i in range(0, 3):
                # offensive
                if (self.v[i] == self.opponent).sum() > 1 and (self.v[i] == self.player).sum() == 0:
                    row=i
                    print('of1')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(row,i)
                    if self.draw_number == 0:
                        break
                elif (self.v[:,i] == self.opponent).sum() > 1 and (self.v[:,i] == self.player).sum() == 0:
                    col=i
                    print('of2')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(i,col)
                    if self.draw_number == 0:
                        break
                elif (self.v.diagonal() == self.opponent).sum() > 1 and (self.v.diagonal() == self.player).sum() == 0:
                    row=i
                    col=i
                    print('of3')
                    self.draw_check(row,col)
                    if self.draw_number == 0:
                        break
                elif (np.fliplr(self.v).diagonal() == self.opponent).sum() > 1 and (np.fliplr(self.v).diagonal() == self.player).sum() == 0:
                    row=i
                    col=2-i
                    print('of4')
                    self.draw_check(row,col)
                    if self.draw_number == 0:
                        break

        if self.draw_number == 1:
            for i in range(0, 3):
                if (self.v[i] == self.opponent).sum() == 1 and (self.v[i] == self.player).sum() == 0:
                    row = i
                    print('of5')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(row,i)
                    if self.draw_number == 0:
                        break
                elif (self.v[:, i] == self.opponent).sum() == 1 and (self.v[:, i] == self.player).sum() == 0:
                    col = i
                    print('of6')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(i,col)
                    if self.draw_number == 0:
                        break
                elif (self.v.diagonal() == self.opponent).sum() == 1 and (self.v.diagonal() == self.player).sum() == 0:
                    row = i
                    col = i
                    print('of7')
                    self.draw_check(row,col)
                    if self.draw_number == 0:
                        break
                elif (np.fliplr(self.v).diagonal() == self.opponent).sum() == 1 and (np.fliplr(self.v).diagonal() == self.player).sum() == 0:
                    row = i
                    col = 2 - i
                    print('of8')
                    self.draw_check(row,col)
                    if self.draw_number == 0:
                        break

        if self.draw_number == 1:
            for i in range(0, 3):
                if (self.v[i] == self.opponent).sum() == 0 and (self.v[i] == self.player).sum() == 0:
                    row = i
                    print('of9')
                    for i in range(0, 3):
                        if self.draw_number == 1:
                            self.draw_check(row,i)
                    if self.draw_number == 0:
                        break


        if self.draw_number == 1:
            if row is None and col is None:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                print('random')
                self.draw_check(row, col)



    def draw_check(self, row, col):
        if row is None:
            row = random.randint(0, 2)
            print('random row')
        if col is None:
            col = random.randint(0, 2)
            print('random col')

        print(f"checking: {row}, {col}")
        if self.v[row,col] not in ['X','O']:
            self.v[row,col]=self.opponent
            self.update_board()
            self.draw_number = 0
            print(self.v)
            self.check_if_won()
            if self.game_end is False:
                self.label_player.config(text="Your turn!")
        # else:
        #     self.draw_number = 1




    def update_board(self):

        self.entry_text11.set(self.v[0, 0])
        self.entry_text21.set(self.v[1, 0])
        self.entry_text31.set(self.v[2, 0])
        self.entry_text12.set(self.v[0, 1])
        self.entry_text22.set(self.v[1, 1])
        self.entry_text32.set(self.v[2, 1])
        self.entry_text13.set(self.v[0, 2])
        self.entry_text23.set(self.v[1, 2])
        self.entry_text33.set(self.v[2, 2])


    def check_if_won(self):
        won = None
        for row in range(0,3):
            if (self.v[row] == self.player).sum() == 3 or (self.v[:,row] == self.player).sum() == 3:
                won='player'
            elif (self.v[row] == self.opponent).sum() == 3 or (self.v[:,row] == self.opponent).sum() == 3:
                won='opponent'
        if (self.v.diagonal() == self.player).sum() == 3 or (np.fliplr(self.v).diagonal() == self.player).sum() == 3:
            won = 'player'
        elif (self.v.diagonal() == self.opponent).sum() == 3 or (np.fliplr(self.v).diagonal() == self.opponent).sum() == 3:
            won = 'opponent'
        print(won)

        if won is not None:
            self.game_end = True
            self.button1.config(state='disabled')
            self.label_player.config(text=f"{won.title()} won!")


    def calculate_score(self):
        pass

game = TicTacToe()