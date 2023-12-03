from setuptools import setup, Command, find_packages

class StartCommand(Command):
    description = "start the application"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        os.system('python main.py')

setup(
    name='HypergraphProject',
    version='0.1',
    packages=find_packages(),
    cmdclass={
        'start': StartCommand,
    }
)
