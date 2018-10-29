from setuptools import setup, find_packages

with open('requirements.txt', 'r') as fp:
    reqs = [x.strip() for x in fp.readlines()]

with open('README.md', 'r') as fp:
    readme = fp.read()

setup(
    name='mc_autofisher',
    version='0.3',
    description='Automated fisher program for Minecraft',
    long_description=readme,
    classifiers=[
      'Programming Language :: Python :: 3.6'
    ],
    keywords='python python3 minecraft',
    url='https://github.com/r-best/MinecraftAutoFisher',
    author='Robert Best',
    author_email='bobbyisbest3@gmail.com',
    license='gpl-3.0',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    zip_safe=False
)
