from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
              name=data['name'],
              description=data['description']
            )
        )
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type":"SUV", "year": 2023,
        "car_make": car_make_instances[0],
        "fuel_type": "gasoline", "transmission": "automatic"},
        {"name": "Qashqai", "type":"SUV",    "year": 2023,
        "car_make": car_make_instances[0],
        "fuel_type": "gasoline", "transmission": "automatic"},
        {"name": "XTRAIL", "type":"SUV",     "year": 2023,
        "car_make": car_make_instances[0],
        "fuel_type": "gasoline", "transmission": "automatic"},
        {"name": "A-Class", "type":"SUV",    "year": 2023,
        "car_make": car_make_instances[1],
        "fuel_type": "electric", "transmission": "automatic"},
        {"name": "C-Class", "type":"SUV",    "year": 2023,
        "car_make": car_make_instances[1],
        "fuel_type": "electric", "transmission": "automatic"},
        {"name": "E-Class", "type":"SUV",    "year": 2023,
        "car_make": car_make_instances[1],
        "fuel_type": "electric", "transmission": "automatic"},
        {"name": "A4", "type":"SUV",         "year": 2023,
        "car_make": car_make_instances[2],
        "fuel_type": "diesel", "transmission": "manual"},
        {"name": "A5", "type":"SUV",         "year": 2023,
        "car_make": car_make_instances[2],
        "fuel_type": "diesel", "transmission": "manual"},
        {"name": "A6", "type":"SUV",         "year": 2023,
        "car_make": car_make_instances[2],
        "fuel_type": "diesel", "transmission": "manual"},
        {"name": "Sorrento", "type":"SUV",   "year": 2023,
        "car_make": car_make_instances[3],
        "fuel_type": "hybrid", "transmission": "automatic"},
        {"name": "Carnival", "type":"SUV",   "year": 2023,
        "car_make": car_make_instances[3],
        "fuel_type": "hybrid", "transmission": "automatic"},
        {"name": "Cerato", "type":"Sedan",   "year": 2023,
        "car_make": car_make_instances[3],
        "fuel_type": "hybrid", "transmission": "automatic"},
        {"name": "Corolla", "type":"Sedan",  "year": 2023,
        "car_make": car_make_instances[4],
        "fuel_type": "plug_in_hybrid", "transmission": "automatic"},
        {"name": "Camry", "type":"Sedan",    "year": 2023,
        "car_make": car_make_instances[4],
        "fuel_type": "plug_in_hybrid", "transmission": "automatic"},
        {"name": "Kluger", "type":"SUV",     "year": 2023,
        "car_make": car_make_instances[4],
        "fuel_type": "plug_in_hybrid", "transmission": "automatic"},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            fuel_type=data['fuel_type'],
            transmission=data['transmission']
        )
