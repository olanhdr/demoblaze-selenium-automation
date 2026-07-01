from utils.data_generator import DataGenerator

dummy_data = DataGenerator

CHECKOUT_DATA = {
            "name": dummy_data.full_name(),
            "country": dummy_data.country(),
            "city": dummy_data.city(),
            "card_number": dummy_data.card_number(),
            "month": dummy_data.month(),
            "year": dummy_data.year(),
            "expected_message": "Thank you for your purchase!"
        }