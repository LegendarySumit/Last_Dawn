transform bg_full:
    xalign 0.5
    yalign 0.5
    xsize config.screen_width
    ysize config.screen_height


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

transform char_far_right:
    xalign 0.92
    yalign 0.95
    xzoom 0.75
    yzoom 0.75



transform demon_approach:
    anchor (0.5, 1.0)
    xalign 1.2 yalign 0.98
    zoom 0.55
    linear 1.2 xalign 0.65

transform demon_center:
    xalign 0.5
    yalign 0.95


transform glow_pulse:
    alpha 0.0
    linear 0.25 alpha 1.0
    linear 0.4 alpha 0.6
    linear 0.3 alpha 0.0

transform hero_intro:
    xalign 0.62
    yalign 0.95
    zoom 0.75

# =========================
# PROTAGONIST — EXTREME RIGHT
# =========================
transform hero_focus:
    xalign 0.78        # extreme right, still visible
    yalign 0.95
    xzoom 0.78
    yzoom 0.78


# =========================
# GROUP SCENE BALANCE
# =========================
transform char_left_wide:
    xalign 0.15
    yalign 0.95
    xzoom 0.7
    yzoom 0.7


transform char_center_focus:
    xalign 0.5
    yalign 0.95
    xzoom 0.7
    yzoom 0.7

transform char_right_wide:
    xalign 0.82
    yalign 0.95
    xzoom 0.6
    yzoom 0.6

transform char_mid_left:
    xalign 0.32
    yalign 0.95
    xzoom 0.7
    yzoom 0.7
