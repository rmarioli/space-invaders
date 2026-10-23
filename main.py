from turtle import Screen
import ship
import bullet
import screen
import scoreboard
import aliens
import obstacles
import time
import random


# ============================ Create screen ===============================
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Space Invadors")
s.tracer(0)


# ===================== Create Elements and variables =========================
ship = ship.Ship((0, -250))
set_up = screen.ScreenSetUp()
scoreboard = scoreboard.Scoreboard()
alien_posy = 205
aliens_created = []
obstacles_created = []
ship_bullet = None
alien_bullets = []
del_bbul = False
shoot_alien_count = 0
shoot_alien_frec = 11
dir_alien = 1
move_alien_down = False
game_on = True


# ============================= Create bullet ===============================
def create_bullet(pos, bullet_direction, objectt):
    global ship_bullet, alien_bullets
    if objectt == "ship":
        if ship_bullet is None:
            ship_bullet = bullet.Bullet(pos, bullet_direction)
    else:
        alien_bullets.append(bullet.Bullet(pos, bullet_direction))


# =========================== Create aliens ===================================
for a in range(0, 3):
    rw_aliens = []
    alien_posx = -322
    for i in range(0, 11):
        alien_posx = alien_posx + 32
        rw_aliens.append(aliens.Alien((alien_posx, alien_posy)))
    aliens_created.append(rw_aliens)
    alien_posy = alien_posy - 30


# ========================== Create obstacles =============================
def create_obstacles(posx):
    obs = []
    obs.append(obstacles.Obstacle((posx-20, -170)))
    obs.append(obstacles.Obstacle((posx-20, -150)))
    obs.append(obstacles.Obstacle((posx, -150)))
    obs.append(obstacles.Obstacle((posx+20, -150)))
    obs.append(obstacles.Obstacle((posx+20, -170)))
    return obs

obstacles_created.append(create_obstacles(-210))
obstacles_created.append(create_obstacles(-70))
obstacles_created.append(create_obstacles(70))
obstacles_created.append(create_obstacles(210))


# ================================ Keys set up ============================
s.listen()
s.onkey(ship.rightt, "Right")
s.onkey(ship.leftt, "Left")
s.onkey(lambda: create_bullet((ship.xcor(), ship.ycor()), 1, "ship"), "space")


# ======================= Start the game =====================================
while game_on:
    s.update()
    time.sleep(0.04)
    shoot_alien_count += 1
    last_alien=0
    first_alien=0

    #======================== Random shoot alien =============================
    if shoot_alien_count == shoot_alien_frec:
        shoot_alien_count = 0
        random_alien = random.choice(random.choice(aliens_created))
        create_bullet((random_alien.xcor(), random_alien.ycor()), -1, "alien")

    if any(alien_bullets):
        for alien_bullet in alien_bullets:
            alien_bullet.bullet_move()
            stop = False
            # ====================== Collision with obstacles =====================================
            for obstac in obstacles_created:
                for square in obstac:
                    if alien_bullet.distance(square) < 15 and abs(alien_bullet.ycor() - square.ycor()) < 10:
                        alien_bullet.hideturtle()
                        alien_bullets.remove(alien_bullet)
                        stop = True
                        if square.obst_damage():
                            square.hideturtle()
                            obstac.remove(square)
                            del square
                        break
                if stop:
                    break

            # ============================= Collision with ship ===============================
            if alien_bullet.distance(ship) < 15 and abs(alien_bullet.ycor() - ship.ycor()) < 15:
                alien_bullet.hideturtle()
                alien_bullets.remove(alien_bullet)
                scoreboard.life_subs()

            # ======================= Delete ship bullet =====================================
            try:
                if alien_bullet.ycor() > 280:
                    alien_bullet.hideturtle()
                    del alien_bullet
                    alien_bullet  = None
            except:
                pass

    # =================== Loop Aliens ====================
    for row_alien in aliens_created:
        for actual_alien in row_alien:
            #=================== Move Logic ====================
            actual_alien.alien_move_x(dir_alien)
            if move_alien_down:
                actual_alien.sety(actual_alien.ycor() - 10)
            #============= Get first and last alien ================
            if actual_alien.xcor() > last_alien:
                last_alien = actual_alien.xcor()
            elif actual_alien.xcor() < first_alien:
                first_alien = actual_alien.xcor()



    if ship_bullet is not None:
        ship_bullet.bullet_move()
        # ========================= Collision with aliens ==========================
        for row_alien in aliens_created:
            for actual_alien in row_alien:
                if ship_bullet.distance(actual_alien) < 15 and abs(ship_bullet.ycor() - actual_alien.ycor()) < 15:
                    scoreboard.point_up()
                    actual_alien.hideturtle()
                    row_alien.remove(actual_alien)
                    del actual_alien
                    del_bbul = True
            if not any(row_alien):
                aliens_created.remove(row_alien)

        # ====================== Collision with obstacles =====================================
        for obstac in obstacles_created:
            for square in obstac:
                if ship_bullet.distance(square) < 15 and abs(ship_bullet.ycor() - square.ycor()) < 10:
                    if square.obst_damage():
                        square.hideturtle()
                        obstac.remove(square)
                        del square
                    del_bbul = True


        # ======================= Delete ship bullet =====================================
        if del_bbul:
            ship_bullet.hideturtle()
            del ship_bullet
            del_bbul = False
            ship_bullet = None
        elif ship_bullet.ycor() > 280:
            ship_bullet.hideturtle()
            del ship_bullet
            ship_bullet = None

    # ====================== Move ships down ============================
    move_alien_down = False
    if last_alien > 280 and dir_alien == 1:
        dir_alien *= -1
    elif first_alien <-280 and dir_alien == -1:
        dir_alien *= -1
        move_alien_down=True

    # =========================== Finish conditions =====================================================
    if not any(aliens_created) or scoreboard.life_score == -1:
        game_on = False


s.exitonclick()