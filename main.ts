//Create sprites 
    let safetonSprite = sprites.create(assets.image`safetonBase`, SpriteKind.Player)
    let jokestarSprite = sprites.create(assets.image`jokestarBase`, SpriteKind.Enemy)
    let bassSprite = sprites.create(assets.image`bassBase`, SpriteKind.Enemy)
    let jazzySprite = sprites.create(assets.image`jazzyBase`, SpriteKind.Enemy)
    let headCollectable = sprites.create(assets.image`headCollectable`, SpriteKind.Food)
    let torsoCollectable = sprites.create(assets.image`torsoCollectable`, SpriteKind.Food)
    let armLeftCollectable = sprites.create(assets.image`armLeftCollectable`, SpriteKind.Food)
    let armRightCollectable = sprites.create(assets.image`armRightCollectable`, SpriteKind.Food)
    let legLeftCollectable = sprites.create(assets.image`legLeftCollectable`, SpriteKind.Food)
    let legRightCollectable = sprites.create(assets.image`legRightCollectable`, SpriteKind.Food)
//Set level 
    tiles.setCurrentTilemap(tilemap`level`)
//Make spawn points 
tiles.placeOnTile(safetonSprite, tiles.getTileLocation(1, 66))
    tiles.placeOnTile(jokestarSprite, tiles.getTileLocation(15, 22))
    tiles.placeOnTile(bassSprite, tiles.getTileLocation(38, 64))
    tiles.placeOnTile(jazzySprite, tiles.getTileLocation(55, 28))
    tiles.placeOnTile(headCollectable, tiles.getTileLocation(98, 58))
    tiles.placeOnTile(torsoCollectable, tiles.getTileLocation(101, 40))
    tiles.placeOnTile(armLeftCollectable, tiles.getTileLocation(55, 28))
    tiles.placeOnTile(armRightCollectable, tiles.getTileLocation(14, 5))
    tiles.placeOnTile(legLeftCollectable, tiles.getTileLocation(4, 86))
    tiles.placeOnTile(legRightCollectable, tiles.getTileLocation(23, 90))
//Text 
    safetonSprite.sayText("I need to find the exit...   (6 parts left)", 3500, false)
//Make camera follow player 
    scene.cameraFollowSprite(safetonSprite)
//Allow player to use wasd and arrow keys to move 
    controller.moveSprite(safetonSprite)
//Allow player to interact with items by space and q 
    controller.A.onEvent(ControllerButtonEvent.Pressed, function() {
        if (safetonSprite.overlapsWith(headCollectable)) {
            sprites.destroy(headCollectable)           
            info.changeScoreBy(1)
        } else if (safetonSprite.overlapsWith(armLeftCollectable)) {
            sprites.destroy(armLeftCollectable)
            info.changeScoreBy(1)
        } else if (safetonSprite.overlapsWith(armRightCollectable)) {
            sprites.destroy(armRightCollectable)
            info.changeScoreBy(1)
        } else if (safetonSprite.overlapsWith(torsoCollectable)) {
            sprites.destroy(torsoCollectable)
            info.changeScoreBy(1)
        } else if (safetonSprite.overlapsWith(legLeftCollectable)) {
            sprites.destroy(legLeftCollectable)
            info.changeScoreBy(1)
        } else if (safetonSprite.overlapsWith(legRightCollectable)) {
            sprites.destroy(legRightCollectable)
            info.changeScoreBy(1)
        }
    })
//Text when item picked up
    info.onScore(1, function() {
        safetonSprite.sayText("This seems old...        (5 parts left)", 3500, false)
    })
    info.onScore(2, function () {
        safetonSprite.sayText("This suit looks strong... (4 parts left)", 3500, false)
    })
    info.onScore(3, function () {
        safetonSprite.sayText("I could probably use this to escape... (3 parts left)", 3500, false)
    })
    info.onScore(4, function () {
        safetonSprite.sayText("I just need 2 more to fix the suit... (2 parts left)", 3500, false)
    })
    info.onScore(5, function () {
        safetonSprite.sayText("Where's the last piece? (1 part left)", 3500, false)
    })
//Allow jumpscares 
    forever(function () {
        if (safetonSprite.overlapsWith(jokestarSprite)) {
            story.startCutscene(function () {
                tiles.setCurrentTilemap(tilemap`cutScene`)
                scene.cameraFollowSprite(secretSprite)
                animation.runImageAnimation(secretSprite, assets.animation`jokestarScene`, 50, false)
                music.play(music.createSong(assets.song`jumpscareSound`), music.PlaybackMode.UntilDone)
            })
            pause(1000)
            game.reset()
        } else if (safetonSprite.overlapsWith(jazzySprite)) {
            story.startCutscene(function () {
                tiles.setCurrentTilemap(tilemap`cutScene`)
                scene.cameraFollowSprite(secretSprite)
                animation.runImageAnimation(secretSprite, assets.animation`jazzyScene`, 50, false)
                music.play(music.createSong(assets.song`jumpscareSound`), music.PlaybackMode.UntilDone)
            })
            pause(1000)
            game.reset()
        } else if (safetonSprite.overlapsWith(bassSprite)) {
            story.startCutscene(function () {
                tiles.setCurrentTilemap(tilemap`cutScene`)
                scene.cameraFollowSprite(secretSprite)
                animation.runImageAnimation(secretSprite, assets.animation`bassScene`, 50, false)
                music.play(music.createSong(assets.song`jumpscareSound`), music.PlaybackMode.UntilDone)
            })
            pause(1000)
            game.reset()
        }
    })
//Set enemy paths 
    //Jokestar path 
        let jokestarDirection = 0
        game.onUpdateInterval(1000, function () {
            if (jokestarDirection == 0) {
                jokestarSprite.vx = 50
                jokestarSprite.vy = 0
                jokestarDirection = 1
            } else if (jokestarDirection == 1) {
                jokestarSprite.vx = 0
                jokestarSprite.vy = 50
                jokestarDirection = 2
            } else if (jokestarDirection == 2) {
                jokestarSprite.vx = -50
                jokestarSprite.vy = 0
                jokestarDirection = 3
            } else if (jokestarDirection == 3) {
                jokestarSprite.vx = 0
                jokestarSprite.vy = -50
                jokestarDirection = 0
            }
            if (jokestarDirection == 0) {
                animation.runImageAnimation(
                    jokestarSprite,
                    assets.animation`jokestarWalkRight`,
                    130,
                    true
                )
            } else if (jokestarDirection == 1) {
                animation.runImageAnimation(
                    jokestarSprite,
                    assets.animation`jokestarWalkRight`,
                    130,
                    true
                )
            } else if (jokestarDirection == 2) {
                animation.runImageAnimation(
                    jokestarSprite,
                    assets.animation`jokestarWalkLeft`,
                    130,
                    true
                )
            } else if (jokestarDirection == 3) {
                animation.runImageAnimation(
                    jokestarSprite,
                    assets.animation`jokestarWalkLeft`,
                    130,
                    true
                )
            }
        })
    //Jazzy path 
        let jazzyDirection = 0
        game.onUpdateInterval(1000, function () {
            if (jazzyDirection == 0) {
                jazzySprite.vx = 50
                jazzySprite.vy = 0
                jazzyDirection = 1
            } else if (jazzyDirection == 1) {
                jazzySprite.vx = 0
                jazzySprite.vy = 50
                jazzyDirection = 2
            } else if (jazzyDirection == 2) {
                jazzySprite.vx = -50
                jazzySprite.vy = 0
                jazzyDirection = 3
            } else if (jazzyDirection == 3) {
                jazzySprite.vx = 0
                jazzySprite.vy = -50
                jazzyDirection = 0
            }
            if (jazzyDirection == 0) {
                animation.runImageAnimation(
                    jazzySprite,
                    assets.animation`jazzyWalkRight`,
                    130,
                    true
                )
            } else if (jazzyDirection == 1) {
                animation.runImageAnimation(
                    jazzySprite,
                    assets.animation`jazzyWalkRight`,
                    130,
                    true
                )
            } else if (jazzyDirection == 2) {
                animation.runImageAnimation(
                    jazzySprite,
                    assets.animation`jazzyWalkLeft`,
                    130,
                    true
                )
            } else if (jazzyDirection == 3) {
                animation.runImageAnimation(
                    jazzySprite,
                    assets.animation`jazzyWalkLeft`,
                    130,
                    true
                )
            }
        })
    //Bass path 
        let bassDirection = 0
        game.onUpdateInterval(1000, function () {
            if (bassDirection == 0) {
                bassSprite.vx = 50
                bassSprite.vy = 0
                bassDirection = 1
            } else if (bassDirection == 1) {
                bassSprite.vx = 0
                bassSprite.vy = 50
                bassDirection = 2
            } else if (bassDirection == 2) {
                bassSprite.vx = -50
                bassSprite.vy = 0
                bassDirection = 3
            } else if (bassDirection == 3) {
                bassSprite.vx = 0
                bassSprite.vy = -50
                bassDirection = 0
            }
            if (bassDirection == 0) {
                animation.runImageAnimation(
                    bassSprite,
                    assets.animation`bassWalkRight`,
                    130,
                    true
                )
            } else if (bassDirection == 1) {
                animation.runImageAnimation(
                    bassSprite,
                    assets.animation`bassWalkRight`,
                    130,
                    true
                )
            } else if (bassDirection == 2) {
                animation.runImageAnimation(
                    bassSprite,
                    assets.animation`bassWalkLeft`,
                    130,
                    true
                )
            } else if (bassDirection == 3) {
                animation.runImageAnimation(
                    bassSprite,
                    assets.animation`bassWalkLeft`,
                    130,
                    true
                )
            }
        })
//Set player animations 
    controller.left.onEvent(ControllerButtonEvent.Pressed, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonWalkLeft`,
            130,
            true
        )
    })
    controller.right.onEvent(ControllerButtonEvent.Pressed, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonWalkRight`,
            130,
            true
        )
    })
    controller.up.onEvent(ControllerButtonEvent.Pressed, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonWalkBackward`,
            130,
            true
        )
    })
    controller.down.onEvent(ControllerButtonEvent.Pressed, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonWalkForward`,
            130,
            true
        )
    })
    controller.left.onEvent(ControllerButtonEvent.Released, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonStandLeft`,
            180,
            true
        )
    })
    controller.right.onEvent(ControllerButtonEvent.Released, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonStandRight`,
            180,
            true
        )
    })
    controller.up.onEvent(ControllerButtonEvent.Released, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonStandLeft`,
            180,
            true
        )
    })
    controller.down.onEvent(ControllerButtonEvent.Released, function
        () {
        animation.runImageAnimation(
            safetonSprite,
            assets.animation`safetonStandRight`,
            180,
            true
        )
    })
//Start cutscene  
    info.onScore(6, function () {
        sprites.destroy(jokestarSprite)
        sprites.destroy(jazzySprite)
        sprites.destroy(bassSprite)
        story.startCutscene(function () {
            tiles.setCurrentTilemap(tilemap`cutScene`)
            let sceneSprite = sprites.create(assets.image`safetonBase`, SpriteKind.Player)
            scene.cameraFollowSprite(sceneSprite)
            animation.runImageAnimation(sceneSprite, assets.animation`endScene`, 200, false)
            music.play(music.createSong(assets.song`deathScene`), music.PlaybackMode.UntilDone)
        })
        pause(9000)
        game.reset()
    })
//Start secret cutscene  
    let secretSprite = sprites.create(assets.image`secretBase`, SpriteKind.Player)
    tiles.placeOnTile(secretSprite, tiles.getTileLocation(50, 41))
    sprites.onOverlap(SpriteKind.Player, SpriteKind.Player, function (sprite: Sprite, otherSprite: Sprite) {
        story.startCutscene(function () {
            tiles.setCurrentTilemap(tilemap`cutScene`)
            scene.cameraFollowSprite(secretSprite)
            animation.runImageAnimation(secretSprite, assets.animation`secretScene`, 50, false)
            music.play(music.createSong(assets.song`jumpscareSound`), music.PlaybackMode.UntilDone)
        })
        pause(1000)
        game.reset()
    })