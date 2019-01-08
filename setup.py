import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python37\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python37\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Dungeons & Pythons",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["classes/__init__.py",
                                            "classes/enemy.py",
                                            "classes/entity.py",
                                            "classes/level.py",
                                            "classes/player.py",
                                            "classes/position.py",
                                            "utilities/__init__.py",
                                            "utilities/drawable.py",
                                            "game.py"]}},
    executables = executables

    )