from codes import Codes

# Turn on TV and sound, open Plex.
codes = [Codes.tv_power, Codes.roku_home, Codes.sound_power, Codes.roku_home, Codes.roku_home, Codes.roku_right, Codes.roku_right, Codes.roku_ok]
Codes.send_commands(codes)
