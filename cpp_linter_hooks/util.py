import subprocess


def check_installed(tool, version='13') -> int:
    command = [f'{tool}-{version} ', '--version']
    try:
        subprocess.run(command, stdout=subprocess.PIPE)
        retval = 0
    except FileNotFoundError:
        # clang-tools exist because install_requires=['clang-tools'] in setup.py
        retval = subprocess.run(['clang-tools', '-i', version], stdout=subprocess.PIPE).returncode
    return retval


def get_expect_version(args) -> str:
    for arg in args:
        if arg.startswith("--version"):  # expect specific clang-tools version.
            # If --version is passed in as 2 arguments, the second is version
            if arg == "--version" and args.index(arg) != len(args) - 1:
                expect_version = args[args.index(arg) + 1]
            # Expected split of --version=14 or --version 14
            else:
                expect_version = arg.replace(" ", "").replace("=", "").replace("--version", "")
            return expect_version
    return None
