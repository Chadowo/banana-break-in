# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    $ b = Character("Banana", color="#dbd02e") # , what_color="#009900
    $ c = Character("[playername]", color="#c52915")

    # Backgrounds.
    # image romantic_couch = Image("carillon.jpg")
    image romantic_couch = Solid((0, 0, 0, 255))

    # Character pictures.
    image b = Image("characters/banana.png")
    image b sad = Image("characters/banana_sad.png")
    image b flattered = Image("characters/banana_flattered.png")
    image b surprised = Image("characters/banana_surprised.png")
    image b angry = Image("characters/banana_angry.png")

    image c = Image("characters/apple.png")
    image c afraid = Image("characters/apple_afraid.png")
    image c asking = Image("characters/apple_asking.png")
    image c confidence = Image("characters/apple_confidence.png")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    $ playername = renpy.input("What is your name?")

    if not playername:
        $ playername = "Camson"
    
    $ playername = playername.strip()

    show c

    # These display lines of dialogue.

    c "test"

    jump mid

    # This ends the game.

    return
