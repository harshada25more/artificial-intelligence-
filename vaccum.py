def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


location = input("Enter location (A/B): ")
status = input("Enter status (Clean/Dirty): ")

action = vacuum_agent(location, status)

print("Action:", action)