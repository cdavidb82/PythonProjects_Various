# find IP address
import ifaddr
import pprint


def find_ip():
    adapters = ifaddr.get_adapters()  # receive all adapter with their IP addresses
    pp = pprint.PrettyPrinter(indent=1)
    for adapter in adapters:
        pp.pprint(f'IPs of network adapter: {adapter.nice_name}')
        for ip in adapter.ips:
            pp.pprint('  %s%s' % (ip.ip, ip.network_prefix))


if __name__ == '__main__':
    find_ip()
