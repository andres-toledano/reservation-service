from flask import Blueprint, request, jsonify
from src.service.reservation_service import ReservationService
from datetime import datetime
from src.service.user_service import UserService

reservation_bp = Blueprint('reservation', __name__, url_prefix='/api/reservation')


@reservation_bp.route('/', methods=['POST'])
def create_reservation():
    data = request.get_json()
    try:
        user_id = data['user_id']
        classroom_id = data['classroom_id']
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])

        reservation = ReservationService.create_if_available(user_id, classroom_id, start_time, end_time)

        if reservation:
            return jsonify({
                'id': reservation.id,
                'user_id': reservation.user_id,
                'classroom_id': reservation.classroom_id,
                'start_time': reservation.start_time.isoformat(),
                'end_time': reservation.end_time.isoformat()
            }), 201
        else:
            return jsonify({'message': 'Time slot not available'}), 409

    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@reservation_bp.route('/available', methods=['GET'])
def get_available_slots():
    classroom_id = request.args.get('classroom_id')
    date_str = request.args.get('date')

    if not classroom_id or not date_str:
        return jsonify({'error': 'Missing classroom_id or date'}), 400

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        slots = ReservationService.get_available_slots(classroom_id, date)
        return jsonify({'available_slots': slots}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
