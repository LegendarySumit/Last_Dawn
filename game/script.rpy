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
# ACT 7 — FIRST SENTINEL
###############################################
label act_first_truth:

    scene bg boss at bg_full
    with fade

    play music bgm_boss fadein 2.0
    play sound sfx_golem_walk loop

    narrator "The ground trembled."

    show demon walk at char_right with dissolve

    narrator "This was no longer survival."

    narrator "This was war."

    return
