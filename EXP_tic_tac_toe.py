import cv2
import numpy as np

# cv2.namedWindow('frame')
frame = np.zeros((729,729,3), np.uint8)
cv2.line(frame, (0,729//3),(729,729//3),(0,255,0),2)
cv2.line(frame, (0,2*729//3),(729,2*729//3),(0,255,0),2)
cv2.line(frame, (729//3,0),(729//3,729),(0,255,0),2)
cv2.line(frame, (2*729//3,0),(2*729//3,729),(0,255,0),2)

winner = np.zeros((300,733,3), np.uint8)
game_end=0

game = np.zeros((3,3))

flag=0

def cross(x, y):
    midpoint = (x+243//2,y+243//2)
    cv2.line(frame,(midpoint[0]-100,midpoint[1]-100),(midpoint[0]+100,midpoint[1]+100),(0,0,255),2)
    cv2.line(frame,(midpoint[0]-100,midpoint[1]+100),(midpoint[0]+100,midpoint[1]-100),(0,0,255),2)

def circle(x, y):
    midpoint = (x+243//2,y+243//2)
    cv2.circle(frame, midpoint, 100, (255,0,0), 2)

# str="Player 1's Turn"
str="frame"

def click_event(event, x, y, flags, param):
    player=1
    global flag,str,game_end
    if game_end:
        return
    checkpoint1=729//3
    checkpoint2=2*729//3
    if x<checkpoint1:x=0
    elif x>=checkpoint1 and x<checkpoint2: x=checkpoint1
    elif x>=checkpoint2: x=checkpoint2
    if y<checkpoint1:y=0
    elif y>=checkpoint1 and y<checkpoint2: y=checkpoint1
    elif y>=checkpoint2: y=checkpoint2

    if event==cv2.EVENT_LBUTTONDOWN and flag%2==0:
        #checking if there's already an input
        if game[x//243][y//243]:
            return
        game[x//243][y//243]=1
        cross(x,y)
        player=2
        flag+=1
        # str="Player {}'s Turn".format(player)
        # cv2.destroyAllWindows()
        cv2.imshow(str, frame)
    
    if event==cv2.EVENT_LBUTTONDOWN and flag%2:
        #checking if there's already an input
        if game[x//243][y//243]:
            return
        game[x//243][y//243]=10
        circle(x,y)
        player=1
        flag+=1
        # str="Player {}'s Turn".format(player)
        # cv2.destroyAllWindows()
        cv2.imshow(str, frame)
    
    checkdiag1=game[0][0]+game[1][1]+game[2][2]
    checkdiag2=game[0][2]+game[1][1]+game[2][0]
    for check1,check2 in zip(game.sum(axis=0),game.sum(axis=1)):
        if check1==3 or check2==3 or checkdiag1==3 or checkdiag2==3:
            cv2.putText(winner, "Player 1 Wins!", (10,150), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,255),2)
            cv2.imshow("Winner",winner)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            game_end=1
            return
        elif check1==30 or check2==30 or checkdiag1==30 or checkdiag2==30:
            cv2.putText(winner, "Player 2 Wins!", (10,150), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,255),2)
            cv2.imshow("Winner",winner)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            game_end=1
            return
    
    game_end=1
    for i in range(3):
        for j in range(3):
            game_end*=game[i][j]
    
    if game_end!=0:
        cv2.putText(winner, "DRAW!", (10,150), cv2.FONT_HERSHEY_COMPLEX, 5, (0,0,255),2)
        cv2.imshow("Winner",winner)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# cv2.putText()

cv2.imshow(str, frame)

print(str)
cv2.setMouseCallback(str,click_event)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

