from setuptools import setup, find_packages


setup(
    name='quoridor_env',
    version='1.0.0',
    description='A quoridor environment for self-play reinforcement learning ',
    author='Lucas Bertola',
    # url='https://github.com/lucasBertola/Connect-4-env',  
    # author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.pt'],
    },
    install_requires=[
        'pygame==2.1.3',
        'gymnasium==0.28.1',
    ]
)

#python setup.py sdist bdist_wheel
#twine upload dist/*