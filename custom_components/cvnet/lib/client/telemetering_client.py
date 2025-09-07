import logging

from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo, DeviceEntryType

from .common.cvnet_base_client import CvnetBaseClient
from ..api.device.telemetering import TelemeteringDeviceApi
from ..model.device import TelemeteringRespond

_LOGGER = logging.getLogger(__name__)

class TelemeteringClient(CvnetBaseClient):
    async def _get_telemetering_data(self) -> TelemeteringRespond:
        return await TelemeteringDeviceApi.get_telemetering_device_detail(self.session, self.config)

    async def get_telemetering_data(self) -> TelemeteringRespond:
        return await self._request(self._get_telemetering_data)

    async def get_data(self) -> dict[str, Any]:
        data = await self.get_telemetering_data()
        # --- 디버깅 코드 ---
        # Home Assistant 로그에 'data' 변수의 실제 내용을 출력합니다.
        # 오류가 발생했으므로, 이번에는 경고(warning) 레벨로 출력하여 로그에 확실히 보이게 합니다.
        _LOGGER.warning(f"CVnet API 응답 데이터 확인 (디버깅): {data}")
        # --- 디버깅 코드 끝 ---

        return {
            "telemetering_electricity": {
                # "type": SensorDeviceClass.ENERGY,
                # "name": "Electricity Consumption",
                "name": "",
                "use_default_name": True,
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "electricity_sensor": {
                    "value": data["electricity"],
                },
            },
            "telemetering_gas": {
                # "type": SensorDeviceClass.GAS,
                # "name": "Gas Consumption",
                "name": "",
                "use_default_name": True,
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "gas_sensor": {
                    "value": data["gas"],
                },
            },
            "telemetering_water": {
                # "type": SensorDeviceClass.WATER,
                # "name": "Water Consumption",
                "name": "",
                "use_default_name": True,
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "water_sensor": {
                    "value": data["water"],
                },
            },
            "telemetering_hotwater": {
                # "type": SensorDeviceClass.HOTWATER,
                # "name": "Hotwater Consumption",
                "name": "",
                "use_default_name": True,
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "hotwater_sensor": {
                    "value": data["hotwater"],
                },
            },
            "telemetering_heating": {
                # "type": SensorDeviceClass.Heating,
                # "name": "Water Consumption",
                "name": "",
                "use_default_name": True,
                "info": DeviceInfo(
                    identifiers={(self.config.unique_id, "telemetering")},
                    entry_type=DeviceEntryType.SERVICE,
                    manufacturer="CVnet",
                    translation_key="telemetering",
                ),
                "heating_sensor": {
                    "value": data["heating"],
                },
            },
        }
