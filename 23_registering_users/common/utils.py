import re


class Utils:
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_address_matcher = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False
