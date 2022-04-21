# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen",color="#ff0000")
define d = Character("Dave",color="#00ffdd")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg highschoolfront
    with Dissolve(.5)

    pause .5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    "Today is your first day at HB High School in Southern California"

    "You feel excited and optimistic about starting your freshman year"

    "but you also feel a hint of nerves and uncertainty"

    "As you are in an unfamiliar setting in a new country"

    "Then I see the most popular girl in school coming towards me"

    e "So, I hear you're british?"

    d "Yeah, that's right. Who told you that?"

    e "Oh y'know its floating around."

    scene bg classroom
    with Dissolve(.5)

    pause .5

    d "I'm pretty sure a lot of news, rumours and gossip gets floated around these hallways"

    e "How did you end up here in the US?"

    d "My Dad got his dream job which had a foreign posting"

    d "So before I knew it, we all packed and ready to go"

    scene bg gymnasium
    with Dissolve(.5)

    pause .5

    e "I bet it must have been a complete culture shock for you?"

    d "A bit but I have been on a few holidays here before"

    e "like vacation?"

    return