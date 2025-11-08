def copy_file(command: str) -> None:
    if not command.strip():
        return
    command_file = command.split()
    if len(command_file) != 3 or command_file[0] != "cp":
        return
    if command_file[1] == command_file[2]:
        return
    try:
        with (
            open(command_file[1], "r") as file_in,
            open(command_file[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
