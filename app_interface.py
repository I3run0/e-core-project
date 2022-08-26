from app_controller import App_controller
from app_person import Person

class App_interface():
    __app_controller: App_controller = App_controller()

    def get_cmd_intro(self) -> str:
        return "**********************************************\n" +\
        "Welcome to the System of Bruno Sobreira Franca\n" +\
        "**********************************************\n\n" +\
        "Type help to ask for help\n"

    def get_cmd_prompt(self) -> str:
        return "(register) "

    def add_person(self) -> None:
        name: str = input("Name: ")
        age: int = int(input("Age: "))

        print()

        self.__app_controller.add_person(Person(name, age))
        print(f'{name} was registered')
        print()

    def show_people_by_age(self) -> None:
        people: str = self.__app_controller.get_people_ordered_by_age()

        if len(people) > 0:
            print("Registered people list sorted by age")
            for person in people:
                print(f'Name: {person.get_name()} ; Age: {person.get_age()} ; Age Group: {person.get_age_group()}')
        else:
            print("Add person to the list")
            
        print()

    def show_people_by_name(self) -> None:
        people: str = self.__app_controller.get_people_ordered_by_nome()

        if len(people) > 0:
            print("Registered people list sorted by name")
            for person in people:
                print(f'Name: {person.get_name()} ; Age: {person.get_age()} ; Age Group: {person.get_age_group()}')
        else:
            print("Add person to the list")
            
        print()

    def show_help(self) -> None:
        print("Type add_person to add a new person\n" +\
            "Type show_people_by_age to show the list fo people sorted by age\n" +\
            "Type show_people_by_name to show the list of people sorted by name\n" +\
            "Type clear_list to cleat the list of people\n" +\
            "Type exit to exit the programz\n")

    def clear_list(self) -> None:
        self.__app_controller.clear_list()

        print("Registered people list was cleaned")
        print()

    def exit(self) -> None:
        print('Thank you for been here.')
        print()
