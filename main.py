def on_forever2():
    basic.show_leds("""
    . # # # .
    # # . . .
    # # # # .
    # # # # .
    . # . # .
    """)
    
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . # # # .
        # # . . .
        # # # # .
        # # # # .
        """)
    basic.pause(100)

def on_forever():
    basic.show_leds("""
    . # # # #
    # # . . #
    # # # # #
    # # # # .
    . # . # .
    """)

sus=randint(1, 15)
if sus==15:
    on_forever()
else:
    on_forever2()
    
