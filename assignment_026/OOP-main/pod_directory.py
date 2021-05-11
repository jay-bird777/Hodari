class Pod_directory:
    __name = ""
    __number = ""
    def __init__(self, pod_name):
        self.pod_name = {}
    def add_person(self, name="", number="", people={}):
        self.__update_name_string(name, number)
        self.pod_name[self.__name] = self.__number
        # for name, number in people.items():
        #     self.pod_name[name] = number
    def __update_name_string(self, name, number):
        self.__name = name
        self.__number = number
    def display_person(self):
        for name, number in self.pod_name.items():
            print(name, number)
test = Pod_directory("test");
test.add_person("James", "510-483-8484")
test.display_person()
