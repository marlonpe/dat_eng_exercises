import pytest

from src.clickstream_generator import generate_clickstream_event

def test_event_structure():
    event = generate_clickstream_event()
    # test all keys are present
    expected_keys = {'user_id', 'timestamp', 'event_type', 'product_id', 'referrer_url', 'current_url',
                     'location', 'device', 'browser', 'session_duration'}
    assert set(event.keys()) == expected_keys

def test_event_data_types():
    event = generate_clickstream_event()
    # assert data types
    assert isinstance(event['user_id'], str)
    assert isinstance(event['timestamp'], str)
    assert isinstance(event['event_type'], str)
    assert isinstance(event['product_id'], str)
    assert isinstance(event['referrer_url'], str)
    assert isinstance(event['current_url'], str)
    assert isinstance(event['location'], str)
    assert isinstance(event['device'], str)
    assert isinstance(event['browser'], str)
    assert isinstance(event['session_duration'], int)