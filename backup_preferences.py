import os
from config import BACKUP_DIR
from utils import execute_shell


def backup():
    domains = execute_shell(["defaults", "domains"])
    domains = domains.split("\n")[0].split(", ")
    domains = ["NSGlobalDomain"] + domains

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    for domain in domains:
        filepath = BACKUP_DIR + domain + ".plist"
        print "Backing up: " + domain + " to " + filepath
        execute_shell(["defaults", "export", domain, filepath])


if __name__ == '__main__':
    backup()
