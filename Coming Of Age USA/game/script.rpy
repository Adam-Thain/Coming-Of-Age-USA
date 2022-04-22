# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Kristina = Character("Kristina",color="#ff0000")
define Kathryn = Character("Kathryn",color="#ff0000")
define Heather = Character("Heather",color="#ff0000")
define Annika = Character("Annika",color="#ff0000")

define Dave = Character("Dave",color="#ff0000")
define Eddy = Character("Eddy",color="#ff0000")
define Johnny = Character("Johnny",color="#ff0000")
define Romesh = Character("Romesh",color="#ff0000")

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

    "Today is your first day at HB High School in Southern California."

    "You feel excited and optimistic about starting your freshman year."

    "but you also feel a hint of nerves and uncertainty."

    "As you are in an unfamiliar setting in a new country."

    "Then I see the most popular girl in school coming towards me."

    Kristina "So, I hear you're british?"

    Dave "Yeah, that's right. Who told you that?"

    Kristina "Oh y'know its floating around."

    scene bg classroom
    with Dissolve(.5)
    pause .5

    show eileen happy

    Dave "I'm pretty sure a lot of news, rumours and gossip gets floated around these hallways."

    Kristina "How did you end up here in the US?"

    Dave "My Dad got his dream job which had a foreign posting..."

    Dave "So before I knew it, we all packed and ready to go."

    scene bg gymnasium
    with Dissolve(.5)
    pause .5

    show eileen happy

    Kristina "I bet it must have been a complete culture shock for you?"

    Dave "A bit but I have been on a few holidays here before."

    Kristina "like vacation?"

    Dave "Yeah, But we call them holidays back in England."

    scene bg beach
    with Dissolve(.5)
    pause .5

    show eileen happy

    "After a short walk, we both arrive at the beach."

    Dave "It's just like the sunsets we used to get on our holidays in Ibiza."

    Kristina "Where's that?"

    Dave "it's a Spanish island in the mediterrean that's known for its nightlife."

    Dave "Think of it like Cancun but better."

    return