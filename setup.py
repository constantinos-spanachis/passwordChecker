from setuptools import setup, find_packages

with open("requirements.txt") as file:
	required_packages = file.read().splitlines()

setup(
	name='password-checker',
	version='0.0.1',
	packages=find_packages(where="src"),
	description="A small package that checks if your password has been used before",
	author_email="c.spanachis@gmail.com",
	author="Constantinos.spanachis",
	url="https://github.com/constantinos-spanachis/passwordChecker",
	classifiers=[
		'Development Status :: ',
		'Natural Language :: English',
		'Programming Language :: Python :: 3',
		"Operating System :: OS Independent"
	],
	long_description=open('README.md').read(),
	package_dir={"": "src"},
	python_requires=">=3.7",
	install_requires=required_packages,
	entry_points = {
		"console_scripts": [
			"check_password = password_checker.main: main_terminal"
		]
	}
)
