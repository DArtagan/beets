import os
import shutil
from beets.plugins import BeetsPlugin

class CopyMovePlugin(BeetsPlugin):
    def __init__(self):
        super(CopyMovePlugin, self).__init__()

        self.register_listener('import_task_files', self.copymove)

    def copymove(self, session, task):
        for item in task.imported_items():
            temp_suffix = '_TEMP'
            shutil.copy2(item.path, item.path + temp_suffix)
            os.remove(item.path)
            os.rename(item.path + temp_suffix, item.path)
