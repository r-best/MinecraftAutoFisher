from setuptools import setup, find_packages
import mc_autofisher

with open('requirements.txt', 'r') as fp:
    reqs = [x.strip() for x in fp.readlines()]

with open('README.md', 'r') as fp:
    readme = fp.read()

setup(
    name='mc_autofisher',
    version=mc_autofisher.__version__,
    description='Automated fishing program for Minecraft',
    long_description=readme,
    classifiers=[
      'Programming Language :: Python :: 3.6'
    ],
    keywords='python python3 minecraft',
    url='https://github.com/r-best/MinecraftAutoFisher',
    author=mc_autofisher.__author__,
    author_email=mc_autofisher.__email__,
    license='gpl-3.0',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    zip_safe=False
)
