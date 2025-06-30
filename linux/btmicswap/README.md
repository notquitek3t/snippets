# Bluetooth mic swap
A lil hack i made around linux's bluetooth utilities and evdev..

### The idea:
When you have a usb headset, you can easily switch between muted and unmuted. On bluetooth, this doesn't exist.

This tool bridges the gap by reading for KEY_NEXTSONG via evdev. When this key is pressed on the headset, pactl is used to switch to headset-head-unit audio profile. This enables the mic, at a loss of audio quality.

It also reads btmon, a deprecated utility, for AT+CHUP. This AT command is sent by a bluetooth headset to.. hang up the call. It's the only input I found that could be received by the Crusher ANC 2. When received, it will switch the headset via pactl back into the a2dp-sink profile.



Aanyways, hopefully someone else has a need for this too
-kai :3
