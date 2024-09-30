# unicorn-playground
Use the g.tec Unicorn to do BCI experiments!

## Setup
1. Install [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)
2. Clone this repository to a local location
    `git clone https://github.com/griffinmilsap/unicorn-playground`
3. Navigate to this directory and set up the virtual environment 
    `uv sync`
4. Activate the resulting virtual environment
    * Linux/OSX: `source .venv/bin/activate`
    * Windows: `.venv/bin/activate.bat`
5. Run the software
    `python -m unicorn-playground --device=XX.XX.XX.XX.XX.XX`

Make sure to turn on the Unicorn device -- press and hold the power button until the light starts flashing blue.  Once the light goes solid-blue, the device is connected and data should be streaming.

### Unicorn Address
Currently, this software only works with g.tec Unicorn devices as input.  Although there is some functionality in the software to scan for and connect to nearby Unicorn devices, it's easiest to just manually specify the device to connect to on the command line.  

If you don't have this address, you can get it a few ways.  One way to get this address requires access to a modern Linux machine with Bluetooth, like a Raspberry Pi. Run `bluetoothctl` on your Pi, then type `scan on` and turn on your Unicorn by holding the button for a few seconds.  Once the device status LED is blinking blue, you should eventually see an advertisement that looks like

```
[NEW] Device 60:B6:47:E1:26:9E 60-B6-47-E1-26-9E
[CHG] Device 60:B6:47:E1:26:9E Name: UN-2023.03.64
[CHG] Device 60:B6:47:E1:26:9E Alias: UN-2023.03.64
```

All Unicorn devices advertise a bluetooth device name of the format `UN-XXXX.XX.XX`, and the associated Bluetooth address here is of the format XX:XX:XX:XX:XX:XX.