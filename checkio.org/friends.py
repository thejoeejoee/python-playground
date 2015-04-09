class Friends(object):
    def __init__(self, connections):
        assert isinstance(connections, (tuple, list))
        self.connections = set()
        for friends in connections:
            friends = sorted(friends)
            self.connections.add(self.__format_connection(friends))

    def add(self, connection):
        pass

    def remove(self, connection):
        pass

    def names(self):
        pass

    def connected(self, friend):
        pass

    @staticmethod
    def __format_connection(friends):
        return ''.join(friends)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"