# pion=pawn roi=king reine=queen cavalier=knight fou=bishop tour=rook
BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
LIGHT_GRAY = '\033[1;37m'
DARK_GRAY = '\033[1;90m'
BRIGHT_RED = '\033[1;91m'
BRIGHT_GREEN = '\033[1;92m'
BRIGHT_YELLOW = '\033[1;93m'
BRIGHT_BLUE = '\033[1;94m'
BRIGHT_MAGENTA = '\033[1;95m'
BRIGHT_CYAN = '\033[1;96m'
WHITE = '\033[1;97m'

def lb_colored(str, color, end='\033[0m'):
    return color + f'{str}' + end
def lb_new_grille():
    return [
        ['1R', '1T', '1B', '1Q', '1K', '1B', '1T', '1R'], 
        ['1P', '1P', '1P', '1P', '1P', '1P', '1P', '1P'], 
        ['■', '□', '■', '□', '■', '□', '■', '□'], 
        ['□', '■', '□', '■', '□', '■', '□', '■'], 
        ['■', '□', '■', '□', '■', '□', '■', '□'], 
        ['□', '■', '□', '■', '□', '■', '□', '■'], 
        ['2P', '2P', '2P', '2P', '2P', '2P', '2P', '2P'],
        ['2R', '2T', '2B', '2Q', '2K', '2B', '2T', '2R'],
    ]
def lb_show(g):
    the_game = lb_colored('\n       A B C D E F G H\n       ---------------\n', WHITE)
    for i in range(len(g)):
        the_game += lb_colored(f'   {8 - i} | ', WHITE)
        for j in range(len(g)):
            if j != 0:
                the_game += ' '
            if g[i][j][0] == '1':
                the_game += lb_colored(g[i][j][1], GREEN)
            elif g[i][j][0] == '2':
                the_game += lb_colored(g[i][j][1], BLUE)
            else:
                the_game += lb_colored(g[i][j], WHITE)
        the_game += '\n'
    return the_game
def lb_convert_xy(xy):
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return (alpha_list.index(xy[0].lower()), 8 - int(xy[1]))
def lb_play(g, fromer, toer):
    g[toer[1]][toer[0]] = g[fromer[1]][fromer[0]]
    if fromer[1] % 2 == 0:
        if fromer[0] % 2 == 0:
            g[fromer[1]][fromer[0]] = '■'
        else:
            g[fromer[1]][fromer[0]] = '□'
    else:
        if fromer[0] % 2 == 0:
            g[fromer[1]][fromer[0]] = '□'
        else:
            g[fromer[1]][fromer[0]] = '■'
def lb_can_play(g, here, to, player):
    print(g)
    fromer = lb_convert_xy(here)
    toer = lb_convert_xy(to)
    if int(g[fromer[1]][fromer[0]][0]) != player or g[fromer[1]][fromer[0]] == '■' or g[fromer[1]][fromer[0]] == '□':
        return False
    if ((g[fromer[1]][fromer[0]][1] == 'P' and (fromer[1] - 1 == toer[1] and player == 2)) or (fromer[1] + 1 == toer[1] and player == 1)) or (g[fromer[1]][fromer[0]][1] == 'B' and (abs(fromer[1] - toer[1]) == abs(fromer[0] - toer[0]))) or (g[fromer[1]][fromer[0]][1] == 'R' and (fromer[0] == toer[0] or toer[1] == fromer[1])) or (g[fromer[1]][fromer[0]][1] == 'K' and (abs(fromer[0] - toer[0]) == 1 or abs(fromer[1] - toer[1] == 1))) or (g[fromer[1]][fromer[0]][1] == 'Q' and ((abs(fromer[1] - toer[1]) == abs(fromer[0] - toer[0])) or (fromer[0] == toer[0] or toer[1] == fromer[1]))):
        lb_play(g, fromer, toer)
        return True
    return False

player = 1
grid = lb_new_grille()
while True:
    print(lb_show(grid))
    if player == 1:
        todo = input(lb_colored('Player 1 : ', GREEN)).lower().split(' ')
    else:
        todo = input(lb_colored('Player 2 : ', BLUE)).lower().split(' ')
    if todo[0] == 'play':
        if not(lb_can_play(grid, todo[1], todo[2], player)):
            print(lb_colored('Error move impossible', RED))
            continue
    elif todo[0] == 'help' or todo[0] == 'h':
        print(f"""
    {lb_colored('Commands :', MAGENTA)} 
        {lb_colored('-', WHITE)} {lb_colored('play [piece\'s position] [piece\'s finished]', CYAN)} {lb_colored('-', WHITE)} {lb_colored('To move a piece', YELLOW)}
        {lb_colored('-', WHITE)} {lb_colored('q', CYAN)} {lb_colored('|', WHITE)} {lb_colored('quit', CYAN)} {lb_colored('|', WHITE)} {lb_colored('exit', CYAN)} {lb_colored('-', WHITE)} {lb_colored('To exit the chess game', YELLOW)}
        {lb_colored('-', WHITE)} {lb_colored('h', CYAN)} {lb_colored('|', WHITE)} {lb_colored('help', CYAN)} {lb_colored('-', WHITE)} {lb_colored('To get help (or not)', YELLOW)}
    {lb_colored('Developed by Louis Blonde :', MAGENTA)} 
        {lb_colored('-', WHITE)} {lb_colored('@omonyx', CYAN)} {lb_colored('-', WHITE)} {lb_colored('Github', YELLOW)}
        {lb_colored('-', WHITE)} {lb_colored('@omonyx_sama', CYAN)} {lb_colored('-', WHITE)} {lb_colored('Instagram', YELLOW)}
               """)
        input('Press ENTER to pass... ')
        continue
    elif todo[0] == 'q' or todo[0] == 'quit' or todo[0] == 'exit':
        exit()
    else:
        print(lb_colored(f'Error \'{todo[0]}\' is not a command', RED))
        continue
    player = player % 2 + 1
