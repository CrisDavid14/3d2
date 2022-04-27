def on_forever():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . #
                # . . . #
    """)
    basic.pause(0.1)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . # .
                # . . # .
    """)
    basic.pause(0.1)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . # . .
                # . # . .
    """)
    basic.pause(0.1)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . # . . .
                # # . . .
    """)
    basic.pause(0.1)
    basic.show_leds("""
        . . . . .
                # . . . .
                . . . . .
                # . . . .
                # . . . .
    """)
    basic.pause(0.1)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
    """)
basic.forever(on_forever)
