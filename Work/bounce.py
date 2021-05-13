# bounce.py
#
# Exercise 1.5

HEIGHT = 100
BOUNCE_COEF = 3/5
ball_height = HEIGHT*BOUNCE_COEF
for i in range(1,11,1):
    print(i, round(ball_height, 4))
    ball_height *= BOUNCE_COEF