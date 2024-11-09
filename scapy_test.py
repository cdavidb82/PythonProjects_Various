from scapy import all as s
import PyInquirer
import netifaces

def get_interfaces():
    return [{"name": k} for k in netifaces.interfaces()]

def get_questions(interfaces):
    return [
        dict(
            type="checkbox",
            name="interfaces",
            message="Interfaces? :",
            choices=interfaces,
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

def main():
    interfaces = get_interfaces()
    questions = get_questions(interfaces)
    answers = PyInquirer.prompt(questions)
    
    if not answers['interfaces']:
        print("Please select at least one interface.")
        return
    
    try:
        results = s.sniff(iface=answers['interfaces'], timeout=int(answers['timeout']))
    except ValueError:
        print("Invalid timeout value.")
        return

    if answers["save"]:
        s.wrpcap("capture.pcap", results)
    else:
        results.nsummary()

if __name__ == "__main__":
    main()
