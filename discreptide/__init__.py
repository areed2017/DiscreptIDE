from sys import argv

from discreptide.model.Settings import Settings
from discreptide.view.Window import Window, open_workspace, open_last_workspace, os


if __name__ == '__main__':
    Settings(os.path.dirname(os.path.abspath(__file__)))
    if len(argv) <= 1:
        open_workspace()
    else:
        if argv[1] == '-l':
            open_last_workspace()
        else:
            open_workspace()

