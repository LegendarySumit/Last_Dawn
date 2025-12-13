# LastDawn 🌑

**LastDawn** is a dark, story-driven visual novel built with **Ren’Py**, focused on atmosphere, survival, and cinematic boss encounters.  
The game follows a lone survivor in a world that collapses overnight after a mysterious mass-abduction event.

---

## 🧠 Concept

One day, without warning, the sky darkens.

People vanish — adults first, then children, then entire families.  
Anyone exposed to the outside world disappears.

You survive by accident.

An ancient artifact binds itself to you, granting resistance to the corruption beyond closed doors.  
As you step into the abandoned world, you uncover the truth behind the abductions, the sentinels guarding the land, and the power controlling it all.

---

## 🎮 Features

- Act-based narrative progression
- Dark fantasy / post-apocalyptic atmosphere
- Cinematic, story-driven combat (non-mechanical)
- Boss encounters with multi-stage animations
- Custom sprite positioning and scene composition
- Character-focused dialogue and pacing
- Heavy use of ambient sound and music

---

## 🗂️ Project Structure

```text
LastDawn/
├── game/
│   ├── script.rpy              # Main story (ACT-based)
│   ├── transforms.rpy          # All positioning & layout logic
│   ├── characters.rpy          # Character definitions
│   ├── images.rpy              # Image registrations
│   ├── options.rpy
│   ├── screens.rpy             # Default Ren’Py screens (mostly unchanged)
│   ├── images/
│   │   ├── backgrounds/
│   │   ├── characters/
│   │   ├── demons/
│   │   └── effects/
│   └── audio/
│       ├── music/
│       └── sfx/
└── README.md
```

## 👥 Characters

You — The protagonist and survivor

Mira — A survivor with awakened abilities

Keon — A hardened fighter with similar powers

The Sentinel — A ruler-class demon guarding the corrupted world

## ⚙️ Built With

Ren’Py 8.x

Python-based scripting

Custom transforms for cinematic staging

Manual asset pipeline

## 🚧 Development Status

In active development

Current focus:

Expanding mid-game acts (post-artifact, pre-group)

Refining boss fight pacing and narration

Improving visual balance and scene blocking

Preparing endgame resolution arc

## ⚠️ Notes

Asset names are case-sensitive

Scene layout is controlled via transforms.rpy

Boss scenes reserve center space by design

Combat is narrative-driven, not mechanical

## 📌 Vision

LastDawn is designed to feel quiet, heavy, and inevitable —
a story where silence matters, survival has weight, and every encounter pushes the world closer to its final dawn.

## 📄 License

This project is currently under development.
Asset usage and licensing will be clarified before public release.
