import argparse
import os
import sys


def hello(args):
    print("Hello Manvir 😎")

def scan(args):
    print(f"Scanning target: {args.target}")

def main():
    parser = argparse.ArgumentParser(description="My CLI Tool")

    subparsers = parser.add_subparsers(dest="command")

    # hello command
    parser_hello = subparsers.add_parser("hello")
    parser_hello.set_defaults(func=hello)

    # scan command
    parser_scan = subparsers.add_parser("scan")
    parser_scan.add_argument("target")
    parser_scan.set_defaults(func=scan)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

    p3 = subparsers.add_parser("update")
    p3.set_defaults(func=update)

def update(args):
    print("[*] Updating tool from GitHub...")

    # Go to project directory
    project_path = os.path.dirname(os.path.dirname(__file__))
    os.chdir(project_path)

    # Pull latest code
    os.system("git pull")

    # Reinstall tool
    os.system(f"{sys.executable} -m pip install -e .")

    print("[+] Update complete! Restart your command.")