import importlib
# import sample
# importlib.reload(sample)

import file_changes

def changes():
    importlib.reload(file_changes)
    file_changes.file_change()

for i in range(5):
    changes()
    input("hit")
