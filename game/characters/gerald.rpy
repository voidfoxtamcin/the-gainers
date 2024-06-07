define gerald = Character(name="Gerald", image="Gerald", color="#835332")

init:
  layeredimage Gerald:
    fit "scale-down"
    xcenter 0.5
    group base:
      attribute naked default:
        "characters/gerald/base_11.png"
      attribute covered:
        "characters/gerald/base_21.png"

    group eyes:
      attribute eyes_close:
        "characters/gerald/eyes_11.png"
      attribute eyes_close_confused:
        "characters/gerald/eyes_12.png"
      attribute eyes_open default:
        "characters/gerald/eyes_21.png"
      attribute eyes_open_confused:
        "characters/gerald/eyes_11.png"
      attribute eyes_happy:
        "characters/gerald/eyes_31.png"
      attribute eyes_happy_confused:
        "characters/gerald/eyes_32.png"

    group mouth:
      attribute mouth_frown:
        "characters/gerald/mouth_11.png"
      attribute mouth_smile default:
        "characters/gerald/mouth_12.png"
      attribute mouth_frown_open:
        "characters/gerald/mouth_21.png"
      attribute mouth_smile_open:
        "characters/gerald/mouth_22.png"