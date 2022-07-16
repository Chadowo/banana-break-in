# Close to the end

# how long it takes to fade out
define fade_out_time = 3.0

transform blink:
    linear .1 alpha 0.0
    pause 0.2
    easeout .1 alpha 1.0
    pause 0.3
    repeat

transform fade_to_black:
    alpha 0.0
    linear fade_out_time alpha 1.0

image fade_black = At(Solid("#000"), fade_to_black)

# ======================================================================================

label truth_yes:
    show b flattered
    b "I knew you would say that, buddy!"

    return

label truth_interrupt:
    show b
    b "fk you"

label cuss_out:
    hide c

    show b angry
    b "Hasta la vista, fuckwad."

    hide b
    show c afraid
    c "W-wait—"

    show b angry

    "The big yellow intruder doesn't show any remorse at watching your body get riddled with bullets."
    "Seriously, what the hell where you expecting, bozo?"

    # if there was a really creepy image of a bullet-ridden apple here....

    show fade_black
    pause fade_out_time

    return