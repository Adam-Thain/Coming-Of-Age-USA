define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        # import os
        # try: os.remove(config.basedir + "/characters/" + name + ".chr")
        # except: pass
        print("Working")

    def restore_all_characters():
        # try: renpy.file("../characters/monika.chr")
        # except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        # try: renpy.file("../characters/natsuki.chr")
        # except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        # try: renpy.file("../characters/yuri.chr")
        # except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        # try: renpy.file("../characters/sayori.chr")
        # except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
        print("Working")

    def restore_relevant_characters():
        # restore_all_characters()
        # if persistent.playthrough == 1 or persistent.playthrough == 2:
        #     delete_character("sayori")
        # elif persistent.playthrough == 3:
        #     delete_character("sayori")
        #     delete_character("natsuki")
        #     delete_character("yuri")
        # elif persistent.playthrough == 4:
        #     delete_character("monika")
        print("Working")

    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False


## Sound definitions
define audio.t1 = "<loop 22.073>backgroundMusic/1.ogg"
define audio.t2 = "<loop 4.499>backgroundMusic/2.ogg"
define audio.t2g = "backgroundMusic/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>backgroundMusic/2.ogg"
define audio.t2g3 = "<loop 4.492>backgroundMusic/2g2.ogg"
define audio.t3 = "<loop 4.618>backgroundMusic/3.ogg"
define audio.t3g = "<to 15.255>backgroundMusic/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>backgroundMusic/3.ogg"
define audio.t3g3 = "<loop 4.618>backgroundMusic/3g2.ogg"
define audio.t3m = "<loop 4.618>backgroundMusic/3.ogg"
define audio.t4 = "<loop 19.451>backgroundMusic/4.ogg"
define audio.t4g = "<loop 1.000>backgroundMusic/4g.ogg"
define audio.t5 = "<loop 4.444>backgroundMusic/5.ogg"
define audio.t5b = "<loop 4.444>backgroundMusic/5.ogg"
define audio.t5c = "<loop 4.444>backgroundMusic/5.ogg"
define audio.t6 = "<loop 10.893>backgroundMusic/6.ogg"
define audio.t6g = "<loop 10.893>backgroundMusic/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>backgroundMusic/6r.ogg"
define audio.t6s = "<loop 43.572>backgroundMusic/6s.ogg"
define audio.t7 = "<loop 2.291>backgroundMusic/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>backgroundMusic/7.ogg"
define audio.t7g = "<loop 31.880>backgroundMusic/7g.ogg"
define audio.t8 = "<loop 9.938>backgroundMusic/8.ogg"
define audio.t9 = "<loop 3.172>backgroundMusic/9.ogg"
define audio.t9g = "<loop 1.532>backgroundMusic/9g.ogg"
define audio.t10 = "<loop 5.861>backgroundMusic/10.ogg"
define audio.t10y = "<loop 0>backgroundMusic/10-yuri.ogg"
define audio.td = "<loop 36.782>backgroundMusic/d.ogg"

define audio.m1 = "<loop 0>backgroundMusic/m1.ogg"
define audio.mend = "<loop 6.424>backgroundMusic/monika-end.ogg"

define audio.ghostmenu = "<loop 0>backgroundMusic/ghostmenu.ogg"
define audio.g1 = "<loop 0>backgroundMusic/g1.ogg"
define audio.g2 = "<loop 0>backgroundMusic/g2.ogg"
define audio.hb = "<loop 0>backgroundMusic/heartbeat.ogg"

define audio.closet_open = "soundEffects/closet-open.ogg"
define audio.closet_close = "soundEffects/closet-close.ogg"
define audio.page_turn = "soundEffects/pageflip.ogg"
define audio.fall = "soundEffects/fall.ogg"     

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "images/Backgrounds/splash.png"
image end:
    truecenter
    "gui/end.png"

## Scenes and Background definitions
image bg beach = "images/Backgrounds/bg beach.png"
image bg britishbay = "images/Backgrounds/bg britishbay.png"
image bg cafeteria = "images/Backgrounds/bg cafateria.png"
image bg classroom = "images/Backgrounds/bg classroom.png"
image bg computerlab = "images/Backgrounds/bg computerlab.png"
image bg countryclub = "images/Backgrounds/bg countryclub#2.png"
image bg gymnasium = "images/Backgrounds/bg gymnasium.png"
image bg highschoolfront = "images/Backgrounds/bg highschoolfront.png"
image bg ibiza = "images/Backgrounds/bg ibiza.png"
image bg library = "images/Backgrounds/bg library.png"
image bg mall = "images/Backgrounds/bg mall.png"
image bg neonarcade = "images/Backgrounds/bg neonarcade.png"
image bg recroom = "images/Backgrounds/bg recroom.png"
image bg sciencelab = "images/Backgrounds/bg sciencelab.png"
image bg sportsfield = "images/Backgrounds/bg sportsfield.png"

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

## Image Definitions
image kristina neutralblush = "images/Characters/Kristina/Summer Uniform/Kristina summer uniform neutral blush.png"
image kristina neutral = "images/Characters/Kristina/Summer Uniform/Kristina summer uniform neutral.png"
image kristina smileblush = "images/Characters/Kristina/Summer Uniform/Kristina summer uniform smile blush.png"
image kristina smile = "images/Characters/Kristina/Summer Uniform/Kristina summer uniform smile.png"
image kristina upsetblush = "images/Characters/Kristina/Summer Uniform/Kristina summer uniform upset Blush.png"
image kristina upset = "images/Characters/Kristina/Summer Uniform/Kristina summer uniform upset.png"

image kathryn frownblush = "images/Characters/kathryn/Summer Uniform/kathryn summer uniform frown blush.png"
image kathryn frown = "images/Characters/kathryn/Summer Uniform/kathryn summer uniform frown.png"
image kathryn smileblush = "images/Characters/kathryn/Summer Uniform/kathryn summer uniform smile blush.png"
image kathryn smile = "images/Characters/kathryn/Summer Uniform/kathryn summer uniform smile.png"
image kathryn openblush = "images/Characters/kathryn/Summer Uniform/kathryn summer uniform open Blush.png"
image kathryn open = "images/Characters/kathryn/Summer Uniform/kathryn summer uniform open.png"

image Annika frownblush = "images/Characters/Annika/Summer Uniform/Annika summer uniform frown blush.png"
image Annika frown = "images/Characters/Annika/Summer Uniform/Annika summer uniform frown.png"
image Annika smileblush = "images/Characters/Annika/Summer Uniform/Annika summer uniform smile blush.png"
image Annika smile = "images/Characters/Annika/Summer Uniform/Annika summer uniform smile.png"
image Annika openblush = "images/Characters/Annika/Summer Uniform/Annika summer uniform open Blush.png"
image Annika open = "images/Characters/Annika/Summer Uniform/Annika summer uniform open.png"

image eddy angry = "images/Characters/Eddy/Eddy angry.png"
image eddy confused = "images/Characters/Eddy/Eddy confused.png"
image eddy cry = "images/Characters/Eddy/Eddy cry.png"
image eddy flustered = "images/Characters/Eddy/Eddy flustered.png"
image eddy happy = "images/Characters/Eddy/Eddy happy.png"
image eddy nervous = "images/Characters/Eddy/Eddy nervous.png"
image eddy normal = "images/Characters/Eddy/Eddy normal.png"
image eddy sad = "images/Characters/Eddy/Eddy sad.png"
image eddy shocked = "images/Characters/Eddy/Eddy shocked.png"

image kento frownblush = "images/Characters/kento/Summer Uniform/kento summer uniform frown blush.png"
image kento frown = "images/Characters/kento/Summer Uniform/kento summer uniform frown.png"
image kento smileblush = "images/Characters/kento/Summer Uniform/kento summer uniform smile blush.png"
image kento smile = "images/Characters/kento/Summer Uniform/kento summer uniform smile.png"
image kento openblush = "images/Characters/kento/Summer Uniform/kento summer uniform open Blush.png"
image kento open = "images/Characters/kento/Summer Uniform/kento summer uniform open.png"

define _dismiss_pause = config.developer
# 
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
# default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
# default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
# default persistent.first_poem = None
# default persistent.seen_colors_poem = None
# default persistent.monika_back = None
# default in_sayori_kill = None
# default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None