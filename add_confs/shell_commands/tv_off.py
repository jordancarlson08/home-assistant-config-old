from codes import Codes

# Turn off TV and sound
codes = [Codes.tv_power, Codes.sound_down, Codes.sound_power]
Codes.send_commands(codes)
