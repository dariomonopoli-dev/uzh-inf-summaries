
def convert(t):
    if isinstance(t,tuple):
        t_convert = list(t)
        for index, element in enumerate(t_convert):
                t_convert[index] = convert(element)
    elif isinstance(t,str):
        t_convert = list(t)
    else:
        raise Warning('converison failed')
    return t_convert



def convert_tuple_to_list(t):
    if not isinstance(t,tuple):
        raise Warning('type error tuple')
    for element in t:
        if not isinstance(element,str):
            raise Warning('type error string')
    try:
        return convert(t)
    except:
        raise Warning('conversion failed')
        

def convert_list_to_tuple(l):
    new_list = []
    for line in l: 
        s = ''
        for i in range(len(line)):
            s+= line[i]
        new_list.append(s)
    return tuple(new_list)


def validity_of_characters(board):
    if isinstance(board,list):
        if board == []:
            return True
        else:
            return validity_of_characters(board[0]) and validity_of_characters(board[1:])
    else:
        return board in [' ','#','o']   
            

def validity_of_length(board):
    try:
        length = int(len(set([len(board[i]) for i in range (len(board))])))
        return length == 1 
    except:
        return False


def validity_of_player_count(board):
    if isinstance(board, list):
        if board == []:
            return False
        else:
            return validity_of_player_count(board[0]) + validity_of_player_count(board[1:]) == 1
    else:
        return board == 'o'

def validity_of_size(board):
    try:
        x = len(board)
    except:
        x = 0   
    try:
        y = min([len(board[i]) for i in range(x)])
    except:
        y = 0   
    return x > 0 and y > 0


def player_coordinate(board):
    x = len(board)
    y = len(board[0])
    for i in range(x):
        for j in range(y):
            if board[i][j] == 'o':
                return i,j

        
def check_move(x,y,board):
    if x not in range(len(board)) or y not in range(len(board[0])):
        return False
    elif board[x][y] == '#':
        return False
    else:
        return True

 
def possibility_of_move(board, move): 
    x,y = player_coordinate(board)
    
    if move == 'up':
        return check_move(x-1,y,board)
    elif move == 'down':
        return check_move(x+1,y,board)
    elif move == 'left':
        return check_move(x,y-1,board)
    elif move == 'right':
        return check_move(x,y+1,board)
    
    
def possible_moves(board):
    moves = ['down','left','right','up']
    possible_moves = []
    for move in moves:
        if possibility_of_move(board,move):
            possible_moves.append(move)
    return tuple(possible_moves)


def validity_of_moving(board):
        return len(possible_moves(board)) >= 1
 

def validity_of_game_state(board):
    if not validity_of_size(board):
        raise Warning('invalid size')
        return False
    elif not validity_of_length(board):
        raise Warning('invalid length')
        return False
    elif not validity_of_characters(board):
        raise Warning('invalid characters')
        return False
    elif not validity_of_player_count(board):
        raise Warning('invalid player count')
        return False
    elif not validity_of_moving(board):
        raise Warning('no possible moves')
        return False
    else:
        return True
    

def validity_of_move(board, move):
    moves = ['down','left','right','up']
    if move not in moves:
        raise Warning ('move not in list of possible moves')
    elif not possibility_of_move(board, move):
        raise Warning ('this move is not possible')
    else:
        return True
   
def move_player(target_x,target_y, board):
     x,y = player_coordinate(board)
     board[x][y] = ' '
     board[target_x][target_y] = 'o'
     return board
        

def execute_move(board, move):
    x,y = player_coordinate(board)
    
    if move == 'up':
        return move_player(x-1,y,board )
    elif move == 'down':
        return move_player(x+1,y,board )
    elif move == 'left':
        return move_player(x,y-1,board )
    elif move == 'right':
        return move_player(x,y+1,board )
    


def update_board(board,move):
    if validity_of_game_state(board):
        if validity_of_move(board, move):
            return execute_move(board, move)
    else:
        raise Warning('Invalid move')


def move(state, direction):
     board = convert_tuple_to_list(state)
     board = update_board(board, direction)
     moves = possible_moves(board)
     board = convert_list_to_tuple(board)
     return (board,moves)


s1 = (
	"#####   ",
	"###    #",
	"#   o ##",
	"   #####"
)
s2 = move(s1, "right")

print("= New State =")
print("\n".join(s2[0]))
print("\nPossible Moves: {}".format(s2[1]))
