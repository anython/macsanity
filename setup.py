from setuptools import setup

setup(
    name='mac-formatter',
    version='0.3.3',
    py_modules=['mac_formatter', 'cli'],
    install_requires=[
        # Your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'mac-formatter=cli:main',
        ],
    },
)
