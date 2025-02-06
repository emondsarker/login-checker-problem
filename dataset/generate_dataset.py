from faker import Faker
import uuid
import argparse
from dataset_limit import DATASET_LIMIT

def generate_username():
    fake = Faker()
    username = fake.first_name() + fake.last_name() + str(uuid.uuid4())

    return username

def generate_dataset(sorted_flag):
    dataset_filename = './dataset.txt'
    usernames = []
    for _ in range(DATASET_LIMIT):
        usernames.append(generate_username())
        if _ % 1000 == 0:
            print(f"Generated {_} usernames.")
    
    if sorted_flag:
        usernames.sort()
        dataset_filename = './sorted_dataset.txt'
    
    with open(dataset_filename, 'w') as f:
        for username in usernames:
            f.write(username + '\n')
    
    print(f"Generated {DATASET_LIMIT} usernames.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a dataset of usernames.')
    parser.add_argument('--sorted', action='store_true', help='Generate sorted usernames')
    args = parser.parse_args()
    
    generate_dataset(args.sorted)