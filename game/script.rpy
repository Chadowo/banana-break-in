# The script of the game goes in this file.

# Declare images/characters used by this game. The color argument colorizes the
# name of the character.

init:

    $ b = Character("Banana", color="#FFFC5C") # , what_color="#009900
    $ c = Character("[playername]", color="#B02712")

    # Backgrounds.
    # image romantic_couch = Image("carillon.jpg")
    image romantic_couch = Solid((0, 0, 0, 255))

    # Character pictures.
    image b = Image("images/characters/banana.png")
    image b sad = Image("images/characters/banana_sad.png")
    image b flattered = Image("images/characters/banana_flattered.png")
    image b surprised = Image("images/characters/banana_surprised.png")
    image b angry = Image("images/characters/banana_angry.png")

    image c = Image("images/characters/apple.png")
    image c afraid = Image("images/characters/apple_afraid.png")
    image c asking = Image("images/characters/apple_asking.png")
    image c confidence = Image("images/characters/apple_confidence.png")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    $ playername = renpy.input("What is your name?", length=32)

    if not playername:
        $ playername = "Camson"
    
    $ playername = playername.strip()

    show c

    # These display lines of dialogue.

    c "test"

    jump mid

    # This ends the game.

    return
