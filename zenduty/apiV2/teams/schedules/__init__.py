
from uuid import UUID
from ..models import Team
from .models import Schedule, Override
from zenduty.apiV2.client import ZendutyClient, ZendutyClientRequestMethod


class ScheduleClient:
    def __init__(self, client: ZendutyClient, team: Team):
        self._client = client
        self._team = team

    def get_all_schedules(self) -> list[Schedule]:
        """Get all schedules

        Returns:
            list[Schedule]: list of schedules
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/schedules/" % str(self._team.unique_id),
            success_code=200,
        )
        return [Schedule(**r) for r in response]

    def get_schedule_by_id(self, schedule_id: UUID) -> Schedule:
        """Get schedule by ID

        Args:
            schedule_id (UUID): schedule id of schedule to fetch

        Returns:
            Schedule: Schedule object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/account/teams/%s/schedules/%s/" % (str(self._team.unique_id), str(schedule_id)),
            success_code=200,
        )
        return Schedule(**response)

    def create_schedule(
        self,
        name: str,
        timezone: str,
        description: str = None,
        summary: str = None,
        layers: list[dict] = [],
        overrides: list[dict] = [],
    ) -> Schedule:
        """Create a schedule object

        Args:
            name (str): A string that represents the Schedule object's name
            description (str): A string that represents the Schedule object's description
            summary (str): A string that represents the Schedule object's summary
            timezone (str): A formatted string that represents the Schedule object's time zone. You can check out the time zone list here https://timezonedb.com/time-zones
            layers (list[dict]): An array of Schedule Layers. See LayerBuilder documentation for more information.
            overrides (list[dict]): An array of Schedule Overrides. See OverrideBuilder documentation for more information.

        Returns:
            Schedule: Created Schedule object
        """
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/account/teams/%s/schedules/" % str(self._team.unique_id),
            request_payload={
                "name": name,
                "summary": summary,
                "description": description,
                "time_zone": timezone,
                "layers": layers,
                "overrides": overrides,
            },
            success_code=201,
        )
        return Schedule(**response)

    def update_schedule(
        self,
        schedule: Schedule,
        name: str,
        timezone: str = None,
        description: str = None,
        summary: str = None,
        layers: list[dict] = None,
        overrides: list[dict] = None,
    ) -> Schedule:
        if timezone is None:
            timezone = schedule.time_zone
        if description is None:
            description = schedule.description
        if summary is None:
            summary = schedule.summary
        if layers is None:
            layers = schedule.layers
        if overrides is None:
            overrides = schedule.overrides

        request_payload = {
            "name": name,
            "summary": summary,
            "description": description,
            "time_zone": timezone,
            "layers": layers,
            "overrides": overrides,
        }
        response = self._client.execute(
            method=ZendutyClientRequestMethod.PUT,
            endpoint="/api/account/teams/%s/schedules/%s/" % (str(self._team.unique_id), str(schedule.unique_id)),
            request_payload=request_payload,
            success_code=200,
        )
        return Schedule(**response)

    def delete_schedule(self, schedule: Schedule):
        self._client.execute(
            method=ZendutyClientRequestMethod.DELETE,
            endpoint="/api/account/teams/%s/schedules/%s/" % (str(self._team.unique_id), str(schedule.unique_id)),
            success_code=204,
        )
    
    def list_overrides(self, schedule: Schedule) -> list[Override]:
        response = self._client.execute(
            method=ZendutyClientRequestMethod.GET,
            endpoint="/api/v2/account/teams/{}/schedules/{}/overrides/" % str(self._team.unique_id) % str(schedule.unique_id),
        )
        return [Override(**override) for override in response]
    
    def create_override(self, schedule: Schedule, override_name: str, user: str, start_time: str, end_time: str ) -> Override:
        request_payload = {
            "name": override_name,
            "user": user,
            "start_time": start_time,
            "end_time": end_time,
        }
        response = self._client.execute(
            method=ZendutyClientRequestMethod.POST,
            endpoint="/api/v2/account/teams/{}/schedules/{}/overrides/" % str(self._team.unique_id) % str(schedule.unique_id),
            request_payload=request_payload,
            success_code=200,
        )
        return Override(**response)
