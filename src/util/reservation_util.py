from datetime import datetime
from src.model.reservation import Reservation


class ReservationUtil:

    @staticmethod
    def is_time_slot_available(classroom_id, start_time, end_time):
        overlapping = Reservation.query.filter(
            Reservation.classroom_id == classroom_id,
            Reservation.start_time < end_time,
            Reservation.end_time > start_time
        ).first()
        return overlapping is None

    @staticmethod
    def get_available_slots(classroom_id, date, opening_hour=9, closing_hour=21):
        reservations = Reservation.query.filter(
            Reservation.classroom_id == classroom_id,
            Reservation.start_time >= datetime.combine(date, datetime.min.time()),
            Reservation.end_time <= datetime.combine(date, datetime.max.time())
        ).order_by(Reservation.start_time).all()

        slots = []
        current = datetime.combine(date, datetime.min.time()).replace(hour=opening_hour, minute=0)
        end = datetime.combine(date, datetime.min.time()).replace(hour=closing_hour, minute=0)

        for reservation in reservations:
            if current < reservation.start_time:
                slots.append({
                    'start': current.isoformat(),
                    'end': reservation.start_time.isoformat()
                })
            current = max(current, reservation.end_time)

        if current < end:
            slots.append({
                'start': current.isoformat(),
                'end': end.isoformat()
            })

        return slots
