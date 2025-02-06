from faker import Faker
import uuid
from dataset_limit import DATASET_LIMIT

def generate_username():
    fake = Faker()
    username = fake.first_name() + fake.last_name() + str(uuid.uuid4())
    print(username)

    return username

def generate_dataset():
    with open('./dataset.txt', 'w') as f:
        for _ in range(DATASET_LIMIT):
            f.write(generate_username() + '\n')

generate_dataset()