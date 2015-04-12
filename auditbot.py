# Auditbot, an IRC bot for managing IRC communities

# import jaraco (Need to figure out the exact import semantics)

import importlib

import json

import os

import psycopg2

import argparse

def main():
    """Implements the command line parsing and starts the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--connect", "-c")
    parser.add_argument("--nick", "-n")
    arguments = parser.parse_args()
    

class Config():
    """Handles configuration files and the basic foundational services for auditbot."""
    def __init__(self):
        config = self.get_config() # Later have command line argument to specify a filepath to load config from.
        postgresql_ip = config["postgresql_ip"]
        global datastore
        datastore = psycopg2.connect(database="auditbot",) # FIX FIX FIX

    def get_config(filepath=None):
        """Load the configuration file. If parameter filepath is given try to load from filepath."""
        try:
            cust_config = open(filepath)
            config = json.load(cust_config)
            return config
        except IOError:
            raise ValueError("Filepath given at command line did not point to a valid file.")
        try:
            sys_config = open("/etc/auditbot/auditbot.config")
        except IOError:
            print("No config file found in /etc/auditbot, trying ~/.auditbot.")
        try:
            home = os.environ['HOME'] # We break windows support right here.
        except KeyError:
            raise OSError("User does not have a home directory in its environment, "
                          "implying we're not using *nix.")
        user_config_path = os.path.join(home, "auditbot/auditbot.config")
        try:
            user_config = open(user_config_path)
        except IOError:
            if not sys_config:
                raise ValueError("Neither /etc/auditbot or ~/.auditbot had a config file, "
                                 "your install is borked.")
            elif sysconfig:
                print("No config file found in ~/.auditbot, using config in /etc/auditbot/auditbot.config")
            else:
                raise ValueError("Somehow sys_config was both true and not true, something "
                                 "very strange has happened inside the config initializer.")
        if user_config:
            config = json.load(user_config)
        elif sys_config:
            config = json.load(sys_config)
        else:
            raise ValueError("Got to end of config file test handling but somehow user "
                             "and system configurations were absent, something strange has happened.")
        return config
    def hostname_match(hostname):
        """Determine whether string parameter hostname is an ipv4, ipv6 address, 
        or dns hostname. Then check against existing hostnames with fuzzy matching.
        If match is found then return True and the id of the potential match."""
        
        hostsplit = hostname.split(".")
        if len(hostsplit) == 1 and hostname.count(":") == 4:
            for character in hostname:
                if character not in "0123456789abcdef":
                    raise ValueError("--connect: Was not given an ipv4, "
                                     "ipv6 or dns hostname.") 
        
class ABControl(irc.client):
    """The controlling event loop for auditbot, based on the client template in the python Jaraco IRC library."""
    def __init__(self):
        modules = # Not quite sure how to import auditbot components.
        self.components = []
        for module in modules:
            self.components.append(modules[module]())
