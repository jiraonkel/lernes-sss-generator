def on_button_a():
    global _symbol
    basic.set_led_color(0x00ff00)
    music.play_tone(494, music.beat(BeatFraction.QUARTER))
    music.play_tone(330, music.beat(BeatFraction.QUARTER))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    _symbol = randint(1, 3)
    if _symbol == 1:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
    elif _symbol == 2:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
    else:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        . . # . .
                        # # . # .
                        # # . . #
        """)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    basic.set_led_color(0xff0000)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

_symbol = 0
basic.set_led_color(0x007fff)

def on_forever():
    pass
basic.forever(on_forever)
