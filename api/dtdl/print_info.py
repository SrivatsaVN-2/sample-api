
def print_info(interface):

    config = interface.get_config()

    if not config:
        print("No configuration provided")
        return

    print("STB Configuration")
    print("------------------")
    print("Natco:", config.get("natco"))
    print("Language:", config.get("model"))
    print("Release Type:", config.get("location"))
