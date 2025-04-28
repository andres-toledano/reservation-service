from src.model.classroom import Classroom


class ClassroomService:
    @staticmethod
    def get_classroom_by_id(classroom_id):
        classroom = Classroom.query.filter_by(id=classroom_id).first()
        return classroom

    @staticmethod
    def get_all_classrooms():
        return Classroom.query.all()
