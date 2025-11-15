import sys
import os

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

def file_on_path(filename):
    get_path = os.environ.get("PATH")
    path_list = get_path.split(os.pathsep)
    for path in path_list:
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
        
def cmd_type(*args):
    if args[0] in cmd_dict:
        print(f"{args[0]} is a shell builtin")
    else:
        file_path = file_on_path(args[0])
        if file_path:
            print(f"{args[0]} is {file_path}")
        else:
            error_msg = f"{args[0]}: not found"
            print(error_msg)

def execute_external(cmd):
    file_path = file_on_path(cmd[0])
    if file_path:
        os.system(" ".join(cmd))
    else:
        invalid_cmd(cmd[0])

    pass


global cmd_dict
cmd_dict = {
    "exit": cmd_exit,
    "echo": cmd_echo,
    "type": cmd_type
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
                execute_external(cmd)
        


if __name__ == "__main__":
    main()
