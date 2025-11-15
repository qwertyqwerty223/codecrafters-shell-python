import sys


def main():
    while True:
        exit_status_codes = ['0', '1']
        sys.stdout.write("$ ")
        user_input = input()

        if user_input:
            cmd = user_input.split(' ')

            # exit command
            if cmd[0] == "exit":
                if len(cmd) > 1 and cmd[1] in exit_status_codes:
                    sys.exit(int(cmd[1]))
                else:
                    sys.exit()

            # to handle rest of the commands (for now)
            error_msg = f"{user_input}: command not found"
            print(error_msg)
        


if __name__ == "__main__":
    main()
