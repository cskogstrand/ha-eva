"""Binary sensor platform for integration_blueprint."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import BINARY_SENSOR_DEVICE_CLASS, DEFAULT_NAME, DOMAIN
from .entity import IntegrationBlueprintEntity


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    """Set up binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([IntegrationBlueprintBinarySensor(coordinator, entry)])


class IntegrationBlueprintBinarySensor(IntegrationBlueprintEntity, BinarySensorEntity):
    """integration_blueprint binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{Platform.BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"
