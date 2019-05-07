# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import glob
import cv2
import os

def load_house_attributes(inputPath):
	# initialize the list of column names in the CSV file and then
	# load it using Pandas
	cols = ["bedrooms", "bathrooms", "area", "zipcode", "price"]
	df = pd.read_csv(inputPath, sep=" ", header=None, names=cols)
	#print(df.head())
	# determine (1) the unique zip codes and (2) the number of data
	# points with each zip code
	zipcodes = df['zipcode'].value_counts().keys().tolist()
	counts = df['zipcode'].value_counts().tolist()
	
	#loop over each of the unique zip codes and their corresponding count
	for(zipcode, count) in zip(zipcodes, counts):
	# the zip code counts for our housing dataset is *extremely*
		# unbalanced (some only having 1 or 2 houses per zip code)
		# so let's sanitize our data by removing any houses with less
		# than 25 houses per zip code
		if count < 25:
			idxs = df[df["zipcode"] == zipcode].index
			df.drop(idxs, inplace=True)
 
	# return the data frame
	return df	
