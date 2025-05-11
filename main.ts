function on_forever2() {
    basic.showLeds(`
    . # # # .
    # # . . .
    # # # # .
    # # # # .
    . # . # .
    `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # . . .
        # # # # .
        # # # # .
        `)
    basic.pause(100)
}

function on_forever() {
    basic.showLeds(`
    . # # # #
    # # . . #
    # # # # #
    # # # # .
    . # . # .
    `)
}

let sus = randint(1, 15)
if (sus == 15) {
    on_forever()
} else {
    on_forever2()
}

