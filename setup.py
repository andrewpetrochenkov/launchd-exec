import setuptools

setuptools.setup(
    name='launchd-exec',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/launchd-exec']
)
