
#!/usr/bin/env python3
import json

def main():
    # Define inventory dynamically
    inventory = {
        "all": {
            "hosts": ["webserver1", "webserver2"],
            "vars": {
                "ansible_user": "ec2-user",
                "ansible_ssh_private_key_file": "/path/to/private/key",
            },
        },
        "_meta": {
            "hostvars": {
                "webserver1": {"ansible_host": "192.168.1.10"},
                "webserver2": {"ansible_host": "192.168.1.11"},
            },
        },
    }

    print(json.dumps(inventory))

if __name__ == "__main__":
    main()
