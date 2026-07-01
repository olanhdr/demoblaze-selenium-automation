from utils.data_generator import DataGenerator

dummy_data = DataGenerator

REGISTRATION_DATA = {
    "valid": {
    "username" : dummy_data.username(),
    "password" : dummy_data.password(),
    "expected_message" : "Sign up successful."
},
    "invalid": {
    "username" : "redgery25",
    "password" : dummy_data.password(),
    "expected_message" : "This user already exist."
    }
}