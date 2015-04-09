class Friends(object):
    CONNECTION_GLUE = '_'

    def __init__(self, connections):
        assert isinstance(connections, (tuple, list))
        self.connections = set()
        for friends in connections:
            self.connections.add(self.__encode_connection(friends))

    def add(self, friends):
        key = self.__encode_connection(friends)
        if key in self.connections:
            return False
        self.connections.add(key)
        return True

    def remove(self, connection):
        key = self.__encode_connection(connection)
        if not key in self.connections:
            return False
        self.connections.remove(key)
        return True

    def names(self):
        names = set()
        for key_connection in self.connections:
            map(lambda key: names.add(key), self.__decode_connection(key_connection))
        return names

    def connected(self, friend):
        connected = set()
        for connection in self.connections:
            friends = self.__decode_connection(connection)
            if friend in friends:
                friends.remove(friend)
                connected.add(friends.pop())
        return connected

    @classmethod
    def __encode_connection(cls, friends):
        return cls.CONNECTION_GLUE.join(sorted(friends))

    @classmethod
    def __decode_connection(cls, connection_key):
        assert isinstance(connection_key, str)
        return connection_key.split(cls.CONNECTION_GLUE)


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"