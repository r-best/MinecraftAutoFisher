from setuptools import setup, find_packages

with open('requirements.txt', 'r') as fp:
    reqs = [x.strip() for x in fp.readlines()]

setup(
    name='Minecraft AutoFisher',
    version='0.1',
    description='',
    long_description='',
    classifiers=[
      'Programming Language :: Python :: 3.6'
    ],
    keywords='',
    url='https://github.com/r-best/MinecraftAutoFisher',
    author='Robert Best',
    author_email='',
    license='',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    zip_safe=False
)
