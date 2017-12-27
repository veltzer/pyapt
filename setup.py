import setuptools

setuptools.setup(
    name='pyapt',
    version='0.0.3',
    description='module to help you maintain third party apt repos in a sane way',
    long_description='module to help you maintain third party apt repos in a sane way',
    url='https://veltzer.github.io/pyapt',
    download_url='https://github.com/veltzer/pyapt',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='pyapt apt apt-key',
    packages=setuptools.find_packages(),
    install_requires=[
        'pylogconf',  # for logging configuration
        'click',  # used for command line parsing
        'pyfakeuse',  # used for ignoring parameters
    ],
    entry_points={
        'console_scripts': [
            'pyapt_update=pyapt.scripts.update:main',
        ],
    },
)
