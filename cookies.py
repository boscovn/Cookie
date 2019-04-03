from cookie import Cookie
class BakeryDelegate:
    def on_cookie_baked(self, cookie: Cookie):
        pass


class Bakery:
    def __init__(self):
    self.delegate: BakeryDelegate = None

    def make_cookie(self):
        cookie = Cookie()
        cookie.size = 6
        cookie.hasChocolateChips = Tr
        if self.delegate:
            self.delegate.on_cook
