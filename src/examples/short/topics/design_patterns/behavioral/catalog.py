"""
A class that uses different static function depending of a parameter passed in
init. Note the use of a single dictionary instead of multiple conditions
"""

from types import MethodType


class Catalog:
    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param: str) -> None:
        """
        dictionary that will be used to determine which static method is
        to be executed but that will be also used to store possible param
        value
        """
        self._static_method_choices = {
            "param_value_1": self._static_method_1,
            "param_value_2": self._static_method_2,
        }
        assert param in self._static_method_choices
        self.param = param

    @staticmethod
    def _static_method_1() -> str:
        return "executed method 1!"

    @staticmethod
    def _static_method_2() -> str:
        return "executed method 2!"

    def main_method(self) -> str:
        """
        will execute either _static_method_1 or _static_method_2
        depending on self.param value
        """
        return self._static_method_choices[self.param]()


# Alternative implementation for different levels of methods
class CatalogInstance:

    """catalog of multiple methods that are executed depending on an init

    parameter
    """

    def __init__(self, param: str) -> None:
        self.x1 = "x1"
        self.x2 = "x2"
        # simple test to validate param value
        if param in self._instance_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    def _instance_method_1(self) -> str:
        return f"Value {self.x1}"

    def _instance_method_2(self) -> str:
        return f"Value {self.x2}"

    _instance_method_choices = {
        "param_value_1": _instance_method_1,
        "param_value_2": _instance_method_2,
    }

    def main_method(self) -> str:
        """will execute either _instance_method_1 or _instance_method_2

        depending on self.param value
        """
        return self._instance_method_choices[self.param](self)


class CatalogClass:

    """catalog of multiple class methods that are executed depending on an init

    parameter
    """

    x1 = "x1"
    x2 = "x2"

    def __init__(self, param: str) -> None:
        assert param in self._class_method_choices
        self.param = param

    @classmethod
    def _class_method_1(cls) -> str:
        return f"Value {cls.x1}"

    @classmethod
    def _class_method_2(cls) -> str:
        return f"Value {cls.x2}"

    _class_method_choices = {
        "param_value_1": _class_method_1,
        "param_value_2": _class_method_2,
    }

    def main_method(self) -> str:
        """
        will execute either _class_method_1 or _class_method_2
        depending on self.param value
        """
        f = CatalogClass._class_method_choices[self.param]
        m = MethodType(f.__func__, CatalogClass)  # type: ignore
        # pylint: disable=not-callable
        return m()


class CatalogStatic:

    """catalog of multiple static methods that are executed depending on an init

    parameter
    """

    def __init__(self, param: str) -> None:
        # simple test to validate param value
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError(f"Invalid Value for Param: {param}")

    @staticmethod
    def _static_method_1() -> str:
        return "executed method 1!"

    @staticmethod
    def _static_method_2() -> str:
        return "executed method 2!"

    _static_method_choices = {
        "param_value_1": _static_method_1,
        "param_value_2": _static_method_2,
    }

    def main_method(self) -> str:
        """
        will execute either _static_method_1 or _static_method_2
        depending on self.param value
        """
        return self._static_method_choices[self.param]()


def main():
    test = Catalog("param_value_2")
    assert test.main_method() == "executed method 2!"

    test = CatalogInstance("param_value_1")
    assert test.main_method() == "Value x1"

    test = CatalogClass("param_value_2")
    assert test.main_method() == "Value x2"

    test = CatalogStatic("param_value_1")
    assert test.main_method() == "executed method 1!"


if __name__ == "__main__":
    main()
