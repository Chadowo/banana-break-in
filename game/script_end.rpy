# Close to the end

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
    hide c

    "The big yellow intruder doesn’t show any remorse at watching your body get riddled with bullets."
    "Seriously, what the hell where you expecting, bozo?"

    return