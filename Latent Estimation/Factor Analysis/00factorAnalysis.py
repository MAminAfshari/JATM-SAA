"""File 00factorAnalysis.py

Preliminary analysis of the indicators using factor analysis.

:author: Michel Bierlaire, EPFL
:date: Mon Sep  9 16:04:57 2019

"""
import pandas as pd
import numpy as np

# The following package can be installed using
# pip install factor_analyzer
# See https://github.com/EducationalTestingService/factor_analyzer
from factor_analyzer import FactorAnalyzer

# We first extract the columns containing the indicators

variables = ["TaxiMoreComfortableThanAuto",
"NeedCarAtWork",
"PreferNotToDrive",
"EcoSysFriendly",
"PreferToUsePT",
"TaxiWaitingTime",
"PreferWalking",
"ParkingNotAvailable",
"PreferToRenACar",
"PreferTaxi",
"UsedCruise",
"PreferElectricAuto",
"PreferHybridAuto",
"TrustAutoDrive",
"UsingSiriORAlexa",
"TrustCruise",
"UseGoogleMas",
"UsingTimeINAuto",
"FacingTraffic",
"SharedApp",
"BeingOnTimeMatters",
"ATUsingCamera",
"TalkingToOperator",
"LandOperatorControl",
"ATWorkWithTaxi",
"MobileIsImportant",
"RecreationRatherWork",
"WorryAboutPrivacy",
"WaitingForNewBrandTech",
"EconomicalSatisfied",
"TechnologyMatter",
"PreferAuto",
"SharingTripIsOk",
"StressfulWhilePassanger"]
#indicators = pd.read_csv('AirportHotel_ID.txt',sep='\t',usecols=variables)
indicators = pd.read_csv('W-DATA2.txt',sep='\t',usecols=variables)
#indicators = pd.read_csv('REC_TRIP_DATA.txt',sep='\t',usecols=variables)


# Negative values are missing values. 
indicators[indicators <= 0] = np.nan
indicators = indicators.dropna(axis = 0, how = 'any') 

# We perform the factor analysis
fa = FactorAnalyzer(rotation='varimax',n_factors=3)
fa.fit(indicators)

# We obtain the factor loadings and label them
labeledResults = pd.DataFrame(fa.loadings_)
labeledResults.index = variables

# We keep only loadings that are 0.4 or higher, in absolute value. 
filter = (labeledResults <= 0.4) & (labeledResults >= -0.4)
labeledResults[filter] = ''
print(labeledResults)
print(fa.corr_)
