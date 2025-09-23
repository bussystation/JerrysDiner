# Create sprites 
safetonSprite = sprites.create(assets.image("""
    safetonBase
"""), SpriteKind.player)
jokestarSprite = sprites.create(assets.image("""
    jokestarBase
"""), SpriteKind.enemy)
bassSprite = sprites.create(assets.image("""
    bassBase
"""), SpriteKind.enemy)
jazzySprite = sprites.create(assets.image("""
    jazzyBase
"""), SpriteKind.enemy)
headCollectable = sprites.create(assets.image("""
    headCollectable
"""), SpriteKind.food)
torsoCollectable = sprites.create(assets.image("""
    torsoCollectable
"""), SpriteKind.food)
armLeftCollectable = sprites.create(assets.image("""
        armLeftCollectable
    """),
    SpriteKind.food)
armRightCollectable = sprites.create(assets.image("""
        armRightCollectable
    """),
    SpriteKind.food)
legLeftCollectable = sprites.create(assets.image("""
        legLeftCollectable
    """),
    SpriteKind.food)
legRightCollectable = sprites.create(assets.image("""
        legRightCollectable
    """),
    SpriteKind.food)
# Set level 
tiles.set_current_tilemap(tilemap("""
    level
"""))
# Make spawn points 
tiles.place_on_tile(safetonSprite, tiles.get_tile_location(2, 67))
tiles.place_on_tile(jokestarSprite, tiles.get_tile_location(15, 22))
tiles.place_on_tile(bassSprite, tiles.get_tile_location(38, 64))
tiles.place_on_tile(jazzySprite, tiles.get_tile_location(55, 28))
tiles.place_on_tile(headCollectable, tiles.get_tile_location(98, 58))
tiles.place_on_tile(torsoCollectable, tiles.get_tile_location(101, 40))
tiles.place_on_tile(armLeftCollectable, tiles.get_tile_location(55, 28))
tiles.place_on_tile(armRightCollectable, tiles.get_tile_location(14, 5))
tiles.place_on_tile(legLeftCollectable, tiles.get_tile_location(4, 86))
tiles.place_on_tile(legRightCollectable, tiles.get_tile_location(23, 90))
# Text 
safetonSprite.say_text("I need to find the exit...   (6 parts left)", 3500, False)
# Make camera follow player 
scene.camera_follow_sprite(safetonSprite)
# Allow player to use wasd and arrow keys to move 
controller.move_sprite(safetonSprite)
# Allow player to interact with items by space and q 

def on_a_pressed():
    if safetonSprite.overlaps_with(headCollectable):
        sprites.destroy(headCollectable)
        info.change_score_by(1)
    elif safetonSprite.overlaps_with(armLeftCollectable):
        sprites.destroy(armLeftCollectable)
        info.change_score_by(1)
    elif safetonSprite.overlaps_with(armRightCollectable):
        sprites.destroy(armRightCollectable)
        info.change_score_by(1)
    elif safetonSprite.overlaps_with(torsoCollectable):
        sprites.destroy(torsoCollectable)
        info.change_score_by(1)
    elif safetonSprite.overlaps_with(legLeftCollectable):
        sprites.destroy(legLeftCollectable)
        info.change_score_by(1)
    elif safetonSprite.overlaps_with(legRightCollectable):
        sprites.destroy(legRightCollectable)
        info.change_score_by(1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Text when item picked up

def on_on_score():
    safetonSprite.say_text("This seems old...        (5 parts left)", 3500, False)
info.on_score(1, on_on_score)

def on_on_score2():
    safetonSprite.say_text("This suit looks strong... (4 parts left)", 3500, False)
info.on_score(2, on_on_score2)

def on_on_score3():
    safetonSprite.say_text("I could probably use this to escape... (3 parts left)",
        3500,
        False)
info.on_score(3, on_on_score3)

def on_on_score4():
    safetonSprite.say_text("I just need 2 more to fix the suit... (2 parts left)",
        3500,
        False)
info.on_score(4, on_on_score4)

def on_on_score5():
    safetonSprite.say_text("Where's the last piece? (1 part left)", 3500, False)
info.on_score(5, on_on_score5)

# Allow jumpscares 

def on_forever():
    if safetonSprite.overlaps_with(jokestarSprite):
        
        def on_start_cutscene():
            tiles.set_current_tilemap(tilemap("""
                cutScene
            """))
            scene.camera_follow_sprite(secretSprite)
            animation.run_image_animation(secretSprite,
                assets.animation("""
                    jokestarScene
                """),
                50,
                False)
            music.play(music.create_song(assets.song("""
                    jumpscareSound
                """)),
                music.PlaybackMode.UNTIL_DONE)
        story.start_cutscene(on_start_cutscene)
        
        pause(1000)
        game.reset()
    elif safetonSprite.overlaps_with(jazzySprite):
        
        def on_start_cutscene2():
            tiles.set_current_tilemap(tilemap("""
                cutScene
            """))
            scene.camera_follow_sprite(secretSprite)
            animation.run_image_animation(secretSprite,
                assets.animation("""
                    jazzyScene
                """),
                50,
                False)
            music.play(music.create_song(assets.song("""
                    jumpscareSound
                """)),
                music.PlaybackMode.UNTIL_DONE)
        story.start_cutscene(on_start_cutscene2)
        
        pause(1000)
        game.reset()
    elif safetonSprite.overlaps_with(bassSprite):
        
        def on_start_cutscene3():
            tiles.set_current_tilemap(tilemap("""
                cutScene
            """))
            scene.camera_follow_sprite(secretSprite)
            animation.run_image_animation(secretSprite,
                assets.animation("""
                    bassScene
                """),
                50,
                False)
            music.play(music.create_song(assets.song("""
                    jumpscareSound
                """)),
                music.PlaybackMode.UNTIL_DONE)
        story.start_cutscene(on_start_cutscene3)
        
        pause(1000)
        game.reset()
forever(on_forever)

# Set enemy paths 
# Jokestar path 
jokestarDirection = 0

def on_update_interval():
    global jokestarDirection
    if jokestarDirection == 0:
        jokestarSprite.vx = 50
        jokestarSprite.vy = 0
        jokestarDirection = 1
    elif jokestarDirection == 1:
        jokestarSprite.vx = 0
        jokestarSprite.vy = 50
        jokestarDirection = 2
    elif jokestarDirection == 2:
        jokestarSprite.vx = -50
        jokestarSprite.vy = 0
        jokestarDirection = 3
    elif jokestarDirection == 3:
        jokestarSprite.vx = 0
        jokestarSprite.vy = -50
        jokestarDirection = 0
    if jokestarDirection == 0:
        animation.run_image_animation(jokestarSprite,
            assets.animation("""
                jokestarWalkRight
            """),
            130,
            True)
    elif jokestarDirection == 1:
        animation.run_image_animation(jokestarSprite,
            assets.animation("""
                jokestarWalkRight
            """),
            130,
            True)
    elif jokestarDirection == 2:
        animation.run_image_animation(jokestarSprite,
            assets.animation("""
                jokestarWalkLeft
            """),
            130,
            True)
    elif jokestarDirection == 3:
        animation.run_image_animation(jokestarSprite,
            assets.animation("""
                jokestarWalkLeft
            """),
            130,
            True)
game.on_update_interval(1000, on_update_interval)

# Jazzy path 
jazzyDirection = 0

def on_update_interval2():
    global jazzyDirection
    if jazzyDirection == 0:
        jazzySprite.vx = 50
        jazzySprite.vy = 0
        jazzyDirection = 1
    elif jazzyDirection == 1:
        jazzySprite.vx = 0
        jazzySprite.vy = 50
        jazzyDirection = 2
    elif jazzyDirection == 2:
        jazzySprite.vx = -50
        jazzySprite.vy = 0
        jazzyDirection = 3
    elif jazzyDirection == 3:
        jazzySprite.vx = 0
        jazzySprite.vy = -50
        jazzyDirection = 0
    if jazzyDirection == 0:
        animation.run_image_animation(jazzySprite,
            assets.animation("""
                jazzyWalkRight
            """),
            130,
            True)
    elif jazzyDirection == 1:
        animation.run_image_animation(jazzySprite,
            assets.animation("""
                jazzyWalkRight
            """),
            130,
            True)
    elif jazzyDirection == 2:
        animation.run_image_animation(jazzySprite,
            assets.animation("""
                jazzyWalkLeft
            """),
            130,
            True)
    elif jazzyDirection == 3:
        animation.run_image_animation(jazzySprite,
            assets.animation("""
                jazzyWalkLeft
            """),
            130,
            True)
game.on_update_interval(1000, on_update_interval2)

# Bass path 
bassDirection = 0

def on_update_interval3():
    global bassDirection
    if bassDirection == 0:
        bassSprite.vx = 50
        bassSprite.vy = 0
        bassDirection = 1
    elif bassDirection == 1:
        bassSprite.vx = 0
        bassSprite.vy = 50
        bassDirection = 2
    elif bassDirection == 2:
        bassSprite.vx = -50
        bassSprite.vy = 0
        bassDirection = 3
    elif bassDirection == 3:
        bassSprite.vx = 0
        bassSprite.vy = -50
        bassDirection = 0
    if bassDirection == 0:
        animation.run_image_animation(bassSprite,
            assets.animation("""
                bassWalkRight
            """),
            130,
            True)
    elif bassDirection == 1:
        animation.run_image_animation(bassSprite,
            assets.animation("""
                bassWalkRight
            """),
            130,
            True)
    elif bassDirection == 2:
        animation.run_image_animation(bassSprite,
            assets.animation("""
                bassWalkLeft
            """),
            130,
            True)
    elif bassDirection == 3:
        animation.run_image_animation(bassSprite,
            assets.animation("""
                bassWalkLeft
            """),
            130,
            True)
game.on_update_interval(1000, on_update_interval3)

# Set player animations 

def on_left_pressed():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonWalkLeft
        """),
        130,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonWalkRight
        """),
        130,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_up_pressed():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonWalkBackward
        """),
        130,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_down_pressed():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonWalkForward
        """),
        130,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_left_released():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonStandLeft
        """),
        180,
        True)
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_right_released():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonStandRight
        """),
        180,
        True)
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_up_released():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonStandLeft
        """),
        180,
        True)
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_released():
    animation.run_image_animation(safetonSprite,
        assets.animation("""
            safetonStandRight
        """),
        180,
        True)
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

# Start cutscene  

def on_on_score6():
    sprites.destroy(jokestarSprite)
    sprites.destroy(jazzySprite)
    sprites.destroy(bassSprite)
    
    def on_start_cutscene4():
        tiles.set_current_tilemap(tilemap("""
            cutScene
        """))
        sceneSprite = sprites.create(assets.image("""
            safetonBase
        """), SpriteKind.player)
        scene.camera_follow_sprite(sceneSprite)
        animation.run_image_animation(sceneSprite,
            assets.animation("""
                endScene
            """),
            200,
            False)
        music.play(music.create_song(assets.song("""
                deathScene
            """)),
            music.PlaybackMode.UNTIL_DONE)
    story.start_cutscene(on_start_cutscene4)
    
    pause(9000)
    game.reset()
info.on_score(6, on_on_score6)

# Start secret cutscene  
secretSprite = sprites.create(assets.image("""
    secretBase
"""), SpriteKind.player)
tiles.place_on_tile(secretSprite, tiles.get_tile_location(50, 41))

def on_on_overlap(sprite, otherSprite):
    
    def on_start_cutscene5():
        tiles.set_current_tilemap(tilemap("""
            cutScene
        """))
        scene.camera_follow_sprite(secretSprite)
        animation.run_image_animation(secretSprite,
            assets.animation("""
                secretScene
            """),
            50,
            False)
        music.play(music.create_song(assets.song("""
                jumpscareSound
            """)),
            music.PlaybackMode.UNTIL_DONE)
    story.start_cutscene(on_start_cutscene5)
    
    pause(1000)
    game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)
