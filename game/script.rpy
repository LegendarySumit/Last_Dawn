###############################################
# PROJECT: VOIDWALKER
###############################################

define flash = Fade(.25, 0, .75, color="#fff")

###############################################
# CHARACTERS
###############################################
define you = Character("You", color="#bdeaff")
define mira = Character("Mira", color="#ffb7d1")
define keon = Character("Keon", color="#ffe0ac")
define narrator = Character(None)

###############################################
# DEMON FIGHT
###############################################
label demon_encounter:

    $ quick_menu  = False

    scene bg secret1 at bg_full:
        xysize (config.screen_width, config.screen_height)
    with fade

    play music bgm_mystery fadein 1.0
    play sound sfx_golem_walk loop

    narrator "Heavy footsteps echo through the empty street..."

    show demon walk at char_right
    with dissolve

    narrator "Something emerges from the shadows."

    show demon walk at demon_approach
    with hpunch

    play sound sfx_growl
    narrator "It charges!"

    show demon cleave at truecenter
    with flash

    play sound sfx_whoosh
    show magicglow at truecenter, glow_pulse
    with dissolve
    pause 0.6
    hide magicglow with dissolve

    show demon hit at truecenter
    with vpunch
    pause 0.3

    show demon death at truecenter
    with dissolve
    play sound sfx_laugh
    pause 0.8

    stop sound fadeout 0.5
    stop music fadeout 1.0

    narrator "The creature collapses, melting into ash."

    return

###############################################
# START
###############################################
label start:
    $ quick_menu =  False

    scene bg opener1 at bg_full:
        xysize (config.screen_width, config.screen_height)
    with fade

    play music bgm_dark fadein 1.0

    narrator "The sky was wrong that day. Colors drained. Air heavy like it was waiting for something."

    show hero_neutral at char_default
    with dissolve

    you "Everything felt… quiet. Too quiet."

    show fog at truecenter 
    with dissolve
    pause 0.4

    narrator "A soft rustling. A slip of paper drifting across the floor. Ink that moved like it was alive."

    show lightburst at truecenter 
    with dissolve

    play sound sfx_whoosh

    narrator "The moment you touched it, something ignited inside you."

    show magicglow at truecenter, glow_pulse
    with dissolve
    pause 1.0
    hide magicglow with dissolve

    you "…What is happening to me?"

    menu:
        "What do you do?"
        "Stay inside.":
            jump stay_path

        "Step outside.":
            jump outside_path

###############################################
# BRANCHES
###############################################

label stay_path:

    narrator "You barricade yourself in. The silence becomes unbearable."

    play music bgm_opener fadein 1.0

    narrator "But something outside starts moving. Heavy. Slow."

    jump demon_ambush

label outside_path:

    scene bg night_mall at bg_full:
        xysize (config.screen_width, config.screen_height)
    play music bgm_mystery fadein 1.0

    narrator "The streets are empty. Dark. Dead silent."

    narrator "Until the footsteps begin…"

    jump demon_ambush

label demon_ambush:

    play music bgm_walk_secret fadein 1.0

    call demon_encounter

    show mira_neutral1 at char_left
    show keon_neutral at char_right
    with fade

    mira "Hey! Are you alive?"
    keon "We heard something. Did you kill that thing?"

    you "I think the paper… saved me."

    menu:
        "Who leads the group?"
        "Mira leads.":
            $ leader = "mira"
            mira "Then stick close. We do this smart."

        "Keon leads.":
            $ leader = "keon"
            keon "Alright. Follow me. We find the source of all this."

    jump scene_end_first

label scene_end_first:

    scene bg secret2 at bg_full:
        xysize (config.screen_width, config.screen_height)
    with fade

    play music bgm_dark fadein 0.8

    narrator "This… is only the beginning."

    return
