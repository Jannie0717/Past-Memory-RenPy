
init python:
    import time
    class calendar_ticker(renpy.Displayable):
        def __init__(self, calendar):
            super(renpy.Displayable,self).__init__()
            self.passed = 0
            self.current = None
            self.calendar = calendar

        def render(self,width,height,st,at):
            if self.current is None:
                self.current = time.time()
            if (time.time() - self.current) > 1:
                self.current = time.time()
                self.calendar.tick()
                # renpy.restart_interaction()

            img = Text(" ")
            t = Transform(img)
            child_render = renpy.render(t, width, height, st, at)
            cw, ch = child_render.get_size()

            rv = renpy.Render(cw, ch)
            rv.blit(child_render,(100, 100))

            renpy.redraw(self, 0)
            return rv
    class calendar_class:
        def __init__(self):
            self.ticker = calendar_ticker(self)
            self.minute = 0
            self.hour = 0
            self.week_day = 0
            self.month = 4
            self.year = 2021
            self.month_day = 16
            self.month_start = 6
            self.day = 1
            self.speed = 1
            self.week_days = [
                _("Sunday"), _("Monday"), _("Tuesday"),
                _("Wednesday"), _("Thursday"), 
                _("Friday"), _("Saturday")
                ]
            self.months = [
                [_("January"), 31],
                [_("February"), 28],
                [_("March"), 31],
                [_("April"), 30],
                [_("May"), 31],
                [_("June"), 30],
                [_("July"), 31],
                [_("August"), 31],
                [_("September"), 30],
                [_("October"), 31],
                [_("November"), 30],
                [_("December"), 31]
                ]
            self.seasons = [
                _("Spring"), _("Summer"), _("Autumn"), _("Winter")
            ]
        def tick(self, n = 1):
            for i in range(n):
                self.minute += 1
                if self.minute > 59:
                    self.minute = 0
                    self.hour_tick()

        def hour_tick(self, n=1):
            for i in range(n):
                self.hour += 1
                if self.hour > 23:
                    self.hour = 0
                    self.day += 1
                    if self.week_day < 6:
                        self.week_day += 1
                    else:
                        self.week_day = 0
                    if self.month_day < self.months[self.month][1]:
                        self.month_day += 1
                    else:
                        self.month_day = 1
                        self.month_start = self.week_day
                        if self.month < 11:
                            self.month += 1
                        else:
                            self.month = 0
                            self.year += 1

        def speed_change(self, d = "reset"):
            if d == "up" and self.speed > 0.1:
                self.speed -= 0.1
            elif d == "down" and self.speed < 3.0:
                self.speed += 0.1
            elif d == "reset":
                self.speed = 2.0
default calendar = calendar_class()
define phone_mode = 0

if phone_mode == 1:
    screen phone_button: #☰

        vbox:
            xalign 1.0
            button:
                background None
                add "phone/smartphone.png"
                action ToggleScreen("phone")
            #button:
            #    background None
            #    add "phone/rotate.png"
            #    action Function(phone.rotate)
        add calendar.ticker

screen phone_modal():
    tag phone
    modal True
    zorder 100
    
    # Use the phone screen from 1&2_phone.rpy
    use phone
    
    # This makes clicking outside the phone do nothing (modal behavior)
    # But the back button will properly close it
    key "K_ESCAPE" action Return()

# =====================================================
# STYLE DEFINITIONS (from original phone.rpy)
# =====================================================

style phone_header_style is default:
    size 28
    color get_phone_theme_value("header_text_colour") 
    xalign 0.5

style phone_channel_button_style is button:
    background None
    hover_background get_phone_theme_value("channel_button_hover_background")
    xpadding 10
    ypadding 8

style phone_channel_name_style is default:
    size 22
    color get_phone_theme_value("channel_name_text_colour")
    bold True

style phone_channel_preview_style is default:
    size 18
    color get_phone_theme_value("channel_preview_text_colour")

style phone_message_style is default:
    size 20
    color get_phone_theme_value("empty_channel_text_colour")
    xalign 0.0

style phone_sender_name_style is default:
    size 16
    color get_phone_theme_value("sender_name_text_colour")
    yoffset 2 
    ypadding 0
    yalign 1.0

# Add the phone button to the overlay
init python:
    if phone_mode == 1:
        if "phone_button" not in config.overlay_screens:
            config.overlay_screens.append("phone_button")


# transform wiggle:
#     rotate_pad False
#     subpixel True
#     ease .1 rotate -4
#     ease .1 rotate 4
#     repeat
# style phone_frame:
#     background "#222"
# style phone_button:
#     background "#222"


# screen phone_top_bar(c):
#     frame: # TOp bar
#         ysize 40 yalign 0.0 xfill True background "#0009"
#         fixed:
#             hbox:
#                 xalign 1.0
#                 text "4G iii"
#                 text "100% B"
#             hbox:
#                 xalign 0.0
#                 text "*"
#                 if c.get_unread() > 0:
#                     text "{} new messages".format(c.get_unread())


# screen phone_list_bg(name, c):
#     frame:
#         xysize(600,900) padding(0,0) background "#222"
#         frame: # Header
#             ysize 80 xfill True yalign 0.0 background "#333b"
#             text name
#             button:
#                 align 0.0,0.5 background "#222" xysize 40,40
#                 text "⬅"
#                 action Function(c.show, "phone")  
#         frame:
#             yoffset 80 background None padding (10,10) yalign 0.0
#             transclude

# screen phone_sms_list(c):
#     tag phone

#     use phone_list_bg(_("Messaging"), c):
#         vbox:
#             for i in c.contacts:
#                 if len(i.sms):
#                     button:
#                         xfill True background "#333b"
#                         hbox:
#                             xfill True
#                             hbox:
#                                 xalign 0.0 xfill True
#                                 hbox:
#                                     xalign 0.0
#                                     if i.img:
#                                         add i.img
#                                     else:
#                                         add "phone/img.png"
#                                     vbox:
#                                         if i.name:
#                                             text i.name xalign 0.0
#                                         else:
#                                             text _("Unknown") xalign 0.0
#                                         text i.sms[-1][1] xalign 0.0
#                                 if i.unread:
#                                     frame:
#                                         xalign 1.0
#                                         background "#f00" xysize 40,40
#                                         text str(i.unread) color "#fff"
#                         action Function(c.show, "sms", i.id)

    


# screen phone_contacts_list(c):
#     tag phone
#     use phone_list_bg(_("Contacts"), c):
#         vbox:
#             button:
#                 xfill True background "#333b" ysize 80
#                 hbox:
#                     text "✚" size 30
#                     text _("Add New Contact")
#                 action Show("phone_contact_edit", phone = c)
#             for i in c.contacts:
#                 button:
#                     xfill True background "#333b"
#                     hbox:
#                         xfill True
#                         hbox:
#                             xalign 0.0
#                             if i.img:
#                                 add i.img
#                             else:
#                                 add "phone/img.png"
#                             vbox:
#                                 if i.name:
#                                     text i.name xalign 0.0
#                                 else:
#                                     text _("Unknown") xalign 0.0
#                                 if i.number:
#                                     text i.number xalign 0.0
#                                 else:
#                                     text _("No number") xalign 0.0
#                         button:
#                             xalign 1.0 background "#222"
#                             text _("Edit")
#                             action Show("phone_contact_edit", c = i)
#                     action Function(c.show, "contact_edit", i.id)
# screen phone_contact_edit(c = None, phone = None):
#     modal True
#     style_prefix "phone"
#     default editing = "name"
#     if c:
#         default name = c.name
#         default number = c.number
#         default img = c.img
#     else:
#         default name = _("Name")
#         default number = _("Number")
#         default img = "phone/img.png"
#     frame:
#         xysize 400,400 background "#333b"
#         vbox:
#             button:
#                 vbox:
#                     add img
#                     text "Change Image"
#                 action Show("phone_image_pick")
#             if editing == "name":
#                 frame:
#                     xysize 300,60
#                     input value ScreenVariableInputValue("name")
#             else:
#                 button:
#                     xysize 300,60
#                     text name
#                     action SetScreenVariable("editing", "name")
#             if editing == "number":
#                 frame:
#                     xysize 300,60
#                     input value ScreenVariableInputValue("number")
#             else:
#                 button:
#                     xysize 300,60
#                     text number
#                     action SetScreenVariable("editing", "number")

#             hbox:
#                 if c:
#                     button:
#                         text _("Apply")
#                         action Function(c.edit, name, number, img), Hide("phone_contact_edit")
#                 else:
#                     button:
#                         text _("Add")
#                         action Function(phone.add, "new_contact", name, number, img), Hide("phone_contact_edit")
#                 button:
#                     text _("Cancel")
#                     action Hide("phone_contact_edit")

# screen phone_image_pick:
#     modal True
#     style_prefix "phone"
#     frame:
#         xysize 500,600 background "#333b"
#         vbox:
#             text _("Choose:")
#             button:
#                 text _("Take an image")
#             button:
#                 text _("Choose from gallery")
#             button:
#                 text _("File explorer")
            
#             button:
#                 text _("Cancel")
#                 action Hide("phone_image_pick")

# transform phone_crop:
#     crop(0,0,600,700)



# screen phone_sms(c = phone_in_use):
#     tag phone

#     frame:
#         xysize(600,900) padding(0,0) background "#222"
#         if c.active:
#             frame: # Header
#                 ysize 80 xfill True yalign 0.0 background "#333b"
#                 if c.active.name:
#                     text c.active.name
#                 else:
#                     text _("Unknown")
#                 button:
#                     align 0.0,0.5 background "#222" xysize 40,40
#                     text "⬅"
#                     action Function(c.show, "sms list")
#             frame: # Main body
#                 background None padding (30,80,30,110) yfill True
#                 viewport id "phone_vp":
#                     draggable True scrollbars None yinitial 1.0
#                     xfill False
#                     yfill False
#                     yalign 1.0
#                     frame:
#                         padding(0,0) background None
#                         vbox:
#                             xfill True spacing 2
#                             for n, i in enumerate(c.active.sms):
#                                 if isinstance(i, basestring):
#                                     pass
#                                 else:
#                                     if i[0] == c.id:
#                                         if not n or not c.active.sms[n-1][0] == i[0]:
#                                             null height 20
#                                             hbox:
#                                                 xalign 1.0 spacing 0
#                                                 frame:
#                                                     style "phone_right" xoffset 64
#                                                     text i[1] color "#000"
#                                                 if c.img:
#                                                     add c.img yalign 0.0
#                                                 else:
#                                                     add "phone/img.png" yalign 0.0
#                                         else:
#                                             frame:
#                                                 xalign 1.0
#                                                 style "phone_right_1"
#                                                 text i[1] color "#000"

#                                     else:
#                                         if not n or not c.active.sms[n-1][0] == i[0]:
#                                             null height 20
#                                             hbox:
#                                                 xalign 0.0 spacing 0
#                                                 if c.active.img:
#                                                     add c.active.img yalign 0.0
#                                                 else:
#                                                     add "phone/img.png" yalign 0.0
#                                                 frame:
#                                                     style "phone_left" xoffset -64
#                                                     text i[1] color "#000"
#                                         else:
#                                             frame:
#                                                 xalign 0.0
#                                                 style "phone_left_1"
#                                                 text i[1] color "#000"

#             vbox: # Input
#                 yalign 1.0 spacing 0
#                 if c.active.current:
#                     if c.active.phase == 1:
#                         text "{} is typing...".format(c.active.name) size 15 xalign 0.0 xoffset 10

#                 frame:
#                     background "#333b" padding 10,10 xfill True margin 10,0,10,10
#                     has hbox
#                     xfill True
#                     if c.active.typing:
#                         frame:
#                             xsize 420 padding 0,0 background None
#                             text c.active.typing xalign 0.0
#                     else:
#                         text "Type text message..." xalign 0.0 color "#0009"
#                     button:
#                         xalign 1.0 ysize 62 background "#222"
#                         text "Send"
#                         if c.active.phase == 3:
#                             action Function(c.active.send, c)

    







# style phone_right:
#     background Frame(im.Flip("phone/frm0.png",True), 10,20,76,10)
#     padding(32,12,96,12)
#     yminimum 64
#     xmaximum 500

# style phone_left:
#     background Frame("phone/frm0.png", 76,20,10,10)
#     padding(96,12,32,12)
#     yminimum 64
#     xmaximum 500
# style phone_right_1:
#     background Frame(im.Flip("phone/frm1.png",True), 10,20,76,10)
#     padding(32,12,96,12)
#     yminimum 64
#     xmaximum 500
# style phone_left_1:
#     background Frame("phone/frm1.png", 76,20,10,10)
#     padding(96,12,32,12)
#     yminimum 64
#     xmaximum 500