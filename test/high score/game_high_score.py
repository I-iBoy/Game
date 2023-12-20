


score = 10

def set_game_hight_score():
    file = open('./test/high_score.txt', 'r')
    old_hight_score = file.read()
    
    if int(old_hight_score) < score:
        file1 = open('./test/high_score.txt', 'w')
        file1.write(str(score))
        file1.close()
    
    file.close()

def reset_hight_score():
    file = open('./test/high_score.txt', 'w')
    file.write(str(0))

set_game_hight_score()
reset_hight_score()