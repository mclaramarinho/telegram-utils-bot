import string


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

    def __init__(self, user):
        self._uid = user.id
        self._username = user.first_name
        self._step = 0
        self._prev = 0
