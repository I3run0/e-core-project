import cmd, sys
from app_interface import App_interface

class App_CMD(cmd.Cmd):
    __app_interface: App_interface = App_interface()

    intro = __app_interface.get_cmd_intro()

    prompt = __app_interface.get_cmd_prompt()


    def do_help(self, arg: str) -> None:
        self.__app_interface.show_help()
    
    def do_add_person(self, arg: str) -> None:
        self.__app_interface.add_person()

    def do_show_people_by_age(self, arg: str) -> None:
        self.__app_interface.show_people_by_age()
    
    def do_show_people_by_name(self, arg: str) -> None:
        self.__app_interface.show_people_by_name()
    
    def do_clear_list(self, arg: str) -> None:
        self.__app_interface.clear_list()
        
    def do_exit(self, arg: str) -> None:
        self.__app_interface.exit()
        sys.exit(1)
