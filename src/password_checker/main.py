import requests
import hashlib
import argparse
from bs4 import BeautifulSoup
from typing import Union, List


def parse_arguments():
	parser = argparse.ArgumentParser(description='Password Check arguments for console scripts')
	parser.add_argument(
		"-p",
		"--passwords",
		help="Your password that you want to check",
		nargs="+",
		required=True,
		default=[]
	)
	return parser.parse_args()


class PasswordChecker:
	"""A safe password checker that will allow you to see how secure your password is."""
	api_url = "https://api.pwnedpasswords.com/range/"
	
	def __init__(self, password: str):
		self._password = password
	
	def extract(self, hex5dig: str) -> requests.get:
		"""
		Sends a request to the api with the first 5 characters of the sha1 hexdigit string.
		
		Args:
			hex5dig: The first 5 characters of the sha1 password

		Returns:
			The results of the request
		
		Raises:
			RuntimeError: If the request was not successful.
		"""
		req_url = self.api_url + hex5dig
		res = requests.get(req_url)
		if not str(res.status_code).startswith('2'):
			raise RuntimeError(f"Error while fetching. Returned status code was {res.status_code}")
		return res
	
	@staticmethod
	def read_response(res: requests.Response) -> BeautifulSoup:
		"""
		Reads the request response into a Beautiful soup object
		Args:
			res: The request response

		Returns:
			The response parsed into Beautiful soup.
		"""
		return BeautifulSoup(res.content, "html.parser")
	
	def hash_pass(self) -> str:
		"""
		Encodes the passes password in SHA1 format and then converts it to hexadecimal upper case string in order to be
		passed as an extension to the API request
		
		Returns:
		Uppercase Hexadecimal SHA1 string.
		"""
		return hashlib.sha1(self._password.encode("utf-8")).hexdigest().upper()
	
	@staticmethod
	def check_pass_breaches(req: BeautifulSoup, tail_pass: str) -> Union[None, int]:
		"""
		Uses the tail of the passed password to check the results of the request and return the count of breaches if
		there are any.
		
		Args:
			req: The request result.
			tail_pass: The tail of the password

		Returns:
			The count of breeches returned for the given password
		"""
		hashes_dict = {i.split(":")[0]: int(i.split(":")[1]) for i in req.text.splitlines()}
		count = None
		if tail_pass in hashes_dict.keys():
			count = hashes_dict[tail_pass]
		return count
	
	def pawnd_check(self) -> Union[None, int]:
		"""
		Hashes a given password and then sends a request to the password check website in order to see how many times
		the password has been used.
		
		Returns:
			The number o breaches
		"""
		hash_pass = self.hash_pass()
		first5_char, tail_pass = hash_pass[:5], hash_pass[5:]
		req_response = self.extract(first5_char)
		req_response = self.read_response(req_response)
		breaches = self.check_pass_breaches(req_response, tail_pass)
		return breaches


def main(pass_list: List[str]) -> None:
	"""
	Accepts a list of passwords and checks how many times they have been breached.
	
	Args:
		pass_list: A list of passwords
	"""
	for password in pass_list:
		breaches = PasswordChecker(password).pawnd_check()
		if breaches:
			print(f"{password} was found {breaches} times. You should update your password")
		else:
			print(f"{password} is safe")


def main_terminal() -> None:
	"""	Uses parsed arguments and then orchestrates the execution of the program. """
	args = parse_arguments()
	if not args.passwords:
		raise ValueError("You have not passed any passwords")
	main(args.passwords)

