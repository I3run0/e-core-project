class Person():
    __name: str
    __age: int
    __age_group: str

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age
        self.__computing_age_group()

    def __computing_age_group(self) -> bool:
        if self.__age < 0:
            self.__age_group = 'Non defined'
            return False

        if 0 <= self.__age and self.__age < 12:
            self.__age_group = 'Kid'

        elif 12 <= self.__age and self.__age < 20:
            self.__age_group = 'Teenager'

        elif 20 <= self.__age and self.__age < 65:
            self.__age_group = 'Adult'
        
        elif 65 <= self.__age:
            self.__age_group = 'Elderly'

        return True

    def get_age(self) -> int:
        return self.__age 

    def get_name(self) -> str:
        return self.__name

    def get_age_group(self) -> str:
        return self.__age_group
