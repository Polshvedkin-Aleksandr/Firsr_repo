import sys
from pathlib import Path
from clean_folder import sort_func
if __name__ == "__main__":
    road = sys.argv
    try:
        path_d = road[1]
        #path_d='E:\Example_Folder'
        if not Path(path_d).exists():
            print("[-] Folder does not exist")
        else:
            sort_func(path_d, v=0)
            print("[!] Sorting complete")
    except IndexError:
        print("[-] Enter folder to sort !")



