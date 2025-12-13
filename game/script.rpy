###############################################
# PROJECT: VOIDWALKER
# Story-driven progression (ACT-based)
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
# ACT 0 — THE WORLD BEFORE
###############################################
label start:
    $ quick_menu = False

    scene bg worldisfine at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    play music bgm_opener fadein 2.0

    narrator "It was just another day."
    narrator "Nothing felt special."
    narrator "The world moved the way it always had."

    narrator "People laughed. Cars passed by. Life went on."

    you "I remember thinking how ordinary everything felt."

    pause 0.8
    stop music fadeout 2.0
    jump act_event

###############################################
# ACT 1 — THE EVENT
###############################################
label act_event:

    scene bg opener1 at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    play music bgm_dark fadein 2.0

    narrator "Then the sky changed."
    narrator "Dark clouds rolled in without warning."
    narrator "The colors of the world began to drain."

    show fog at truecenter with dissolve
    pause 1.0

    narrator "The air grew heavy."
    narrator "Unnatural."

    narrator "Like something unseen had arrived."

    pause 1.0
    jump act_abductions

###############################################
# ACT 2 — THE ABDUCTIONS
###############################################
label act_abductions:

    scene bg night1 at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    play music bgm_mystery fadein 2.0

    narrator "People started disappearing."
    narrator "Adults vanished first."
    narrator "Then children."
    narrator "Babies."

    narrator "Anyone who stepped outside."
    narrator "Anyone exposed."

    narrator "Those who stayed indoors… survived."

    you "My parents went out that night."

    pause 1.0
    jump act_failed_abduction

###############################################
# ACT 3 — FAILED ABDUCTION
###############################################
label act_failed_abduction:

    scene bg opener2 at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    narrator "I was alone."
    narrator "The middle room window was open."

    play sound sfx_longgrowl

    narrator "Something noticed me."
    narrator "A presence."
    narrator "Dark. Watching."

    narrator "It came for me."

    pause 0.8
    jump act_artifact

###############################################
# ACT 4 — THE ARTIFACT
###############################################
label act_artifact:

    play sound sfx_whoosh

    narrator "But I wasn’t taken."
    narrator "Instead… something fell."

    show lightburst at truecenter with dissolve
    show magicglow at truecenter, glow_pulse

    narrator "A piece of paper."
    narrator "Covered in symbols that moved."

    pause 1.2
    hide magicglow with dissolve

    narrator "Something ignited inside me."

    you "…I can feel it."

    narrator "Power."
    narrator "Resistance."
    narrator "Awareness."

    pause 1.0
    jump act_first_steps

###############################################
# ACT 4.5 — FIRST STEPS OUTSIDE
###############################################
label act_first_steps:

    scene bg night1 at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    play music bgm_mystery fadein 2.0

    narrator "I stepped outside."

    narrator "The air was wrong."
    narrator "But it didn’t touch me."

    narrator "I realized then—"
    narrator "Whatever took the others… couldn’t take me."

    you "So this is what it feels like…"

    narrator "Freedom."
    narrator "And isolation."

    pause 1.0
    jump act_night_mall

###############################################
# ACT 4.6 — NIGHT MALL
###############################################
label act_night_mall:

    scene bg night_mall at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    play music bgm_walk_secret fadein 2.0

    narrator "Stores stood open."
    narrator "Lights still on."
    narrator "No people."

    narrator "Food."
    narrator "Water."
    narrator "Medicine."

    narrator "The world had stopped."
    narrator "But it hadn’t gone dark yet."

    narrator "Something was keeping it this way."

    pause 0.8

    play sound sfx_growl

    narrator "That was when I felt it."

    narrator "Eyes."
    narrator "Watching from far away."

    you "I’m not alone out here…"

    pause 1.0
    jump act_the_call


###############################################
# ACT 4.7 — THE CALL
###############################################
label act_the_call:

    scene bg secret1 at bg_full
    with fade

    play music bgm_dark fadein 2.0

    narrator "The symbol burned in my mind."

    narrator "Images flooded in."
    narrator "Tunnels."
    narrator "Depth."
    narrator "A place where they came from."

    narrator "A den."

    narrator "I didn’t know why."
    narrator "But I knew I would have to go there."

    you "This isn’t over."

    pause 1.0
    jump act_world_after


###############################################
# ACT 5 — THE WORLD AFTER
###############################################
label act_world_after:

    scene bg secret1 at bg_full
    with fade

    show hero_neutral at hero_focus
    with dissolve

    play music bgm_mystery fadein 2.0

    narrator "The world was empty."
    narrator "Dark."
    narrator "Silent."
    narrator "Wrong."

    narrator "I scavenged."
    narrator "I survived."

    pause 1.0
    jump act_meeting_others

###############################################
# ACT 6 — MEETING OTHERS
###############################################

label act_meeting_others:

    scene bg secret2 at bg_full
    with fade

    play music bgm_walk_secret fadein 2.0

    show mira_neutral1 at char_left_wide
    show hero_neutral at char_center_focus
    show keon_neutral at char_right_wide
    with dissolve

    mira "You too?"
    mira "You can walk out here?"

    keon "So we’re not the only ones."

    you "You survived… like me?"

    narrator "They had powers too."
    narrator "Different."
    narrator "But similar."

    narrator "We weren’t alone anymore."

    pause 0.8

    jump act_first_truth

###############################################
# ACT 7 — THE CASTLE & THE SENTINEL (CLIMAX)
###############################################
label act_first_truth:

    scene bg boss at bg_full
    with fade

    play music bgm_boss fadein 3.0

    # Party enters the castle
    # Party positions BEFORE demon appears
    show mira_neutral1 at char_left_wide
    show keon_neutral at char_mid_left
    show hero_neutral at char_far_right
    with dissolve

    pause 0.4
    # Demon enters center
    play sound sfx_growl
    show demon walk at demon_center
    with dissolve



    narrator "We finally reached it."
    narrator "The heart of the corruption."

    mira "This place… it’s alive."
    keon "No. It’s watching us."

    you "Stay sharp. Whatever did this… is here."

    pause 1.0

    # Demon reveal
    play sound sfx_golem_walk loop
    narrator "The ground began to shake."

    show demon walk at truecenter
    with hpunch

    play sound sfx_growl
    narrator "A massive presence emerged from the darkness."

    keon "That’s not a guardian."
    mira "That’s a ruler."

    you "Get ready."

    pause 1.0

    ################################
    # FIGHT — PHASE 1 (SPELLS)
    ################################
    narrator "We attacked first."

    show magicglow at truecenter, glow_pulse
    play sound sfx_whoosh
    pause 0.5
    hide magicglow with dissolve

    show demon hit at truecenter
    with vpunch
    play sound sfx_growl

    mira "It worked!"
    keon "Don’t stop!"

    ################################
    # FIGHT — PHASE 2 (COUNTER)
    ################################
    play sound sfx_laugh
    narrator "The creature laughed."

    show demon cleave at truecenter
    with flash
    play sound sfx_whoosh

    narrator "It struck back."

    mira "Again!"
    keon "Now!"

    show magicglow at truecenter, glow_pulse
    play sound sfx_whoosh
    pause 0.4
    hide magicglow with dissolve

    show demon hit at truecenter
    with vpunch
    play sound sfx_growl

    ################################
    # FIGHT — PHASE 3 (LOOPED EXCHANGE)
    ################################
    narrator "The battle dragged on."

    play sound sfx_laugh
    pause 0.5

    show demon hit at truecenter
    with vpunch
    pause 0.4

    narrator "Spell after spell."
    narrator "Strike after strike."

    play sound sfx_growl
    pause 0.4

    ################################
    # FINAL BLOW
    ################################
    narrator "This was it."

    you "Together!"

    show magicglow at truecenter, glow_pulse
    play sound sfx_whoosh
    pause 0.8
    hide magicglow with dissolve

    stop sound fadeout 0.5

    ################################
    # DEATH SEQUENCE (FULL)
    ################################
    show demon death at truecenter
    with dissolve
    play sound sfx_laugh
    pause 1.5

    stop music fadeout 3.0

    narrator "The sentinel screamed."
    narrator "Then fell silent."

    narrator "The castle trembled… and grew still."

    pause 1.0
    return
