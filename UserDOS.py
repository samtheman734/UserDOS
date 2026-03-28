import os
from pathlib import Path

# Directories for simulation
base_dirs = {
    "general": Path("general"),
    "documents": Path("documents"),
    "home": Path("home")
}

# Initialize sample file lists
general = []
docs = []
home = []

# Ensure directories exist
for dir_path in base_dirs.values():
    dir_path.mkdir(exist_ok=True)

# Helper functions
def show_help():
    print("""
MS-DOS Commands:
HELP                       - Show this help message
DIR [<drive>:][<path>]     - List directory contents
COPY <source> <dest>       - Copy file
DEL <filename>             - Delete a file
REN <old> <new>            - Rename a file
TYPE <filename>            - Display file contents
CLS                        - Clear screen
EXIT                       - Exit
""")

def list_directory(target):
    if target not in base_dirs:
        print("Unknown directory.")
        return
    dir_path = base_dirs[target]
    files = list(dir_path.iterdir())
    print(f" Directory of {target}:")
    for f in files:
        print(f"  {f.name}")
    print(f"{len(files)} file(s)")

def copy_file():
    src_name = input("Source filename: ").strip()
    dest_name = input("Destination filename: ").strip()
    target = input("Target directory (general, documents, home): ").strip().lower()
    if target not in base_dirs:
        print("Unknown directory.")
        return
    src_path = base_dirs[target] / src_name
    dest_path = base_dirs[target] / dest_name
    try:
        if src_path.exists():
            with open(src_path, 'rb') as f_src, open(dest_path, 'wb') as f_dest:
                f_dest.write(f_src.read())
            print(f"Copied '{src_name}' to '{dest_name}'.")
        else:
            print("Source file not found.")
    except Exception as e:
        print(f"Error copying file: {e}")

def delete_file():
    filename = input("File to delete: ").strip()
    target = input("Target directory (general, documents, home): ").strip().lower()
    if target not in base_dirs:
        print("Unknown directory.")
        return
    file_path = base_dirs[target] / filename
    try:
        if file_path.exists():
            file_path.unlink()
            print(f"Deleted '{filename}'.")
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def rename_file():
    old_name = input("Old filename: ").strip()
    new_name = input("New filename: ").strip()
    target = input("Target directory (general, documents, home): ").strip().lower()
    if target not in base_dirs:
        print("Unknown directory.")
        return
    old_path = base_dirs[target] / old_name
    new_path = base_dirs[target] / new_name
    try:
        if old_path.exists():
            old_path.rename(new_path)
            print(f"Renamed '{old_name}' to '{new_name}'.")
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error renaming file: {e}")
        
def make_file():
    filename = input("New filename: ").strip()
    target = input("Target directory (general, documents, home): ").strip().lower()
    if target not in base_dirs:
        print("Unknown directory.")
        return
    file_path = base_dirs[target] / filename
    print("Enter text. Type 'EOF' on a new line to finish.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "EOF":
            break
        lines.append(line)
    try:
        with open(file_path, 'w') as f:
            f.write("\n".join(lines))
        print(f"File '{filename}' created successfully.")
        # Update file list if necessary
        if target == "general":
            general.append(filename)
        elif target == "documents":
            docs.append(filename)
        elif target == "home":
            home.append(filename)
    except Exception as e:
        print(f"Error creating file: {e}")

def display_file():
    filename = input("Filename: ").strip()
    target = input("Target directory (general, documents, home): ").strip().lower()
    if target not in base_dirs:
        print("Unknown directory.")
        return
    file_path = base_dirs[target] / filename
    try:
        if file_path.exists():
            with open(file_path, 'r') as f:
                print(f.read())
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Start of the emulator
def main():
    print("""
Starting MS-DOS...

A:\>dir/w

Volume in drive A is BOOT622
Volume Serial Number is 3505-18E3
Directory of A:\

SYS.COM        COMMAND.COM     ATTRIB.EXE     CHKDSK.EXE    DELTREE.EXE
FDISK.LXE      LABEL.EXE       MEM.EXE        MSCDX.EXE     QBRASIC.EXE
UNDELETE.EXE   CD2.SYS         EDI.BAT        HIMEM.SYS     MOUSE.COM
AUTOEXEC.BAT   MOUSE.EXE       CD1.SYS        CD3.SYS       DOSKEY.COM
FREELDR.EXE    SEVER.EXE       SHARE.EXE      XCOPY.EXE     QBASE.ICM
CD4.SYS        CD1.SYS         DEBUG.EXE      TEST.BAS      QUITEMU.COM
CONFIG.SYS

42 file(s)  1,183,761 bytes
116,736 bytes free

""")
    

    while True:
        command = input("A:\\> ").strip()
        if not command:
            continue
        parts = command.split()
        cmd = parts[0].upper()

        if cmd == "HELP":
            show_help()
        elif cmd == "DIR":
            target = parts[1].lower() if len(parts) > 1 else "general"
            list_directory(target)
        elif cmd == "COPY":
            copy_file()
        elif cmd in ("DEL", "ERASE"):
            delete_file()
        elif cmd == "REN":
            rename_file()
        elif cmd == "TYPE":
            display_file()
        elif cmd == "CLS":
            clear_screen()
        elif cmd == "EDIT" or cmd == "COPY CON":
            make_file()
        elif cmd == "EXIT":
            print("A:\\> System halted.")
            break
        else:
            print("Bad command or file name.")

if __name__ == "__main__":
    main()