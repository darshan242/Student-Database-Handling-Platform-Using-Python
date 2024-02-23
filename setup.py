import cx_Freeze
import sys


includefiles=['student3_118006.ico']
excludes=[]
packages=[]
base=None
if sys.platform=='win32':
    base='Win32GUI'

shortcut_table=[
    ("DesktopShortcut",#Shortcut
     "DesktopFolder",#Directory_
     "StudentManagementSystem",#Name
     "TARGETDIR",# cOMPONENT
     "[TARGETDIR]\StudentManagementSystem.exe",#Target
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",#WkDir
     )
]

msi_data={'Shortcut': shortcut_table}
bdist_msi_option={"data":msi_data}
cx_Freeze.setup(
    version="0.1",
    description="Student Database Management System By Darshan Mardane",
    author="Darshan Mardane ",
    name="Student Management System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_option,},
    executables=[
        cx_Freeze.Executable(
            script="StudentManagementSystem.py",
            base=base,
            icon='student3_118006.ico'
        )
    ]

)
