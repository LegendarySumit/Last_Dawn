# images.rpy
# Register backgrounds (scaled to the current screen size)
# images.rpy — BACKGROUNDS (NO SCALING HERE)
image bg worldisfine = "images/backgrounds/worldisfine.png"
image bg night1 = "images/backgrounds/nightscene1.png"
image bg night_mall = "images/backgrounds/nightscenemall.png"
image bg opener1 = "images/backgrounds/nightsceneopenervn.png"
image bg opener2 = "images/backgrounds/nightsceneopenervn2.png"
image bg secret1 = "images/backgrounds/secretplace1.png"
image bg secret2 = "images/backgrounds/secretplace2.png"
image bg boss = "images/backgrounds/thebosschamber.png"


# Effects (overlay) — scaled down so they don't cover the whole screen
image magicglow = Transform("images/effects/magicglow.png", anchor=(0.5, 0.5), zoom=0.4)
image fog = Transform("images/effects/whitefog.png", anchor=(0.5, 0.5), zoom=0.75)
image lightburst = Transform("images/effects/lighteffect.png", anchor=(0.5, 0.5), zoom=0.7)

# Character images (hero)
image hero neutral = "images/characters/hero/hero_neutral.png"
image hero angry   = "images/characters/hero/hero_angry.png"
image hero doubtful = "images/characters/hero/hero_doubtful.png"
image hero flirt   = "images/characters/hero/hero_flirt.png"
image hero fluster = "images/characters/hero/hero_fluster.png"
image hero happy   = "images/characters/hero/hero_happy.png"
image hero pleasure = "images/characters/hero/hero_pleasure.png"
image hero sad     = "images/characters/hero/hero_sad.png"
image hero scared  = "images/characters/hero/hero_scared.png"

# Character images (girl)
image mira_neutral1 = "images/characters/girl/girl_neutral1.png"
image mira_neutral2 = "images/characters/girl/girl_neutral2.png"
image mira_angry    = "images/characters/girl/girl_angry.png"
image mira_sad      = "images/characters/girl/girl_sad.png"
image mira_shock    = "images/characters/girl/girl_shock.png"
image mira_smile1   = "images/characters/girl/girl_smile1.png"
image mira_smile2   = "images/characters/girl/girl_smile2.png"
image mira_smirk1   = "images/characters/girl/girl_smirk1.png"
image mira_smirk2   = "images/characters/girl/girl_smirk2.png"

# Character images (boy)
image keon_neutral   = "images/characters/boy/boy_neutral.png"
image keon_happy     = "images/characters/boy/boy_happy.png"
image keon_angry     = "images/characters/boy/boy_angry.png"
image keon_confused  = "images/characters/boy/boy_confused.png"
image keon_flirt     = "images/characters/boy/boy_flirt.png"
image keon_fluster   = "images/characters/boy/boy_fluster.png"
image keon_pleasure  = "images/characters/boy/boy_pleasure.png"
image keon_sad       = "images/characters/boy/boy_sad.png"
image keon_surprised = "images/characters/boy/boy_surprised.png"

# Demon (monster) — use Animation for multi-frame sequences.
# Idle (single frame or simple animation)
image demon idle = "images/monsters/demon/demon_idle.png"

# Walk
image demon walk:
    zoom 10.0
    "images/monsters/demon/demon_walk.png"
    pause 0.08

# Attack (single frame provided, but we keep as short animation)
image demon cleave:
    zoom 10.0
    "images/monsters/demon/demon_cleave.png"
    pause 0.12

# Take hit
image demon hit = Transform("images/monsters/demon/demon_take_hit.png", anchor=(0.5, 0.5), zoom=10.0)

# Death sequence (list the frames you uploaded)
image demon death:
    zoom 10.0
    "images/monsters/demon/demon_death1.png"
    pause 0.06
    "images/monsters/demon/demon_death2.png"
    pause 0.06
    "images/monsters/demon/demon_death3.png"
    pause 0.06
    "images/monsters/demon/demon_death4.png"
    pause 0.06
    "images/monsters/demon/demon_death5.png"
    pause 0.06
    "images/monsters/demon/demon_death6.png"
    pause 0.06
    "images/monsters/demon/demon_death7.png"
    pause 0.06
    "images/monsters/demon/demon_death8.png"
    pause 0.06
