import argparse

from pathlib import Path

import ezmsg.core as ez
from ezmsg.panel.application import Application, ApplicationSettings
from ezmsg.tasks.task import TaskSettings
from ezmsg.unicorn.device import UnicornSettings

from .playground import UnicornPlayground, UnicornPlaygroundSettings

class Args:
    data_dir: Path
    buffer_dur: float
    address: str
    n_samp: int

def command():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--data-dir',
        type = lambda x: Path(x).expanduser(),
        default = Path.home() / 'unicorn-playground-data',
        help = 'path for data storage.  default: ~/unicorn-playground-data'
    )

    parser.add_argument(
        '--buffer-dur',
        type = float,
        default = 20.0,
        help = 'maximum buffer duration for data storage. default: 20.0 (sec)'
    )

    unicorn_group = parser.add_argument_group('unicorn')

    unicorn_group.add_argument(
        '--address',
        default = 'simulator',
        help = 'address of device to connect to (XX:XX:XX:XX:XX:XX). default: simulator' 
    )

    unicorn_group.add_argument(
        '--n-samp',
        type = int,
        default = 10,
        help = 'number of samples per eeg message. default: 10'
    )

    args = parser.parse_args(namespace = Args)
        
    app = Application(
        ApplicationSettings(
            port = 0,
            name = 'Unicorn Playground'
        )
    )

    playground = UnicornPlayground(
        UnicornPlaygroundSettings(
            device_settings = UnicornSettings(
                address = args.address,
                n_samp = args.n_samp
            ),
            task_settings = TaskSettings(
                data_dir = args.data_dir,
                buffer_dur = args.buffer_dur
            )
        )
    )

    app.panels = {
        'unicorn': playground.UNICORN.app,
        'ssvep': playground.SSVEP.app
    }

    ez.run(
        APP = app,
        PLAYGROUND = playground
    )