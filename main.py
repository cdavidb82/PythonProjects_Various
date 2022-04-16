from scapy import all as s
import PyInquirer
import netifaces


def main():
    questions = [
        dict(
            type="checkbox",
            name="interfaces",
            message="Interfaces? :",
            choices=[{"name": k} for k in netifaces.interfaces()],
        ),
        dict(
            type="input",
            name="timeout",
            message="How long? "
        ),
        dict(
            type="confirm",
            name="save",
            message="Do you want to save these to a file?"
        ),
    ]

    answers = PyInquirer.prompt(questions)
    results = s.sniff(iface=answers['interfaces'], timeout=int(answers['timeout']))

    if answers["save"]:
        s.wrpcap("capture.pcap", results)
    else:
        results.nsummary()


if __name__ == "__main__":
    main()
