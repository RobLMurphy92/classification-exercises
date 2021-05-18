import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def prep_iris(df):
    '''
    takes in a df of the iris dataset as it is acquired and returns a cleaned df
    arguements: df: a pandas df with the expected feature names and columns return: 
    clean_df: a dataframe with the cleaning operations performed on it
    '''
    df = df.drop_duplicates()
    df = df.drop(columns = ['species_id'])
    df = df.rename(columns={"species_name": "species"})
    dummy_species_name = pd.get_dummies(df[['species']]) 
    df = pd.concat([df, dummy_species_name], axis=1)
    return df


    def train_validate_test_split(df, seed=123):
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed, stratify=df.survived
    )
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed,
        stratify=train_and_validate.survived,
    )
    return train, validate, test
    