layeredimage Tamcin:
    fit "scale-down"

    group base:
        attribute normal default:
            "tamcin_base"
        attribute arm_up:
            "tamcin_raise_arm"

    group eyes:
        attribute idle default:
            "tamcin_expression_idle"
        attribute blink:
            "tamcin_expression_blink"
        attribute happy:
            "tamcin_expression_happy"

    group mouth:
        attribute shut default:
            "tamcin_mouth_close"
        attribute talk:
            "tamcin_mouth_open"

layeredimage Twill:
    fit "scale-down"

    group base:
        attribute normal default:
            "twill_base"

    group eyes:
        attribute idle default:
            "twill_eyes_open"
        attribute blink:
            "twill_eyes_close"
        attribute happy:
            "twill_eyes_happy"

    group mouth:
        attribute shut default:
            "twill_mouth_close"
        attribute talk:
            "twill_mouth_open"

image Phone:
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    "item handphone.png"

image Ringing:
    xalign 0.5
    yalign 0.5
    xanchor 0.5
    yanchor 0.5
    "item handphone_ring_1"
    pause 0.2
    "item handphone_ring_2"
    pause 0.2
    "item handphone_ring_3"
    pause 0.2
    "item handphone_ring_4"
    pause 0.2
    repeat