import argparse
import ipaddress


def subnet_calc():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="host", required=True)
    parser.add_argument("-m", "--mask", help="mask", required=True)

    args = parser.parse_args()

    iface = ipaddress.ip_interface(f"{args.host}/{args.mask}")
    network = iface.network.network_address
    broadcast = iface.network.broadcast_address
    netmask = iface.netmask
    cidr = args.mask
    hosts = list(iface.network.hosts())
    minimum_host = min(hosts, default=None)
    maximum_host = max(hosts, default=None)

    print(
        f"""
    Network:                {network}/{cidr}
    Network Mask:           {netmask}
    Broadcast:              {broadcast}
    Minimum Hosts:          {minimum_host}
    Maximum Hosts:          {maximum_host}
    Hosts per Network:      {len(hosts)}
    """
    )


if __name__ == "__main__":
    subnet_calc()
