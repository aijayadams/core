#'connection_class': 'cloud_poll',
# 'domain': 'genie_aladdin',
# 'entry_id': '3329dcf7db96450e8dd33fb8bc810100',
# 'options': {},
# 'source': 'user',
# 'system_options': {'disable_new_entities': False},
# 'title': 'Garage Door ',
# 'unique_id': None,
# 'version': 1}

from genie_aladdin.api import AladdinConnection
from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_GARAGE_DOOR,
    BinarySensorEntity,
)
from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Add cert-expiry entry."""
    async_add_entities([AugustDoorBinarySensor()])
    return True


class AugustDoorBinarySensor(BinarySensorEntity):
    """Representation of an August Door binary sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = True

    @property
    def available(self):
        return True

    @property
    def is_on(self):
        return self._state

    @property
    def device_class(self):
        """Return the class of this device."""
        return DEVICE_CLASS_GARAGE_DOOR

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Garage Door Open"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_info(self):
        """Return the device_info of the device."""
        return {"identifiers": DOMAIN}

    async def async_update(self):
        self._state = False
