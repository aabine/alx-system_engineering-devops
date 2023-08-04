# 0x08. Networking Basics #1

Welcome to the Networking Basics #1 repository! This repository covers fundamental networking concepts, and it includes practical Bash scripts to help you experiment and understand networking tasks.

## Change Your Home IP Address

The `change_home_ip.sh` script allows you to modify your home IP address on localhost. It also resolves `facebook.com` to `8.8.8.8` in the `/etc/hosts` file. This script helps you customize your local network configuration and host resolution.

```bash
#!/bin/bash

# Backup original hosts file
sudo cp /etc/hosts /etc/hosts.bak

# Change localhost to 127.0.0.2 and resolve facebook.com to 8.8.8.8
sudo sed -i 's/^127.0.0.1/127.0.0.2/' /etc/hosts
echo "8.8.8.8 facebook.com" | sudo tee -a /etc/hosts

echo "Hosts configuration completed. Your home IP is now set to 127.0.0.2."
```

## Show Attached IP Addresses

The `show_attached_ips.sh` script displays the IP addresses attached to your system's network interfaces. It provides an overview of your network configuration and is useful for troubleshooting and understanding network interfaces.

```bash
#!/bin/bash

# Show attached IP addresses
ip addr
# Show all IPv4 addresses
ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | cut -b 11-
```

## Port Listening

The `port_listener.sh` script sets up a simple listening server on port 98 on localhost using the `netcat` (nc) command. It waits for incoming connections and is handy for testing network connectivity and protocols.

```bash
#!/bin/bash

# Check if nc (netcat) is available
if ! command -v nc &>/dev/null; then
  echo "Error: netcat (nc) command not found. Please install netcat first."
  exit 1
fi

# Start listening on port 98
nc -l -p 98
```

## Usage

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your_username/0x08-networking-basics-1.git
   cd 0x08-networking-basics-1
   ```

2. Run the scripts using `sudo` to execute commands with elevated privileges:
   ```
   sudo ./change_home_ip.sh
   sudo ./show_attached_ips.sh
   sudo ./port_listener.sh
   ```

Explore these Bash scripts to learn and experiment with networking concepts. Enjoy networking exploration and enhance your skills!
