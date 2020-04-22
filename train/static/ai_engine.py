import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import random
import warnings


def aimodel(uid, settings, featureSettings):
    # dependencies: psycopg2, scikitlearn, pandas, numpy, sqlalchemy, xgboost
    print(uid)
    print(settings)
    print(featureSettings)
