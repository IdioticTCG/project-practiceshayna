@namespace
class SpriteKind:
    NPC = SpriteKind.create()

def on_b_pressed():
    animation.run_image_animation(Nola, assets.animation("""
        action
    """), 80, False)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_left_pressed():
    Nola.set_image(assets.image("""
        nola0
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    Nola.set_image(assets.image("""
        nola
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

interactionCount = 0
Nola: Sprite = None
scene.set_background_image(assets.image("""
    rogers house
"""))
Nola = sprites.create(assets.image("""
    nola
"""), SpriteKind.player)
Roger = sprites.create(assets.image("""
    roger
"""), SpriteKind.NPC)
Nola.set_position(28, 91)
Roger.set_position(136, 91)
controller.move_sprite(Nola, 50, 50)
Nola.z = 1
Dream = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
Dream.set_position(75, 55)
TicTacToePlayer = 0
TicTacToe = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
dialogueBank = ["Do you have my dream yet? Yes?  Thank you, mouse man!",
    "DIET PEPSI! You've fetched me my dream! In return, I will grant you three wishes. Just kidding, heh heh.",
    "Without dreams, this meager helping of life is nought but an all-consuming void of empty and ebony. My heart yearns for salvation, I hunger for dreams. Thank you for finding me my reverie, jerk."]
music.set_volume(20)
music.play(music.create_song(assets.song("""
        basic track
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_forever():
    Nola.y = 91
    Nola.z = 1000
forever(on_forever)

def on_forever2():
    global interactionCount
    if Roger.overlaps_with(Nola):
        interactionCount = interactionCount + 1
        if interactionCount == 1:
            music.play(music.melody_playable(music.ba_ding),
                music.PlaybackMode.UNTIL_DONE)
            game.show_long_text("I'm Roger, and I love trash! Ya know what else I love??? Having dreams. But ever since our dreams were severed from us, everything has just felt pointless. I need you to help me find my dream, mister dreamcatcher!",
                DialogLayout.CENTER)
        pause(800)
        if interactionCount == 2:
            game.show_long_text("Will you catch my dream for me?        Yes! = press A",
                DialogLayout.CENTER)
        if interactionCount == 3:
            scene.camera_shake(4, 500)
            effects.star_field.start_screen_effect()
            scene.set_background_image(assets.image("""
                SnowyForest
            """))
            Roger.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
            """))
            pause(500)
            music.stop_all_sounds()
            game.show_long_text("You made it to the forest! Now it's time to find Roger's dream and bring it home. To use your dreamcatcher net, press B. Be careful, though. Dreams are tricky things, and they're known for challenging people to games like tic tac toe.",
                DialogLayout.CENTER)
forever(on_forever2)
