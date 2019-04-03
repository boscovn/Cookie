from cookie import Cookie
from bakery_delegate import BakeryDelegate


class Bakery:
    def __init__(self):
    self.delegate: BakeryDelegate = None

    def make_cookie(self):
        cookie = Cookie()
        cookie.size = 6
        cookie.hasChocolateChips = True
        if self.delegate:
            self.delegate.on_cook
