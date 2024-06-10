﻿label start:
    $ quick_menu = False
    $ should_show_side_image = False

    stop music fadeout 1.0
    scene black
    with Fade(1.0,0.0,1.0,color=color.black)

    if persistent.chapter_one_complete == False:
        $ persistent.char_name = renpy.input("What is your name? If you let it empty, your default name will be \"Dan\"", "Dan")
        $ persistent.char_name = persistent.char_name.strip()

        if persistent.char_name == "":
            $ persistent.char_name = "Dan"

    elif persistent.chapter_one_complete == True:
        menu:
            "Select the chapter"
            "Chapter 1":
                jump story_begin
            "Chapter 2":
                jump chapter_two

    show screen splash_screen("CHAPTER 1", "BEGINNING")
    with Fade(1.0,1.0,1.0,color=color.white)
    pause(2.0)
    hide screen splash_screen
    jump story_begin
    return