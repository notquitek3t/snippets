import asyncio, os, time, sys
from evdev import InputDevice, categorize, ecodes, KeyEvent, list_devices

DEVICE_NAME = "Crusher ANC 2 (AVRCP)"
CARD = "bluez_card.8C_0D_D9_3C_8F_BE"

async def watch_device(dev):
    print(f"Watching device: {dev.path} - {dev.name}")
    async for event in dev.async_read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == KeyEvent.key_down:
                if key_event.keycode == 'KEY_NEXTSONG':
                    print(f"{dev.name} ({dev.path}): NEXTSONG pressed")
                    os.system("paplay /home/k3t/lib/mic.mp3")
                    time.sleep(1)
                    os.system(f"pactl set-card-profile {CARD} headset-head-unit")


async def bluetooth_mic_swap():
    # Run btmon as async subprocess
    proc = await asyncio.create_subprocess_exec(
        'btmon',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    print("Started btmon monitoring...")

    stdout = proc.stdout

    while True:
        # Read one line at a time asynchronously
        line = await stdout.readline()
        if not line:
            break  # EOF

        if b'Channel: 65' in line and b'len 13' in line:
            # Read next line for data
            data_line = await stdout.readline()
            if not data_line:
                break

            data_line = data_line.rstrip(b'\n')
            tokens = data_line.split()
            if len(tokens) < 13:
                continue

            try:
                raw_bytes = bytes(int(b, 16) for b in tokens[:13])
            except ValueError:
                continue

            if b"AT+CHUP" in raw_bytes:
                print("AT+CHUP detected!")
                # Use asyncio subprocess or just run sync here; sync call is fine for pactl
                os.system(f"pactl set-card-profile {CARD} a2dp-sink")

async def main():
    devices = [InputDevice(path) for path in list_devices()]
    target_devices = [dev for dev in devices if dev.name == DEVICE_NAME]

    if not target_devices:
        print(f"No devices named '{DEVICE_NAME}' found.")
        return

    # Create asyncio tasks for device watchers
    tasks = [asyncio.create_task(watch_device(dev)) for dev in target_devices]

    # Also add the bluetooth mic swap task
    tasks.append(asyncio.create_task(bluetooth_mic_swap()))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
  while True:
    try:
        asyncio.run(main())
    except:
        sys.exit(0)
