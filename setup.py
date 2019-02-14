import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables=[cx_Freeze.Executable("mygame.py", icon="icon.ico", base = "Win32GUI")]
cx_Freeze.setup(
    name="Kostchevskys PvP Game",
    options={"build_exe": {"packages":["pygame", "os", "sys"], "include_files":[
        "map_bullet_collision.txt", "map_player_collision.txt",
        "data",
        "colours.py","config.py","events.py","maps.py","mygame.py","sprites.py"]}},
    executables=executables
    )