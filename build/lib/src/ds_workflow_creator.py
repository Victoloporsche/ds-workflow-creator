import os
from directories_and_files import directories, files


class DsWorkflowCreator:
    def __init__(self, directories, files):
        self.directories = directories
        self.files = files

    def _create_directories(self):
        for dir in self.directories:
            os.makedirs(dir, exist_ok=True)
            with open(os.path.join(dir, ".gitkeep"), "w") as f:
                pass

    def _create_files(self):
        for file in self.files:
            with open(file, "w") as f:
                pass

    def create_my_ds_workflow(self):
        self._create_directories()
        self._create_files()


if __name__ == "__main__":
    ds_workflow_creator = DsWorkflowCreator(directories, files)
    ds_workflow_creator.create_my_ds_workflow()
