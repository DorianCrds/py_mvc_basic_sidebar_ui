from src.models.example_model import ExampleModel


class MainController:
    def __init__(self):

        self.example_model = ExampleModel()

    def get_all_elements(self):
        return self.example_model.get_all_elements()

    def get_element_by_id(self):
        return self.example_model.get_element_by_id()
