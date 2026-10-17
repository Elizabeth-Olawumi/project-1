lead = {
    "first_name": "Ruth",
    "phone": "08123456787",
    "messages": 5,
    "asked_for_pricing": True
}
tags = ["new_lead", "asked_for_pricing", "money_paid"]
messages_after_reply = lead["messages"] + 1

print(lead["first_name"])
print(messages_after_reply)
print(tags[2])
print(len(tags))