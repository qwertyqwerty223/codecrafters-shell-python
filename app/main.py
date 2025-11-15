import sys

def invalid_cmd(cmd):
    error_msg = f"{cmd}: command not found"
    print(error_msg)


def cmd_exit(status_code='0'):
        exit_status_codes = ['0', '1']
        if status_code in exit_status_codes:
            sys.exit(int(status_code))
        else:
            invalid_cmd(f"exit {status_code}")


def cmd_echo(*args):
    print(*args)


cmd_dict = {
    "exit": cmd_exit,
    "echo": cmd_echo
}


def main():
    while True:
        sys.stdout.write("$ ")
        user_input = input()

        if user_input:
            cmd = user_input.split(' ')

            # handle existing commands
            if cmd[0] in cmd_dict:
                if len(cmd) > 1:
                    cmd_dict[cmd[0]](*(cmd[1:]))
                else:
                    cmd_dict[cmd[0]]()
            else:
            # to handle rest of the commands (for now)
                invalid_cmd(user_input)
        


if __name__ == "__main__":
    main()
