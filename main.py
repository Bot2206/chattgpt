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
    
forever(on_forever2)