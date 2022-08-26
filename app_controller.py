from app_person import Person

class App_controller():
    __people_ordered_age: list = []
    __people_ordered_name: list = []

    def add_person(self, person: Person) -> None:
        if len(self.__people_ordered_age) == 0:
            self.__people_ordered_age.append(person)
            self.__people_ordered_name.append(person)

        else:
            id_to_insert = 0
            while  id_to_insert < len(self.__people_ordered_age)\
                and person.get_age() > self.__people_ordered_age[id_to_insert].get_age():
                id_to_insert += 1

            self.__people_ordered_age.insert(id_to_insert, person)

            id_to_insert = 0
            while id_to_insert < len(self.__people_ordered_name)\
                and person.get_name() > self.__people_ordered_name[id_to_insert].get_name():
                id_to_insert += 1

            self.__people_ordered_name.insert(id_to_insert, person)
    
    def clear_list(self) -> None:
        self.__people_ordered_age.clear()
        self.__people_ordered_name.clear()

    def get_people_ordered_by_age(self) -> list:
        return self.__people_ordered_age
    
    def get_people_ordered_by_nome(self) -> list:
        return self.__people_ordered_name
