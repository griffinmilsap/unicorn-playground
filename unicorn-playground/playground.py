import typing

import ezmsg.core as ez

from ezmsg.unicorn.dashboard import UnicornDashboard, UnicornDashboardSettings
from ezmsg.unicorn.device import UnicornSettings
from ezmsg.tasks.ssvep.task import SSVEPTask
from ezmsg.tasks.task import TaskSettings

class UnicornPlaygroundSettings(ez.Settings):
    device_settings: UnicornSettings
    task_settings: TaskSettings

class UnicornPlayground(ez.Collection):
    SETTINGS = UnicornPlaygroundSettings

    UNICORN = UnicornDashboard()
    SSVEP = SSVEPTask()

    def configure(self) -> None:
        self.UNICORN.apply_settings(
            UnicornDashboardSettings(
                device_settings = self.SETTINGS.device_settings
            )
        )

        self.SSVEP.apply_settings(
            self.SETTINGS.task_settings
        )

    @property
    def panels(self):
        return {
            'unicorn': self.UNICORN.app,
            'ssvep': self.SSVEP.app
        }


