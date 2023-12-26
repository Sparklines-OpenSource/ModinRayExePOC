from cx_Freeze import setup, Executable
import os
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': [
        "ray",
        "pydantic"
    ], 
    'include_files' : [
       "titanic.csv"
    ],
    'excludes': ["tkinter"],
}

base = 'console'

executables = [
    Executable('app.py', base=base, target_name = 'data_reader')
]

setup(name='Modin_Data_Reader',
      version = '1.0',
      description = 'Modin Cx_Freeze test',
      options = {'build_exe': build_options},
      executables = executables)
