from src.model.user import User


class UserService:
    @staticmethod
    def get_user_by_uid(uid):
        user = User.query.filter_by(uid=uid).first()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()