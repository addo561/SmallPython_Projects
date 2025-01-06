import random


class TicTactoe:
    def __init__(self):
        self.board = []
        
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)    
        
        
    def get_random_first_player(self):
        return random.randint(0,1)
    
    def fix_player(self,row,col,player):
        self.board[row][col] = player
    

    def hasWon(self,player):
        win = None
        
        n = len(self.board)
        
        #check-row
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win        
        
        #check-col
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win            
                
        #check diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
               win = False
               break
        if win : 
            return win           
            
        win= True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False  
                break   
        if win:
            return win
        
    
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True    
    
    def is_board_filled(self):
        for i in self.board:
            for j in i:
                if j == '-':
                    return False
        return True
    
    def swap_turn(self,player):
        return 'X' if player == '0' else '0'
    
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item , end=' ')
            print()    
    
    def start(self):
        self.create_board()
        
        player = 'X' if self.get_random_first_player() == 1 else '0'
        while True:
            print(f'Player {player} turn')
            
            self.show_board()
            
            row,col = list(map(int,input('Enter row and column: ').split()))
            print() 
            
            #fixing spot
            self.fix_player(row-1,col-1,player)    
            
            # check for win
            if self.hasWon(player):
                print(f'Player {player} wins')
                break
            
            
            #check for draw
            if self.is_board_filled():
                print('Draw')
                break      
            
            
            #swapping turn 
            player = self.swap_turn(player)
            
            
        print()
        self.show_board()
            
tic_tac_toe = TicTactoe()
tic_tac_toe.start()            