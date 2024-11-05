import socket
import re
from common_ports import ports_and_services


def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    host_ip = target
    hostname = target
    # print(target)
    if is_ip(target) and verbose:
        try:
            hostname = socket.gethostbyaddr(target)[0]
        except socket.herror:
            pass
    elif verbose:
        host_ip = socket.gethostbyname(target)

    try:
        # print(hostname,host_ip)
        for port in range(port_range[0], port_range[1]+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            # print(port)
            # returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                # print(f"Port {port} is open")
                open_ports.append(port)
            s.close()
    except KeyboardInterrupt:
        return "Exiting program!!!"
    except socket.gaierror:
        if re.search('[a-zA-Z]', target):
            return "Error: Invalid hostname"
        return "Error: Invalid IP address"
    except socket.error:
        return "Error: Invalid IP address"

    if verbose:
        result = f"Open ports for {hostname} ({host_ip})\n"
        if hostname == host_ip:
            result = f"Open ports for {hostname}\n"
        header = "PORT     SERVICE\n"
        body = ""
        for port in open_ports:
            service_name = ports_and_services.get(port, "unknown")
            body += f"{port}{' ' * (9 - len(str(port)))}{service_name}\n"
        # print(result + header + body)
        return (result + header + body.strip('\n'))

    return (open_ports)


def is_ip(address):
    return address.replace('.', '').isnumeric()
