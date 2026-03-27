## -----------------------------------------------------
## Phone System with Integrated Chat
## -----------------------------------------------------
image screen_background_image = Transform("phone/screen.png", zoom=1.0)

init -1 python:
    import re

    # =====================================================
    # CHAT CONFIGURATION (from phone.rpy)
    # =====================================================
    
    # configurable variables for easy plug-and-play
    phone_config = {
        # Sound Configuration
        "play_sound_send": True,
        "play_sound_receive": True,
        "no_sound_current_chat": False, # For incoming messages, only play if not viewing the chat
        # String Configurations
        "preview_no_message": "Empty chat...",
        "channels_title": "Messages",
        "history_timestamp_prefix": "Time:",
        "phone_player_name": "Me",
        "group_added": "{adder} added {participant} to the group.",
        "group_joined": "{participant} joined the group.",
        "group_left": "{participant} left the group.",
        # UI Configurations
        "message_font_size": 24,
        "choice_font_size": 24,
        "timestamp_font_size": 20,
        "auto_scroll": True,
        "show_sender_in_preview": True,
        "default_icon": "phone/icon.png",
        "user_colour": "#FFFFFF",
        "character_colour": "#000000",
        "timestamp_colour": "#000000",
        "sort_channels_by_latest": True,
        "message_padding": 0.025,
        "preview_max_length": 25,
        "emojis": {
            "size": 32,
        },

        "phone_theme": "light",  # default theme
        "light": {
            # colours for light mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for light mode
            "screen_background_image": "phone/screen.png",
            "header_background_image": "phone/header.png",
            #"base_background_image": "phone/base.png",
            "back_button_idle_image": "phone/back.png",
            "back_button_notif_image": "phone/back_notif.png",
            "notification_dot_image": "phone/notif.png",
            "player_bubble_image": "phone/player_bubble.png",
            "player_bubble_hover_image": "phone/player_bubble_hover.png",
            "character_bubble_image": "phone/character_bubble.png",
        },
        "dark": { 
            # colours for dark mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#FFFFFF",
            "timestamp_text_colour": "#AAAAAA",
            "header_text_colour": "#FFFFFF",
            "channel_name_text_colour": "#FFFFFF",
            "channel_preview_text_colour": "#BBBBBB",
            "sender_name_text_colour": "#AAAAAA",
            "channel_divider_colour": "#444444",
            "channel_button_hover_background": "#333333",
            "empty_channel_text_colour": "#FFFFFF",
            # dark mode images
            "screen_background_image": "phone/skins/dark_mode/screen.png",
            "header_background_image": "phone/skins/dark_mode/header.png",
            "base_background_image": "phone/skins/dark_mode/base.png",
            "back_button_idle_image": "phone/skins/dark_mode/back.png",
            "back_button_notif_image": "phone/skins/dark_mode/back_notif.png",
            "notification_dot_image": "phone/skins/dark_mode/notif.png",
            "player_bubble_image": "phone/skins/dark_mode/player_bubble.png",
            "player_bubble_hover_image": "phone/skins/dark_mode/player_bubble_hover.png",
            "character_bubble_image": "phone/skins/dark_mode/character_bubble.png",
        },
        "flip": {
            # colours for flip phone mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for flip phone mode
            "screen_background_image": "phone/skins/flip_phone/screen.png",
            "header_background_image": "phone/header.png",
            "base_background_image": "phone/skins/flip_phone/base.png",
            "back_button_idle_image": "phone/back.png",
            "back_button_notif_image": "phone/back_notif.png",
            "notification_dot_image": "phone/notif.png",
            "player_bubble_image": "phone/player_bubble.png",
            "player_bubble_hover_image": "phone/player_bubble_hover.png",
            "character_bubble_image": "phone/character_bubble.png",
        },
        "status_bar": {
            # colours for status bar phone mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for status bar phone mode
            "screen_background_image": "phone/screen.png",
            "header_background_image": "phone/skins/status_bar/header.png",
            #"base_background_image": "phone/base.png",
            "back_button_idle_image": "phone/back.png",
            "back_button_notif_image": "phone/back_notif.png",
            "notification_dot_image": "phone/notif.png",
            "player_bubble_image": "phone/player_bubble.png",
            "player_bubble_hover_image": "phone/player_bubble_hover.png",
            "character_bubble_image": "phone/character_bubble.png",
        },
        # Gameplay Configurations
        "pause": { # no pause = messages will not wait for user time or user input before sending the next one
            "do_pause": True, # should we wait for a click to send the next message? like traditional dialogue
            "pause_time": False, # if we want to pause, should we auto-continue after a set amount of time? if false, just wait for a click
            "pause_length": 1.0 # if using pause_time, how long do we wait?
        }
    }

    # =====================================================
    # CHAT DATA VARIABLES
    # =====================================================
    
    # variables to hold the phone data
    phone_channel_data = {} # {channel_name: {"display_name": "...", "icon": "...", "participants": [], "is_group": False}}
    phone_channels = {}  # {channel_name: [(id, sender, message_string, kind, ...), ...]}
    channel_last_message_id = {} # {channel_name: last_id}
    channel_seen_latest = {} # {channel_name: seen_status} (this could be more intricate to track if EACH message was seen, but that's overkill)
    channel_notifs = {} # {channel_name: notification_status} (True/False)
    channel_visible = {} # {channel_name: visible_status} (True/False)
    current_phone_view = "channel_list" # where when the phone starts it should start at
    disable_phone_menu_switch = False # lock back button, basically
    phone_choice_options = [] # this will hold the currently active choices
    phone_choice_channel = None  # this holds the channel that the above choice aligns to (one at a time)
    channel_latest_global_id = {} # latest global channel id
    _phone_global_message_counter = 0  # latest global message counter

    # replace inline images natively
    def replace_emojis(text):
        """ Replaces custom emoji tags like <emoji_name> with Ren'Py image tags.
            This is an internal helper function to allow for easy emoji syntax in messages.
            Args:
                text (str): The message text that might contain emoji tags.
        """
        def sub(match):
            name = match.group(1)
            return "{image=%s}" % name
        return re.sub(r"<([A-Za-z0-9_]+)>", sub, text)

    # creates a new phone channel
    def create_phone_channel(channel_id, display_name, participants, icon_path, is_group=False):
        """ Creates a new phone channel, like a DM or a group chat.
            This function sets up the basic information for a new chat conversation.
            Args:
                channel_id (str): A unique identifier for the channel (e.g., "vanessa_dm").
                display_name (str): The name that appears at the top of the chat screen.
                participants (list): A list of strings with the names of everyone in the chat.
                icon_path (str): The file path to the icon for this channel.
                is_group (bool, optional): Set to True if this is a group chat. Defaults to False.
        """
        global phone_channel_data, phone_channels, channel_last_message_id, channel_notifs, channel_seen_latest, channel_visible
        if channel_id not in phone_channel_data:
            phone_channel_data[channel_id] = {
                "display_name": display_name,
                "icon": icon_path,
                "participants": participants,
                "is_group": is_group
            }
            phone_channels[channel_id] = []
            channel_last_message_id[channel_id] = 0
            channel_notifs[channel_id] = False
            channel_seen_latest[channel_id] = True
            channel_visible[channel_id] = True
            channel_latest_global_id[channel_id] = 0

    # add messages to a channel in the phone (kind 0 = normal message, kind 1 = timestamp, kind 2 = photo, kind 3 = has emojis)
    def send_phone_message(sender, message_text, channel_name, message_kind=0, summary_alt="none", image_x=320, image_y=320, do_pause=True):
        """ Sends a message to a specific phone channel and updates the UI.
            Args:
                sender (str): The name of the character sending the message.
                message_text (str): The content of the message or the path to an image.
                channel_name (str): The unique ID of the channel to send the message to.
                message_kind (int, optional): The type of message. 
                    0=text, 1=timestamp, 2=photo, 3=text with emoji. Defaults to 0.
                summary_alt (str, optional): Alternative text for the channel preview list. Defaults to "none".
                image_x (int, optional): The max width for a photo message. Defaults to 320.
                image_y (int, optional): The max height for a photo message. Defaults to 320.
                do_pause (bool, optional): Whether to pause the game after the message is sent. Defaults to True.
        """
        global _phone_global_message_counter, current_global_id
        # in case a channel doesn't exist, we now expect them to be explicitly made before-hand~
        if channel_name not in phone_channels:
            renpy.log("Tried to send message to non-existent channel: " + channel_name)
            return
        # sound logic (except for time stamps)
        if message_kind != 1:
            if sender == phone_config["phone_player_name"]:
                if phone_config.get("play_sound_send", False):
                    renpy.sound.play("audio/phone/send.mp3", channel="sound")
            else:
                play_the_sound = True
                if phone_config.get("no_sound_current_chat", False):
                    if current_phone_view == channel_name:
                        play_the_sound = False
                if phone_config.get("play_sound_receive", False) and play_the_sound:
                    renpy.sound.play("audio/phone/receive.mp3", channel="sound")
        _phone_global_message_counter += 1
        current_global_id = _phone_global_message_counter
        channel_latest_global_id[channel_name] = current_global_id
        last_id = channel_last_message_id.get(channel_name, 0)
        current_id = last_id + 1
        channel_last_message_id[channel_name] = current_id
        message_data = (current_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y)
        phone_channels[channel_name].append(message_data)
        channel_notifs[channel_name] = True
        channel_seen_latest[channel_name] = False
        renpy.restart_interaction()
        if message_kind == 0:
            narrator.add_history(kind="adv", who=sender, what=message_text)
        elif message_kind == 1:
            narrator.add_history(kind="adv", who=phone_config["history_timestamp_prefix"], what=message_text)
        elif message_kind == 2:
            narrator.add_history(kind="adv", who=sender, what="Sent a photo.")
        renpy.checkpoint()
        if do_pause and phone_config["pause"]["do_pause"]:
            if phone_config["pause"]["pause_time"]:
                renpy.pause(phone_config["pause"]["pause_length"])
            else:
                renpy.pause()

    # basically clear notifs / mark as read for all
    def clear_notifications():
        """ Marks all channels as read and clears all notification dots.
            This is useful for when the story starts, to clear any pre-loaded messages,
            or if you want to programmatically mark everything as seen.
        """
        global channel_notifs, channel_seen_latest
        for channel_name in phone_channel_data.keys():
            if channel_name in channel_notifs:
                channel_notifs[channel_name] = False
            if channel_name in channel_seen_latest:
                channel_seen_latest[channel_name] = True
        renpy.restart_interaction()
    
    # =====================================================
    # RESTORED: function to reset the phone data
    # =====================================================
    def reset_phone_data():
        """ Resets all phone data to a clean slate.
            This function clears all channels, messages, and notifications.
            You can add initial setup calls (like create_phone_channel)
            inside this function to pre-populate the phone.
        """
        global current_phone_view, phone_channels, channel_last_message_id, channel_notifs, channel_seen_latest, channel_visible, phone_channel_data
        global channel_latest_global_id, _phone_global_message_counter
        # reset all our data
        phone_channel_data = {}
        phone_channels = {}
        channel_last_message_id = {}
        channel_notifs = {}
        channel_seen_latest = {}
        channel_visible = {}
        channel_latest_global_id = {}
        _phone_global_message_counter = 0
        current_phone_view = "channel_list"
        


        renpy.restart_interaction()

    # pause the text messages for a certain length
    def phone_pause(length=1.0):
        """ Pauses the game for a specific amount of time within the phone.
            This is a simple wrapper around renpy.pause() for convenience, allowing for
            timed delays between messages without relying on the automatic pause config.
            Args:
                length (float, optional): The duration of the pause in seconds. Defaults to 1.0.
        """
        renpy.pause(length)

    # hide the text box stuff when the phone is up
    def phone_start():
        """ Activates phone mode, preparing the UI for the phone screen.
            This function sets a flag that can be used to hide the normal
            dialogue window, ensuring the phone UI doesn't overlap with it.
            It should be called right before showing the phone_ui screen.
        """
        global phone_mode
        phone_mode = True
        renpy.restart_interaction()

    # restore the text box stuff when the phone is down
    def phone_end():
        """ Deactivates phone mode, restoring the normal game UI.
            This function resets the flag set by phone_start(), which should
            bring back the standard dialogue window. It should be called
            right after hiding the phone_ui screen.
        """
        global phone_mode
        phone_mode = False
        renpy.restart_interaction()

    # disable switching phone screens
    def lock_phone_screen():
        """ Disables the back button on the phone screen.
            This locks the player into the current view (a specific chat)
            and prevents them from returning to the channel list. Useful for
            scripted sequences where you need the player's focus.
        """
        global disable_phone_menu_switch
        disable_phone_menu_switch = True

    # enable switching phone screens
    def unlock_phone_screen():
        """ Enables the back button on the phone screen.
            This restores the player's ability to navigate back to the channel
            list from a chat view (basically just undoing the effect of lock_phone_screen()).
        """
        global disable_phone_menu_switch
        disable_phone_menu_switch = False

    # present choices to the user in the phone
    def present_phone_choices(choices, channel_name):
        """ Presents a set of choices to the player within a phone channel.
            This function displays tappable choice bubbles for the player. The game
            will pause and wait for the player to make a selection.
            Args:
                choices (list): A list of tuples defining the choices. Each tuple is in the
                    format ("preview_text", "message_to_send", action).
                    - "preview_text": The text shown on the choice button.
                    - "message_to_send": The message text that gets sent. If None, uses preview_text.
                    - "action": A Ren'Py action (like Call() or Jump()) to run after sending. Can be None.
                channel_name (str): The unique ID of the channel where the choices will appear.
        """
        # choices should be a list of tuples, like:
        # [("Choice Text 1", Jump("response_label_1")), ("Choice Text 2", Jump("response_label_2"))]
        global phone_choice_options, phone_choice_channel
        phone_choice_options = choices
        phone_choice_channel = channel_name
        renpy.ui.interact()  # make the game wait for the user..

    # gets the last message to show in the phone preview
    def get_channel_preview(channel_name):
        """ Gets the preview text for a channel to display on the channel list.
            This function retrieves the last message of a channel, formats it for
            the preview (e.g., adding sender for group chats, truncating), and
            returns it. It's an internal function used by the phone_ui screen.

            Args:
                channel_name (str): The unique ID of the channel to get the preview for.
        """
        if channel_name in phone_channels and phone_channels[channel_name]:
            for last_message_tuple in reversed(phone_channels[channel_name]):
                if last_message_tuple[3] != 1:  # skip message_kind=1 (index is now 3)
                    summary_alt = last_message_tuple[5] if len(last_message_tuple) > 5 else None
                    if summary_alt and summary_alt != "none":
                        return summary_alt
                    sender = last_message_tuple[1]
                    message_text = last_message_tuple[2]
                    message_kind = last_message_tuple[3]
                    preview_text = message_text
                    if message_kind == 3: # has emojis, get rid of them with fire
                        preview_text = re.sub(r"<[^>]+>", "", preview_text).strip()
                    # prepend sender if it's a group chat and not from the player
                    is_group = phone_channel_data.get(channel_name, {}).get("is_group", False)
                    if is_group and sender != phone_config["phone_player_name"]:
                        full_preview = "{}: {}".format(sender, preview_text)
                    else:
                        full_preview = preview_text
                    max_len = phone_config.get("preview_max_length", 35) 
                    if len(full_preview) > max_len:
                        # Slice it to make room for the "..."
                        return full_preview[:max_len - 3] + "..."
                    else:
                        return full_preview
        return phone_config["preview_no_message"]

    # force the user to go to a certain channel (can also be channel_list)
    def switch_channel_view(channel_name):
        """ Forces the phone to open a specific channel or the channel list.
            This can be used to guide the player to a new message or event in a
            different chat without requiring them to tap on it manually.
            Args:
                channel_name (str): The unique ID of the channel to switch to. Can also be
                    "channel_list" to return to the main message list.
        """
        global current_phone_view, channel_notifs, channel_seen_latest
        current_phone_view = channel_name
        if channel_name in channel_notifs:
            channel_notifs[channel_name] = False
        if channel_name in channel_seen_latest:
            channel_seen_latest[channel_name] = True
        renpy.restart_interaction()

    # hide a channel without deleting the data
    def hide_phone_channel(channel_name):
        """ Hides a channel from the channel list without deleting its history.
            The channel and its messages are preserved and can be made visible again
            using show_phone_channel().
            Args:
                channel_name (str): The unique ID of the channel to hide.
        """
        global channel_visible
        if channel_name in channel_visible:
            channel_visible[channel_name] = False
            renpy.restart_interaction()

    # show a channel that was hidden
    def show_phone_channel(channel_name):
        """ Makes a previously hidden channel visible again on the channel list.
            This function reverses the effect of hide_phone_channel().
            Args:
                channel_name (str): The unique ID of the channel to show.
        """
        global channel_visible
        if channel_name in channel_visible:
            channel_visible[channel_name] = True
            renpy.restart_interaction()

    # perma hide a channel aka delete it lol
    def delete_phone_channel(channel_name):
        """ Permanently deletes a channel and all of its associated data.
            This action is irreversible and will remove the channel, its messages,
            and all related settings from the phone.
            Args:
                channel_name (str): The unique ID of the channel to delete.
        """
        global phone_channel_data, phone_channels, channel_last_message_id, channel_seen_latest, channel_notifs, channel_visible, channel_latest_global_id, current_phone_view
        if channel_name in phone_channel_data:
            del phone_channel_data[channel_name]
        if channel_name in phone_channels:
            del phone_channels[channel_name]
        if channel_name in channel_last_message_id:
            del channel_last_message_id[channel_name]
        if channel_name in channel_seen_latest:
            del channel_seen_latest[channel_name]
        if channel_name in channel_notifs:
            del channel_notifs[channel_name]
        if channel_name in channel_visible:
            del channel_visible[channel_name]
        if channel_name in channel_latest_global_id:
            del channel_latest_global_id[channel_name]
        # make sure they aren't viewing a dead chat
        if current_phone_view == channel_name:
            switch_channel_view("channel_list")
        renpy.restart_interaction()

    # add someone to a group
    def add_participant_to_group(channel_name, new_participant_name, added_by_name=None):
        """ Adds a participant to a group chat and posts a notification message.
            This will update the channel's participant list and send a system message
            (like "X added Y to the group") to the chat.
            Args:
                channel_name (str): The unique ID of the group channel.
                new_participant_name (str): The name of the character being added.
                added_by_name (str, optional): The name of the character who added the new
                    participant. If None, a generic "joined" message is shown. Defaults to None.
        """
        if channel_name in phone_channel_data and phone_channel_data[channel_name]["is_group"]:
            phone_channel_data[channel_name]["participants"].append(new_participant_name)
            if added_by_name:
                template = phone_config.get("group_added", "{adder} added {participant} to the group.")
                message_text = template.format(adder=added_by_name, participant=new_participant_name)
            else:
                template = phone_config.get("group_joined", "{participant} joined the group.")
                message_text = template.format(participant=new_participant_name)
            send_phone_message("", message_text, channel_name, message_kind=1, do_pause=True)

    def remove_participant_from_group(channel_name, participant_to_remove):
        """Removes a participant from a group chat and posts a notification message.
            This will update the channel's participant list and send a system message
            (like "X left the group") to the chat.
            Args:
                channel_name (str): The unique ID of the group channel.
                participant_to_remove (str): The name of the character to remove.
        """
        if channel_name in phone_channel_data and phone_channel_data[channel_name]["is_group"]:
            if participant_to_remove in phone_channel_data[channel_name]["participants"]:
                phone_channel_data[channel_name]["participants"].remove(participant_to_remove)
                template = phone_config.get("group_left", "{participant} left the group.")
                message_text = template.format(participant=participant_to_remove)
                send_phone_message("", message_text, channel_name, message_kind=1, do_pause=True)

    # see if there is any current notifications at all
    def has_any_notification():
        """Checks if any channel has an active notification."""
        return any(channel_notifs.values())

    # same as above, but ignore the active channel (for instance, used to change the back icon)
    def has_any_notification_not_active():
        """Checks if any channel OTHER than the current one has an active notification."""
        return any(has_notif for channel, has_notif in channel_notifs.items() if channel != current_phone_view)

    # helper to grab values per theme
    def get_phone_theme_value(key):
        """Retrieves a theme-specific value from phone_config based on the current theme."""
        current_theme = phone_config["phone_theme"]
        # Accessing directly using the theme name as a key
        return phone_config[current_theme].get(key)

    # set the phone's theme to change via code (ex. if user wants dark mode instead)
    def set_phone_theme(theme_name):
        """Sets the phone's theme to a new value.
            This function changes the current theme of the phone UI, which can be used
            to switch between light, dark, or flip themes dynamically.
            Args:
                theme_name (str): The name of the theme to switch to (e.g., "light", "dark", "flip").
        """
        if theme_name in phone_config:
            phone_config["phone_theme"] = theme_name
            renpy.restart_interaction()
        else:
            renpy.log("Invalid phone theme: " + theme_name)


# =====================================================
# PHONE SYSTEM CLASSES (from phone Class.rpy)
# =====================================================

init python:
    class phone_class:
        def __init__(self, id, width=600, height=900):
            self.id = id
            self.width = width
            self.height = height
            self.frame = [20,50,20,100]
            self.x = 10
            self.y = 10

            self.apps = []
            self.apps.append(phone_app(_("Camera"), "phone/camera.png", "phone_camera"))
            self.apps.append(phone_app(_("Contacts"), "phone/contacts.png", "phone_contacts"))
            self.apps.append(phone_app(_("Calls"), "phone/calls.png", "phone_calls"))
            self.apps.append(phone_app(_("Calendar"), "phone/calendar.png", "phone_calendar"))
            self.apps.append(phone_app(_("Album"), "phone/album.png", "phone_album"))
            self.apps.append(phone_app(_("Chat"), "phone/chat.png", "phone_chat_integrated"))
            self.apps.append(phone_app(_("Weather"), "phone/weather.png", "phone_weather"))
            self.apps.append(phone_app(_("Calculator"), "phone/calculator.png", "phone_calculator"))

            self.portrait = True
            self.rotation = 0
            self.bg = "#222"

            self.photos = []
            self.photo_index = 1

        def dragged(self, drags, drops):
            self.x = drags[0].x
            self.y = drags[0].y
        def rotate(self):
            if self.portrait:
                self.rotation = -90
            else:
                self.rotation = 90
        def rotate_done(self):
            self.width, self.height = self.height, self.width
            self.portrait = not self.portrait
            self.rotation = 0
            
    class phone_app:
        def __init__(self, name, icon, screen, bg = "#222"):
            self.name = name
            self.icon = icon
            self.screen = screen
            self.bg = bg

    config.underlay.append(
        renpy.Keymap(
            K_BACKQUOTE=lambda: renpy.run(ToggleScreen("phone_desktop"))
        )
    )

    def phone_go_home():
        """Return to the phone desktop from any app"""
        global current_phone_view
        current_phone_view = "channel_list"
        renpy.hide_screen("phone_chat_integrated")
        renpy.hide_screen("phone_camera")
        renpy.hide_screen("phone_album")
        renpy.hide_screen("phone_calculator")
        renpy.hide_screen("phone_weather")
        renpy.hide_screen("phone_contacts")
        renpy.hide_screen("phone_calls")
        renpy.show_screen("phone_desktop")
        renpy.restart_interaction()


# =====================================================
# INTEGRATED CHAT SCREEN
# =====================================================

screen phone_chat_integrated(p=phone):
    tag phone
    use phone_main(p):
        frame:
            xysize(p.width, p.height) 
            background None
            padding 0, 0
            
            # Chat UI using the images from phone_config
            $ theme_val = get_phone_theme_value
            
            # Screen background
            add theme_val("screen_background_image")
            
            # Header (with title)
            frame:
                background theme_val("header_background_image")
                xfill True
                ysize 100
                ypos 0
                
                # Back button
                if current_phone_view != "channel_list" and disable_phone_menu_switch == False:
                    $ back_icon_path = theme_val("back_button_notif_image") if has_any_notification_not_active() else theme_val("back_button_idle_image")
                    imagebutton:
                        xpos 10
                        ypos 0
                        idle back_icon_path
                        hover back_icon_path
                        focus_mask True
                        xysize (50, 50)
                        action SetVariable("current_phone_view", "channel_list")
                
                # Channel title
                if current_phone_view != "channel_list" and current_phone_view in phone_channel_data:
                    hbox:
                        xalign 0.5
                        ypos 30
                        if current_phone_view in phone_channel_data:
                            add phone_channel_data[current_phone_view]["icon"]:
                                xysize (50, 50)
                                ypos -15
                            text " " + phone_channel_data[current_phone_view]["display_name"]:
                                style "phone_header_style"
                                color theme_val("header_text_colour")
                                size 24
                else:
                    text phone_config["channels_title"]:
                        style "phone_header_style"
                        color theme_val("header_text_colour")
                        size 28
                        xalign 0.5
                        yalign 0.5
            
            # Base overlay
            add theme_val("base_background_image")
            
            # Main content area
            fixed:
                xsize 560
                ysize 770
                xpos 20
                ypos 100
                
                if current_phone_view == "channel_list":
                    # CHANNEL LIST VIEW
                    viewport:
                        id "channel_viewport"
                        xfill True
                        yfill True
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        
                        vbox:
                            spacing 10
                            $ visible_channels = [ch for ch in phone_channel_data.keys() if channel_visible.get(ch, True)]
                            python:
                                if phone_config["sort_channels_by_latest"]:
                                    channel_list_to_display = sorted(visible_channels, key=lambda ch_name: channel_latest_global_id.get(ch_name, 0), reverse=True)
                                else:
                                    channel_list_to_display = visible_channels
                            
                            for channel_name in channel_list_to_display:
                                button:
                                    action [
                                        SetDict(channel_notifs, channel_name, False),
                                        SetVariable("current_phone_view", channel_name)
                                    ]
                                    style "phone_channel_button_style"
                                    xfill True
                                    
                                    vbox:
                                        hbox:
                                            spacing 5
                                            # Channel icon
                                            add phone_channel_data[channel_name]["icon"]:
                                                xysize (50, 50)
                                                yalign 0.3
                                            
                                            # Channel name and preview
                                            vbox:
                                                text phone_channel_data[channel_name]["display_name"]:
                                                    style "phone_channel_name_style"
                                                    color theme_val("channel_name_text_colour")
                                                text get_channel_preview(channel_name):
                                                    style "phone_channel_preview_style"
                                                    color theme_val("channel_preview_text_colour")
                                            
                                            # Notification dot
                                            if channel_notifs.get(channel_name, False):
                                                add theme_val("notification_dot_image"):
                                                    xalign 1.0
                                                    yalign 0
                                                    xoffset -5
                                                    size (25, 25)
                                        
                                        # Divider
                                        frame:
                                            background theme_val("channel_divider_colour")
                                            xfill True
                                            ysize 1
                
                else:
                    # CHAT VIEW
                    viewport:
                        id "chat_viewport"
                        xfill True
                        yfill True
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable False
                        
                        vbox:
                            spacing 8
                            xfill True
                            
                            if current_phone_view in phone_channels:
                                $ latest_channel_id = channel_last_message_id.get(current_phone_view, 0)
                                $ last_sender_in_chat_view = None
                                
                                # Display all messages
                                for message_data in phone_channels[current_phone_view]:
                                    $ msg_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y = message_data
                                    
                                    if sender == phone_config["phone_player_name"]:
                                        $ bubble_image = theme_val("player_bubble_image")
                                        $ text_colour = theme_val("message_player_text_colour")
                                        $ anim_direction = 1
                                        $ bubble_alignment = 1.0
                                    else:
                                        $ bubble_image = theme_val("character_bubble_image")
                                        $ text_colour = theme_val("message_character_text_colour")
                                        $ anim_direction = -1
                                        $ bubble_alignment = 0.0
                                    
                                    $ msg_padding = phone_config["message_padding"]
                                    
                                    # Show sender name for group chats
                                    $ is_group_chat = phone_channel_data[current_phone_view]["is_group"]
                                    if is_group_chat and sender != phone_config["phone_player_name"] and sender != last_sender_in_chat_view:
                                        text sender:
                                            style "phone_sender_name_style"
                                            color theme_val("sender_name_text_colour")
                                            xalign msg_padding
                                            xoffset 5
                                    
                                    # Message bubble
                                    if message_kind == 0:  # Text
                                        if bubble_alignment == 0.0:
                                            # Left-aligned (character)
                                            frame:
                                                xpos msg_padding
                                                xanchor 0.0
                                                background Frame(bubble_image, 23, 23)
                                                padding (15, 10)
                                                xmaximum 400
                                                if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                    at message_appear(anim_direction)
                                                    $ channel_seen_latest[current_phone_view] = True
                                                    $ channel_notifs[current_phone_view] = False
                                                text message_text:
                                                    color text_colour
                                                    size phone_config["message_font_size"]
                                                    layout "tex"
                                        else:
                                            # Right-aligned (player)
                                            frame:
                                                xpos 1.0 - msg_padding
                                                xanchor 1.0
                                                background Frame(bubble_image, 23, 23)
                                                padding (15, 10)
                                                xmaximum 400
                                                if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                    at message_appear(anim_direction)
                                                    $ channel_seen_latest[current_phone_view] = True
                                                    $ channel_notifs[current_phone_view] = False
                                                text message_text:
                                                    color text_colour
                                                    size phone_config["message_font_size"]
                                                    layout "tex"
                                        $ last_sender_in_chat_view = sender
                                    
                                    elif message_kind == 1:  # Timestamp
                                        null height 5
                                        hbox:
                                            xalign 0.5
                                            xmaximum 360
                                            if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                at timestamp_appear()
                                                $ channel_seen_latest[current_phone_view] = True
                                                $ channel_notifs[current_phone_view] = False
                                            text message_text:
                                                color theme_val("timestamp_text_colour")
                                                size phone_config["timestamp_font_size"]
                                                layout "tex"
                                        null height 15
                                        $ last_sender_in_chat_view = None
                                    
                                    elif message_kind == 2:  # Photo
                                        if bubble_alignment == 0.0:
                                            # Left-aligned (character)
                                            frame:
                                                xpos msg_padding
                                                xanchor 0.0
                                                background Frame(bubble_image, 23, 23)
                                                padding (10, 10)
                                                xmaximum 400
                                                if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                    at message_appear(anim_direction)
                                                    $ channel_seen_latest[current_phone_view] = True
                                                    $ channel_notifs[current_phone_view] = False
                                                add Image(message_text) at scale_to_fit(image_x, image_y)
                                        else:
                                            # Right-aligned (player)
                                            frame:
                                                xpos 1.0 - msg_padding
                                                xanchor 1.0
                                                background Frame(bubble_image, 23, 23)
                                                padding (10, 10)
                                                xmaximum 400
                                                if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                    at message_appear(anim_direction)
                                                    $ channel_seen_latest[current_phone_view] = True
                                                    $ channel_notifs[current_phone_view] = False
                                                add Image(message_text) at scale_to_fit(image_x, image_y)
                                        $ last_sender_in_chat_view = sender
                                    
                                    elif message_kind == 3:  # Text with emojis
                                        if bubble_alignment == 0.0:
                                            # Left-aligned (character)
                                            frame:
                                                xpos msg_padding
                                                xanchor 0.0
                                                background Frame(bubble_image, 23, 23)
                                                padding (10, 10)
                                                xmaximum 400
                                                if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                    at message_appear(anim_direction)
                                                    $ channel_seen_latest[current_phone_view] = True
                                                    $ channel_notifs[current_phone_view] = False
                                                hbox:
                                                    spacing 5
                                                    xmaximum 380
                                                    text replace_emojis(message_text):
                                                        size phone_config["message_font_size"]
                                                        color text_colour
                                                        layout "tex"
                                        else:
                                            # Right-aligned (player)
                                            frame:
                                                xpos 1.0 - msg_padding
                                                xanchor 1.0
                                                background Frame(bubble_image, 23, 23)
                                                padding (10, 10)
                                                xmaximum 400
                                                if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                    at message_appear(anim_direction)
                                                    $ channel_seen_latest[current_phone_view] = True
                                                    $ channel_notifs[current_phone_view] = False
                                                hbox:
                                                    spacing 5
                                                    xmaximum 380
                                                    text replace_emojis(message_text):
                                                        size phone_config["message_font_size"]
                                                        color text_colour
                                                        layout "tex"
                                        $ last_sender_in_chat_view = sender
                            
                            # Choices
                            if phone_choice_options and phone_choice_channel == current_phone_view:
                                null height 20
                                vbox:
                                    xalign 0.5
                                    spacing 8
                                    for i, (preview_text, actual_message, action) in enumerate(phone_choice_options):
                                        $ message_to_send = actual_message if actual_message is not None else preview_text
                                        $ text_colour = theme_val("message_player_text_colour")
                                        textbutton preview_text at choice_appear(delay = i * 0.1):
                                            action [
                                                SetVariable("phone_choice_options", []),
                                                SetVariable("phone_choice_channel", None),
                                                SetVariable("disable_phone_menu_switch", False),
                                                Function(send_phone_message, sender=phone_config["phone_player_name"], message_text=message_to_send, channel_name=current_phone_view, do_pause=False),
                                                If(action is not None, action),
                                                #Return()
                                            ]
                                            background Frame(theme_val("player_bubble_image"), 23, 23)
                                            idle_background Frame(theme_val("player_bubble_image"), 23, 23)
                                            hover_background Frame(theme_val("player_bubble_hover_image"), 23, 23)
                                            text_color text_colour
                                            text_size phone_config["choice_font_size"]
                                            text_align 0.5
                                            xalign 0.5
                                            padding (15, 10)
                            
                            null height 30



# =====================================================
# PHONE DESKTOP (Main Launcher) - FIXED
# =====================================================

screen phone(p=phone):
    tag phone
    zorder 100
    modal True


    
    # The phone frame with drag capability
    drag:
        pos(p.x, p.y)
        dragged p.dragged
        
    use phone_main:
        frame:
            xysize(p.width,p.height) background p.bg
            hbox:
                box_wrap True spacing 6 box_wrap_spacing 6 xalign .5
                for i in p.apps:
                    button:
                        vbox:
                            add i.icon
                            text i.name xalign .5 size 20
                        action Show(i.screen)
                



# =====================================================
# PHONE MAIN FRAME
# =====================================================

screen phone_main(p=phone):
    
    zorder 100
    tag phone
    if p.rotation:
        timer 0.4 repeat True action Function(p.rotate_done)
    
    drag:
        pos(p.x, p.y)
        dragged p.dragged
        
        if p.rotation:
            at phone_rotate(p.rotation)
        
        frame:
            if p.portrait:
                background Frame("phone/frame.png", 44, 50, 44, 100)
                padding p.frame[0], p.frame[1], p.frame[2], p.frame[3]
            else:
                background Frame("phone/frame1.png", 50, 44, 100, 44)
                padding p.frame[1], p.frame[2], p.frame[3], p.frame[0]
            
            fixed:
                xysize(p.width, p.height)
                transclude
                
                if p.portrait:
                    hbox:
                        align 0.5,1.0 yoffset 70 spacing 140
                        button:
                            background None 
                            text "↩"
                            action Return()
                        button:
                            background None
                            text "⌂"
                            action Show("phone")
                        button:
                            background None
                            text "⊡"
                            action Show("phone_settings")
                else:
                    hbox:
                        align 1.0,0.5 xoffset 70 spacing 140
                        at rotate(-90)
                        button:
                            background None
                            text "↩"
                            action Return()
                        button:
                            background None
                            text "⌂"
                            action Show("phone")
                        button:
                            background None
                            text "⊡"
                            action Show("phone_settings")
                
               




# =====================================================
# PHONE ROTATION TRANSFORM
# =====================================================

transform phone_rotate(r):
    rotate_pad False
    ease 0.42 rotate r
    rotate 0


# =====================================================
# CHAT ANIMATIONS
# =====================================================

transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0
    alpha 1.0

transform timestamp_appear():
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

transform choice_appear(delay=0.0):
    alpha 0.0
    yoffset 50
    pause delay
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

transform scale_to_fit(maxw, maxh):
    size (maxw, maxh)
    fit "contain"


# =====================================================
# OTHER PHONE APPS (placeholders)
# =====================================================

# Camera
init python:
    import os
    import time

    phone_camera_image = None
    phone_camera_image_old = []

    def save_scaled_cropped_screenshot(p):

        if p.portrait:
            left = p.frame[0]
            top = p.frame[1]
        else:
            left = p.frame[1]
            top = p.frame[2]

        crop = (p.x + left, p.y + top, p.width, p.height)
        scale = (1920, 1080)

        # ✅ FIXED DIRECTORY (IMPORTANT)
        directory = os.path.join(renpy.config.gamedir, "phone", "DCIM")

        # ✅ CREATE FOLDER IF NOT EXISTS
        if not os.path.exists(directory):
            os.makedirs(directory)

        # ✅ KEEP YOUR INDEX SYSTEM (but safer)
        filename = "IMG-{:04}.jpg".format(p.photo_index)
        p.photo_index += 1

        fullpath = os.path.join(directory, filename)

        ui.pausebehavior(0.0)
        ui.interact(suppress_overlay=True, suppress_window=True)

        surf = renpy.display.draw.screenshot(renpy.game.interface.surftree)
        surf = renpy.display.scale.smoothscale(surf, scale)
        surf = surf.subsurface(crop)
        renpy.display.render.mutated_surface(surf)

        try:
            renpy.display.scale.image_save_unscaled(surf, fullpath)
            return filename
        except Exception as e:
            print("SAVE ERROR:", e)
            if renpy.config.debug:
                raise
            return None

    def phone_remove_pick():
        global phone_camera_image, phone_camera_image_old
        phone_camera_image_old.append(Crop((0, 0, 600, 600), phone_camera_image))
        phone_camera_image = None
    
    photos = []
    def camera_take_photo(p):
        newPhoto = renpy.invoke_in_new_context(save_scaled_cropped_screenshot, p = p)

        renpy.transition(Fade(0,0,0.2,color=(255,255,255,128)))

        p.photos.append(newPhoto)

screen phone_camera(p = phone):
    tag phone
    use phone_main:
        frame:
            xysize(p.width,p.height) background "#0006" padding 0,0
            if phone_camera_image:
                add phone_camera_image
                # text str(phone_camera_image)
                # timer 2 repeat True action Function(phone_remove_pick)

            if len(p.photos):
                button:
                    align 1.0,1.0 background "#000c" offset -10,-10
                    add Crop((0,0,600,600),"phone/DCIM/" + p.photos[-1]) at zoom(.2)
                    action Show("phone_album") 

            vbox:
                align 1.0,.5 spacing 10
                button:
                    xysize 80,80 background "#0009"
                    text "Capture" size 15 align .5,.5
                    action Function(camera_take_photo, p = p)
                button:
                    xysize 80,80 background "#0009"
                    text "Film" size 15 align .5,.5
                    action Function(camera_take_photo, p = p)
                button:
                    xysize 80,80 background "#0009"
                    text "close" size 15 align .5,.5
                    action Show("phone_desktop")

screen camera_flash:
    add "#fff"
    timer .1 action Hide("camera_flash")

# Photo album
screen phone_album(p = phone):
    tag phone
    default selected = None
    use phone_main:
        frame:
            xysize(p.width,p.height) background "#333" padding 0,0
            if len(p.photos):
                hbox:
                    box_wrap True
                    for i in p.photos:
                        button:
                            vbox:
                                add Crop((0,0,600,600),"phone/DCIM/" + i) at zoom(.2)
                                text i size 16
                            action SetScreenVariable("selected", i)
            if selected:
                button:
                    padding 0,0 align .5,.5
                    add "phone/DCIM/"+selected at zoom(image_fit("phone/DCIM/"+selected, p.width, p.height))
                    action SetScreenVariable("selected", None)

            hbox:
                spacing 10 align 1.0,1.0 offset -10,-10
                button:
                    background "#111"
                    text "Camera" size 15
                    action Show("phone_camera") 



screen phone_calculator(p=phone):
    tag phone
    use phone_main(p):
        frame:
            xysize(p.width, p.height)
            background "#333"
            text "Calculator App" align 0.5,0.5 color "#FFF"

screen phone_weather(p=phone):
    tag phone
    use phone_main(p):
        frame:
            xysize(p.width, p.height)
            background "#333"
            text "Weather App" align 0.5,0.5 color "#FFF"

screen phone_contacts(p=phone):
    tag phone
    use phone_main(p):
        frame:
            xysize(p.width, p.height)
            background "#333"
            text "Contacts App" align 0.5,0.5 color "#FFF"

screen phone_calls(p=phone):
    tag phone
    use phone_main(p):
        frame:
            xysize(p.width, p.height)
            background "#333"
            text "Calls App" align 0.5,0.5 color "#FFF"


# =====================================================
# INITIALIZATION
# =====================================================

# Phone instance - REMOVE these lines if they're defined elsewhere
default test_phone = phone_class("aye")
default phone = test_phone

# Phone mode flag
define phone_mode = False

# Initialize chat data
init python:
    # Store original sound settings
    original_sound_send = phone_config.get("play_sound_send")
    original_sound_receive = phone_config.get("play_sound_receive")
    
    # Disable sounds during initialization
    phone_config["play_sound_send"] = False
    phone_config["play_sound_receive"] = False
    
    # Initialize chat data
    reset_phone_data()
    
    # Restore original sound settings
    phone_config["play_sound_send"] = original_sound_send
    phone_config["play_sound_receive"] = original_sound_receive


# =====================================================
# EMOJI DEFINITIONS
# =====================================================

image emoji_sob = "phone/emoji/sob.png"
image emoji_dizzy = "phone/emoji/dizzy.png"