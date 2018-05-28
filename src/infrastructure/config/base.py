# coding: utf-8
import os


class Config:

    POCKET_CONSUMER_KEY = ""
    POCKET_ACCESS_TOKEN = ""

    MONGO_URI = "mongo:27017"
    MONGO_DB_NAME = "toshokan"


class EnvironmentConfig(Config):

    POCKET_CONSUMER_KEY = os.getenv("TOSHOKAN_POCKET_CONSUMER_KEY")
    POCKET_ACCESS_TOKEN = os.getenv("TOSHOKAN_POCKET_ACCESS_TOKEN")
