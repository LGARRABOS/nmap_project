import subprocess

def main():
    host = input("Enter Host: ")
    packet = int(input("\nEnter Packet: "))
    print("\n")
    ping = subprocess.getoutput(f"ping -w {packet} {host}")
    print(ping)

main()