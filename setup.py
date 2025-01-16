from setuptools import setup, find_packages

setup(
    name="agenteinv",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'PyQt6>=6.0.0',
    ],
    entry_points={
        'console_scripts': [
            'agenteinv=agenteinv.main:main',
        ],
    },
)
