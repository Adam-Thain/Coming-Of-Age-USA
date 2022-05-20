# The script of the game goes in this file.

label start:

    $ anticheat = persistent.anticheat

    $ chapter = 0

    $ _dismiss_pause = config.developer

    $ Kr_name = "Girl 1"
    $ Ka_name = "Girl 2"
    $ He_name = "Girl 3"
    $ An_name = "Girl 4"
    $ Ne_name = "Girl 5"
    $ Na_name = "Girl 6"
    $ Ak_name = "Girl 7"
    $ Es_name = "Girl 8"

    $ Ed_name = "???"
    $ Jo_name = "Boy 1"
    $ Ro_name = "Boy 2"
    $ So_name = "Boy 3"
    $ St_name = "Boy 4"
    $ Ke_name = "Boy 5"
    $ Fe_name = "Boy 6"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:

        call Prologue

        $ chapter = 0
        call chapter1

        $ chapter = 1
        call chapter2

        $ chapter = 2
        call chapter3

        $ chapter = 3
        call epilogue1

        # python:
        #     try: renpy.file(config.basedir + "/hxppy thxughts.png")
        #     except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

        call endgame

        return

    # elif persistent.playthrough == 1:
        # $ chapter = 0
        # call ch10_main
        # jump playthrough2


    # elif persistent.playthrough == 2:
        # $ chapter = 0
        # call ch20_main

        # label playthrough2:


        #     call poem
        #     python:
        #         try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
        #         except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())


        #     $ chapter = 1
        #     call ch21_main
        #     call poemresponse_start
        #     call ch21_end


        #     call poem (False)
        #     python:
        #         try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        #         except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())


        #     $ chapter = 2
        #     call ch22_main
        #     call poemresponse_start
        #     call ch22_end


        #     call poem (False)


        #     $ chapter = 3
        #     call ch23_main
        #     if y_appeal >= 3:
        #         call poemresponse_start2
        #     else:
        #         call poemresponse_start

        #     if persistent.demo:
        #         stop music fadeout 2.0
        #         scene black with dissolve_cg
        #         "End of demo"
        #         return

        #     call ch23_end

        #     return
        
    # elif persistent.playthrough == 3:
        # jump ch30_main

    # elif persistent.playthrough == 4:
        # $ chapter = 0
        # call ch40_main
        # jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return