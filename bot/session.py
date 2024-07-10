import string

# Session step
# 0 = start
# 1 = rem_bg
# 2 = shorten_url

steps = {
    "start": 0,
    "back_to_menu": 0,
    "rem_bg": 1,
    "shorten_url": 2,
    "to_pdf": 3,
    "about": 4,
}

class Session:
    _uid: int
    _username: string
    _step: int
    _prev: int

    @property
    def uid(self):
        return self._uid

    @property
    def username(self):
        return self._username

    @property
    def step(self):
        return self._step

    @property
    def prev(self):
        return self._prev

    def __init__(self):
        self._step = 0
        self._prev = 0

    def set_user(self, user):
        self._uid = user.id
        self._username = user.first_name

    def change_step(self, callback_data: string):
        try:
            found = False

            for k in steps:
                if callback_data == k:
                    self._prev = self._step
                    self._step = steps[k]
                    found = True
                    break
            if not found:
                raise "Invalid step"

        except Exception as ex:
            raise ex

