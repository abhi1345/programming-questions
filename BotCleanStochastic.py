#!/bin/python3

def nextMove(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
    
    
    
    else:
        i = 0
        while i < len(board):
            if 'd' in board[i]:
                if i < posr:
                    print("UP")

                elif i > posr:
                    print("DOWN")


                elif i == posr:
                    index = board[i].index('d')
                    
                    if index > posc:
                        print("RIGHT")
                        
                    else:
                        print("LEFT")



            i += 1
    
    
    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
