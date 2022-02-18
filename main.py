@namespace
class SpriteKind:
    npc = SpriteKind.create()
    block = SpriteKind.create()
    boss = SpriteKind.create()
    npcasset = SpriteKind.create()
    trap = SpriteKind.create()
    notaprojectile = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    boss2.set_position(122, 24)
sprites.on_overlap(SpriteKind.player, SpriteKind.boss, on_on_overlap)

def on_on_overlap2(sprite11, otherSprite9):
    info.change_life_by(-1)
    lumber_jack.set_position(160, randint(52, 75))
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_b_pressed():
    global projectile
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e f c . . . . 
                        . f d d d d e e e f f . . . . . 
                        . . f f f f f e e e e f . . . . 
                        . . . . f f e e e e e e f . f f 
                        . . . f e e f e e f e e f . e f 
                        . . f e e f e e f e e e f . e f 
                        . f b d f d b f b b f e f f e f 
                        . f d d f d d f d d b e f f f f 
                        . . f f f f f f f f f f f f f .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e f c . . . . 
                        . f d d d d e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f f e e e e e f . f f 
                        . . f d b f e e f f e e f . e f 
                        . f f d d f e f f e e e f . e f 
                        . f f f f f f e b b f e f f e f 
                        . f d d f e e e d d b e f f f f 
                        . . f f f f f f f f f f f f f .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f e e e e e f . . . . . 
                        . . . f d d d d d e e f . . . . 
                        . . f f f d d f f d e f f . . . 
                        . c d d e e d d d d e d d f . . 
                        . c c d d d d c d d e d f f f . 
                        . c d c c c c d d d e d f b d f 
                        . . c d d d d d d e e f f d d f 
                        . . . c d d d d e e f f e f f f 
                        . . . . f f f e e f e e e f . . 
                        . . . . f e e e e e e e f f f . 
                        . . . f e e e e e e f f f e f . 
                        . . f f e e e e f f f f f e f . 
                        . f b d f e e f b b f f f e f . 
                        . f d d f e e f d d b f f f f . 
                        . f f f f f f f f f f f f f . .
            """),
            img("""
                . . . . . f f f f f . . . . . . 
                        . . . . f e e e e e f . . . . . 
                        . . . f d d d d d d e f . . . . 
                        . . f d f f d d f f d f f . . . 
                        . c d d d e e d d d d e d f . . 
                        . c d c d d d d c d d e f f . . 
                        . c d d c c c c d d d e f f f f 
                        . . c d d d d d d d e f f b d f 
                        . . . c d d d d e e f f f d d f 
                        . . . . f f f e e f e e e f f f 
                        . . . . f e e e e e e e f f f . 
                        . . . f e e e e e e f f f e f . 
                        . . f f e e e e f f f f f e f . 
                        . f b d f e e f b b f f f e f . 
                        . f d d f f f f d d b f f f f . 
                        . f f f f f f f f f f f f f . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . . f d d d d d e e f f . . . . 
                        . c d d d f f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c f f d d c d d e e b d c . . . 
                        f d d f e f f f e e e f . . . . 
                        f d d f e e e f f f f f . . . . 
                        f f f f f e e e e e f f . f f . 
                        . f f f e f f e e e f f . e f . 
                        . f b d f e f f b b f f f e f . 
                        . f d d f e e f d d b f f e f . 
                        . f f f f f f f f f f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . . f d d f d d e e f f . . . . 
                        . c d d d f d d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c f f f f d d d e e f c f . . . 
                        . f b d f f f e e e e f . . . . 
                        . f d d f e f f f e e f . . . . 
                        . . f f f e e e e f f f . f f . 
                        . . f e e f e e e e f f . e f . 
                        . f f e e e f f f f f f f e f . 
                        . f b d f e e f b b f f f e f . 
                        . f d d f f e e d d b f f f f . 
                        . f f f f f f f f f f f f f . .
            """)],
        100,
        False)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . f f . . . . . . . . . . . . . 
                    . f 5 5 . . . . . . . . . . . f 
                    . . 5 5 5 . . . . . . . . . 5 5 
                    . . . 5 5 5 . . . . . . . 5 5 5 
                    . . . . 5 5 5 . . . . . 5 5 5 . 
                    . . . . . 5 5 5 . . . 5 5 5 . . 
                    . . . . . . 5 5 5 5 5 5 5 . . . 
                    . . . . . . . 5 5 5 5 5 . . . . 
                    . . . . . . . . 5 5 5 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        -200,
        0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global projectile
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . . c f e e e d d c c c c c 
                        . . . . . f f e e e d d d d f . 
                        . . . . f e e e e f f f f f . . 
                        f f . f e e e e e e f f . . . . 
                        f e . f e e f e e f e e f . . . 
                        f e . f e e e f e e f e e f . . 
                        f e f f e f b b f b d f d b f . 
                        f f f f e b d d f d d f d d f . 
                        . f f f f f f f f f f f f f . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . . c f e e e d d c c c c c 
                        . . . . . f f e e e d d d d f . 
                        . . . . f e e e f f e e e f . . 
                        f f . f e e e e e f f f f f . . 
                        f e . f e e f f e e f b d f . . 
                        f e . f e e e f f e f d d f f . 
                        f e f f e f b b e f f f f f f . 
                        f f f f e b d d e e e f d d f . 
                        . f f f f f f f f f f f f f . .
            """),
            img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f e e e e e f . . . . 
                        . . . . f e e d d d d d f . . . 
                        . . . f f e d f f d d f f f . . 
                        . . f d d e d d d d e e d d c . 
                        . f f f d e d d c d d d d c c . 
                        f d b f d e d d d c c c c d c . 
                        f d d f f e e d d d d d d c . . 
                        f f f e f f e e d d d d c . . . 
                        . . f e e e f e e f f f . . . . 
                        . f f f e e e e e e e f . . . . 
                        . f e f f f e e e e e e f . . . 
                        . f e f f f f f e e e e f f . . 
                        . f e f f f b b f e e f d b f . 
                        . f f f f b d d f e e f d d f . 
                        . . f f f f f f f f f f f f f .
            """),
            img("""
                . . . . . . f f f f f . . . . . 
                        . . . . . f e e e e e f . . . . 
                        . . . . f e d d d d d d f . . . 
                        . . . f f d f f d d f f d f . . 
                        . . f d e d d d d e e d d d c . 
                        . . f f e d d c d d d d c d c . 
                        f f f f e d d d c c c c d d c . 
                        f d b f f e d d d d d d d c . . 
                        f d d f f f e e d d d d c . . . 
                        f f f e e e f e e f f f . . . . 
                        . f f f e e e e e e e f . . . . 
                        . f e f f f e e e e e e f . . . 
                        . f e f f f f f e e e e f f . . 
                        . f e f f f b b f e e f d b f . 
                        . f f f f b d d f f f f d d f . 
                        . . f f f f f f f f f f f f f .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d d d d d f . . 
                        . . . f d d e e d f f d d d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d f f c 
                        . . . . f e e e f f f e f d d f 
                        . . . . f f f f f e e e f d d f 
                        . f f . f f e e e e e f f f f f 
                        . f e . f f e e e f f e f f f . 
                        . f e f f f b b f f e f d b f . 
                        . f e f f b d d f e e f d d f . 
                        . . f f f f f f f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d d f d d f . . 
                        . . . f d d e e d d f d d d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . f c f e e d d d f f f f c 
                        . . . . f e e e e f f f d b f . 
                        . . . . f e e f f f e f d d f . 
                        . f f . f f f e e e e f f f . . 
                        . f e . f f e e e e f e e f . . 
                        . f e f f f f f f f e e e f f . 
                        . f e f f f b b f e e f d b f . 
                        . f f f f b d d e e f f d d f . 
                        . . f f f f f f f f f f f f f .
            """)],
        100,
        False)
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . f f . . . . . . . . . . . . . 
                    . f 5 5 . . . . . . . . . . . f 
                    . . 5 5 5 . . . . . . . . . 5 5 
                    . . . 5 5 5 . . . . . . . 5 5 5 
                    . . . . 5 5 5 . . . . . 5 5 5 . 
                    . . . . . 5 5 5 . . . 5 5 5 . . 
                    . . . . . . 5 5 5 5 5 5 5 . . . 
                    . . . . . . . 5 5 5 5 5 . . . . 
                    . . . . . . . . 5 5 5 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite7, otherSprite6):
    if info.score() == 25:
        boss2.set_image(img("""
            ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ..........ffff..........
                        ........ff1111ff........
                        .......fb111111bf.......
                        .......f11111111f.......
                        ......fd11111111df......
                        ...968fd11111111df......
                        ..968.fd11111111df......
                        ..968.fd11111111df......
                        ..968.fddd1111dddff.....
                        ..968.fbdb2dd2bdbfcf....
                        ..9668fcdc2112cdcfbf....
                        ...966fffbdb1bdffcf.....
                        ....fcb1bcffffff........
                        ....f1c1c1ffffff........
                        ....fdfdfdfffff.........
                        .....f.f.f..............
                        ........................
                        ........................
                        ........................
        """))
        boss2.set_position(122, 24)
        info.change_score_by(1)
    elif info.score() == 75:
        boss2.destroy()
        scene.set_background_color(9)
        tiles.set_current_tilemap(tilemap("""
            level5
        """))
        mySprite.set_position(40, 110)
    else:
        info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.boss, on_on_overlap3)

def on_on_overlap4(sprite8, otherSprite7):
    if game.ask_for_number("what is the password?", 2) == 10:
        password1.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.block, on_on_overlap4)

def on_on_overlap5(sprite10, otherSprite8):
    info.change_score_by(1)
    otherSprite8.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap5)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . f f 
                        c c c c c d d d e e f c . f e f 
                        . f d d d d d e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f e f 
                        . . . f e f f e f e e e e f f . 
                        . . . f e f f e f e e e e f . . 
                        . . . f d b f d b f f e f . . . 
                        . . . f d d c d d b b d f . . . 
                        . . . . f f f f f f f f f . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        c d e e d d d d e e d d f . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e b d c . f f 
                        . f d d d d e e e f f c . f e f 
                        . f f f f f f e e e e f . f e f 
                        . f f f f e e e e e e e f f e f 
                        f d d f d d f e f e e e e f f . 
                        f d b f d b f e f e e e e f . . 
                        f f f f f f f f f f f f e f . . 
                        . . . . . . . . . f c d d f . . 
                        . . . . . . . . . . f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f f . . . . 
                        . c d d d d d d e e d d f . . . 
                        . c d f d d f d e e b d c . . . 
                        c d d f d d f d e e b d c . f f 
                        c d e e d d d d e e f c . f e f 
                        c d d d d c d e e e f . . f e f 
                        . f c c c d e e e f f . . f e f 
                        . . f f f f f e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . f f e f e e f e e e e f . . 
                        . f e f f e e f f f e e e f . . 
                        f d d b d d c f f f f f f b f . 
                        f d d c d d d f . . f c d d f . 
                        . f f f f f f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f f f . . . . 
                        . . f d d d e e e e d d f . . . 
                        . c d d d d d e e e b d c . . . 
                        . c d d d d d d e e b d c . . . 
                        c d d f d d f d e e f c . f f . 
                        c d d f d d f d e e f . . f e f 
                        c d e e d d d d e e f . . f e f 
                        . f d d d c d e e f f . . f e f 
                        . . f f f d e e e e e f . f e f 
                        . . . . f e e e e e e e f f f . 
                        . . . . f f e e e e e b f f . . 
                        . . . f e f f e e c d d f f . . 
                        . . f d d b d d c f f f . . . . 
                        . . f d d c d d d f f . . . . . 
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . . . 
                        . . . f e e e e e f . . . . . . 
                        . . f d d d d e e e f . . . . . 
                        . c d f d d f d e e f f . . . . 
                        . c d f d d f d e e d d f . . . 
                        c d e e d d d d e e b d c . . . 
                        c d d d d c d d e e b d c . . . 
                        c c c c c d d e e e f c . . . . 
                        . f d d d d e e e f f . . . . . 
                        . . f f f f f e e e e f . . . . 
                        . . . . f f e e e e e e f . f f 
                        . . . f e e f e e f e e f . e f 
                        . . f e e f e e f e e e f . e f 
                        . f b d f d b f b b f e f f e f 
                        . f d d f d d f d d b e f f f f 
                        . . f f f f f f f f f f f f f .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_countdown_end():
    global password1
    password1 = sprites.create(img("""
            d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 1 1 1 1 1 1 
                    b b b b b b b b b b b b b b b b 
                    b b b b b b b b b b b b b b b b 
                    d d d d d d d b b 1 1 1 1 1 1 1 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d 
                    d d d d d d d b b 1 d d d d d d
        """),
        SpriteKind.block)
    if info.score() == 10:
        mySprite.set_position(12, 11)
        password1.set_position(103, 25)
        projectile.destroy()
        scene.set_background_color(10)
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
info.on_countdown_end(on_countdown_end)

def on_on_overlap6(sprite3, otherSprite3):
    global lumber_jack
    wizard.set_image(img("""
        . . . . . . . c c c . . . . . . 
                . . . . . . c b 5 c . . . . . . 
                . . . . c c c 5 5 c c c . . . . 
                . . c c b c 5 5 5 5 c c c c . . 
                . c b b 5 b 5 5 5 5 b 5 b b c . 
                . c b 5 5 b b 5 5 b b 5 5 b c . 
                . . f 5 5 5 b b b b 5 5 5 c . . 
                . . f f 5 5 5 5 5 5 5 5 f f . . 
                . . f f f b f e e f b f f f . . 
                . . f f f 1 f b b f 1 f f f . . 
                . . . f f b b b b b b f f . . . 
                . . . e e f e e e e f e e . . . 
                . . e b c b 5 b b 5 b f b e . . 
                . . e e f 5 5 5 5 5 5 f e e . . 
                . . . . c b 5 5 5 5 b c . . . . 
                . . . . . f f f f f f . . . . .
    """))
    for index in range(1):
        wizard.say_text("The lumber jacks are attacking us help us!")
        pause(1000)
        wizard.say_text(game.ask("Help the wizard?"))
    if True:
        wizard.destroy(effects.fire, 500)
        info.start_countdown(10)
        for index2 in range(10):
            lumber_jack = sprites.create(img("""
                    ..............ffffff....
                                    .............f2feeeeff..
                                    ............f222feeeeff.
                                    .......cc...feeeeffeeef.
                                    .......cdc.fe2222eeffff.
                                    .......cddcf2effff222ef.
                                    ........cddcffeeefffffff
                                    .........cddce44fbe44eff
                                    ..........cdceddf14d4eef
                                    ..........cccdeddd4eeef.
                                    ...........edd4e44eeff..
                                    ............ee442222f...
                                    .............f2e2222f...
                                    .............f554444f...
                                    ..............ffffff....
                                    ................fff.....
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                                    ........................
                """),
                SpriteKind.enemy)
            lumber_jack.set_position(160, randint(52, 75))
            lumber_jack.set_velocity(-100, 0)
            lumber_jack.follow(mySprite, 50)
            animation.run_image_animation(lumber_jack,
                [img("""
                        . . . . f f f f f f . . . . . . 
                                        . . . f 2 f e e e e f f . . . . 
                                        . . f 2 2 2 f e e e e f f . . . 
                                        . . f e e e e f f e e e f . . . 
                                        . f e 2 2 2 2 e e f f f f . . . 
                                        . f 2 e f f f f 2 2 2 e f . . . 
                                        . f f f e e e f f f f f f f . . 
                                        . f e e 4 4 f b e 4 4 e f f . . 
                                        . . f e d d f 1 4 d 4 e e f . . 
                                        . . . f d d d d 4 e e e f . . . 
                                        . . f f f f f f f f f f f f f . 
                                        . . . f 2 2 2 e d d 4 . b b b . 
                                        . . . f 2 2 2 e d d e . b b b . 
                                        . . . f 5 5 4 f e e f . . . . . 
                                        . . . . f f f f f f . . . . . . 
                                        . . . . . . f f f . . . . . . .
                    """),
                    img("""
                        . . . . . . . . . . . . . . . . 
                                        . . . . f f f f f f . . . . . . 
                                        . . . f 2 f e e e e f f . . . . 
                                        . . f 2 2 2 f e e e e f f . . . 
                                        . . f e e e e f f e e e f . . . 
                                        . f e 2 2 2 2 e e f f f f . . . 
                                        . f 2 e f f f f 2 2 2 e f . . . 
                                        . f f f e e e f f f f f f f . . 
                                        . f e e 4 4 f b e 4 4 e f f . . 
                                        . . f e d d f 1 4 d 4 e e f . . 
                                        . . . f d d d e e e e e f . . . 
                                        . . f f f f f f f f f f f f f f 
                                        . . . f 2 2 e d d e f . . b b b 
                                        . . f f 5 5 f e e f f f . b b b 
                                        . . f f f f f f f f f f . b b b 
                                        . . . f f f . . . f f . . . . .
                    """),
                    img("""
                        . . . . f f f f f f . . . . . . 
                                        . . . f 2 f e e e e f f . . . . 
                                        . . f 2 2 2 f e e e e f f . . . 
                                        . . f e e e e f f e e e f . . . 
                                        . f e 2 2 2 2 e e f f f f . . . 
                                        . f 2 e f f f f 2 2 2 e f . . . 
                                        . f f f e e e f f f f f f f . . 
                                        . f e e 4 4 f b e 4 4 e f f . . 
                                        . . f e d d f 1 4 d 4 e e f . . 
                                        . . . f d d d d 4 e e e f . . . 
                                        . . . f e 4 4 4 e e f f . . . . 
                                        . . f f f f f f f f f f f f f f 
                                        . . . f 2 2 2 e d d e . . b b b 
                                        . . . f 5 5 4 f e e f . . b b b 
                                        . . . . f f f f f f . . . b b b 
                                        . . . . . . f f f . . . . . . .
                    """),
                    img("""
                        . . . . . . . . . . . . . . . . 
                                        . . . . f f f f f f . . . . . . 
                                        . . . f 2 f e e e e f f . . . . 
                                        . . f 2 2 2 f e e e e f f . . . 
                                        . . f e e e e f f e e e f . . . 
                                        . f e 2 2 2 2 e e f f f f . . . 
                                        . f 2 e f f f f 2 2 2 e f . . . 
                                        . f f f e e e f f f f f f f . . 
                                        . f e e 4 4 f b e 4 4 e f f . . 
                                        . . f e d d f 1 4 d 4 e e f . . 
                                        . . . f d d d d 4 e e e f . . . 
                                        . f f f f f f f f f f f f f f f 
                                        . . . f 2 2 2 2 e d d e . b b b 
                                        . . f f 5 5 4 4 f e e f . b b b 
                                        . . f f f f f f f f f f . b b b 
                                        . . . f f f . . . f f . . . . .
                    """)],
                500,
                True)
            pause(500)
sprites.on_overlap(SpriteKind.player, SpriteKind.npc, on_on_overlap6)

def on_on_overlap7(sprite2, otherSprite2):
    info.change_life_by(-1)
    trap2.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.trap, SpriteKind.player, on_on_overlap7)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        f f . c d b e e d d c d d d d c 
                        f e f . c f e e d d d c c c c c 
                        f e f . . f f e e d d d d d f . 
                        f e f . f e e e e f f f f f . . 
                        f e f f e e e e e e e f . . . . 
                        . f f e e e e f e f f e f . . . 
                        . . f e e e e f e f f e f . . . 
                        . . . f e f f b d f b d f . . . 
                        . . . f d b b d d c d d f . . . 
                        . . . f f f f f f f f f . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . . f e e d f d d f d c . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        f f . c d b e e e d d c c c c c 
                        f e f . c f f e e e d d d d f . 
                        f e f . f e e e e f f f f f f . 
                        f e f f e e e e e e e f f f f . 
                        . f f e e e e f e f d d f d d f 
                        . . f e e e e f e f b d f b d f 
                        . . f e f f f f f f f f f f f f 
                        . . f d d c f . . . . . . . . . 
                        . . f f f f . . . . . . . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . f f e e e d d d d f . . 
                        . . . f d d e e d d d d d d c . 
                        . . . c d b e e d f d d f d c . 
                        f f . c d b e e d f d d f d d c 
                        f e f . c f e e d d d d e e d c 
                        f e f . . f e e e d c d d d d c 
                        f e f . . f f e e e d c c c f . 
                        f e f . f e e e e f f f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f e e e e f e e f e f f . . 
                        . . f e e e f f f e e f f e f . 
                        . f b f f f f f f c d d b d d f 
                        . f d d c f . . f d d d c d d f 
                        . . f f f . . . f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . f f f e e e e e f . . . 
                        . . . f d d e e e e d d d f . . 
                        . . . c d b e e e d d d d d c . 
                        . . . c d b e e d d d d d d c . 
                        . f f . c f e e d f d d f d d c 
                        f e f . . f e e d f d d f d d c 
                        f e f . . f e e d d d d e e d c 
                        f e f . . f f e e d c d d d f . 
                        f e f . f e e e e e d f f f . . 
                        . f f f e e e e e e e f . . . . 
                        . . f f b e e e e e f f . . . . 
                        . . f f d d c e e f f e f . . . 
                        . . . . f f f c d d b d d f . . 
                        . . . . . f f d d d c d d f . . 
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . f f f f f . . . . 
                        . . . . . . f e e e e e f . . . 
                        . . . . . f e e e d d d d f . . 
                        . . . . f f e e d f d d f d c . 
                        . . . f d d e e d f d d f d c . 
                        . . . c d b e e d d d d e e d c 
                        . . . c d b e e d d c d d d d c 
                        . . . . c f e e e d d c c c c c 
                        . . . . . f f e e e d d d d f . 
                        . . . . f e e e e f f f f f . . 
                        f f . f e e e e e e f f . . . . 
                        f e . f e e f e e f e e f . . . 
                        f e . f e e e f e e f e e f . . 
                        f e f f e f b b f b d f d b f . 
                        f f f f e b d d f d d f d d f . 
                        . f f f f f f f f f f f f f . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap8(sprite6, otherSprite5):
    info.change_life_by(-1)
    projectile2.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.notaprojectile, SpriteKind.player, on_on_overlap8)

def on_overlap_tile(sprite5, location):
    global wizard
    if info.score() == 75:
        info.set_life(5)
        wizard = sprites.create(img("""
                . . . . f f f f . . . . 
                            . . f f e e e e f f . . 
                            . f f e e e e e e f f . 
                            f f f f 4 e e e f f f f 
                            f f f 4 4 4 e e f f f f 
                            f f f 4 4 4 4 e e f f f 
                            f 4 e 4 4 4 4 4 4 e 4 f 
                            f 4 4 f f 4 1 1 1 1 1 1 
                            f e 4 d d d 1 1 1 1 1 1 
                            . f e d d b 1 f 1 f 1 f 
                            . f f e 4 4 1 1 1 1 1 1 
                            e 4 f b 1 1 1 1 1 1 1 1 
                            4 d f 1 1 1 1 1 1 f d 4 
                            4 4 f 6 6 6 6 6 6 f 4 4 
                            . . . f f f f f f . . . 
                            . . . f f . . f f . . .
            """),
            SpriteKind.npcasset)
        wizard.set_position(80, 105)
        mySprite.set_position(53, 100)
        tiles.set_current_tilemap(tilemap("""
            level6
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile)

def on_menu_pressed():
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def on_overlap_tile2(sprite9, location2):
    global boss2
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
    boss2 = sprites.create(assets.image("""
        myImage
    """), SpriteKind.boss)
    boss2.follow(mySprite, 60)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_north,
    on_overlap_tile2)

def on_on_overlap9(sprite4, otherSprite4):
    global trap2, projectile2
    if info.score() == 75:
        wizard.say_text("Wow you made it! You took out the evil monkey ghoul thanks alot! Here take this gualet it will make your punches more leathel",
            10000,
            True)
        wizard.set_image(img("""
            . . . . f f f f . . . . 
                        . . f f e e e e f f . . 
                        . f f e e e e e e f f . 
                        f f f f 4 e e e f f f f 
                        f f f 4 4 4 e e f f f f 
                        f f f 4 4 4 4 e e f f f 
                        f 4 e 4 4 4 4 4 4 e 4 f 
                        f 4 4 f f 4 4 f f 4 4 f 
                        f e 4 d d d d d d 4 e f 
                        . f e d d b b d d e f . 
                        . f f e 4 4 4 4 e f f . 
                        e 4 f b 1 1 1 1 b f 4 e 
                        4 d f 1 1 1 1 1 1 f d 4 
                        4 4 f 6 6 6 6 6 6 f 4 4 
                        . . . f f f f f f . . . 
                        . . . f f . . f f . . .
        """))
        music.power_up.play()
        game.splash("You recived a gualet upgrade!")
    info.set_score(1000)
    pause(15000)
    wizard.say_text("I WAS THE ENEMEY TH WHOLE TIME SUCKA DIE! I HAVE TRAPS!",
        2000,
        True)
    wizard.follow(mySprite, 50)
    for index3 in range(20):
        trap2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . f f . . . . . . . . . . . . . 
                            . f 5 5 . . . . . . . . . . . f 
                            . . 5 5 5 . . . . . . . . . 5 5 
                            . . . 5 5 5 . . . . . . . 5 5 5 
                            . . . . 5 5 5 . . . . . 5 5 5 . 
                            . . . . . 5 5 5 . . . 5 5 5 . . 
                            . . . . . . 5 5 5 5 5 5 5 . . . 
                            . . . . . . . 5 5 5 5 . . . . . 
                            . . . . . . 5 5 5 5 5 5 . . . . 
                            . . . . . 5 5 5 . . 5 5 5 . . . 
                            . . . . 5 5 5 . . . . 5 5 5 . . 
                            . . . 5 5 5 . . . . . . 5 5 5 . 
                            . . 5 5 5 . . . . . . . . 5 5 5 
                            . f 5 5 . . . . . . . . . . 5 5 
                            . f f . . . . . . . . . . . . .
            """),
            SpriteKind.trap)
        trap2.set_position(randint(40, 90), randint(50, 90))
        projectile2 = sprites.create(img("""
                . . . . . . 5 5 . . . . . . . . 
                            . . . . . . 5 1 5 . . . . . . . 
                            . . 5 5 . . 5 1 5 . . 5 5 . . . 
                            . . 5 1 5 . 5 1 5 2 5 1 5 . . . 
                            . . . 5 1 5 5 1 5 2 1 5 . . . . 
                            5 5 5 5 2 1 5 1 1 1 5 . . . . . 
                            5 1 1 1 1 1 1 1 1 2 5 5 5 5 5 5 
                            . 5 5 5 2 5 1 1 1 1 1 1 1 1 1 5 
                            . . . . . 2 1 1 1 5 5 2 5 5 5 . 
                            . . . . 5 1 5 1 5 1 2 . . . . . 
                            . . . 5 1 5 2 1 5 5 1 5 . . . . 
                            . . 5 1 5 . 2 1 5 . 5 1 5 . . . 
                            . . 5 5 . . 5 1 5 . . 5 5 . . . 
                            . . . . . . 5 1 5 . . . . . . . 
                            . . . . . . 5 1 5 . . . . . . . 
                            . . . . . . 5 5 . . . . . . . .
            """),
            SpriteKind.notaprojectile)
        projectile2.follow(mySprite, 60)
        pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.npcasset, on_on_overlap9)

projectile2: Sprite = None
trap2: Sprite = None
password1: Sprite = None
projectile: Sprite = None
lumber_jack: Sprite = None
boss2: Sprite = None
mySprite: Sprite = None
wizard: Sprite = None
wizard = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . c c . . . . . . . . 
            . . . . . . c 5 c . . . . . . . 
            . . . . c c c 5 5 c c c . . . . 
            . . c c c c 5 5 5 5 c b c c . . 
            . c b b 5 b 5 5 5 5 b 5 b b c . 
            . c b 5 5 b b 5 5 b b 5 5 b c . 
            . . c 5 5 5 b b 1 1 1 1 1 1 1 1 
            . . f f 5 5 5 5 1 1 1 1 1 1 1 1 
            . . f f f b f e 1 1 1 1 1 1 1 1 
            . . f f f 1 f b 1 f 1 f 1 f 1 f 
            . . . f f b b b 1 1 1 1 1 1 1 1 
            . . e b b f e e e e b b e . . . 
            . . e e f 5 5 b b e b b e . . . 
            . . . f 5 5 5 5 5 e e c . . . . 
            . . . . f f f f f f f . . . . .
    """),
    SpriteKind.npc)
mySprite = sprites.create(img("""
        . . . . . 5 5 5 5 5 . . . . . . 
            5 5 5 5 5 e e e e e 5 5 5 5 5 5 
            . . . f d d d d d e e f . . . . 
            . . f f f d d f f d e f f . . . 
            . c d d e e d d d d e d d f . . 
            . c c d d d d c d d e d f f f . 
            . c d c c c c d d d e d f b d f 
            . . c d d d d d d e e f f d d f 
            . . . c d d d d e e f f e f f f 
            . . . . f f f e e f e e e f . . 
            . . . . f e e e e e e e f f f . 
            . . . f e e e e e e f f f e f . 
            . . f f e e e e f f f f f e f . 
            . f b d f e e f b b f f f e f . 
            . f d d f e e f d d b f f f f . 
            . f f f f f f f f f f f f f . .
    """),
    SpriteKind.player)
info.set_life(3)
wizard.set_position(54, 37)
controller.move_sprite(mySprite)
scene.set_background_color(7)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(mySprite)
mySprite.set_stay_in_screen(True)