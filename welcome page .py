#!/usr/bin/env python3
# Python script to print "GYMFI" as ASCII art and a welcome message
# ANSI color codes for styling
CYAN = '\033[96m'
LIGHT_CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'
def print_welcome():
    ascii_art = r"""
 ██████╗  __     __   ██████╗ 
██╔════╝  \ \   / / ██╔═══  ██╗
██║  ███╗  \ \_/ /  ██║     ██║
██║   ██║   \   /   ██      ██║
╚██████╔╝    | |    ╚█     ██╔╝
 ╚═════╝     |_|     ╚═════╝ 
"""
    print(f"{CYAN}{BOLD}{ascii_art}{RESET}")
    print(f"{LIGHT_CYAN}Welcome to Gym Membership System!{RESET}")
if __name__ == "__main__":
    print_welcome()