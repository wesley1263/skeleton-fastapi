def is_valid_mac_address(mac_address: str) -> bool:
    import re

    regex = re.compile(r"^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$")
    return regex.match(mac_address) is not None


def is_valid_ip_address(ip_address: str) -> bool:
    import re

    regex = re.compile(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    )
    return regex.match(ip_address) is not None
