print("Checking module contents...\n")

import crm.followupboss_client as fub
import agents.email_agent_local as email_local
import agents.sms_agent_local as sms_local
import agents.call_script_local as call_local

print("\n== Dir of crm.followupboss_client ==")
print(dir(fub))

print("\n== Dir of agents.email_agent_local ==")
print(dir(email_local))

print("\n== Dir of agents.sms_agent_local ==")
print(dir(sms_local))

print("\n== Dir of agents.call_script_local ==")
print(dir(call_local))
