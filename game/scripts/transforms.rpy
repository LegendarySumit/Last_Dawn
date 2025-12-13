transform bg_full:
    # Keep backgrounds contained within the screen without over-scaling or cropping.
    size (config.screen_width, config.screen_height)
    fit "contain"
    xalign 0.5
    yalign 0.5

transform char_default:
    anchor (0.5, 1.0)
    xalign 0.5
    yalign 0.98
    zoom 0.55

transform char_left:
    anchor (0.5, 1.0)
    xalign 0.22
    yalign 0.98
    zoom 0.55

transform char_right:
    anchor (0.5, 1.0)
    xalign 0.78
    yalign 0.98
    zoom 0.55

transform demon_approach:
    anchor (0.5, 1.0)
    xalign 1.2 yalign 0.98
    zoom 0.55
    linear 1.2 xalign 0.65

transform glow_pulse:
    alpha 0.0
    linear 0.25 alpha 1.0
    linear 0.4 alpha 0.6
    linear 0.3 alpha 0.0