namespace SpriteKind {
    export const NPC = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    Nola,
    assets.animation`action`,
    80,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    Nola.setImage(assets.image`nola0`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    Nola.setImage(assets.image`nola`)
})
let interactionCount = 0
let Nola: Sprite = null
scene.setBackgroundImage(assets.image`rogers house`)
Nola = sprites.create(assets.image`nola`, SpriteKind.Player)
let Roger = sprites.create(assets.image`roger`, SpriteKind.NPC)
Nola.setPosition(28, 91)
Roger.setPosition(136, 91)
controller.moveSprite(Nola, 50, 50)
Nola.z = 1
let Dream = sprites.create(img`
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
    `, SpriteKind.Food)
Dream.setPosition(75, 55)
let TicTacToePlayer = 0
let TicTacToe = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
let dialogueBank = ["Do you have my dream yet? Yes?  Thank you, mouse man!", "DIET PEPSI! You've fetched me my dream! In return, I will grant you three wishes. Just kidding, heh heh.", "Without dreams, this meager helping of life is nought but an all-consuming void of empty and ebony. My heart yearns for salvation, I hunger for dreams. Thank you for finding me my reverie, jerk."]
music.setVolume(20)
music.play(music.createSong(assets.song`basic track`), music.PlaybackMode.LoopingInBackground)
forever(function () {
    Nola.y = 91
    Nola.z = 1000
})
forever(function () {
    if (Roger.overlapsWith(Nola)) {
        interactionCount = interactionCount + 1
        if (interactionCount == 1) {
            music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
            game.showLongText("I'm Roger, and I love trash! Ya know what else I love??? Having dreams. But ever since our dreams were severed from us, everything has just felt pointless. I need you to help me find my dream, mister dreamcatcher!", DialogLayout.Center)
        }
        pause(800)
        if (interactionCount == 2) {
            game.showLongText("Will you catch my dream for me?        Yes! = press A", DialogLayout.Center)
        }
        if (interactionCount == 3) {
            scene.cameraShake(4, 500)
            effects.starField.startScreenEffect()
            scene.setBackgroundImage(assets.image`SnowyForest`)
            Roger.setImage(img`
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
                `)
            pause(500)
            music.stopAllSounds()
            game.showLongText("You made it to the forest! Now it's time to find Roger's dream and bring it home. To use your dreamcatcher net, press B. Be careful, though. Dreams are tricky things, and they're known for challenging people to games like tic tac toe.", DialogLayout.Center)
        }
    }
})
