define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
define config.developer = False

# python early:
#     import singleton
#     me = singleton.SingleInstance()

init python:
    def restore_all_characters():
        print("working")
        

## Scenes and Background definitions
image bg beach = "images/Locations/bg beach.png"
image bg britishbay = "images/Locations/bg britishbay.png"
image bg cafeteria = "images/Locations/bg cafateria.png"
image bg classroom = "images/Locations/bg classroom.png"
image bg computerlab = "images/Locations/bg computerlab.png"
image bg countryclub = "images/Locations/bg countryclub#2.png"
image bg gymnasium = "images/Locations/bg gymnasium.png"
image bg highschoolfront = "images/Locations/bg highschoolfront.png"
image bg ibiza = "images/Locations/bg ibiza.png"
image bg library = "images/Locations/bg library.png"
image bg mall = "images/Locations/bg mall.png"
image bg neonarcade = "images/Locations/bg neonarcade.png"
image bg recroom = "images/Locations/bg recroom.png"
image bg sciencelab = "images/Locations/bg sciencelab.png"
image bg sportsfield = "images/Locations/bg sportsfield.png"

## Primary Protagonist Definitions
define Nar = Character(ctc="ctc", ctc_position="fixed")
define Da = DynamicCharacter("Da_name", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

## Primary Female Character Definitions
define Kr = DynamicCharacter('Kr_name', image="kristina", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Ka = DynamicCharacter('Ka_name', image="kathryn", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define He = DynamicCharacter('He_name', image="heather", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define An = DynamicCharacter('An_name', image="annika", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Ne = DynamicCharacter('Ne_name', image="neomi", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Na = DynamicCharacter('Na_name', image="nadia", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Ak = DynamicCharacter('Ak_name', image="akira", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Es = DynamicCharacter('Es_name', image="estella", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

## Primary Male Character Definitions
define Ed = DynamicCharacter('Ed_name', image="eddy", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Jo = DynamicCharacter('Jo_name', image="johnny", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Ro = DynamicCharacter('Ro_name', image="romesh", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define So = DynamicCharacter('So_name', image="sol", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define St = DynamicCharacter('St_name', image="stefan", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Ke = DynamicCharacter('Ke_name', image="kento", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define Fe = DynamicCharacter('Fe_name', image="fernando", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

## Name Definitions
define Da_name = "Dave"

define Kr_name = "Kristina"
define Ka_name = "Kathryn"
define He_name = "Heather"
define An_name = "Annika"
define Ne_name = "Neomi"
define Na_name = "Nadia"
define Ak_name = "Akira"
define Es_name = "Estella"

define Ed_name = "Eddy"
define Jo_name = "Johnny"
define Ro_name = "Romesh"
define So_name = "Sol"
define St_name = "Stefan"
define Ke_name = "Kento"
define Fe_name = "Fernando"

image kristina neutralblush = Image("images/Characters/Kristina/Summer Uniform/Kristina summerUniform neutral blush.png")
image kristina neutral = Image("images/Characters/Kristina/Summer Uniform/Kristina summerUniform neutral.png")
image kristina smileblush = Image("images/Characters/Kristina/Summer Uniform/Kristina summerUniform smile blush.png")
image kristina smile = Image("images/Characters/Kristina/Summer Uniform/Kristina summerUniform smile.png")
image kristina upsetblush = Image("images/Characters/Kristina/Summer Uniform/Kristina summerUniform upset Blush.png")
image kristina upset = Image("images/Characters/Kristina/Summer Uniform/Kristina summerUniform upset.png")

image kathryn frownblush = Image("images/Characters/kathryn/Summer Uniform/kathryn summerUniform frown blush.png")
image kathryn frown = Image("images/Characters/kathryn/Summer Uniform/kathryn summerUniform frown.png")
image kathryn smileblush = Image("images/Characters/kathryn/Summer Uniform/kathryn summerUniform smile blush.png")
image kathryn smile = Image("images/Characters/kathryn/Summer Uniform/kathryn summerUniform smile.png")
image kathryn openblush = Image("images/Characters/kathryn/Summer Uniform/kathryn summerUniform open Blush.png")
image kathryn open = Image("images/Characters/kathryn/Summer Uniform/kathryn summerUniform open.png")

image Annika frownblush = Image("images/Characters/Annika/Summer Uniform/Annika summerUniform frown blush.png")
image Annika frown = Image("images/Characters/Annika/Summer Uniform/Annika summerUniform frown.png")
image Annika smileblush = Image("images/Characters/Annika/Summer Uniform/Annika summerUniform smile blush.png")
image Annika smile = Image("images/Characters/Annika/Summer Uniform/Annika summerUniform smile.png")
image Annika openblush = Image("images/Characters/Annika/Summer Uniform/Annika summerUniform open Blush.png")
image Annika open = Image("images/Characters/Annika/Summer Uniform/Annika summerUniform open.png")

image eddy angry = Image("images/Characters/Eddy/Eddy angry.png")
image eddy confused = Image("images/Characters/Eddy/Eddy confused.png")
image eddy cry = Image("images/Characters/Eddy/Eddy cry.png")
image eddy flustered = Image("images/Characters/Eddy/Eddy flustered.png")
image eddy happy = Image("images/Characters/Eddy/Eddy happy.png")
image eddy nervous = Image("images/Characters/Eddy/Eddy nervous.png")
image eddy normal = Image("images/Characters/Eddy/Eddy normal.png")
image eddy sad = Image("images/Characters/Eddy/Eddy sad.png")
image eddy shocked = Image("images/Characters/Eddy/Eddy shocked.png")

image kento frownblush = Image("images/Characters/kento/Summer Uniform/kento summerUniform frown blush.png")
image kento frown = Image("images/Characters/kento/Summer Uniform/kento summerUniform frown.png")
image kento smileblush = Image("images/Characters/kento/Summer Uniform/kento summerUniform smile blush.png")
image kento smile = Image("images/Characters/kento/Summer Uniform/kento summerUniform smile.png")
image kento openblush = Image("images/Characters/kento/Summer Uniform/kento summerUniform open Blush.png")
image kento open = Image("images/Characters/kento/Summer Uniform/kento summerUniform open.png")