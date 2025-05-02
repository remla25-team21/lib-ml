from setuptools import setup, find_packages

setup(
    name='lib-ml',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=open('requirements.txt').read().splitlines(),
    include_package_data=True,
)