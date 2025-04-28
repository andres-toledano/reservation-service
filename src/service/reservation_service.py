from src import db
from src.model.reservation import Reservation
from src.util.reservation_util import ReservationUtil


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
        if ReservationUtils.is_time_slot_available(classroom_id, start_time, end_time):
            return ReservationService.create(user_id, classroom_id, start_time, end_time)
        return None

    @staticmethod
    def get_available_slots(classroom_id, date):
        return ReservationUtils.get_available_slots(classroom_id, date)
