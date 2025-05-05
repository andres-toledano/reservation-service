from src import db
from src.model.reservation import Reservation
from src.util.reservation_util import ReservationUtil
from src.service.user_service import UserService


class ReservationService:

    @staticmethod
    def create(user_id, classroom_id, start_time, end_time):
        reservation = Reservation(
            user_id=user_id,
            classroom_id=classroom_id,
            start_time=start_time,
            end_time=end_time
        )
        db.session.add(reservation)
        db.session.commit()
        return reservation

    @staticmethod
    def create_if_available(user_id, classroom_id, start_time, end_time):
        if ReservationUtil.is_time_slot_available(classroom_id, start_time, end_time):
            return ReservationService.create(user_id, classroom_id, start_time, end_time)
        return None

    @staticmethod
    def get_available_slots(classroom_id, date):
        return ReservationUtil.get_available_slots(classroom_id, date)

    @staticmethod
    def get_reservation_by_user_id(user_id):
        return Reservation.query.filter_by(user_id=user_id).all()

    @staticmethod
    def delete_reservation(reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            db.session.delete(reservation)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_reservations():
        return Reservation.query.all()
