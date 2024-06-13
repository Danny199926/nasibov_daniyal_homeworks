# public
# protected
# private

class Wrapper:
    # public
    x = 2

    def public(self):
        return f'Это публичный метод'

    # protected
    _y = 1

    def _protected(self):
        return f'Это частично защищенный метод'

    # private
    __c = 6

    def __private(self):
        return f'Это приватный метод'


class ChildWrapper(Wrapper):

    def check_protected_atr(self):
        return self._y

    def check_private_atr(self):
        return self.__c


child_wrapper = ChildWrapper()
print(child_wrapper.check_protected_atr())
print(child_wrapper._Wrapper__c)
