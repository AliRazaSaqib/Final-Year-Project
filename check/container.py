class Container(object):
    """
    Object to contains the computation result
    """
    def __init__(self):
        self.container = []
        return

    def get_length(self):
        """
        To return the current container's length
        :return: length of the container
        """
        return self.container.__len__()

    def append_block(self, newData):
        """
        Insert a data block to the container
        :param newData: data to be inserted into the block
        """
        self.container.append(newData)
        return

    def sort_by_features(self):
        """
        Sort all the container's data based on certain key
        """
        self.container = sorted(self.container, key=lambda x:(x[1], x[2]))
        return

    """
    Functions for debug purpose
    """
    def print_all_container(self):
        """
        Prints all the elements inside the container
        """
        for index in range(0, self.container.__len__()):
            print(self.container[index])
        return

    def print_container(self, count):
        """
        Prints certain elements inside the container
        """
        print(f"Element's index: {self.get_length()}")
        if count > self.get_length():
            self.print_all_container()
        else:
            for index in range(0, count):
                print(self.container[index])
        return