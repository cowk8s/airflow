import argparse
from typing import TypeVar

from rich.console import Console

from docs.exts.docs_build.code_utils import CONSOLE_WIDTH
from docs.exts.docs_build.package_filter import process_package_filters

TEXT_RED = '\033[31m'
TEXT_RESET = '\033[0m'

if __name__ not in ("__main__", "__mp_main__"):
    raise SystemExit(
        "This file is intended to be executed as an executable program. You cannot use it as a module."
        "To run this script, run the ./build_docs.py command"
    )

CHANNEL_INVITATION = """\
If you need help, write to #documentation channel on Airflow's Slack.
Channel link: https://apache-airflow.slack.com/archives/CJ1LVREHX
Invitation link: https://s.apache.org/airflow-slack\
"""

console = Console(force_terminal=True, color_system="standard", width=CONSOLE_WIDTH)

T = TypeVar('T')

def _get_parser():
    parser = argparse.ArgumentParser(
        description='Builds documentation and runs spell checking',
        epilog="List of supported documentation packages:",
    )
    parser.formatter_class = argparse.RawTextHelpFormatter
    parser.add_argument(
        '--disable-checks', dest='disable_checks', action='store_true', help='Disables extra checks'
    )

    parser.add_argument(
        "--package-filter",
        action="append",
        help=(
            "Filter specifying for which packages the documentation is to be built. Wildcard are supported."
        ),
    )

    return parser

def main():
    """Main code"""
    args = _get_parser().parse_args()

    package_filters = args.package_filter

    current_packages = process_package_filters()


if __name__ == "__main__":
    main();