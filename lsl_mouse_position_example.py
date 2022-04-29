import pylsl
import pyautogui

# Set up the stream info and outlet
info = pylsl.StreamInfo(name='MousePosition', type='mouse', channel_count=2, channel_format=pylsl.cf_float32)
outlet = pylsl.StreamOutlet(info)

# Now run forever:
while True:
    # Get the mouse cursor position
    x, y = pyautogui.position()
    print(f'x: {x}, y: {y}')
    # Send the mouse cursor position to LSL
    outlet.push_sample([x, y])