# The script of the game goes in this file.

##################### Declare characters used by this game. The color argument colorizes the #####################
######################################## name of the character. ##################################################

define h = Character('Hammett' , color="#ac28ed")
define e = Character('Ethan Alterberth' , color="#0be663")

define Y = Character("You")
define y = Character("[povname]")

define persistent.ethan_cg_1_unlocked = False  



############################################## Declare images needed #############################################

#================================================= CHAR: Hammett ================================================#
#_______________________________________________  OUTFIT: Doctor  _______________________________________________#
#----------------------------------------------- POSE: pose_normal ----------------------------------------------#
#++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: smiling +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_normal = Image("Hammett_pose_normal.png")
image Hammett_pose_normal_smile_talking = Image("Hammett_smile_talking.png")
image Hammett_pose_normal_smile_talking2 = Image("Hammett_smile_talking2.png")
image Hammett_pose_normal_happy = Image("Hammett_happy.png")

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: confuse +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_normal_confuse = Image("Hammett_pose_confuse.png")

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: akward +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_posen_akward = Image("Hammett_posen_akward.png")
image Hammett_posen_akward2 = Image("Hammett_posen_akward2.png")
image Hammett_posen_akward3 = Image("Hammett_posen_akward3.png")

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: funny ++++++++++++++++++++++++++++++++++++++++++++++#



#---------------------------------------------- POSE: pose_writing ----------------------------------------------#
#++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: normal ++++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_writing = Image("Hammett_pose_writing.png")

#-------------------------------------------------- Placeholder --------------------------------------------------#

image placeholderH1 = Image("placeholderH1.png")
image placeholderH2 = Image("placeholderH2.png")
image placeholderH3 = Image("placeholderH3.png")
image placeholderH4 = Image("placeholderH4.png")
image placeholderH5 = Image("placeholderH5.png")

#================================================ CHAR: Ethan ===================================================#
#______________________________________________  OUTFIT: casual  ________________________________________________#
#---------------------------------------------- POSE: normal_pose -----------------------------------------------#
image Ethan_normal_pose = Image("Ethan_normal_pose.png")

#___________________________________________  OUTFIT: hospital gown _____________________________________________#
image Ethan_normal_pose_ingown = Image("Ethan_normal_pose_ingown.png")
image Ethan_normal_pose_ingown_talking = Image("Ethan_normal_pose_ingown_talking.png")

#---------------------------------------------- POSE: questioning -----------------------------------------------#
image Ethan_questioning_ingown_talking = Image("Ethan_questioning_ingown_talking.png")
image Ethan_questioning_ingown_suspicious = Image("Ethan_questioning_ingown_suspicious.png")

#---------------------------------------------- Placeholder ----------------------------------------------#

image placeholderE1 = Image("placeholderE1.png")
image placeholderE2 = Image("placeholderE2.png")
image placeholderE3 = Image("placeholderE3.png")
image placeholderE4 = Image("placeholderE4.png")

image D2HR_hammett1 = Image("placeholder/placeholder_hammetta.png")
image D2HR_hammett1:
    "placeholder/placeholder_hammetta.png"
    zoom 0.5

image D2HR_hammett2 = Image("placeholder/placeholder_hammettb.png")
image D2HR_hammett2:
    "placeholder/placeholder_hammettb.png"
    zoom 0.5

image D2HR_hammett3 = Image("placeholder/placeholder_hammettc.png")
image D2HR_hammett3:
    "placeholder/placeholder_hammettc.png"
    zoom 0.5

image D2HR_Ethan1 = Image("placeholder/placeholder_ethanb.png")
image D2HR_Ethan1:
    "placeholder/placeholder_ethanb.png"
    zoom 0.6

image D2HR_Ethan2 = Image("placeholder/placeholder_ethana.png")
image D2HR_Ethan2:
    "placeholder/placeholder_ethana.png"
    zoom 0.6

image claire = Image("placeholder/placeholder_claire.png")
image claire:
    "placeholder/placeholder_claire.png"
    zoom 0.6

image D2HR_ophelia = Image("placeholder/placeholder_ophelia.png")
image D2HR_ophelia:
    "placeholder/placeholder_ophelia.png"
    zoom 0.6

image D2HR_hospitalbed = Image("placeholder/placeholder_hospitalroom.png")
image D2HR_hospitalbed:
    "placeholder/placeholder_hospitalroom.png"
    zoom 0.6

image D2HR_hospitalgallery = Image("placeholder/placeholder_hospitalrooms.png")
image D2HR_hospitalgallery:
    "placeholder/placeholder_hospitalrooms.png"
    zoom 0.6

image D2HR_hospitalgalleryO = Image("placeholder/placeholder_hospitalroomsb.png")
image D2HR_hospitalgalleryO:
    "placeholder/placeholder_hospitalroomsb.png"
    zoom 0.6

image D2HR_hospitalpeeking = Image("placeholder/placeholder_hospitalpeeking.png")
image D2HR_hospitalpeeking:
    "placeholder/placeholder_hospitalpeeking.png"
    zoom 0.6

#================================================= CG: Hammett =================================================#
#================================================== CG: Ethan ==================================================#

image Ethan_D1_CG1a_shock = Image("CGs/Ethan_D1_CG1a_shock.png")
image Ethan_D1_CG1b_shy = Image("CGs/Ethan_D1_CG1b_shy.png")

#============================================ CG: pastmemory_hammett ============================================#

image pastmemory_hammett1 = Image("pastmemory_hammett1.png")

#============================================= CG: pastmemory_ethan =============================================#

#================================================== Background ==================================================#

image bg Hospital_room_night = Image("bg_byouin000shade_night000-studio.jpg")
image bg Hospital_room_afternoon = Image("bg_byouin000shade-studio.jpg")
image bg Hospital_room_morning = Image("bg_byouin000-studio.jpg")
image bg Hospital_counter = Image("bg_nurce_st-studio.jpg")
image bg Hospital_infirmary = Image("bg_sinryousitu-studio.jpg")

#Credit--: Gutari Nyanko from itch.io

image bg black_screen = Image("bg_black_screen.png")
image warningscreen = Image("warningscreen.png")

################################################## Define images #################################################

#================================================= CHAR: Hammett ================================================#
#_______________________________________________  OUTFIT: Doctor  _______________________________________________#
#----------------------------------------------- POSE: pose_normal ----------------------------------------------#
#++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: smiling +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_normal:
    "Hammett_pose_normal.png"
    zoom 0.8

image Hammett_pose_normal_smile_talking:
    "Hammett_smile_talking.png"
    zoom 0.8

image Hammett_pose_normal_smile_talking2:
    "Hammett_smile_talking2.png"
    zoom 0.8

image Hammett_pose_normal_happy:
    "Hammett_happy.png"
    zoom 0.8

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: confuse +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_normal_confuse:
    "Hammett_pose_confuse.png"
    zoom 0.8

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: akward +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_posen_akward:
    "Hammett_posen_akward.png"
    zoom 0.8

image Hammett_posen_akward2:
    "Hammett_posen_akward2.png"
    zoom 0.8

image Hammett_posen_akward3:
    "Hammett_posen_akward3.png"
    zoom 0.8

#+++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: funny ++++++++++++++++++++++++++++++++++++++++++++++#



#----------------------------------------------- POSE: pose_normal ----------------------------------------------#
#++++++++++++++++++++++++++++++++++++++++++++++ EXPRESSION: smiling +++++++++++++++++++++++++++++++++++++++++++++#

image Hammett_pose_writing:
    "Hammett_pose_writing.png"
    zoom 0.8

#-------------------------------------------------- Placeholder --------------------------------------------------#

image placeholderH1:
    "placeholderH1.png"

image placeholderH2:
    "placeholderH2.png"

image placeholderH3:
    "placeholderH3.png"

image placeholderH4:
    "placeholderH4.png"

image placeholderH5:
    "placeholderH5.png"

#================================================ CHAR: Ethan ===================================================#
#______________________________________________  OUTFIT: casual  ________________________________________________#
#---------------------------------------------- POSE: normal_pose -----------------------------------------------#
image Ethan_normal_pose:
    "Ethan_normal_pose.png"
    zoom 0.45

#___________________________________________  OUTFIT: hospital gown _____________________________________________#
image Ethan_normal_pose_ingown:
    "Ethan_normal_pose_ingown.png"
    zoom 0.45

image Ethan_normal_pose_ingown_talking:
    "Ethan_normal_pose_ingown_talking.png"
    zoom 0.45

#---------------------------------------------- POSE: questioning -----------------------------------------------#
image Ethan_questioning_ingown_talking:
    "Ethan_questioning_ingown_talking.png"
    zoom 0.45

image Ethan_questioning_ingown_suspicious:
    "Ethan_questioning_ingown_suspicious.png"
    zoom 0.45

#-------------------------------------------------- Placeholder --------------------------------------------------#

image placeholderE1:
    "placeholderE1.png"

image placeholderE2:
    "placeholderE2.png"

image placeholderE3:
    "placeholderE3.png"

image placeholderE4:
    "placeholderE4.png"

#================================================== CG: Ethan ==================================================#
image Ethan_D1_CG1a_shock:
    "CGs/Ethan_D1_CG1a_shock.png"

image Ethan_D1_CG1b_shy:
    "CGs/Ethan_D1_CG1b_shy.png"


#============================================ CG: pastmemory_hammett ============================================#
image pastmemory_hammett1:
    "pastmemory_hammett1.png"

#============================================= CG: pastmemory_ethan =============================================#

#================================================== Background ==================================================#
image bg Hospital_room_night:
    "bg_byouin000shade_night000-studio.jpg"
    zoom 1.5

image bg Hospital_room_afternoon:
    "bg_byouin000shade-studio.jpg"
    zoom 1.5

image bg Hospital_room_morning:
    "bg_byouin000-studio.jpg"
    zoom 1.5

image bg Hospital_counter:
    "bg_nurce_st-studio.jpg"
    zoom 3.0

image bg Hospital_infirmary:
    "bg_sinryousitu-studio.jpg"
    zoom 1.5

image bg black_screen:
    "bg_black_screen.png"

image warningscreen:
    "warningscreen.png"
#================================================== CGs ==================================================#


image CG_a_red = "CGs/a_red.png"
image CG_a_orange = "CGs/a_orange.png"
image CG_a_yellow = "CGs/a_yellow.png"
image CG_a_green = "CGs/a_green.png"
image CG_a_blue = "CGs/a_blue.png"
image CG_a_indigo = "CGs/a_indigo.png"


image CG_b_red = "CGs/b_red.png"
image CG_b_orange = "CGs/b_orange.png"
image CG_b_yellow = "CGs/b_yellow.png"
image CG_b_green = "CGs/b_green.png"
image CG_b_blue = "CGs/b_blue.png"
image CG_b_indigo = "CGs/b_indigo.png"

################################################## Define transition #################################################

transform upper_body_center:
    xalign 0.5      # center horizontally
    yalign 1.0      # align bottom with screen bottom
    yoffset 1500     # move image up (adjust this number to your liking)

transform offscreenbottomleft:
    xpos 0.0 xanchor 1.0 ypos 2.0 yanchor 1.0

define leftside = MoveTransition(
                    delay=0.3,
                    enter =offscreenbottomleft,
                    leave =offscreenbottomleft,
                    old =False,
                    layers =['master'],
                    time_warp =ease,
                    enter_time_warp =None,
                    leave_time_warp =None)

transform slide_left:
    xalign 0.0  # Move character to the left side
    yalign 1.0
    linear 0.5 xalign 0.0  # Move smoothly over 0.5 seconds

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat

transform bounce_once:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform moving_closer:
    xpos 0.3888
    ypos 0.0933
    pause 0.15
    ease 1.0 zoom 4.0 xpos 0.06 ypos 0.0

transform exit_right:
    linear 0.5 xalign 1.5

############################################## The game starts here. #############################################
#==================================================== Day 0 =====================================================#

label start:
    
    $ quick_menu = False
    window hide
    show warningscreen with dissolve
    $ renpy.pause(2.0)
    scene black
    hide warningscreen with dissolve
    #start of the story
    $ quick_menu = True
    
    play music "audio/spotidownloader.com - rainy day - Stream Cafe.mp3" volume 0.5
    scene black

    $ povpronouce = renpy.input("What is your pronounce? (He/She/They)", length = 10)

    $ povgendertitle = ""
    
    if povpronouce in ["He" , "Him" , "he" , "him"]:
        $ povgendertitle = "Mr. "
        
    elif povpronouce in ["She" , "Her" , "she" , "her"]:
        $ povgendertitle = "Ms. "
        
    elif povpronouce in ["They" , "Them" , "they" , "them"]:
        $ povgendertitle = "Mx. "
       
    else:
        "Invailable pronounce. Please try again."
        jump pronounce
    
    jump naming

label naming:

    $ povname = renpy.input("What is your name?", length = 32)
    jump naming_double_checking

label naming_double_checking:
    "[povgendertitle][povname]"
    menu:
        "Yes":
            jump start_of_story
        "No":
            jump pronounce

label start_of_story:
    "Date: June 13
    Time: 6 p.m. (bgm: engine sound)"
    "Erstonia, the town where you been born, is known for its romantic and relaxing atmosphere."
    "You decided to return to your hometown, travel around, taking things slowly, and eventually find a job."
    "After a long ride, the sky has darkened and the night has fallen."
    "The lack of the street lamps along the highway making the road appear pitch black, expect for the path illuminated by your car headlights."
    "You begin to feel drowsy, not because it is night, but because of the four-hours drive."
    "Just then, you notice a faint glow in the distance. It is the light from your hometown, Warm like a gentle spirit, inviting and comforting."
    "The town has changed compared to what you remembered, but the feeling remains the same." 
    "Excitement begins to build as you get closer to the city."
    Y "Speeding a little more shouldn't hurt. It's not like someone would be standing in the middle of the highway at night."

    "After thinking that, you press the accelerator."
    play sound "audio/notification-sound.mp3" volume 0.8
    "Your phone recieves a new notification."
    "You glance at your phone, which is placed on the passenger seat."
    "It's a message from Friendzoe, a viral social media application."
    "You quickly check the contain of the message, it is a friend request from a stranger."
    play sound "audio/notification-sound.mp3" volume 0.8
    stop music fadeout 2.0
    "When you look back at the road, you suddenly realize that a green-haired man is standing in the middle of the highway." 
    "It's too late to stop the car."
    "The green-haired man notices you as well, but it's too late for him to move out of the way." 
    "You quickly turn the steering wheel to the right." 
    play sound "audio/237375__squareal__car-crash.mp3" 
    "Your car crashes into the woods beside the road." with hpunch
    "The impact throws your head forward into the steering wheel before your body falls back into the seat."
    Y "(That was a close call...)"
    "The impact is too strong, and everything fades to black."
    "You fall into a coma."
    show text "You have a car crash..." at truecenter
    with dissolve
    pause 2
    hide text "You have a car crash..."
    hide black
    jump forgotten_memory_H1

label forgotten_memory_H1:
    play music "audio/569865__theojt__peaceful-ambiance-theme-2.mp3" volume 0.5
    show pastmemory_hammett1 with dissolve
    Y "Can you read the story book for me? Pleassseeee."
    "A little boy" "O..Okay."
    "A little boy" "Once upon a time, there's a poor girl who is being made things difficult by her cruel stepmother and her stepsister."
    "A little boy" "One day, an old lady come to the house and ask for a glass of water, the kind girl offers a glass of water and a freshly made slice of pie for the old lady."
    "A little boy" "The old lady was very grateful for the offer and thank the kind girl."
    "A little boy" "But the stepmother and the stepsister does not like the girl, they assign the girl with impossible task."
    "A little boy" "The stepmother had assign the girl to clean 5 kilograms of dirty feathers, drain water of a lake and build a castle, or else she will be locked in the storage room and straved."
    "A little boy" "The girl felt hopeless as it was impossible for her to accomplish such diffcult task."
    "A little boy" "The old lady from before had known the unfair task given to the kind girl, to repay the kindness of the girl."
    "A little boy" "The old lady help the girl achieve the task."
    hide pastmemory_hammett1 with dissolve
    stop music fadeout 1.0
    jump day0

label day0:
    scene bg Hospital_room_night
    "Time: 11:47 p.m."
    "You slowly regaining your conscious, and finding yourself laying on a hospital bed."
    Y "Am I...in a hospital?"
    "A sudden sharp pain occured on your head, reminding you that you just had a car accident."
    Y "Urggg...my head hurts so much...."
    Y "That green hair guy, did he doge the car?"

    "There's someone knocking on the door."
    Y "Come in."

    
    scene bg Hospital_room_afternoon
    
    play sound "audio/440499__christutorials__light-switch-turn-off-sound.mp3" volume 0.8

    play music "audio/spotidownloader.com - study time - Stream Cafe.mp3" volume 0.5
    "A dark purple hair man with losen pony tail open the door and show up in the room. "
    play sound "audio/Sound Effects - Footsteps.mp3" volume 0.8
    show Hammett_pose_normal at upper_body_center
    with moveinright

    "The dark purple hair man was wearing a medical gown, he must be your doctor."
    "???" "Good day [povgendertitle] [povname], I see you have waken from your coma."
    show Hammett_pose_normal_happy at upper_body_center
    hide Hammett_pose_normal
    "???" "If you will excuse me, I need to do some initial check up on you, I promise it won't be long."
    Y "Go ahead."
    "After medical check up..."
    show Hammett_pose_writing at upper_body_center
    hide Hammett_pose_normal_happy
    "???" "Seems like there's no major issues nor internal bleeding..." 
    show Hammett_pose_normal_happy at upper_body_center
    hide Hammett_pose_writing
    "???" "You may rest the night, [povgendertitle] [povname]."
    show Hammett_pose_normal at upper_body_center
    hide Hammett_pose_normal_happy
    Y "Erm, doctor. Can I know when can I leave the hospital?"
    "???" "Not sure yet, since we need to do deep inspection on you to ensure your health, [povgendertitle] [povname]"
    Y "Can I know your name?"
    show Hammett_posen_akward at upper_body_center
    hide Hammett_pose_normal
    "???" "..."
    show Hammett_posen_akward2 at upper_body_center
    hide Hammett_posen_akward
    stop music fadeout 2.0
    play music "audio/spotidownloader.com - honey's waltz - Stream Cafe.mp3" volume 0.5
    "???" "Ouhh ermm, s...sorry for my late introduction, the name is Hammett"
    show Hammett_posen_akward3 at upper_body_center, bounce
    hide Hammett_posen_akward2
    "???" "If you need anything, call us through the bell. Wish you have a good rest! BYEE!! "
    hide Hammett_posen_akward3
    show Hammett_posen_akward3 at upper_body_center
    show Hammett_posen_akward3 at offscreenright with move
    
    stop music fadeout 4.0
    play sound "audio/440499__christutorials__light-switch-turn-off-sound.mp3" volume 0.8
    hide Hospital_room_afternoon
    scene bg Hospital_room_night
    play music "audio/spotidownloader.com - rainy day - Stream Cafe.mp3" volume 0.5 fadein 1.0
    
    "After the light swtich off, the darkness fills the room."
    "But you still thinking."
    y "What a 'good' start in this town."
    "You made an undeniable complaint about your unlucky encounter."
    "After a while, you felt a strong feeling of drowsiness strucks your head and you fell into slumber."
    scene bg black_screen
    hide Hospital_room_night
    stop music 
    jump day1_start

#==================================================== Day 1 =====================================================#

label day1_start:
    scene black
    $ renpy.pause(2.0)

    hide black
    scene D2HR_hospitalbed with dissolve

    show D2HR_hammett1
    y "!!!"
    $ renpy.pause(1.0)
    hide D2HR_hammett1

    play music "audio/spotidownloader.com - matcha mochi - Stream Cafe.mp3"
    
    show D2HR_hammett2
    h "Good morning sleepy head~ it's time for your checkups~"
    hide D2HR_hammett2
    
    show D2HR_hammett3
    h "Talk to me whenever you are ready, I'll be outside the room."
    hide D2HR_hammett3

    play sound "audio/Sound Effects - Footsteps.mp3"
    $ renpy.pause(2.0)
    stop sound fadeout 1.0

    $ phone_mode += 1
    $ phone_start()
    window hide
    $ create_phone_channel("vanessa_dm", "Vanessa", ["Vanessa", phone_config["phone_player_name"]], "phone/icons/vanessa.png")
    $ send_phone_message("", "8:23 a.m.", "vanessa_dm", 1)
    $ send_phone_message("Vanessa", "If you want to know about the accident, come to the hospital's 3rd Floor in room 34.", "vanessa_dm")
    "Someone just send a message. Check your phone's Message."
    call screen phone_modal
    $ phone_end()
    window show
    y "Is it the green hair guy? How did he know my number?"
    y "Might as well meet him after the morning checkups."
    scene black with dissolve
    hide D2HR_hospitalbed
    $ renpy.pause(2.0)
    scene bg Hospital_room_morning with dissolve
    hide black

    menu:
        "Call Dr. Hammett":
            jump day1_morning
    
label day1_morning:
    y "Dr. Hammett, I'm ready for the checkups now."
    show Hammett_pose_normal at upper_body_center
    $ renpy.pause(2.0)
    h "Now let's us continue what we left."

    scene black with dissolve
    $ renpy.pause(2.0)
    hide black
    scene bg Hospital_room_morning
    show Hammett_pose_normal_happy at upper_body_center
    h "Glad to inform you that you are quite healthy except for a slight concussion judging that you just experience an accident."
    h "Yet, you need to stay at this hospital today for observation."
    h "If there is no any danger symthoms, you are free from the hospital."
    h "And that's all from me, is there anything you want to ask me?"

    y "Nothing."

    h "Alright, if you need me, you can call us from the phone."
    hide Hammett_pose_normal_happy
    "It's seems like there's a lot of free time, did you want to go out?"

    menu:
        "Yes":
            jump day1_morning_gallery
        "No":
            jump day1_afktimechoice

label day1_morning_gallery:
    scene D2HR_hospitalgallery with dissolve
    hide bg Hospital_room_morning
    "Where did you want to go?"
    menu:
        "3rd Floor":
            jump day1_morning_3rdFloor_gallery

        "Back to Room":
            jump day1_afktimechoice

        "1st Floor":
            jump day1_morning_1stFloor_gallery

        #"Ground Floor":
        #    jump

label day1_morning_3rdFloor_gallery:
    scene D2HR_hospitalgalleryO with dissolve
    hide D2HR_hospitalgallery
    define day1_morning_ethan = 0
    if day1_morning_ethan == 0:
        y "There is a room with an open door, is it that person who message me?"
        menu:
            "Go inside the room":
                jump day1_morning_ethan

            "Don't":
                jump day1_morning_3rdFloor_choice
    else:
        "There's nothing to explore about in this floor."
        menu:
            "Back your room":
                jump day1_morning_3rdFloor_choice
            "Go to 1st Floor":
                jump day1_morning_1stFloor_gallery

            #"Ground Floor":
            #    jump

label day1_morning_3rdFloor_choice:
    "Where else would you want to go?"
    menu:
        "Stay in 3rd Floor":
            jump day1_morning_3rdFloor_gallery

        "Go back to rest":
            jump day1_afktimechoice

        "1st Floor":
            jump day1_morning_1stFloor_gallery

        #"Ground Floor":
        #    jump

label day1_morning_ethan:
    $ day1_morning_ethan = 1
    "Since the door is open, you went inside wthout knocking the door."
    scene  D2HR_Ethan1 with dissolve
    hide D2HR_hospitalgalleryO
    e "..."
    "A familiar face appears in the room, it's the person you almost crash into yesterday."
    "It seems like he didn't sense your presence."
    y "E...Excuse me?"
    scene D2HR_Ethan2
    hide D2HR_Ethan1
    y "Didn't mean to interupt you, but are you the person who message me?"
    e "Ahh yes, it's me."
    e "You must be the person who almost crash into me"
    y "'How is he so calm about it?'"
    y "About that, I'm really really sorry about it! Because of my uncareful of driving behaviour..."
    y "I'll cover up your hospital bill!"
    e "Ohh, about that, you don't need to actually."
    y "Eh? Is there anything I can make it up for you?"
    e "I was thinking to ask you to help me one thing."
    y "And, what is it?"
    e "Help me tidy up my shop, and you are free from the debt"
    e "..."
    y "???"
    y "That's it?"
    e "Yeap."
    y "'What a strange person, I though he will ask for higher compensation? Is he trying to minimize the drama??'"
    e "Do come to the shop tommorrow morning, I'll send the location to you later."

    jump day1_morning_3rdFloor_gallery

label day1_morning_1stFloor_gallery:
    scene D2HR_hospitalgallery with dissolve
    hide D2HR_hospitalgalleryO
    "???" "Good morning Dr. ~"
    "You hear a kid's cheerful voice echo the entire hallway."

    "Did you want to investigate the source?"
    menu:
        "Yes":
            jump day1_morning_1stFloor_choice

        "No":
            "You choose to ignore the voice."
            "Where did you want to go?"
            menu:
                "Back to your room":
                    jump day1_afktimechoice
                "3rd Floor":
                    jump day1_morning_3rdFloor_gallery


    

label day1_morning_1stFloor_choice:
    "The source of the voice is coming from Room 12 and the door isn't fully closed."
    
    scene D2HR_hospitalpeeking with dissolve
    hide D2HR_hospitalgallery
    y "It's him. Is this his another patient?"
    "Did you want to peek into the room?"
    menu:
        "Yes":
            jump day1_morning_hammett

        "No":
            y "I don't think it's ethical to peek into someone's room."
            "Where did you want to go?"
            menu:
                "Back to your room":
                    jump day1_afktimechoice
                "3rd Floor":
                    jump day1_morning_3rdFloor_gallery

label day1_morning_hammett:
    scene bg Hospital_room_morning with dissolve
    hide D2HR_hospitalpeeking
    show D2HR_ophelia
    show claire at bounce
    show Hammett_pose_normal at upper_body_center, slide_left

    "Cheerful kid" "Dr.!! Can I PLSSSSS have a colour pencils?!"
    "Droopy kid" "..."
    h "Sure! Only if you take this medicine first, then I will get you one tommorrow."
    h "Do we have a deal?"
    "Cheerful kid" "DEAL!!"
    "Cheerful kid" "Ophelia! We can do doodles together tommorrow!! YAY~"


label day1_afktimechoice:
    "How long did you plan to rest?"
    #menu:
        #"Afternoon":
        #    jump

        #"Night":
        #    jump


label day1_end:








label credits:
    scene black
    $ quick_menu = False
    window hide
    $ credits_speed = 15  # Speed of scrolling

    show theend:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.0)
    hide theend

    show endcred at credits_scroll
    with dissolve
    $ renpy.pause(credits_speed)

    scene black
    with dissolve

    show thanks:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.0)

    return

init python:
    credits = [('Backgrounds', 'Gutari Nyanko'), ('Phone Function', 'Uncle Mugen & Nighten'), ('Interactive Phone', 'Zoey (Kleineluka)')]
    credits_s = "{size=80}Credits\n\n"
    c1 = ""
    for c in credits:
        if c1 != c[0]:
            credits_s += "\n{size=50}" + c[0] + "\n"
        credits_s += "{size=30}" + c[1] + "\n"
        c1 = c[0]
    credits_s += "\n{size=50}Engine\n{size=30}Ren'Py (8.3.6)"

init:
    image endcred = Text(credits_s, text_align=0.5, size=40, color="#FFFFFF")
    image theend = Text("{size=40}The End", text_align=0.5, color="#FFFFFF")
    image thanks = Text("{size=40}Thanks for Playing the Demo!! Stay tuned for the future update!!", text_align=0.5, color="#FFFFFF")

    transform credits_scroll:
        xalign 0.5
        ypos 1.2  # Start BELOW the screen (off-screen)
        linear 15.0 ypos -0.2  # Move UPWARDS off-screen over 15 seconds





