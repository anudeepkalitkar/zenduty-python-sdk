import zenduty
from zenduty.exceptions import ApiException
from zenduty import apiV2
from zenduty.apiV2 import APIException
api_instance = zenduty.TeamsApi(zenduty.ApiClient("ENTER-YOUR-ACCESS-TOKEN-HERE"))

try:
    # Get Incidents
    api_response = api_instance.get_teams()
    print(api_response.data)
except ApiException as e:
    print("Exception when calling TeamsApi->api_account_teams_get: %s\n" % e)

apiv2_instance = apiV2.TeamsClient(apiV2.ZendutyClient(apiV2.ZendutyCredential("ENTER-YOUR-ACCESS-TOKEN-HERE")))

try:
    # Get Teams
    api_response = apiv2_instance.list_teams()
    print(api_response.data)
except APIException as e:
    print("Exception when calling TeamsApi->api_account_teams_get: %s\n" % e)
