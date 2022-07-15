# The mid-game with romance and narration



# The game starts here.



label mid:

    # The save_name variable sets the name of the save game. Like all
    # variables declared outside of init blocks, this variable is
    # saved and restored with a save file.
    $ save_name = "Cozy Time"
    $ real_number = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene romantic_couch

    "As you eye him from top to bottom, you can't help but feel a little... {i}ba-bump.{/i}"
    "The way he tilts from side to side while he listens and you talk..."
    "... you enjoy watching the lopsided glimmer of his beady eyes..."
    "... when you breathe in, his fragrance tells a hardened history, of a soul seeking harbor."
    "To put it plainly, you like the potential of what you see."

    menu:
        "You want to ask, \"Have you ever... "

        "... been to Baxter's Nightclub?\"":
            jump asked_nightclub

        "... unpeeled yourself?\"":
            jump asked_unpeeled


label asked_unpeeled:

    show c
    c "Have you ever... unpeeled yourself?"

    hide c
    show b
    b "Oh [playername], you are so straight-forward."

    hide b
    "Banana picks up the wine bottle and begins refilling your glass. When he sets it back down, he looks at you expectantly."
    "You’ve already drank several glasses of wine and are starting to feel tipsy."


label asked_nightclub:
    show c
    c "Have you ever been to Baxter's Nightclub?"

    hide c
    show b
    b "Actually, I’m new to the area, so I‘ve been busy unpacking and settling down."

    hide b
    "It seems like Banana has taken the initiative to explore the neighborhood.
    You don’t know much about this fruit, though, and you’d like to find out more."

    menu:
        "What to say?"

        "\"Baxter’s is legit, I can take you there some day.\"":
            jump offer_tour

        "\"Where did you move from?\"":
            jump asked_moved

label offer_tour:

    show b flattered
    b "Really? I might take you up on the offer."

    hide b
    show c confidence
    c "Yeap, just call me anytime."

    "It is an opportune moment to slip him your number, but there’s no paper or pen nearby."

    hide c
    show b flattered
    "Luckily for you, Banana hands over his phone to you, which shows the {b}Add New Contact{/b} screen."
    "In the touchscreen era, we don’t have to entertain old-fashioned nonsense."

    menu:
        b "Here, can you input your number?"

        "(Input a fake number)":
            $ real_number = False
            "You type in the number to a rejection hotline and return the phone to him."

        "(Input your real number)":
            $ real_number = True
            "You type in your mobile number and hand the phone back to him."
           
    b "Sweet, you didn’t mistype anything, right? I totally get it,
    when you have waxy fingers, typing is a pain on mobile devices..."

    hide b
    "..."
    
    show b
    "Banana brings the phone to his head, over the spot where mammals typically grow ears, and starts calling."

    if real_number:
        jump input_real
    else:
        jump input_fake

label input_real:
    
    hide b

    "You hear a royalty-free tune coming from your phone."
    "Banana seems satisfied, at least."

    show b
    b "With that out of the way, I suppose you may have some other questions. Don’t feel shy, let us strengthen our connection :)"

    menu:
        "Now's your chance to get closer to Banana."

        "\"Where did you move from?\"":
            jump asked_moved
        
        "\"Have you ever... been unpeeled?\"":
            jump asked_unpeeled

label input_fake:
    $ p = Character("Phone", color="#6b6b6b")

    p "Hello, this is not the person you are trying to call. The person who gave you this number obviously did not want you to have their real number."
    p "In case you are wondering why, it may because you are ugly, short, maniac, or you’re just stupid. Have luck getting a mate, loser."

    show b
    b "I see how it is."

    jump cuss_out

label asked_moved:

    show b
    b "I came from the Underside. So glad to not have to wake up at 4 A.M. to some dumb asses yelling."
    "How’s the noise around here?"

    hide b

    "\"The underside?\" What kind of a place has a moniker like that?"
    "You hope that Banana is not actually a mafia lord."

    menu:
        "Banana asked about the noise around here. Your answser?"

        "\"The noise isn’t too bad...\"":
            jump mention_sirens
        
        "\"The walls here are thinner than crackers... \"":
            jump mention_thin_walls


label mention_sirens:
    show c confidence
    c "The noise isn’t too bad. Only the normal stuff like sirens and bar fights."
    
    hide c

    show b
    b "Now that you’ve mentioned sirens, I gotta say, I’m not a huge fan of the cops."
    "Those bastards make any excuse to pat you down with a friendly nudge of a taser."
    show b sad
    b "Have you ever been pulled over while on the way to your niece’s birthday party, and when they spotted your gift cash,
    they took it away in the name of public safety?"

    hide b
    show c afraid
    c "That’s... oddly specific. And understandable."
    
    jump truth_dare

label mention_thin_walls:

    show c
    c "The walls here are thinner than crackers, and someone’s illegal emotional support animal keeps howling, right above my bedroom ceiling."
    
    hide c
    
    show b
    b "Oh my, want me to take care of it ;) ?"

    hide b

    show c afraid
    "..."
    "..."
    show c confidence
    c "On second thought, it’s just a minor nitpick and nothing too serious, and there’s no need to go out of your way on our date.
    Let’s hit it off with positive vibes!"

    hide c
    show b
    b "Ok, if you say so, buddy."


label truth_dare:
    hide c

    show b surprised
    b "So, I just had this PERFECT idea to kill some time, how about we play some good ol’ Truth n’ Dare?"

    hide b

    show c afraid
    c "Uh..."

    hide c

    show b flattered
    b "Perfect, I’ll start with Truth:
    Do you feel a {i}deep{/i} connection between us, a match made in haven, like Bread and Butter, bees and flowers, ketchup and mustard..."
    "... and how for every light, there is a shadow, and for every yin, a yang..."
    "... for every corn there is a dog, and for every pop star fanclub, a deluge of haters."
    "Like peas in a pod, birds of a feather, it takes two points to tangoline..."
    "... do you feel awe, that unfathomable wonder of intimate connection, the confidence of unbreakable trust..."
    "... even when your eyes wander, they return to where they should be, that flutter of attraction becomes a greater monument,"
    "like the carp that climbs a waterfall and effort turns into a dragon of devotion, that's how strong our connection is, and—"
    
    hide b

    "He’s not stopping..."

    menu:
        "Do something about it?"

        "Say, \"Yes, I know what you mean! Spark are flying!\"":
            jump truth_yes
        
        "Say, \"Excuse me...\"":
            jump truth_interrupt

    return
