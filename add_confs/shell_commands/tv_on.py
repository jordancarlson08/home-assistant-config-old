from codes import Codes

# Turn off TV and sound
codes = [Codes.tv_power, Codes.sound_up]
Codes.send_commands(codes)
