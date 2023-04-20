import tkinter as tk

class Connect4:

    def __init__(self):

        self.state = 0

        self.board_dict = {}
        for i in range(7):
            self.board_dict[i] = [2,2,2,2,2,2,2]
        print(self.board_dict)

        self.window = tk.Tk()
        self.window.title("Connect 4")

        self.top_frame = tk.Frame(self.window)
        self.top_frame.grid(row = 1, column = 1)

        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.grid(row = 2, column = 1)

        self.quit_button = tk.Button(self.bottom_frame, text = "Quit Game", command = self.quit)
        self.quit_button.grid(row = 1, column = 1)

        self.play_again_button = tk.Button(self.bottom_frame, text = "Play Again", command = self.play_again)
        self.play_again_button.grid(row = 1, column = 2)

        self.canvas = tk.Canvas(self.top_frame, width = 700, height = 700, background = "Yellow")
        self.canvas.grid(row = 1, column = 1)


        for i in range(7):
            for j in range(7):
                self.canvas.create_oval(i * 100, j * 100, 100 + (i * 100), 100 + (j * 100), tag = "setup", fill = "White")

        self.canvas.bind("<ButtonRelease-1>", self.click_handler)

        self.window.mainloop()

    

    def click_handler(self, event):
        column = -1
        if event.x < 100:
            column = 0
        elif event.x < 200:
            column = 1
        elif event.x < 300:
            column = 2
        elif event.x < 400:
            column = 3
        elif event.x < 500:
            column = 4
        elif event.x < 600:
            column = 5
        elif event.x < 700:
            column = 6
        
        if self.board_dict[column][0] == 2:
            self.place_token(column)

    def place_token(self, column):
        num_of_tokens = 0
        counter = -1
        num = self.board_dict[column][counter]
        while num != 2:
            num_of_tokens += 1
            counter -= 1
            num = self.board_dict[column][counter]
        self.board_dict[column][6 - num_of_tokens] = self.state
        print(num_of_tokens)

        if self.state == 1:
            self.canvas.create_oval(column * 100, 600 - num_of_tokens * 100, (column * 100) + 100, 700 - num_of_tokens * 100, fill = "Red", tag = "gameplay")
            if self.check_winner(column, 6 - num_of_tokens) == True:
                print("winner found")
                self.state = 2
            else:
                self.state = 0
        elif self.state == 0:
            self.canvas.create_oval(column * 100, 600 - num_of_tokens * 100, (column * 100) + 100, 700 - num_of_tokens * 100, fill = "Blue", tag = "gameplay")
            if self.check_winner(column, 6 - num_of_tokens) == True:
                print("winner found")
                self.state = 2
            else:
                self.state = 1

        
        
        print(self.board_dict)

    def check_winner(self, column, row):
        try:
            winner_found = False
            if row >= 3:
                if self.board_dict[column][row + 1] == self.state and self.board_dict[column][row + 2] == self.state and self.board_dict[column][row + 3] == self.state:
                    winner_found = True
                elif self.board_dict[column - 1][row + 1] == self.state and self.board_dict[column - 2][row + 2] == self.state and self.board_dict[column - 3][row + 3] == self.state:
                    winner_found = True
                elif self.board_dict[column + 1][row + 1] == self.state and self.board_dict[column + 2][row + 2] == self.state and self.board_dict[column + 3][row + 3] == self.state:
                    winner_found = True


            return winner_found
        except IndexError:
            print("error 1 found")
            pass
        except KeyError:
            print("error 2 found")
            pass


    def quit(self):
        self.window.destroy()

    def play_again(self):
        self.board_dict = {}
        for i in range(7):
            self.board_dict[i] = [2,2,2,2,2,2,2]
        self.canvas.delete("gameplay")
        

if __name__ == "__main__":
    Connect4()
