#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from config import app, db
from models import User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        import ipdb; ipdb.set_trace()
        # Seed code goes here!
