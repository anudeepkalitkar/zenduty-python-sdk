from datetime import timedelta
from zenduty.apiV2.accounts.roles import AccountRoleClient
from zenduty.apiV2.events import EventClient
from zenduty.apiV2.events.router import RouterClient
from zenduty.apiV2.incidents import IncidentClient
from zenduty.apiV2.incidents.notes import IncidentNoteClient
from zenduty.apiV2.teams import TeamsClient
from zenduty.apiV2.accounts.members import AccountMemberClient
from zenduty.apiV2.authentication.zenduty_credential import ZendutyCredential
from zenduty.apiV2.teams.escalation_policies.rules import RuleBuilder
from zenduty.apiV2.teams.escalation_policies.targets import TargetBuilder
from zenduty.apiV2.client import ZendutyClient

cred = ZendutyCredential(
    "76ceb7873258d74203707623d8f6aed855b11916"
)  # Default credentials to ZENDUTY_API_KEY env variable if not provided. (use export ZENDUTY_API_KEY="<YOUR KEY>")
client = ZendutyClient(credential=cred, use_https=True)  # defaults to default service endpoint zenduty.com

# >>>>>>>> Accout member client
member_client = AccountMemberClient(client=client)
team = "8b0e01fe-a64d-4252-89ac-7e231dc9a4e3"
# member = member_client.invite(
#     team_id=team,
#     email="john.doe@zenduty.com",
#     first_name="John",
#     last_name="doe",
#     role=3,
# )

# print("Created member...")
# print(member)
# member_by_id = member_client.get_account_member("78a7a407-d630-4874-aca5-c")
# updated_member = member_client.update_account_member(
#     member_by_id,
#     first_name="hello",
# )
# print(updated_member)


# print("updating member...")
# print(updated_member)

# member = member_client.delete_account_member(member_by_id)


# >>>>>>> Account Role client

role_client = AccountRoleClient(client=client)

# role_create = role_client.create_account_role(name="test", description="test", permissions=["sla_read"])
# print("Created role...", role_create)
# get_role = role_client.get_account_role(account_role_id="9679863a-ee17-4403-baa1-f1d11e004080")
# print("Get role...", get_role)

# all_roles = role_client.list_account_roles()
# print("All roles...", all_roles)


# update_role = role_client.update_account_role(get_role, name="test_updated", permissions=["sla_read"])
# print(update_role)

# delete_role = role_client.delete_account_role(account_role_id="3d4206bf-6b3c-477d-8b22-ea1a69767f3d")


# >>>>>>>>>>>> Global Events Router

# router_client = RouterClient(client=client)

# all_routers = router_client.get_all_routers()
# print(all_routers)

# router = router_client.get_router_by_id(router_id="409a712d-9ed3-421b-9277-a0d0943026cc")
# print(router)

# create_router = router_client.create_router(name="hello", description="hello")
# print(create_router)
# router = get_router_by_id("29af7730-734e-4c5d-8085-7b44b70f718e")
# update_router = router_client.update_router(
#     router, name="bro", description="bro"
# )
# print(update_router)

# delete_router = router_client.delete_router(router)

# >>>>>>>>>>>> Events

# event_client = EventClient(client=client)

# get_client = event_client.get_router_client()
# print(get_client)

# create_event = event_client.create_event(
#     integration_key="df590379-3298-41e7-8743-a33abc960964",
#     alert_type="info",
#     message="This is info alert11",
#     summary="This is the incident summary111",
#     entity_id=123455,
#     payload={"status": "ACME Payments are failing", "severity": "1", "project": "kubeprod"},
#     urls=[{"link_url": "https://www.example.com/alerts/12345/", "link_text": "Alert URL"}],
# )
# print(create_event)


# >>>>>>>>>>>> Incident


incident_client = IncidentClient(client=client)

# create_incident = incident_client.create_incident(title="test", service="5acb143b-feb5-4224-8d27-31be349d9f93")
# print(create_incident)

# update_incident = incident_client.update_incident(
#     incident_id="zL6QUtkis7sRX8Hm4twQ7R", status=2, service="5acb143b-feb5-4224-8d27-31be349d9f93"
# )
# print(update_incident)


# list_incidents = incident_client.get_all_incidents(page=1)
# print(list_incidents)

# all_alerts = incident_client.get_alerts_for_incident(incident_number=129)
# print(all_alerts)

## >>>>>>>>>>>>>>>> Incdent Tags and Notes
# incident = incident_client.get_incident_by_unique_id_or_incident_number(incident_id="D8nd9yLtQDqkrqLBXfkKBA")
# incident = incident_client.get_incident_by_unique_id_or_incident_number(incident_id=384)

# note_client = incident_client.get_note_client(incident)

# tag_client = incident_client.get_tags_client(incident)


# all_tags = tag_client.get_all_tags()
# print(all_tags)

# tag_by_id = tag_client.get_tag_by_id(tag_unique_id="1b6ddf90-256e-4cd3-b794-60ee8a8ab549")
# print(tag_by_id)


# create_tag = tag_client.create_tag(team_tag="52b202cb-42a6-4687-9393-4bbf2b5a449a")
# print(create_tag)

# delete_tag = tag_client.delete_tag(tag_by_id)


# get_all_notes = note_client.get_all_incident_notes()
# print(get_all_notes)

# note_by_id = note_client.get_incident_note_by_id(incident_note_unique_id="XJibLaC6pqVZJck62hEJiV")
# print(note_by_id)

# update_note = note_client.update_incident_note(note_by_id, note="updated note")
# print(update_note)

# delete_note = note_client.delete_incident_note(note_by_id)

# create_note = note_client.create_incident_note(note="This is a test note")
# print(create_note)


## >>>>>>>>>>>>>>>> Teams

team_client = TeamsClient(client=client)

# create_team = team_client.create_team(name="Test Team")
# print(create_team)

# list_teams = team_client.list_teams()
# print(list_teams)


team_by_id = team_client.find_team_by_id(team_id="8b0e01fe-a64d-4252-89ac-7e231dc9a4e3")

# print(team_by_id)

# update_team = team_client.update_team(team_id="8f82a80a-1969-4cde-a0d7-2180db7016f4", name="Test Team Updated")
# print(update_team)

# delete_team = team_client.delete_team(team_id="8f82a80a-1969-4cde-a0d7-2180db7016f4")

# team_member = team_client.find_team_member(team_by_id, member_unique_id="b8b76b17-23c3-4a47-b7c2-7ca8dbc60b78")
# print(team_member)


# update_team_member = team_client.update_team_member(
#     team_by_id, member_id="b8b76b17-23c3-4a47-b7c2-7ca8dbc60b78", role=1
# )
# print(update_team_member)

# add_team_member = team_client.add_team_member(team_by_id, username="3ed1ddac-eae2-4246-a46c-e")
# print(add_team_member)


# delete_team_member = team_client.delete_team_member(team_by_id, member_id="b8b76b17-23c3-4a47-b7c2-7ca8dbc60b78")

# list_team_members = team_client.list_team_members(team_by_id)
# print(list_team_members)


# team_permissions = team_client.fetch_team_permissions(team_by_id)
# print(team_permissions)

# updated_team_permissions = team_client.update_team_permissions(permissions=["service_read"], team=team_by_id)
# print(updated_team_permissions)


## >>>>>>>>>>>>>>>>> ESCALATION POLICIES

# esp_client = team_client.get_escalation_policy_client(team_by_id)

# all_esp = esp_client.get_all_policies()
# print(all_esp)


# esp_by_id = esp_client.get_esp_by_id(esp_id="3e773789-6da2-4d4b-ae6f-7dc71bb8bb4a")
# print(esp_by_id)

# rules = [{"delay": 0, "targets": [{"target_type": 2, "target_id": "3ed1ddac-eae2-4246-a46c-e"}], "position": 1}]
# update_esp = esp_client.update_esp(esp=esp_by_id, name="Test Updated", rules=rules)
# print(update_esp)


# delete_esp = esp_client.delete_esp(esp=esp_by_id)

# create_esp = esp_client.create_esp(name="Test", rules=rules)
# print(create_esp)


## >>>>>>>>>>>>>>>>> Maintenance

# maintenance_client = team_client.get_maintenance_client(team_by_id)

# create_maintenance = maintenance_client.create_team_maintenance(
#     name="Test Maintenance",
#     start_time="2022-07-08T18:06:00",
#     end_time="2022-07-08T18:06:00",
#     service_ids=["d8b4079c-1da7-4575-a62e-f81332379179"],
# )
# print(create_maintenance)

# all_maintenance = maintenance_client.get_all_maintenance()
# print(all_maintenance)
# maintenance_by_id = maintenance_client.get_maintenance_by_id(maintenance_id="b3f9fef6-6695-4992-b431-e741cd7487e2")
# print(maintenance_by_id)

# update_maintenance = maintenance_client.update_maintenance(
#     maintenance_by_id,
#     name="Test Maintenance Updated",
#     start_time="2022-07-08T18:06:00",
#     end_time="2022-07-08T18:06:00",
#     service_ids=["d8b4079c-1da7-4575-a62e-f81332379179"],
# )
# print(update_maintenance)

# delete_maintenance = maintenance_client.delete_maintenance(maintenance_by_id)


## >>>>>>>>>>>>>>>>> Postmortem

# postmortem_client = team_client.get_postmortem_client(team_by_id)

# create_postmortem = postmortem_client.create_postmortem(
#     author="3ed1ddac-eae2-4246-a46c-e",
#     incidents=["HBjEtT42aBszGXHUq7RJSb"],
#     title="Test Postmortem",
# )
# print(create_postmortem)
# postmortem_by_id = postmortem_client.get_postmortem_by_id(postmortem_id="a309a104-dd79-46a3-8c9f-7b5a004694d5")

# update_postmortem = postmortem_client.update_postmortem(
#     postmortem_by_id,
#     author="3ed1ddac-eae2-4246-a46c-e",
#     incidents=["fjPAJaUAVMC2smL8KS455i"],
#     title="Test Postmortem Updated",
# )
# print(update_postmortem)


# delete_postmortem = postmortem_client.delete_postmortem(postmortem_by_id)


## Priorities

# priority_client = team_client.get_priority_client(team_by_id)

# create_priority = priority_client.create_priority(name="Test Priority", description="Test Priority", color="red")
# print(create_priority)

# all_priorities = priority_client.get_all_priorities()
# print(all_priorities)

# priority_by_id = priority_client.get_priority_by_id(priority_id="cfe65879-626b-4cd2-a9eb-23173fb33cba")
# print(priority_by_id)


# update_priority = priority_client.update_priority(
#     priority_by_id, name="Test Priority Updated", description="Test Priority"
# )
# print(update_priority)

# delete_priority = priority_client.delete_priority(priority_by_id)


## >>>>>>>>>>>>>>>>> Roles

# role_client = team_client.get_incident_role_client(team_by_id)


# create_role = role_client.create_incident_role(title="Test Role", description="Test Role", rank=1)
# print(create_role)
# role_by_id = role_client.get_incident_role_by_id(role_id="3bb215ed-90e5-4267-8fcf-cc159ef43cb4")
# update_role = role_client.update_incident_role(
#     role_by_id,
#     title="Test Role Updated",
# )
# print(update_role)

# delete_role = role_client.delete_incident_role(role_by_id)


## >>>>>>>>>>>>>>>>> Schedules

# schedule_client = team_client.get_schedule_client(team_by_id)

# all_schedules = schedule_client.get_all_schedules()
# print(all_schedules)

# schedule_by_id = schedule_client.get_schedule_by_id(schedule_id="570a5652-b383-45b0-8537-ffaa4866be13")
# print(schedule_by_id)

# layers = [
#     {
#         "name": "Layer 1",
#         "is_active": True,
#         "restriction_type": 0,
#         "restrictions": [],
#         "rotation_start_time": "2024-07-29T03:30:00.000Z",
#         "rotation_end_time": None,
#         "shift_length": 86400,
#         "users": [
#             {
#                 "user": "3ed1ddac-eae2-4246-a46c-e",
#                 "position": 1,
#             }
#         ],
#     }
# ]
# overrides = [
#     {
#         "name": "",
#         "user": "3ed1ddac-eae2-4246-a46c-e",
#         "start_time": "2024-07-29T11:54:34.745000Z",
#         "end_time": "2024-07-29T18:29:59.999000Z",
#     }
# ]
# create_schedule = schedule_client.create_schedule(
#     name="hello", timezone="Asia/Kolkata", layers=layers, overrides=overrides
# )
# print(create_schedule)

# update_schedule = schedule_client.update_schedule(schedule=schedule_by_id, name="Test Updated")
# print(update_schedule)


## >>>>>>>>>>>>> SERVICES
# service_client = team_client.get_service_client(team_by_id)


# all_services = service_client.get_all_services()
# print(all_services)

# service_by_id = service_client.get_service_by_id(service_id="d8b4079c-1da7-4575-a62e-f81332379179")
# print(service_by_id)

# create_service = service_client.create_service(
#     name="Test Service",
#     escalation_policy="7609b426-f660-4c0a-857c-a654f88b350f",
#     team_priority="b7daa557-dcf3-4c98-86fd-d3de10d8e702",
#     sla="be8ac506-4ef9-41df-9496-3cc898c7b083",
# )
# print(create_service)

# update_service = service_client.update_service(
#     service_by_id,
#     name="Test Service Updated",
#     escalation_policy="7609b426-f660-4c0a-857c-a654f88b350f",
#     team_priority="b7daa557-dcf3-4c98-86fd-d3de10d8e702",
#     sla="be8ac506-4ef9-41df-9496-3cc898c7b083",
# )
# print(update_service)


## >>>>>>>>>>>>>>>>>>>>>>> Integraion
# integration_client = service_client.get_integration_client(svc=service_by_id)

# all_integrations = integration_client.get_all_integrations()
# print(all_integrations)

# integration_by_id = integration_client.get_intg_by_id(intg="01388f00-895e-48ae-ae2f-bb628569015a")
# print(integration_by_id)

# create_integration = integration_client.create_intg(
#     name="Test Integration", summary="Test Integration", application="27c9800c-2856-490d-8119-790be1308dd4"
# )
# print(create_integration)

# update_integration = integration_client.update_intg(
#     intg=integration_by_id, name="Test Integration Updated", application="27c9800c-2856-490d-8119-790be1308dd4"
# )
# print(update_integration)


## for alerts
# team_by_id = team_client.find_team_by_id(team_id="36d73d10-1b65-4548-b8b2-c6ea5a87bf65")

# service_client = team_client.get_service_client(team_by_id)
# service_by_id = service_client.get_service_by_id(service_id="8d123616-edb0-4f3d-8f0d-a3bec3abc5ff")

# intgration_client = service_client.get_integration_client(svc=service_by_id)
# intg_by_id = intgration_client.get_intg_by_id(intg="14bf30a5-e364-4ef9-8ce3-2db612a85f8b")


# alerts = intgration_client.get_intg_alerts_iter(intg=intg_by_id, page=1)
# print(alerts)

## >>>>>>>>>>>>>>>>>>>>>>> SLA
# sla_client = team_client.get_sla_client(team_by_id)
# all_slas = sla_client.get_all_slas()
# print(all_slas)

# create_sla = sla_client.create_sla(name="Test SLA", escalations=[])
# print(create_sla)
# sla_by_id = sla_client.get_sla_by_id(sla_id="46e495a3-e118-4b27-b1ea-0191e2e14320")

# update_sla = sla_client.update_sla(sla=sla_by_id, name="Test SLA Updated", escalations=[])
# print(update_sla)


## >>>>>>>>>>>>>>>>>>. Tags
# tag_client = team_client.get_tag_client(team_by_id)
# create_tag = tag_client.create_tag(name="TestXsadasd", color="red")
# print(create_tag)

## >>>>>>>>>>>>>>>>>>. Task Templates
task_template_client = team_client.get_task_template_client(team_by_id)
# create_task_template = task_template_client.create_task_template(
#     name="Test Task Template", summary="Test Task Template"
# )
# print(create_task_template)

all_task_templates = task_template_client.get_all_task_template()
# print(all_task_templates)
task_template_by_id = task_template_client.get_task_template_by_id(
    task_template_id="27a762f3-0062-4a09-b49c-d3a10a464dd7"
)
# print("****")
# print(task_template_by_id)

# update_task_template = task_template_client.update_task_template(
#     task_template_by_id, name="Test Task Template Updated"
# )
# print(update_task_template)
