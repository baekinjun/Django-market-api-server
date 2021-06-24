from .model import LaboratoryPageDao


class LaboratoryPageService:
    def __init__(self):
        self.laboratory_page_dao = LaboratoryPageDao()

    def lab_title(self, id):
        res = self.laboratory_page_dao.lab_title(id)
        return res

    def lab_data(self, id):
        res = self.laboratory_page_dao.lab_data(id)
        return res
