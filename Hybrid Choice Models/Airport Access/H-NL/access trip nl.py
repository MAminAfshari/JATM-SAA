from telnetlib import TM
import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.logging as blog
import biogeme.distributions as dist
from biogeme.expressions import Beta, bioDraws, PanelLikelihoodTrajectory, MonteCarlo, log, bioNormalCdf, Elem, RandomVariable, Integrate
import sys
import biogeme.biogeme as bio
from biogeme import models
import biogeme.exceptions as excep
import biogeme.distributions as dist
import biogeme.results as res
from biogeme.expressions import (
    Beta,
    RandomVariable,
    exp,
    log,
    Integrate,
)
from biogeme.nests import OneNestForNestedLogit, NestsForNestedLogit


# Read the data
df = pd.read_csv('AirportHotel_ID.txt' , sep='\t')
database = db.Database('Example', df)

# The following statement allows you to use the names of the variable
# as Python variable.
globals().update(database.variables)

HHM1       = (HHM == 1 or HHM == 2 or HHM == 3)
HHM2       = (HHM == 4 or HHM == 5)
IGN	       = (GN - 1)
IAGE1      = (AGE == 1)
IAGE2      = (AGE == 2)
IAGE3      = (AGE == 3)
IAGE4      = (AGE == 4)
IAGE5      = (AGE == 5)
IAGE6      = (AGE == 6)
IEDU1      = (EDU == 1)
IEDU2      = (EDU == 2)
IEDU3      = (EDU == 3)
IWORK1     = (IWORK == 1)
IWORK2     = (IWORK == 2)
IWORK3     = (IWORK == 3)
IWORK4     = (IWORK == 4)
IWORK5     = (IWORK == 5)
IWORK6     = (IWORK == 6)
IOPW1      = (IOPW == 1 or IOPW == 2)
IOPW2      = (IOPW == 3 or IOPW == 4)
IRTEH1     = (IRTEH - 1)
IWTEH1     = (IWTEH - 1)
ITT1       = (ITT == 1)
ITT2       = (ITT == 2)
ITT3       = (ITT == 3)
HINC1      = (HHINC  == 1)
HINC2      = (HHINC  == 2)
HINC3      = (HHINC  == 3)
HINC4      = (HHINC  == 4)
HINC5      = (HHINC  == 5)
HINC6      = (HHINC  == 6)
HINC7      = (HHINC  == 7)
IPHU1	   = (PHU == 1)
IPHU2	   = (PHU == 2)
IPHU3	   = (PHU == 3)
IPHU4	   = (PHU == 4)
MM_AU      = (MAIN_MODE == 1)
MM_PT      = (MAIN_MODE == 2)
MM_RH      = (MAIN_MODE == 3)
MM_BK      = (MAIN_MODE == 4)
MM_WA      = (MAIN_MODE == 5)
SM_AU      = (SEC_MODE == 1)
SM_PT      = (SEC_MODE == 2)
SM_RH      = (SEC_MODE == 3)
SM_BK      = (SEC_MODE == 4)
SM_WA      = (SEC_MODE == 5)
TTSTATION1 = (TTSTA ==1)
TTSTATION2 = (TTSTA ==2)
RH1        = (TAXI  == 1)
RH2        = (TAXI  == 2)
RH3        = (TAXI  == 3)
RH4        = (TAXI  == 4)
CAR_OW0    = (HHCOW == 0)
CAR_OW1    = (HHCOW == 1)
CAR_OW2    = (HHCOW == 2)
IMEHTR     = (MEHTR == 0 or MEHTR == 1 or MEHTR == 2 or MEHTR == 3)
IEMTR      = (EMTR  == 0 or EMTR  == 1 or EMTR  == 2 or EMTR  == 3)
RHUSE1     = (RHUSE1 == 1)
RHUSE2     = (RHUSE2 == 2)
RHUSE3     = (RHUSE3 == 3)
RHUSE4     = (RHUSE4 == 4)
RHUSE5     = (RHUSE5 == 5)
RHUSE6     = (RHUSE6 == 6)

PREPT1      = (PreferToUsePT == 4 or PreferToUsePT == 5)
PREPT2      = (PreferToUsePT == 1 or PreferToUsePT == 2)
PREWALK1    = (PreferWalking== 4 or PreferWalking == 5)
PREWALK2    = (PreferWalking== 1 or PreferWalking == 2)
STRPASS1    = (StressfulWhilePassanger == 4 or StressfulWhilePassanger == 5)
STRPASS2    = (StressfulWhilePassanger == 1 or StressfulWhilePassanger == 2)
PRENTCAR1   = (PreferToRenACar == 4 or PreferToRenACar ==5)    
PRENTCAR2   = (PreferToRenACar == 1 or PreferToRenACar ==2)  
PRETAXI1    = (PreferTaxi == 4 or PreferTaxi == 5)
PRETAXI2    = (PreferTaxi == 1 or PreferTaxi == 2)
USEDCRU1    = (UsedCruise == 4 or UsedCruise == 5)
USEDCRU2    = (UsedCruise == 1 or UsedCruise == 2)
PRELECT1    = (PreferElectricAuto == 4 or PreferElectricAuto == 5)
PRELECT2    = (PreferElectricAuto == 1 or PreferElectricAuto == 2)
PREHYB1     = (PreferHybridAuto == 4 or PreferHybridAuto == 5)
PREHYB2     = (PreferHybridAuto == 1 or PreferHybridAuto == 2)
TRUSTCRU1   = (TrustCruise == 4 or TrustCruise == 5)
TRUSTCRU2   = (TrustCruise == 1 or TrustCruise == 2)
USEDMAP1    = (UseGoogleMas == 4 or UseGoogleMas == 5)
USEDMAP2    = (UseGoogleMas == 1 or UseGoogleMas == 2)
USETIME1    = (UsingTimeINAuto == 4 or UsingTimeINAuto == 5)
USETIME2    = (UsingTimeINAuto == 1 or UsingTimeINAuto == 2)
UNITAPP1    = (SharedApp == 4 or SharedApp == 5)
UNITAPP2    = (SharedApp == 1 or SharedApp == 2)
CAMERA1     = (ATUsingCamera == 4 or ATUsingCamera == 5)
CAMERA2     = (ATUsingCamera == 1 or ATUsingCamera == 2)
ATINTEGTAXI1= (ATWorkWithTaxi == 4 or ATWorkWithTaxi == 5)
ATINTEGTAXI2= (ATWorkWithTaxi == 1 or ATWorkWithTaxi == 2)
MOBIMPORT1  = (MobileIsImportant == 4 or MobileIsImportant == 5)
MOBIMPORT2  = (MobileIsImportant == 1 or MobileIsImportant == 2)
RECIMPORT1  = (RecreationRatherWork == 4 or RecreationRatherWork == 5)
RECIMPORT2  = (RecreationRatherWork == 1 or RecreationRatherWork == 2)
PRIVACY1    = (WorryAboutPrivacy == 4 or WorryAboutPrivacy == 5)
PRIVACY2    = (WorryAboutPrivacy == 1 or WorryAboutPrivacy == 2)
ECOSATIS1   = (EconomicalSatisfied == 4 or EconomicalSatisfied == 5)
ECOSATIS2   = (EconomicalSatisfied == 1 or EconomicalSatisfied == 2)

TMCA1 = (TaxiMoreComfortableThanAuto  == 4 or TaxiMoreComfortableThanAuto  == 5)
TMCA2 = (TaxiMoreComfortableThanAuto  == 1 or TaxiMoreComfortableThanAuto  == 2)
NCAW1 = (NeedCarAtWork == 4 or NeedCarAtWork == 5)
NCAW2 = (NeedCarAtWork == 1 or NeedCarAtWork == 2)
PNTD1 = (PreferNotToDrive == 4 or PreferNotToDrive == 5)
PNTD2 = (PreferNotToDrive == 1 or PreferNotToDrive == 2)
ECOF1 = (EcoSysFriendly == 4 or EcoSysFriendly == 5)
ECOF2 = (EcoSysFriendly == 1 or EcoSysFriendly == 2)
TWT1 = (TaxiWaitingTime == 4 or TaxiWaitingTime == 5)
TWT2 = (TaxiWaitingTime == 1 or TaxiWaitingTime == 2)
PAUTO1 =(PreferAuto == 4 or PreferAuto == 5)
PAUTO2 =(PreferAuto == 1 or PreferAuto == 2)
PNA1 = (ParkingNotAvailable == 4 or ParkingNotAvailable == 5)
PNA2 = (ParkingNotAvailable == 1 or ParkingNotAvailable == 2)
TAUTOD1 = (TrustAutoDrive == 4 or TrustAutoDrive == 5)
TAUTOD2 = (TrustAutoDrive == 1 or TrustAutoDrive == 2)
UAORS1 = (UsingSiriORAlexa == 4 or UsingSiriORAlexa == 5)
UAORS2 = (UsingSiriORAlexa == 1 or UsingSiriORAlexa == 2)
FTRAFFIC1 = (FacingTraffic == 4 or FacingTraffic == 5)
FTRAFFIC2 = (FacingTraffic == 1 or FacingTraffic == 2)
BOTM1 = (BeingOnTimeMatters == 4 or BeingOnTimeMatters == 5)
BOTM2 = (BeingOnTimeMatters == 1 or BeingOnTimeMatters == 2)
TTOPERA1 = (TalkingToOperator == 4 or TalkingToOperator == 5)
TTOPERA2 = (TalkingToOperator == 1 or TalkingToOperator == 2)
LOC1 = (LandOperatorControl == 4 or LandOperatorControl == 5)
LOC2 = (LandOperatorControl == 1 or LandOperatorControl == 2)
TECHMA1 = (TechnologyMatter == 4 or TechnologyMatter == 5)
TECHMA2 = (TechnologyMatter == 1 or TechnologyMatter == 2)
WFNBTECH1 = (WaitingForNewBrandTech == 4 or WaitingForNewBrandTech == 5)
WFNBTECH2 = (WaitingForNewBrandTech == 1 or WaitingForNewBrandTech == 2)
SHAREDM1 = (SharingTripIsOk == 4 or SharingTripIsOk == 5)
SHAREDM2 = (SharingTripIsOk == 1 or SharingTripIsOk == 2)
MU       = Beta('MU', 1, 1, 10, 0)

logger = blog.get_screen_logger(level=blog.INFO)
logger.info('Example m01_latent_variable.py')

# Parameters to be estimated

ASC_AU            = Beta('01 Constant Auto',               0, None, None, 0)
ASC_RH            = Beta('02 Constant Ride-Hailing',       0, None, None, 1)
ASC_AT            = Beta('03 Constant Air Flying Taxi',    0, None, None, 0)#
ASC_PT            = Beta('04 Constant Public Transport',   0, None, None, 0)
B_TT              = Beta('*Car Travel Time',                  0, None, None, 0)
B_COST            = Beta('*Car Cost',                          0, None, None, 0)
B_AU_TT           = Beta('*Auto Travel Time',              0, None, None, 0)
B_AU_CO           = Beta('*Auto Cost',                     0, None, None, 0)
B_AU_WT           = Beta('*Auto Wait Time',                0, None, None, 0)
B_PT_TT           = Beta('*Public Transport Travel Time',  0, None, None, 0)
B_PT_CO           = Beta('*Public Transport Cost',         0, None, None, 1)#
B_PT_WT           = Beta('*Public Transport Wait Time',    0, None, None, 0)
B_AT_TT           = Beta('*Air Taxi Flying Travel Time',   0, None, None, 0)
B_AT_CO           = Beta('*Air Taxi Flying Cost',          0, None, None, 0)
B_AT_WT           = Beta('*Air Taxi Wait Time',            0, None, None, 0)
B_RH_TT           = Beta('*Ride-Hailing Travel Time',      0, None, None, 0)#
B_RH_CO           = Beta('*Ride-Hailing Cost',             0, None, None, 0)
B_RH_WT           = Beta('*Ride-Hailing Wait Time',        0, None, None, 0)

B_MM_AU_AU           = Beta('Main Mode Auto-AU',                 0, None, None, 0)
B_MM_PT_AU           = Beta('Main Mode Public Transport-AU',     0, None, None, 0)
B_MM_RH_AU           = Beta('Main Mode Ride Hailing-AU',         0, None, None, 0)
B_MM_BK_AU           = Beta('Main Mode Bike-AU',                 0, None, None, 0)
B_MM_WA_AU           = Beta('Main Mode Walk-AU',                 0, None, None, 0)
B_SM_AU_AU           = Beta('Alternate Mode Auto-AU',            0, None, None, 0)
B_SM_PT_AU           = Beta('Alternate Mode Public Transport-AU',0, None, None, 0)
B_SM_RH_AU           = Beta('Alternate Mode Ride Hailing-AU',    0, None, None, 0)
B_SM_BK_AU           = Beta('Alternate Mode Bike-AU',            0, None, None, 0)
B_SM_WA_AU           = Beta('Alternate Mode Walk-AU',            0, None, None, 0)
B_HHM1_AU            = Beta('Household Size <= 3-AU',            0, None, None, 0)
B_HHM2_AU            = Beta('Household Size >  3-AU',            0, None, None, 0)
B_IGN_AU             = Beta('Gender-AU',                         0, None, None, 0)
B_IEDU1_AU           = Beta('Education Level 1-AU',              0, None, None, 0)
B_IEDU2_AU           = Beta('Education Level 2-AU',              0, None, None, 0)
B_IEDU3_AU           = Beta('Education Level 3-AU',              0, None, None, 0)
B_IAGE1_AU           = Beta('Age < 18-AU',                       0, None, None, 0)
B_IAGE2_AU           = Beta('Age 18 - 24-AU',                    0, None, None, 0)
B_IAGE3_AU           = Beta('Age 25 - 34-AU',                    0, None, None, 0)
B_IAGE4_AU           = Beta('Age 35 - 44-AU',                    0, None, None, 0)
B_IAGE5_AU           = Beta('Age 45 - 54-AU',                    0, None, None, 0)
B_IAGE6_AU           = Beta('Age 55 - 64-AU',                    0, None, None, 0)
B_IWORK1_AU          = Beta('Occupation Owner-AU',               0, None, None, 0)
B_IWORK2_AU          = Beta('Occupation Employee Private-AU',    0, None, None, 0)
B_IWORK3_AU          = Beta('Occupation Employee Public-AU',     0, None, None, 0)
B_IWORK4_AU          = Beta('Occupation Student-AU',             0, None, None, 0)
B_IWORK5_AU          = Beta('Occupation Retired-AU',             0, None, None, 0)
B_IWORK6_AU          = Beta('Occupation Unofficial-AU',          0, None, None, 0)
B_IOPW1_AU           = Beta('B_IOPW1-AU',                        0, None, None, 0)
B_IOPW2_AU           = Beta('B_IOPW2-AU',                        0, None, None, 0)
B_IRTEH1_AU          = Beta('Residence in Tehran-AU',            0, None, None, 0)
B_IWTEH1_AU          = Beta('Workplace in Tehran-AU',            0, None, None, 0)
B_ITT1_AU            = Beta('Typical Commute < 30 min-AU',       0, None, None, 0)
B_ITT2_AU            = Beta('Typical Commute 30 - 60 min-AU',    0, None, None, 0)
B_ITT3_AU            = Beta('Typical Commute 60 - 90 min-AU',    0, None, None, 0)
B_HINC1_AU           = Beta('Household Income < 3.5 Mt-AU',      0, None, None, 0)
B_HINC2_AU           = Beta('Household Income 3.5 - 6 Mt-AU',    0, None, None, 0)
B_HINC3_AU           = Beta('Household Income 6 - 9 Mt-AU',      0, None, None, 0)
B_HINC4_AU           = Beta('Household Income 9 - 14 Mt-AU',     0, None, None, 0)
B_HINC5_AU           = Beta('Household Income 14 - 20 Mt-AU',    0, None, None, 0)
B_HINC6_AU           = Beta('Household Income 20 - 30 Mt-AU',    0, None, None, 0)
B_IPHU1_AU           = Beta('B_IPHU1-AU',                        0, None, None, 0)
B_IPHU2_AU           = Beta('B_IPHU2-AU',                        0, None, None, 0)
B_IPHU3_AU           = Beta('B_IPHU3-AU',                        0, None, None, 0)
B_TTSTATION1_AU      = Beta('B_TT TO STATION1-AU',               0, None, None, 0)
B_TTSTATION2_AU      = Beta('B_TT TO STATION2-AU',               0, None, None, 0)
B_RH1_AU             = Beta('Ride Hailing Use > Once / Week-AU', 0, None, None, 0)
B_RH2_AU             = Beta('Ride Hailing Use = Once / Week-AU', 0, None, None, 0)
B_RH3_AU             = Beta('Ride Hailing Use = Once / Month-AU',0, None, None, 0)
B_RH4_AU             = Beta('Ride Hailing Use < Once / Month-AU',0, None, None, 0)
B_CAR_OW0_AU         = Beta('Car Ownership 0-AU',                0, None, None, 0)
B_CAR_OW1_AU         = Beta('Car Ownership 1-AU',                0, None, None, 0)
B_CAR_OW2_AU         = Beta('Car Ownership 2-AU',                0, None, None, 0)
B_IMEHTR_AU          = Beta('THR Flight Freq-AU',                0, None, None, 0)
B_IEMTR_AU           = Beta('IKA Flight Freq-AU',                0, None, None, 0)

B_TMCA1_AU       = Beta('Taxi More Comfortable Than Auto/AGREE-AU' ,0, None, None, 1)
B_TMCA2_AU       = Beta('Taxi More Comfortable Than Auto/DAGREE-AU',0, None, None, 0)
B_NCAW1_AU       = Beta('Need Car At Work/AGREE-AU'                ,0, None, None, 0)
B_NCAW2_AU       = Beta('Need Car At Work/DAGREE-AU'               ,0, None, None, 0)
B_PNTD1_AU       = Beta('Prefer Not To Drive/AGREE-AU'             ,0, None, None, 0)
B_PNTD2_AU       = Beta('Prefer Not To Drive/DAGREE-AU'            ,0, None, None, 1)
B_ECOF1_AU       = Beta('Ecosystem Friendly/AGREE-AU'              ,0, None, None, 0)
B_ECOF2_AU       = Beta('Ecosystem Friendly/DAGREE-AU'             ,0, None, None, 0)
B_TWT1_AU        = Beta('Taxi Waiting Time/AGREE-AU'               ,0, None, None, 0)
B_TWT2_AU        = Beta('Taxi Waiting Time/DAGREE-AU'              ,0, None, None, 0)
B_PAUTO1_AU      = Beta('Prefer Auto/AGREE-AU'                     ,0, None, None, 0)
B_PAUTO2_AU      = Beta('Prefer Auto/DAGREE-AU'                    ,0, None, None, 0)
B_PNA1_AU        = Beta('Parking Is Not Available/AGREE-AU'        ,0, None, None, 0)
B_PNA2_AU        = Beta('Parking Is Not Available/DAGREE-AU'       ,0, None, None, 0)
B_TAUTOD1_AU     = Beta('Trust Automatic Drive/AGREE-AU'           ,0, None, None, 0)
B_TAUTOD2_AU     = Beta('Trust Automatic Drive/DAGREE-AU'          ,0, None, None, 0)
B_UAORS1_AU      = Beta('Using Siri OR Alexa/AGREE-AU'             ,0, None, None, 0)
B_UAORS2_AU      = Beta('Using Siri OR Alexa/DAGREE-AU'            ,0, None, None, 0)
B_FTRAFFIC1_AU   = Beta('FacingTraffic/AGREE-AU'                   ,0, None, None, 0)
B_FTRAFFIC2_AU   = Beta('FacingTraffic/DAGREE-AU'                  ,0, None, None, 0)
B_BOTM1_AU       = Beta('Being On Time Matters/AGREE-AU'           ,0, None, None, 0)
B_BOTM2_AU       = Beta('Being On Time Matters/DAGREE-AU'          ,0, None, None, 0)
B_TTOPERA1_AU    = Beta('Talking To Operator/AGREE-AU'             ,0, None, None, 0)
B_TTOPERA2_AU    = Beta('Talking To Operator/DAGREE-AU'            ,0, None, None, 0)
B_LOC1_AU        = Beta('Land Operator Control/AGREE-AU'           ,0, None, None, 0)
B_LOC2_AU        = Beta('Land Operator Control/DAGREE-AU'          ,0, None, None, 0)
B_TECHMA1_AU     = Beta('Technology Matter/AGREE-AU'               ,0, None, None, 0)
B_TECHMA2_AU     = Beta('Technology Matter/DAGREE-AU'              ,0, None, None, 0)
B_WFNBTECH1_AU   = Beta('Waiting For New Brand Tech/AGREE-AU'      ,0, None, None, 0)
B_WFNBTECH2_AU   = Beta('Waiting For New Brand Tech/DAGREE-AU'     ,0, None, None, 0)
B_SHAREDM1_AU    = Beta('Sharing Trip Is Ok/AGREE-AU'              ,0, None, None, 0)
B_SHAREDM2_AU    = Beta('Sharing Trip Is Ok/DAGREE-AU'             ,0, None, None, 0)

B_PREPT1_AU      = Beta('Prefer To Use PT/AGREE-AU'                ,0, None, None, 0)
B_PREPT2_AU      = Beta('Prefer To Use PT/DAGREE-AU'               ,0, None, None, 0)
B_PREWALK1_AU    = Beta('Prefer Walking/AGREE-AU'                  ,0, None, None, 0)
B_PREWALK2_AU    = Beta('Prefer Walking/DAGREE-AU'                 ,0, None, None, 0)
B_STRPASS1_AU    = Beta('Stressful As a Passanger/AGREE-AU'        ,0, None, None, 0)
B_STRPASS2_AU    = Beta('Stressful As a Passanger/DAGREE-AU'       ,0, None, None, 0)
B_PRENTCAR1_AU   = Beta('Prefer To Rent a Car/AGREE-AU'            ,0, None, None, 0)    
B_PRENTCAR2_AU   = Beta('Prefer To Rent a Car/DAGREE-AU'           ,0, None, None, 0)  
B_PRETAXI1_AU    = Beta('Prefer Taxi/AGREE-AU'                     ,0, None, None, 1)
B_PRETAXI2_AU    = Beta('Prefer Taxi/DAGREE-AU'                    ,0, None, None, 0)
B_USEDCRU1_AU    = Beta('Used Cruise/AGREE-AU'                     ,0, None, None, 0)
B_USEDCRU2_AU    = Beta('Used Cruise/DAGREE-AU'                    ,0, None, None, 0)
B_PRELECT1_AU    = Beta('Prefer Electric Car/AGREE-AU'             ,0, None, None, 0)
B_PRELECT2_AU    = Beta('Prefer Electric Car/DAGREE-AU'            ,0, None, None, 0)
B_PREHYB1_AU     = Beta('Prefer Hybrid Auto/AGREE-AU'              ,0, None, None, 0)
B_PREHYB2_AU     = Beta('Prefer Hybrid Auto/DAGREE-AU'             ,0, None, None, 0)
B_TRUSTCRU1_AU   = Beta('Trust Cruise/AGREE-AU'                    ,0, None, None, 0)
B_TRUSTCRU2_AU   = Beta('Trust Cruise/DAGREE-AU'                   ,0, None, None, 0)
B_USEDMAP1_AU    = Beta('Use Google Map/AGREE-AU'                  ,0, None, None, 0)
B_USEDMAP2_AU    = Beta('Use Google Map/DAGREE-AU'                 ,0, None, None, 0)
B_USETIME1_AU    = Beta('Using Time in Auto/AGREE-AU'              ,0, None, None, 0)
B_USETIME2_AU    = Beta('Using Time in Auto/DAGREE-AU'             ,0, None, None, 0)
B_UNITAPP1_AU    = Beta('AT and RH Use Unit APP/AGREE-AU'          ,0, None, None, 0)
B_UNITAPP2_AU    = Beta('AT and RH Use Unit APP/DAGREE-AU'         ,0, None, None, 0)
B_CAMERA1_AU     = Beta('AT Using Camera/AGREE-AU'                 ,0, None, None, 0)
B_CAMERA2_AU     = Beta('AT Using Camera/DAGREE-AU'                ,0, None, None, 0)
B_ATINTEGTAXI1_AU= Beta('AT Work With Taxi/AGREE-AU'               ,0, None, None, 0)
B_ATINTEGTAXI2_AU= Beta('AT Work With Taxi/DAGREE-AU'              ,0, None, None, 0)
B_MOBIMPORT1_AU  = Beta('Mobile Is Important/AGREE-AU'             ,0, None, None, 0)
B_MOBIMPORT2_AU  = Beta('Mobile Is Important/DAGREE-AU'            ,0, None, None, 1)
B_RECIMPORT1_AU  = Beta('Recreation Rather Work/AGREE-AU'          ,0, None, None, 0)
B_RECIMPORT2_AU  = Beta('Recreation Rather Work/DAGREE-AU'         ,0, None, None, 0)
B_PRIVACY1_AU    = Beta('Worry About Privacy/AGREE-AU'             ,0, None, None, 0)
B_PRIVACY2_AU    = Beta('Worry About Privacy/DAGREE-AU'            ,0, None, None, 0)
B_ECOSATIS1_AU   = Beta('Economical Satisfied/AGREE-AU'            ,0, None, None, 0)
B_ECOSATIS2_AU   = Beta('Economical Satisfied/DAGREE-AU'           ,0, None, None, 0)

#RH
#RH
#RH

B_MM_AU_RH           = Beta('Main Mode Auto-RH',                 0, None, None, 0)
B_MM_PT_RH           = Beta('Main Mode Public Transport-RH',     0, None, None, 0)
B_MM_RH_RH           = Beta('Main Mode Ride Hailing-RH',         0, None, None, 0)
B_MM_BK_RH           = Beta('Main Mode Bike-RH',                 0, None, None, 0)
B_MM_WA_RH           = Beta('Main Mode Walk-RH',                 0, None, None, 0)
B_SM_AU_RH           = Beta('Alternate Mode Auto-RH',            0, None, None, 0)
B_SM_PT_RH           = Beta('Alternate Mode Public Transport-RH',0, None, None, 0)
B_SM_RH_RH           = Beta('Alternate Mode Ride Hailing-RH',    0, None, None, 0)
B_SM_BK_RH           = Beta('Alternate Mode Bike-RH',            0, None, None, 0)
B_SM_WA_RH           = Beta('Alternate Mode Walk-RH',            0, None, None, 0)
B_HHM1_RH            = Beta('Household Size <= 3-RH',            0, None, None, 0)
B_HHM2_RH            = Beta('Household Size >  3-RH',            0, None, None, 0)
B_IGN_RH             = Beta('Gender-RH',                         0, None, None, 0)
B_IEDU1_RH           = Beta('Education Level 1-RH',              0, None, None, 0)
B_IEDU2_RH           = Beta('Education Level 2-RH',              0, None, None, 0)
B_IEDU3_RH           = Beta('Education Level 3-RH',              0, None, None, 0)
B_IAGE1_RH           = Beta('Age < 18-RH',                       0, None, None, 0)
B_IAGE2_RH           = Beta('Age 18 - 24-RH',                    0, None, None, 0)
B_IAGE3_RH           = Beta('Age 25 - 34-RH',                    0, None, None, 0)
B_IAGE4_RH           = Beta('Age 35 - 44-RH',                    0, None, None, 0)
B_IAGE5_RH           = Beta('Age 45 - 54-RH',                    0, None, None, 0)
B_IAGE6_RH           = Beta('Age 55 - 64-RH',                    0, None, None, 0)
B_IWORK1_RH          = Beta('Occupation Owner-RH',               0, None, None, 0)
B_IWORK2_RH          = Beta('Occupation Employee Private-RH',    0, None, None, 0)
B_IWORK3_RH          = Beta('Occupation Employee Public-RH',     0, None, None, 0)
B_IWORK4_RH          = Beta('Occupation Student-RH',             0, None, None, 0)
B_IWORK5_RH          = Beta('Occupation Retired-RH',             0, None, None, 0)
B_IWORK6_RH          = Beta('Occupation Unofficial-RH',          0, None, None, 0)
B_IOPW1_RH           = Beta('B_IOPW1-RH',                        0, None, None, 0)
B_IOPW2_RH           = Beta('B_IOPW2-RH',                        0, None, None, 0)
B_IRTEH1_RH          = Beta('Residence in Tehran-RH',            0, None, None, 0)
B_IWTEH1_RH          = Beta('Workplace in Tehran-RH',            0, None, None, 0)
B_ITT1_RH            = Beta('Typical Commute < 30 min-RH',       0, None, None, 0)
B_ITT2_RH            = Beta('Typical Commute 30 - 60 min-RH',    0, None, None, 0)
B_ITT3_RH            = Beta('Typical Commute 60 - 90 min-RH',    0, None, None, 0)
B_HINC1_RH           = Beta('Household Income < 3.5 Mt-RH',      0, None, None, 0)
B_HINC2_RH           = Beta('Household Income 3.5 - 6 Mt-RH',    0, None, None, 0)
B_HINC3_RH           = Beta('Household Income 6 - 9 Mt-RH',      0, None, None, 0)
B_HINC4_RH           = Beta('Household Income 9 - 14 Mt-RH',     0, None, None, 0)
B_HINC5_RH           = Beta('Household Income 14 - 20 Mt-RH',    0, None, None, 0)
B_HINC6_RH           = Beta('Household Income 20 - 30 Mt-RH',    0, None, None, 1)
B_IPHU1_RH           = Beta('B_IPHU1-RH',                        0, None, None, 0)
B_IPHU2_RH           = Beta('B_IPHU2-RH',                        0, None, None, 0)
B_IPHU3_RH           = Beta('B_IPHU3-RH',                        0, None, None, 0)
B_TTSTATION1_RH      = Beta('B_TT TO STATION1-RH',               0, None, None, 0)
B_TTSTATION2_RH      = Beta('B_TT TO STATION2-RH',               0, None, None, 0)
B_RH1_RH             = Beta('Ride Hailing Use > Once / Week-RH', 0, None, None, 0)
B_RH2_RH             = Beta('Ride Hailing Use = Once / Week-RH', 0, None, None, 0)
B_RH3_RH             = Beta('Ride Hailing Use = Once / Month-RH',0, None, None, 0)
B_RH4_RH             = Beta('Ride Hailing Use < Once / Month-RH',0, None, None, 0)
B_CAR_OW0_RH         = Beta('Car Ownership 0-RH',                0, None, None, 0)
B_CAR_OW1_RH         = Beta('Car Ownership 1-RH',                0, None, None, 0)
B_CAR_OW2_RH         = Beta('Car Ownership 2-RH',                0, None, None, 0)
B_IMEHTR_RH          = Beta('THR Flight Freq-RH',                0, None, None, 0)
B_IEMTR_RH           = Beta('IKA Flight Freq-RH',                0, None, None, 0)

B_TMCA1_RH       = Beta('Taxi More Comfortable Than Auto/AGREE-RH' ,0, None, None, 0)
B_TMCA2_RH       = Beta('Taxi More Comfortable Than Auto/DAGREE-RH',0, None, None, 0)
B_NCAW1_RH       = Beta('Need Car At Work/AGREE-RH'                ,0, None, None, 0)
B_NCAW2_RH       = Beta('Need Car At Work/DAGREE-RH'               ,0, None, None, 0)
B_PNTD1_RH       = Beta('Prefer Not To Drive/AGREE-RH'             ,0, None, None, 1)
B_PNTD2_RH       = Beta('Prefer Not To Drive/DAGREE-RH'            ,0, None, None, 0)
B_ECOF1_RH       = Beta('Ecosystem Friendly/AGREE-RH'              ,0, None, None, 0)
B_ECOF2_RH       = Beta('Ecosystem Friendly/DAGREE-RH'             ,0, None, None, 0)
B_TWT1_RH        = Beta('Taxi Waiting Time/AGREE-RH'               ,0, None, None, 0)
B_TWT2_RH        = Beta('Taxi Waiting Time/DAGREE-RH'              ,0, None, None, 0)
B_PAUTO1_RH      = Beta('Prefer Auto/AGREE-RH'                     ,0, None, None, 0)
B_PAUTO2_RH      = Beta('Prefer Auto/DAGREE-RH'                    ,0, None, None, 0)
B_PNA1_RH        = Beta('Parking Is Not Available/AGREE-RH'        ,0, None, None, 0)
B_PNA2_RH        = Beta('Parking Is Not Available/DAGREE-RH'       ,0, None, None, 0)
B_TAUTOD1_RH     = Beta('Trust Automatic Drive/AGREE-RH'           ,0, None, None, 0)
B_TAUTOD2_RH     = Beta('Trust Automatic Drive/DAGREE-RH'          ,0, None, None, 0)
B_UAORS1_RH      = Beta('Using Siri OR Alexa/AGREE-RH'             ,0, None, None, 0)
B_UAORS2_RH      = Beta('Using Siri OR Alexa/DAGREE-RH'            ,0, None, None, 0)
B_FTRAFFIC1_RH   = Beta('FacingTraffic/AGREE-RH'                   ,0, None, None, 0)
B_FTRAFFIC2_RH   = Beta('FacingTraffic/DAGREE-RH'                  ,0, None, None, 0)
B_BOTM1_RH       = Beta('Being On Time Matters/AGREE-RH'           ,0, None, None, 0)
B_BOTM2_RH       = Beta('Being On Time Matters/DAGREE-RH'          ,0, None, None, 0)
B_TTOPERA1_RH    = Beta('Talking To Operator/AGREE-RH'             ,0, None, None, 0)
B_TTOPERA2_RH    = Beta('Talking To Operator/DAGREE-RH'            ,0, None, None, 0)
B_LOC1_RH        = Beta('Land Operator Control/AGREE-RH'           ,0, None, None, 0)
B_LOC2_RH        = Beta('Land Operator Control/DAGREE-RH'          ,0, None, None, 0)
B_TECHMA1_RH     = Beta('Technology Matter/AGREE-RH'               ,0, None, None, 0)
B_TECHMA2_RH     = Beta('Technology Matter/DAGREE-RH'              ,0, None, None, 0)
B_WFNBTECH1_RH   = Beta('Waiting For New Brand Tech/AGREE-RH'      ,0, None, None, 0)
B_WFNBTECH2_RH   = Beta('Waiting For New Brand Tech/DAGREE-RH'     ,0, None, None, 0)
B_SHAREDM1_RH    = Beta('Sharing Trip Is Ok/AGREE-RH'              ,0, None, None, 0)
B_SHAREDM2_RH    = Beta('Sharing Trip Is Ok/DAGREE-RH'             ,0, None, None, 0)

B_PREPT1_RH      = Beta('Prefer To Use PT/AGREE-RH'                ,0, None, None, 0)
B_PREPT2_RH      = Beta('Prefer To Use PT/DAGREE-RH'               ,0, None, None, 0)
B_PREWALK1_RH    = Beta('Prefer Walking/AGREE-RH'                  ,0, None, None, 0)
B_PREWALK2_RH    = Beta('Prefer Walking/DAGREE-RH'                 ,0, None, None, 0)
B_STRPASS1_RH    = Beta('Stressful As a Passanger/AGREE-RH'        ,0, None, None, 0)
B_STRPASS2_RH    = Beta('Stressful As a Passanger/DAGREE-RH'       ,0, None, None, 0)
B_PRENTCAR1_RH   = Beta('Prefer To Rent a Car/AGREE-RH'            ,0, None, None, 0)    
B_PRENTCAR2_RH   = Beta('Prefer To Rent a Car/DAGREE-RH'           ,0, None, None, 0)  
B_PRETAXI1_RH    = Beta('Prefer Taxi/AGREE-RH'                     ,0, None, None, 0)
B_PRETAXI2_RH    = Beta('Prefer Taxi/DAGREE-RH'                    ,0, None, None, 0)
B_USEDCRU1_RH    = Beta('Used Cruise/AGREE-RH'                     ,0, None, None, 1)
B_USEDCRU2_RH    = Beta('Used Cruise/DAGREE-RH'                    ,0, None, None, 0)
B_PRELECT1_RH    = Beta('Prefer Electric Car/AGREE-RH'             ,0, None, None, 0)
B_PRELECT2_RH    = Beta('Prefer Electric Car/DAGREE-RH'            ,0, None, None, 0)
B_PREHYB1_RH     = Beta('Prefer Hybrid Auto/AGREE-RH'              ,0, None, None, 0)
B_PREHYB2_RH     = Beta('Prefer Hybrid Auto/DAGREE-RH'             ,0, None, None, 0)
B_TRUSTCRU1_RH   = Beta('Trust Cruise/AGREE-RH'                    ,0, None, None, 0)
B_TRUSTCRU2_RH   = Beta('Trust Cruise/DAGREE-RH'                   ,0, None, None, 0)
B_USEDMAP1_RH    = Beta('Use Google Map/AGREE-RH'                  ,0, None, None, 0)
B_USEDMAP2_RH    = Beta('Use Google Map/DAGREE-RH'                 ,0, None, None, 0)
B_USETIME1_RH    = Beta('Using Time in Auto/AGREE-RH'              ,0, None, None, 0)
B_USETIME2_RH    = Beta('Using Time in Auto/DAGREE-RH'             ,0, None, None, 0)
B_UNITAPP1_RH    = Beta('AT and RH Use Unit APP/AGREE-RH'          ,0, None, None, 0)
B_UNITAPP2_RH    = Beta('AT and RH Use Unit APP/DAGREE-RH'         ,0, None, None, 0)
B_CAMERA1_RH     = Beta('AT Using Camera/AGREE-RH'                 ,0, None, None, 0)
B_CAMERA2_RH     = Beta('AT Using Camera/DAGREE-RH'                ,0, None, None, 0)
B_ATINTEGTAXI1_RH= Beta('AT Work With Taxi/AGREE-RH'               ,0, None, None, 0)
B_ATINTEGTAXI2_RH= Beta('AT Work With Taxi/DAGREE-RH'              ,0, None, None, 0)
B_MOBIMPORT1_RH  = Beta('Mobile Is Important/AGREE-RH'             ,0, None, None, 0)
B_MOBIMPORT2_RH  = Beta('Mobile Is Important/DAGREE-RH'            ,0, None, None, 0)
B_RECIMPORT1_RH  = Beta('Recreation Rather Work/AGREE-RH'          ,0, None, None, 0)
B_RECIMPORT2_RH  = Beta('Recreation Rather Work/DAGREE-RH'         ,0, None, None, 0)
B_PRIVACY1_RH    = Beta('Worry About Privacy/AGREE-RH'             ,0, None, None, 0)
B_PRIVACY2_RH    = Beta('Worry About Privacy/DAGREE-RH'            ,0, None, None, 0)
B_ECOSATIS1_RH   = Beta('Economical Satisfied/AGREE-RH'            ,0, None, None, 0)
B_ECOSATIS2_RH   = Beta('Economical Satisfied/DAGREE-RH'           ,0, None, None, 0)

#AT

B_MM_AU_AT           = Beta('Main Mode Auto-AT',                 0, None, None, 0)
B_MM_PT_AT           = Beta('Main Mode Public Transport-AT',     0, None, None, 0)
B_MM_RH_AT           = Beta('Main Mode Ride Hailing-AT',         0, None, None, 0)
B_MM_BK_AT           = Beta('Main Mode Bike-AT',                 0, None, None, 0)
B_MM_WA_AT           = Beta('Main Mode Walk-AT',                 0, None, None, 0)
B_SM_AU_AT           = Beta('Alternate Mode Auto-AT',            0, None, None, 0)
B_SM_PT_AT           = Beta('Alternate Mode Public Transport-AT',0, None, None, 0)
B_SM_RH_AT           = Beta('Alternate Mode Ride Hailing-AT',    0, None, None, 0)
B_SM_BK_AT           = Beta('Alternate Mode Bike-AT',            0, None, None, 0)
B_SM_WA_AT           = Beta('Alternate Mode Walk-AT',            0, None, None, 0)
B_HHM1_AT            = Beta('Household Size <= 3-AT',            0, None, None, 0)
B_HHM2_AT            = Beta('Household Size >  3-AT',            0, None, None, 0)
B_IGN_AT             = Beta('Gender-AT',                         0, None, None, 0)
B_IEDU1_AT           = Beta('Education Level 1-AT',              0, None, None, 0)
B_IEDU2_AT           = Beta('Education Level 2-AT',              0, None, None, 0)
B_IEDU3_AT           = Beta('Education Level 3-AT',              0, None, None, 0)
B_IAGE1_AT           = Beta('Age < 18-AT',                       0, None, None, 0)
B_IAGE2_AT           = Beta('Age 18 - 24-AT',                    0, None, None, 1)
B_IAGE3_AT           = Beta('Age 25 - 34-AT',                    0, None, None, 0)
B_IAGE4_AT           = Beta('Age 35 - 44-AT',                    0, None, None, 0)
B_IAGE5_AT           = Beta('Age 45 - 54-AT',                    0, None, None, 0)
B_IAGE6_AT           = Beta('Age 55 - 64-AT',                    0, None, None, 0)
B_IWORK1_AT          = Beta('Occupation Owner-AT',               0, None, None, 0)
B_IWORK2_AT          = Beta('Occupation Employee Private-AT',    0, None, None, 0)
B_IWORK3_AT          = Beta('Occupation Employee Public-AT',     0, None, None, 0)
B_IWORK4_AT          = Beta('Occupation Student-AT',             0, None, None, 0)
B_IWORK5_AT          = Beta('Occupation Retired-AT',             0, None, None, 0)
B_IWORK6_AT          = Beta('Occupation Unofficial-AT',          0, None, None, 0)
B_IOPW1_AT           = Beta('B_IOPW1-AT',                        0, None, None, 0)
B_IOPW2_AT           = Beta('B_IOPW2-AT',                        0, None, None, 0)
B_IRTEH1_AT          = Beta('Residence in Tehran-AT',            0, None, None, 0)
B_IWTEH1_AT          = Beta('Workplace in Tehran-AT',            0, None, None, 0)
B_ITT1_AT            = Beta('Typical Commute < 30 min-AT',       0, None, None, 0)
B_ITT2_AT            = Beta('Typical Commute 30 - 60 min-AT',    0, None, None, 0)
B_ITT3_AT            = Beta('Typical Commute 60 - 90 min-AT',    0, None, None, 0)
B_HINC1_AT           = Beta('Household Income < 3.5 Mt-AT',      0, None, None, 0)
B_HINC2_AT           = Beta('Household Income 3.5 - 6 Mt-AT',    0, None, None, 0)
B_HINC3_AT           = Beta('Household Income 6 - 9 Mt-AT',      0, None, None, 0)
B_HINC4_AT           = Beta('Household Income 9 - 14 Mt-AT',     0, None, None, 0)
B_HINC5_AT           = Beta('Household Income 14 - 20 Mt-AT',    0, None, None, 0)
B_HINC6_AT           = Beta('Household Income 20 - 30 Mt-AT',    0, None, None, 0)
B_IPHU1_AT           = Beta('B_IPHU1-AT',                        0, None, None, 0)
B_IPHU2_AT           = Beta('B_IPHU2-AT',                        0, None, None, 0)
B_IPHU3_AT           = Beta('B_IPHU3-AT',                        0, None, None, 0)
B_TTSTATION1_AT      = Beta('B_TT TO STATION1-AT',               0, None, None, 0)
B_TTSTATION2_AT      = Beta('B_TT TO STATION2-AT',               0, None, None, 0)
B_RH1_AT             = Beta('Ride Hailing Use more Once Week AT', 0, None, None, 0)
B_RH2_AT             = Beta('Ride Hailing Use eq Once Week AT', 0, None, None, 0)
B_RH3_AT             = Beta('Ride Hailing Use eq Once Month AT',0, None, None, 0)
B_RH4_AT             = Beta('Ride Hailing Use less Once Month AT',0, None, None, 0)
B_CAR_OW0_AT         = Beta('Car Ownership 0-AT',                0, None, None, 0)
B_CAR_OW1_AT         = Beta('Car Ownership 1-AT',                0, None, None, 0)
B_CAR_OW2_AT         = Beta('Car Ownership 2-AT',                0, None, None, 0)
B_IMEHTR_AT          = Beta('THR Flight Freq-AT',                0, None, None, 0)
B_IEMTR_AT           = Beta('IKA Flight Freq-AT',                0, None, None, 0)

B_TMCA1_AT       = Beta('Taxi More Comfortable Than Auto/AGREE-AT' ,0, None, None, 1)
B_TMCA2_AT       = Beta('Taxi More Comfortable Than Auto/DAGREE-AT',0, None, None, 0)
B_NCAW1_AT       = Beta('Need Car At Work/AGREE-AT'                ,0, None, None, 0)
B_NCAW2_AT       = Beta('Need Car At Work/DAGREE-AT'               ,0, None, None, 0)
B_PNTD_AT        = Beta('Prefer Not To Drive/AGREE-AT'             ,0, None, None, 0)
B_PNTD2_AT       = Beta('Prefer Not To Drive/DAGREE-AT'            ,0, None, None, 0)
B_ECOF1_AT       = Beta('Ecosystem Friendly/AGREE-AT'              ,0, None, None, 0)
B_ECOF2_AT       = Beta('Ecosystem Friendly/DAGREE-AT'             ,0, None, None, 0)
B_TWT1_AT        = Beta('Taxi Waiting Time/AGREE-AT'               ,0, None, None, 0)
B_TWT2_AT        = Beta('Taxi Waiting Time/DAGREE-AT'              ,0, None, None, 0)
B_PAUTO1_AT      = Beta('Prefer Auto/AGREE-AT'                     ,0, None, None, 0)
B_PAUTO2_AT      = Beta('Prefer Auto/DAGREE-AT'                    ,0, None, None, 0)
B_PNA1_AT        = Beta('Parking Is Not Available/AGREE-AT'        ,0, None, None, 0)
B_PNA2_AT        = Beta('Parking Is Not Available/DAGREE-AT'       ,0, None, None, 0)
B_TAUTOD1_AT     = Beta('Trust Automatic Drive/AGREE-AT'           ,0, None, None, 0)
B_TAUTOD2_AT     = Beta('Trust Automatic Drive/DAGREE-AT'          ,0, None, None, 0)
B_UAORS1_AT      = Beta('Using Siri OR Alexa/AGREE-AT'             ,0, None, None, 0)
B_UAORS2_AT      = Beta('Using Siri OR Alexa/DAGREE-AT'            ,0, None, None, 0)
B_FTRAFFIC1_AT   = Beta('FacingTraffic/AGREE-AT'                   ,0, None, None, 0)
B_FTRAFFIC2_AT   = Beta('FacingTraffic/DAGREE-AT'                  ,0, None, None, 0)
B_BOTM1_AT       = Beta('Being On Time Matters/AGREE-AT'           ,0, None, None, 0)
B_BOTM2_AT       = Beta('Being On Time Matters/DAGREE-AT'          ,0, None, None, 0)
B_TTOPERA1_AT    = Beta('Talking To Operator/AGREE-AT'             ,0, None, None, 0)
B_TTOPERA2_AT    = Beta('Talking To Operator/DAGREE-AT'            ,0, None, None, 0)
B_LOC1_AT        = Beta('Land Operator Control/AGREE-AT'           ,0, None, None, 0)
B_LOC2_AT        = Beta('Land Operator Control/DAGREE-AT'          ,0, None, None, 0)
B_TECHMA1_AT     = Beta('Technology Matter/AGREE-AT'               ,0, None, None, 1)
B_TECHMA2_AT     = Beta('Technology Matter/DAGREE-AT'              ,0, None, None, 0)
B_WFNBTECH1_AT   = Beta('Waiting For New Brand Tech/AGREE-AT'      ,0, None, None, 0)
B_WFNBTECH2_AT   = Beta('Waiting For New Brand Tech/DAGREE-AT'     ,0, None, None, 0)
B_SHAREDM1_AT    = Beta('Sharing Trip Is Ok/AGREE-AT'              ,0, None, None, 0)
B_SHAREDM2_AT    = Beta('Sharing Trip Is Ok/DAGREE-AT'             ,0, None, None, 0)

B_PREPT1_AT      = Beta('Prefer To Use PT/AGREE-AT'                ,0, None, None, 1)
B_PREPT2_AT      = Beta('Prefer To Use PT/DAGREE-AT'               ,0, None, None, 0)
B_PREWALK1_AT    = Beta('Prefer Walking/AGREE-AT'                  ,0, None, None, 0)
B_PREWALK2_AT    = Beta('Prefer Walking/DAGREE-AT'                 ,0, None, None, 0)
B_STRPASS1_AT    = Beta('Stressful As a Passanger/AGREE-AT'        ,0, None, None, 0)
B_STRPASS2_AT    = Beta('Stressful As a Passanger/DAGREE-AT'       ,0, None, None, 0)
B_PRENTCAR1_AT   = Beta('Prefer To Rent a Car/AGREE-AT'            ,0, None, None, 0)    
B_PRENTCAR2_AT   = Beta('Prefer To Rent a Car/DAGREE-AT'           ,0, None, None, 0)  
B_PRETAXI1_AT    = Beta('Prefer Taxi/AGREE-AT'                     ,0, None, None, 0)
B_PRETAXI2_AT    = Beta('Prefer Taxi/DAGREE-AT'                    ,0, None, None, 0)
B_USEDCRU1_AT    = Beta('Used Cruise/AGREE-AT'                     ,0, None, None, 0)
B_USEDCRU2_AT    = Beta('Used Cruise/DAGREE-AT'                    ,0, None, None, 1)
B_PRELECT1_AT    = Beta('Prefer Electric Car/AGREE-AT'             ,0, None, None, 0)
B_PRELECT2_AT    = Beta('Prefer Electric Car/DAGREE-AT'            ,0, None, None, 0)
B_PREHYB1_AT     = Beta('Prefer Hybrid Auto/AGREE-AT'              ,0, None, None, 0)
B_PREHYB2_AT     = Beta('Prefer Hybrid Auto/DAGREE-AT'             ,0, None, None, 0)
B_TRUSTCRU1_AT   = Beta('Trust Cruise/AGREE-AT'                    ,0, None, None, 0)
B_TRUSTCRU2_AT   = Beta('Trust Cruise/DAGREE-AT'                   ,0, None, None, 0)
B_USEDMAP1_AT    = Beta('Use Google Map/AGREE-AT'                  ,0, None, None, 0)
B_USEDMAP2_AT    = Beta('Use Google Map/DAGREE-AT'                 ,0, None, None, 0)
B_USETIME1_AT    = Beta('Using Time in Auto/AGREE-AT'              ,0, None, None, 1)
B_USETIME2_AT    = Beta('Using Time in Auto/DAGREE-AT'             ,0, None, None, 0)
B_UNITAPP1_AT    = Beta('AT and RH Use Unit APP/AGREE-AT'          ,0, None, None, 0)
B_UNITAPP2_AT    = Beta('AT and RH Use Unit APP/DAGREE-AT'         ,0, None, None, 0)
B_CAMERA1_AT     = Beta('AT Using Camera/AGREE-AT'                 ,0, None, None, 0)
B_CAMERA2_AT     = Beta('AT Using Camera/DAGREE-AT'                ,0, None, None, 0)
B_ATINTEGTAXI1_AT= Beta('AT Work With Taxi/AGREE-AT'               ,0, None, None, 0)
B_ATINTEGTAXI2_AT= Beta('AT Work With Taxi/DAGREE-AT'              ,0, None, None, 0)
B_MOBIMPORT1_AT  = Beta('Mobile Is Important/AGREE-AT'             ,0, None, None, 0)
B_MOBIMPORT2_AT  = Beta('Mobile Is Important/DAGREE-AT'            ,0, None, None, 0)
B_RECIMPORT1_AT  = Beta('Recreation Rather Work/AGREE-AT'          ,0, None, None, 0)
B_RECIMPORT2_AT  = Beta('Recreation Rather Work/DAGREE-AT'         ,0, None, None, 0)
B_PRIVACY1_AT    = Beta('Worry About Privacy/AGREE-AT'             ,0, None, None, 0)
B_PRIVACY2_AT    = Beta('Worry About Privacy/DAGREE-AT'            ,0, None, None, 0)
B_ECOSATIS1_AT   = Beta('Economical Satisfied/AGREE-AT'            ,0, None, None, 0)
B_ECOSATIS2_AT   = Beta('Economical Satisfied/DAGREE-AT'           ,0, None, None, 0)

#PT
#PT
#PT

B_MM_AU_PT           = Beta('Main Mode Auto-PT',                 0, None, None, 0)
B_MM_PT_PT           = Beta('Main Mode Public Transport-PT',     0, None, None, 0)
B_MM_RH_PT           = Beta('Main Mode Ride Hailing-PT',         0, None, None, 0)
B_MM_BK_PT           = Beta('Main Mode Bike-PT',                 0, None, None, 0)
B_MM_WA_PT           = Beta('Main Mode Walk-PT',                 0, None, None, 0)
B_SM_AU_PT           = Beta('Alternate Mode Auto-PT',            0, None, None, 0)
B_SM_PT_PT           = Beta('Alternate Mode Public Transport-PT',0, None, None, 0)
B_SM_RH_PT           = Beta('Alternate Mode Ride Hailing-PT',    0, None, None, 0)
B_SM_BK_PT           = Beta('Alternate Mode Bike-PT',            0, None, None, 0)
B_SM_WA_PT           = Beta('Alternate Mode Walk-PT',            0, None, None, 0)
B_HHM1_PT            = Beta('Household Size <= 3-PT',            0, None, None, 0)
B_HHM2_PT            = Beta('Household Size >  3-PT',            0, None, None, 0)
B_IGN_PT             = Beta('Gender-PT',                         0, None, None, 0)
B_IEDU1_PT           = Beta('Education Level 1-PT',              0, None, None, 0)
B_IEDU2_PT           = Beta('Education Level 2-PT',              0, None, None, 0)
B_IEDU3_PT           = Beta('Education Level 3-PT',              0, None, None, 0)
B_IAGE1_PT           = Beta('Age < 18-PT',                       0, None, None, 0)
B_IAGE2_PT           = Beta('Age 18 - 24-PT',                    0, None, None, 0)
B_IAGE3_PT           = Beta('Age 25 - 34-PT',                    0, None, None, 0)
B_IAGE4_PT           = Beta('Age 35 - 44-PT',                    0, None, None, 0)
B_IAGE5_PT           = Beta('Age 45 - 54-PT',                    0, None, None, 0)
B_IAGE6_PT           = Beta('Age 55 - 64-PT',                    0, None, None, 0)
B_IWORK1_PT          = Beta('Occupation Owner-PT',               0, None, None, 0)
B_IWORK2_PT          = Beta('Occupation Employee Private-PT',    0, None, None, 0)
B_IWORK3_PT          = Beta('Occupation Employee Public-PT',     0, None, None, 0)
B_IWORK4_PT          = Beta('Occupation Student-PT',             0, None, None, 0)
B_IWORK5_PT          = Beta('Occupation Retired-PT',             0, None, None, 0)
B_IWORK6_PT          = Beta('Occupation Unofficial-PT',          0, None, None, 0)
B_IOPW1_PT           = Beta('B_IOPW1-PT',                        0, None, None, 0)
B_IOPW2_PT           = Beta('B_IOPW2-PT',                        0, None, None, 0)
B_IRTEH1_PT          = Beta('Residence in Tehran-PT',            0, None, None, 0)
B_IWTEH1_PT          = Beta('Workplace in Tehran-PT',            0, None, None, 0)
B_ITT1_PT            = Beta('Typical Commute < 30 min-PT',       0, None, None, 0)
B_ITT2_PT            = Beta('Typical Commute 30 - 60 min-PT',    0, None, None, 0)
B_ITT3_PT            = Beta('Typical Commute 60 - 90 min-PT',    0, None, None, 0)
B_HINC1_PT           = Beta('Household Income < 3.5 Mt-PT',      0, None, None, 0)
B_HINC2_PT           = Beta('Household Income 3.5 - 6 Mt-PT',    0, None, None, 1)
B_HINC3_PT           = Beta('Household Income 6 - 9 Mt-PT',      0, None, None, 0)
B_HINC4_PT           = Beta('Household Income 9 - 14 Mt-PT',     0, None, None, 0)
B_HINC5_PT           = Beta('Household Income 14 - 20 Mt-PT',    0, None, None, 0)
B_HINC6_PT           = Beta('Household Income 20 - 30 Mt-PT',    0, None, None, 0)
B_IPHU1_PT           = Beta('B_IPHU1-PT',                        0, None, None, 0)
B_IPHU2_PT           = Beta('B_IPHU2-PT',                        0, None, None, 0)
B_IPHU3_PT           = Beta('B_IPHU3-PT',                        0, None, None, 0)
B_TTSTATION1_PT      = Beta('B_TT TO STATION1-PT',               0, None, None, 0)
B_TTSTATION2_PT      = Beta('B_TT TO STATION2-PT',               0, None, None, 0)
B_RH1_PT             = Beta('Ride Hailing Use > Once / Week-PT', 0, None, None, 0)
B_RH2_PT             = Beta('Ride Hailing Use = Once / Week-PT', 0, None, None, 0)
B_RH3_PT             = Beta('Ride Hailing Use = Once / Month-PT',0, None, None, 0)
B_RH4_PT             = Beta('Ride Hailing Use < Once / Month-PT',0, None, None, 0)
B_CAR_OW0_PT         = Beta('Car Ownership 0-PT',                0, None, None, 0)
B_CAR_OW1_PT         = Beta('Car Ownership 1-PT',                0, None, None, 0)
B_CAR_OW2_PT         = Beta('Car Ownership 2-PT',                0, None, None, 0)
B_IMEHTR_PT          = Beta('THR Flight Freq-PT',                0, None, None, 0)
B_IEMTR_PT           = Beta('IKA Flight Freq-PT',                0, None, None, 0)

B_TMCA1_PT       = Beta('Taxi More Comfortable Than Auto/AGREE-PT' ,0, None, None, 0)
B_TMCA2_PT       = Beta('Taxi More Comfortable Than Auto/DAGREE-PT',0, None, None, 0)
B_NCAW1_PT       = Beta('Need Car At Work/AGREE-PT'                ,0, None, None, 0)
B_NCAW2_PT       = Beta('Need Car At Work/DAGREE-PT'               ,0, None, None, 0)
B_PNTD1_PT       = Beta('Prefer Not To Drive/AGREE-PT'             ,0, None, None, 0)
B_PNTD2_PT       = Beta('Prefer Not To Drive/DAGREE-PT'            ,0, None, None, 0)
B_ECOF1_PT       = Beta('Ecosystem Friendly/AGREE-PT'              ,0, None, None, 0)
B_ECOF2_PT       = Beta('Ecosystem Friendly/DAGREE-PT'             ,0, None, None, 0)
B_TWT1_PT        = Beta('Taxi Waiting Time/AGREE-PT'               ,0, None, None, 0)
B_TWT2_PT        = Beta('Taxi Waiting Time/DAGREE-PT'              ,0, None, None, 0)
B_PAUTO1_PT      = Beta('Prefer Auto/AGREE-PT'                     ,0, None, None, 0)
B_PAUTO2_PT      = Beta('Prefer Auto/DAGREE-PT'                    ,0, None, None, 0)
B_PNA1_PT        = Beta('Parking Is Not Available/AGREE-PT'        ,0, None, None, 0)
B_PNA2_PT        = Beta('Parking Is Not Available/DAGREE-PT'       ,0, None, None, 0)
B_TAUTOD1_PT     = Beta('Trust Automatic Drive/AGREE-PT'           ,0, None, None, 0)
B_TAUTOD2_PT     = Beta('Trust Automatic Drive/DAGREE-PT'          ,0, None, None, 0)
B_UAORS1_PT      = Beta('Using Siri OR Alexa/AGREE-PT'             ,0, None, None, 0)
B_UAORS2_PT      = Beta('Using Siri OR Alexa/DAGREE-PT'            ,0, None, None, 0)
B_FTRAFFIC1_PT   = Beta('FacingTraffic/AGREE-PT'                   ,0, None, None, 0)
B_FTRAFFIC2_PT   = Beta('FacingTraffic/DAGREE-PT'                  ,0, None, None, 0)
B_BOTM1_PT       = Beta('Being On Time Matters/AGREE-PT'           ,0, None, None, 0)
B_BOTM2_PT       = Beta('Being On Time Matters/DAGREE-PT'          ,0, None, None, 0)
B_TTOPERA1_PT    = Beta('Talking To Operator/AGREE-PT'             ,0, None, None, 0)
B_TTOPERA2_PT    = Beta('Talking To Operator/DAGREE-PT'            ,0, None, None, 0)
B_LOC1_PT        = Beta('Land Operator Control/AGREE-PT'           ,0, None, None, 0)
B_LOC2_PT        = Beta('Land Operator Control/DAGREE-PT'          ,0, None, None, 0)
B_TECHMA1_PT     = Beta('Technology Matter/AGREE-PT'               ,0, None, None, 0)
B_TECHMA2_PT     = Beta('Technology Matter/DAGREE-PT'              ,0, None, None, 0)
B_WFNBTECH1_PT   = Beta('Waiting For New Brand Tech/AGREE-PT'      ,0, None, None, 0)
B_WFNBTECH2_PT   = Beta('Waiting For New Brand Tech/DAGREE-PT'     ,0, None, None, 0)
B_SHAREDM1_PT    = Beta('Sharing Trip Is Ok/AGREE-PT'              ,0, None, None, 0)
B_SHAREDM2_PT    = Beta('Sharing Trip Is Ok/DAGREE-PT'             ,0, None, None, 0)

B_PREPT1_PT      = Beta('Prefer To Use PT/AGREE-PT'                ,0, None, None, 0)
B_PREPT2_PT      = Beta('Prefer To Use PT/DAGREE-PT'               ,0, None, None, 0)
B_PREWALK1_PT    = Beta('Prefer Walking/AGREE-PT'                  ,0, None, None, 0)
B_PREWALK2_PT    = Beta('Prefer Walking/DAGREE-PT'                 ,0, None, None, 0)
B_STRPASS1_PT    = Beta('Stressful As a Passanger/AGREE-PT'        ,0, None, None, 0)
B_STRPASS2_PT    = Beta('Stressful As a Passanger/DAGREE-PT'       ,0, None, None, 0)
B_PRENTCAR1_PT   = Beta('Prefer To Rent a Car/AGREE-PT'            ,0, None, None, 0)    
B_PRENTCAR2_PT   = Beta('Prefer To Rent a Car/DAGREE-PT'           ,0, None, None, 0)  
B_PRETAXI1_PT    = Beta('Prefer Taxi/AGREE-PT'                     ,0, None, None, 0)
B_PRETAXI2_PT    = Beta('Prefer Taxi/DAGREE-PT'                    ,0, None, None, 0)
B_USEDCRU1_PT    = Beta('Used Cruise/AGREE-PT'                     ,0, None, None, 0)
B_USEDCRU2_PT    = Beta('Used Cruise/DAGREE-PT'                    ,0, None, None, 0)
B_PRELECT1_PT    = Beta('Prefer Electric Car/AGREE-PT'             ,0, None, None, 0)
B_PRELECT2_PT    = Beta('Prefer Electric Car/DAGREE-PT'            ,0, None, None, 0)
B_PREHYB1_PT     = Beta('Prefer Hybrid Auto/AGREE-PT'              ,0, None, None, 0)
B_PREHYB2_PT     = Beta('Prefer Hybrid Auto/DAGREE-PT'             ,0, None, None, 0)
B_TRUSTCRU1_PT   = Beta('Trust Cruise/AGREE-PT'                    ,0, None, None, 0)
B_TRUSTCRU2_PT   = Beta('Trust Cruise/DAGREE-PT'                   ,0, None, None, 0)
B_USEDMAP1_PT    = Beta('Use Google Map/AGREE-PT'                  ,0, None, None, 0)
B_USEDMAP2_PT    = Beta('Use Google Map/DAGREE-PT'                 ,0, None, None, 0)
B_USETIME1_PT    = Beta('Using Time in Auto/AGREE-PT'              ,0, None, None, 0)
B_USETIME2_PT    = Beta('Using Time in Auto/DAGREE-PT'             ,0, None, None, 0)
B_UNITAPP1_PT    = Beta('AT and RH Use Unit APP/AGREE-PT'          ,0, None, None, 0)
B_UNITAPP2_PT    = Beta('AT and RH Use Unit APP/DAGREE-PT'         ,0, None, None, 0)
B_CAMERA1_PT     = Beta('AT Using Camera/AGREE-PT'                 ,0, None, None, 0)
B_CAMERA2_PT     = Beta('AT Using Camera/DAGREE-PT'                ,0, None, None, 0)
B_ATINTEGTAXI1_PT = Beta('AT Work With Taxi/AGREE-PT'              ,0, None, None, 0)
B_ATINTEGTAXI2_PT = Beta('AT Work With Taxi/DAGREE-PT'             ,0, None, None, 0)
B_MOBIMPORT1_PT  = Beta('Mobile Is Important/AGREE-PT'             ,0, None, None, 1)
B_MOBIMPORT2_PT  = Beta('Mobile Is Important/DAGREE-PT'            ,0, None, None, 0)
B_RECIMPORT1_PT  = Beta('Recreation Rather Work/AGREE-PT'          ,0, None, None, 0)
B_RECIMPORT2_PT  = Beta('Recreation Rather Work/DAGREE-PT'         ,0, None, None, 0)
B_PRIVACY1_PT    = Beta('Worry About Privacy/AGREE-PT'             ,0, None, None, 0)
B_PRIVACY2_PT    = Beta('Worry About Privacy/DAGREE-PT'            ,0, None, None, 0)
B_ECOSATIS1_PT   = Beta('Economical Satisfied/AGREE-PT'            ,0, None, None, 0)
B_ECOSATIS2_PT   = Beta('Economical Satisfied/DAGREE-PT'           ,0, None, None, 0)

#################################

B_MM_AU           = Beta('Main Mode Auto',                 0, None, None, 0)
B_MM_PT           = Beta('Main Mode Public Transport',     0, None, None, 0)
B_MM_RH           = Beta('Main Mode Ride Hailing',         0, None, None, 0)
B_MM_BK           = Beta('Main Mode Bike',                 0, None, None, 0)
B_MM_WA           = Beta('Main Mode Walk',                 0, None, None, 0)
B_SM_AU           = Beta('Alternate Mode Auto',            0, None, None, 0)
B_SM_PT           = Beta('Alternate Mode Public Transport',0, None, None, 0)
B_SM_RH           = Beta('Alternate Mode Ride Hailing',    0, None, None, 0)
B_SM_BK           = Beta('Alternate Mode Bike',            0, None, None, 0)
B_SM_WA           = Beta('Alternate Mode Walk',            0, None, None, 0)

B_IAGE1           = Beta('Age < 18',                       0, None, None, 0)
B_IAGE2           = Beta('Age 18 - 24',                    0, None, None, 0)
B_IAGE3           = Beta('Age 25 - 34',                    0, None, None, 0)
B_IAGE4           = Beta('Age 35 - 44',                    0, None, None, 0)
B_IAGE5           = Beta('Age 45 - 54',                    0, None, None, 0)
B_IAGE6           = Beta('Age 55 - 64',                    0, None, None, 0)
B_IWORK1          = Beta('Occupation Owner',               0, None, None, 0)
B_IWORK2          = Beta('Occupation Employee Private',    0, None, None, 0)
B_IWORK3          = Beta('Occupation Employee Public',     0, None, None, 0)
B_IWORK4          = Beta('Occupation Student',             0, None, None, 0)
B_IWORK5          = Beta('Occupation Retired',             0, None, None, 0)
B_IWORK6          = Beta('Occupation Unofficial',          0, None, None, 0)
B_IOPW1           = Beta('B_IOPW1',                        0, None, None, 0)
B_IOPW2           = Beta('B_IOPW2',                        0, None, None, 0)
B_IRTEH1          = Beta('Residence in Tehran',            0, None, None, 0)
B_IWTEH1          = Beta('Workplace in Tehran',            0, None, None, 0)
B_ITT1            = Beta('Typical Commute < 30 min',       0, None, None, 0)
B_ITT2            = Beta('Typical Commute 30 - 60 min',    0, None, None, 0)
B_ITT3            = Beta('Typical Commute 60 - 90 min',    0, None, None, 0)
B_HINC1           = Beta('Household Income < 3.5 Mt',      0, None, None, 0)
B_HINC2           = Beta('Household Income 3.5 - 6 Mt',    0, None, None, 0)
B_HINC3           = Beta('Household Income 6 - 9 Mt',      0, None, None, 0)
B_HINC4           = Beta('Household Income 9 - 14 Mt',     0, None, None, 0)
B_HINC5           = Beta('Household Income 14 - 20 Mt',    0, None, None, 0)
B_HINC6           = Beta('Household Income 20 - 30 Mt',    0, None, None, 0)
B_IPHU1           = Beta('B_IPHU1',                        0, None, None, 0)
B_IPHU2           = Beta('B_IPHU2',                        0, None, None, 0)
B_IPHU3           = Beta('B_IPHU3',                        0, None, None, 0)
B_TTSTATION1      = Beta('B_TT TO STATION1',               0, None, None, 0)
B_TTSTATION2      = Beta('B_TT TO STATION2',               0, None, None, 0)
B_RH1             = Beta('Ride Hailing Use > Once / Week', 0, None, None, 0)
B_RH2             = Beta('Ride Hailing Use = Once / Week', 0, None, None, 0)
B_RH3             = Beta('Ride Hailing Use = Once / Month',0, None, None, 0)
B_RH4             = Beta('Ride Hailing Use < Once / Month',0, None, None, 0)
B_CAR_OW0         = Beta('Car Ownership 0',                0, None, None, 0)
B_CAR_OW1         = Beta('Car Ownership 1',                0, None, None, 0)
B_CAR_OW2         = Beta('Car Ownership 2',                0, None, None, 0)
B_IMEHTR          = Beta('THR Flight Freq',                0, None, None, 0)
B_IEMTR           = Beta('IKA Flight Freq',                0, None, None, 0)

B_TMCA1       = Beta('Taxi More Comfortable Than Auto/AGREE' ,0, None, None, 0)
B_TMCA2       = Beta('Taxi More Comfortable Than Auto/DAGREE',0, None, None, 0)
B_NCAW1       = Beta('Need Car At Work/AGREE'                ,0, None, None, 0)
B_NCAW2       = Beta('Need Car At Work/DAGREE'               ,0, None, None, 0)
B_PNTD1       = Beta('Prefer Not To Drive/AGREE'             ,0, None, None, 0)
B_PNTD2       = Beta('Prefer Not To Drive/DAGREE'            ,0, None, None, 0)
B_ECOF1       = Beta('Ecosystem Friendly/AGREE'              ,0, None, None, 0)
B_ECOF2       = Beta('Ecosystem Friendly/DAGREE'             ,0, None, None, 0)
B_TWT1        = Beta('Taxi Waiting Time/AGREE '              ,0, None, None, 0)
B_TWT2        = Beta('Taxi Waiting Time/DAGREE'              ,0, None, None, 0)
B_PAUTO1      = Beta('Prefer Auto/AGREE'                     ,0, None, None, 0)
B_PAUTO2      = Beta('Prefer Auto/DAGREE'                    ,0, None, None, 0)
B_PNA1        = Beta('Parking Is Not Available/AGREE'        ,0, None, None, 0)
B_PNA2        = Beta('Parking Is Not Available/DAGREE'       ,0, None, None, 0)
B_TAUTOD1     = Beta('Trust Automatic Drive/AGREE'           ,0, None, None, 0)
B_TAUTOD2     = Beta('Trust Automatic Drive/DAGREE'          ,0, None, None, 0)
B_UAORS1      = Beta('Using Siri OR Alexa/AGREE'             ,0, None, None, 0)
B_UAORS2      = Beta('Using Siri OR Alexa/DAGREE'            ,0, None, None, 0)
B_FTRAFFIC1   = Beta('FacingTraffic/AGREE'                   ,0, None, None, 0)
B_FTRAFFIC2   = Beta('FacingTraffic/DAGREE'                  ,0, None, None, 0)
B_BOTM1       = Beta('Being On Time Matters/AGREE'           ,0, None, None, 0)
B_BOTM2       = Beta('Being On Time Matters/DAGREE'          ,0, None, None, 0)
B_TTOPERA1    = Beta('Talking To Operator/AGREE'             ,0, None, None, 0)
B_TTOPERA2    = Beta('Talking To Operator/DAGREE'            ,0, None, None, 0)
B_LOC1        = Beta('Land Operator Control/AGREE'           ,0, None, None, 0)
B_LOC2        = Beta('Land Operator Control/DAGREE'          ,0, None, None, 0)
B_TECHMA1     = Beta('Technology Matter/AGREE'               ,0, None, None, 0)
B_TECHMA2     = Beta('Technology Matter/DAGREE'              ,0, None, None, 0)
B_WFNBTECH1   = Beta('Waiting For New Brand Tech/AGREE'      ,0, None, None, 0)
B_WFNBTECH2   = Beta('Waiting For New Brand Tech/DAGREE'     ,0, None, None, 0)
B_SHAREDM1    = Beta('Sharing Trip Is Ok/AGREE'              ,0, None, None, 0)
B_SHAREDM2    = Beta('Sharing Trip Is Ok/DAGREE'             ,0, None, None, 0)

B_PREPT1      = Beta('Prefer To Use PT/AGREE '               ,0, None, None, 0)
B_PREPT2      = Beta('Prefer To Use PT/DAGREE '              ,0, None, None, 0)
B_PREWALK1    = Beta('Prefer Walking/AGREE'                  ,0, None, None, 0)
B_PREWALK2    = Beta('Prefer Walking/DAGREE'                 ,0, None, None, 0)
B_STRPASS1    = Beta('Stressful As a Passanger/AGREE'        ,0, None, None, 0)
B_STRPASS2    = Beta('Stressful As a Passanger/DAGREE'       ,0, None, None, 0)
B_PRENTCAR1   = Beta('Prefer To Rent a Car/AGREE'            ,0, None, None, 0)    
B_PRENTCAR2   = Beta('Prefer To Rent a Car/DAGREE'           ,0, None, None, 0)  
B_PRETAXI1    = Beta('Prefer Taxi/AGREE'                     ,0, None, None, 0)
B_PRETAXI2    = Beta('Prefer Taxi/DAGREE'                    ,0, None, None, 0)
B_USEDCRU1    = Beta('Used Cruise/AGREE'                     ,0, None, None, 0)
B_USEDCRU2    = Beta('Used Cruise/DAGREE'                    ,0, None, None, 0)
B_PRELECT1    = Beta('Prefer Electric Car/AGREE'             ,0, None, None, 0)
B_PRELECT2    = Beta('Prefer Electric Car/DAGREE'            ,0, None, None, 0)
B_PREHYB1     = Beta('Prefer Hybrid Auto/AGREE'              ,0, None, None, 0)
B_PREHYB2     = Beta('Prefer Hybrid Auto/DAGREE'             ,0, None, None, 0)
B_TRUSTCRU1   = Beta('Trust Cruise/AGREE'                    ,0, None, None, 0)
B_TRUSTCRU2   = Beta('Trust Cruise/DAGREE'                   ,0, None, None, 0)
B_USEDMAP1    = Beta('Use Google Map/AGREE'                  ,0, None, None, 0)
B_USEDMAP2    = Beta('Use Google Map/DAGREE'                 ,0, None, None, 0)
B_USETIME1    = Beta('Using Time in Auto/AGREE'              ,0, None, None, 0)
B_USETIME2    = Beta('Using Time in Auto/DAGREE'             ,0, None, None, 0)
B_UNITAPP1    = Beta('AT and RH Use Unit APP/AGREE'          ,0, None, None, 0)
B_UNITAPP2    = Beta('AT and RH Use Unit APP/DAGREE'         ,0, None, None, 0)
B_CAMERA1     = Beta('AT Using Camera/AGREE'                 ,0, None, None, 0)
B_CAMERA2     = Beta('AT Using Camera/DAGREE'                ,0, None, None, 0)
B_ATINTEGTAXI1= Beta('AT Work With Taxi/AGREE'               ,0, None, None, 0)
B_ATINTEGTAXI2= Beta('AT Work With Taxi/DAGREE'              ,0, None, None, 0)
B_MOBIMPORT1  = Beta('Mobile Is Important/AGREE'             ,0, None, None, 0)
B_MOBIMPORT2  = Beta('Mobile Is Important/DAGREE'            ,0, None, None, 0)
B_RECIMPORT1  = Beta('Recreation Rather Work/AGREE'          ,0, None, None, 0)
B_RECIMPORT2  = Beta('Recreation Rather Work/DAGREE'         ,0, None, None, 0)
B_PRIVACY1    = Beta('Worry About Privacy/AGREE'             ,0, None, None, 0)
B_PRIVACY2    = Beta('Worry About Privacy/DAGREE'            ,0, None, None, 0)
B_ECOSATIS1   = Beta('Economical Satisfied/AGREE'            ,0, None, None, 0)
B_ECOSATIS2   = Beta('Economical Satisfied/DAGREE'           ,0, None, None, 0)

B_RHUSE1          = Beta('RH FOR 01AIRPORT',                 0, None, None, 0)
B_RHUSE2          = Beta('RH FOR 02WORK ALWAYS',             0, None, None, 0)
B_RHUSE3          = Beta('RH FOR 03WORK OCCASIONLY',         0, None, None, 0)
B_RHUSE4          = Beta('RH FOR 04NIGHT OUT',               0, None, None, 0)
B_RHUSE5          = Beta('RH FOR 05REC',                     0, None, None, 0)
B_RHUSE6          = Beta('RH FOR 06OTHERS',                  0, None, None, 0)
B_RHUSE1_AU          = Beta('RH FOR 01AIRPORT-AU',                 0, None, None, 0)
B_RHUSE2_AU          = Beta('RH FOR 02WORK ALWAYS-AU',             0, None, None, 0)
B_RHUSE3_RH          = Beta('RH FOR 03WORK OCCASIONLY-RH',         0, None, None, 0)
B_RHUSE6_RH          = Beta('RH FOR 06OTHERS-RH',                  0, None, None, 0)
B_RHUSE1_PT          = Beta('RH FOR 01AIRPORT-PT',                 0, None, None, 0)
B_RHUSE4_PT          = Beta('RH FOR 04NIGHT OUT-PT',               0, None, None, 0)
B_RHUSE6_PT          = Beta('RH FOR 06OTHERS-PT',                  0, None, None, 0)

MODELNAMEPT = 'Access_PTGuy_latent'
try:
    struct_results_pt = res.bioResults(pickleFile=f'{MODELNAMEPT}.pickle')
except excep.BiogemeError:
    print(
        f'Run first the script {MODELNAMEPT}.py in order to generate the '
        f'file {MODELNAMEPT}.pickle, and move it to the directory saved_results'
    )
    sys.exit()
struct_betas_pt = struct_results_pt.getBetaValues()

MODELNAMESAFE = 'Access_SAFEGUY_latent'
try:
    struct_results_safe = res.bioResults(pickleFile=f'{MODELNAMESAFE}.pickle')
except excep.BiogemeError:
    print(
        f'Run first the script {MODELNAMESAFE}.py in order to generate the '
        f'file {MODELNAMESAFE}.pickle, and move it to the directory saved_results'
    )
    sys.exit()
struct_betas_safe = struct_results_safe.getBetaValues()

MODELNAMETECH = 'Access_TechGuy_latent'
try:
    struct_results_tech = res.bioResults(pickleFile=f'{MODELNAMETECH}.pickle')
except excep.BiogemeError:
    print(
        f'Run first the script {MODELNAMETECH}.py in order to generate the '
        f'file {MODELNAMETECH}.pickle, and move it to the directory saved_results'
    )
    sys.exit()
struct_betas_tech = struct_results_tech.getBetaValues()

PTGUY_coef_intercept = struct_betas_pt['PTGUY_coef_intercept']
PTGUY_coef_IAGE5 = struct_betas_pt['PTGUY_coef_Age 45 - 54'] 
PTGUY_coef_IWORK4 = struct_betas_pt['PTGUY_coef_Occupation Student']
PTGUY_coef_IWORK5 = struct_betas_pt['PTGUY_coef_Occupation Retired'] 
PTGUY_coef_IRTEH1 = struct_betas_pt['PTGUY_coef_IRTEH1'] 
PTGUY_coef_HINC2 = struct_betas_pt['PTGUY_coef_Household Income 3.5 - 6'] 
PTGUY_coef_HINC3 = struct_betas_pt['PTGUY_coef_Household Income 6 - 9'] 
PTGUY_coef_HINC6 = struct_betas_pt['PTGUY_coef_Household Income 20 - 30'] 
PTGUY_coef_IPHU3 = struct_betas_pt['PTGUY_coef_IPHU3'] 
PTGUY_coef_RH2 = struct_betas_pt['PTGUY_coef_Ride Hailing Use = Once Week-RH'] 
PTGUY_coef_RH3 = struct_betas_pt['PTGUY_coef_Ride Hailing Use = Once Month-RH'] 
PTGUY_coef_RH4 = struct_betas_pt['PTGUY_coef_Ride Hailing Use < Once Month-RH'] 
PTGUY_coef_CAR_OW2 = struct_betas_pt['PTGUY_coef_CAR_OW2'] 

SAFEGUY_coef_intercept  = struct_betas_safe['SAFEGUY_coef_intercept'] 
SAFEGUY_coef_IGN = struct_betas_safe['SAFEGUY_coef_IGN']  
SAFEGUY_coef_IEDU3 = struct_betas_safe['SAFEGUY_coef_IEDU3'] 
SAFEGUY_coef_IWORK3 = struct_betas_safe['SAFEGUY_coef_Occupation Employee Public'] 
SAFEGUY_coef_IWORK6 = struct_betas_safe['SAFEGUY_coef_Occupation Unofficial'] 
SAFEGUY_coef_IRTEH1 = struct_betas_safe['SAFEGUY_coef_IRTEH1'] 
SAFEGUY_coef_IWTEH1 = struct_betas_safe['SAFEGUY_coef_IWTEH1'] 
SAFEGUY_coef_HINC2 = struct_betas_safe['SAFEGUY_coef_Household Income 3.5 - 6']
SAFEGUY_coef_HINC5 = struct_betas_safe['SAFEGUY_coef_Household Income 14 - 20']  
SAFEGUY_coef_IPHU1 = struct_betas_safe['SAFEGUY_coef_IPHU1'] 
SAFEGUY_coef_IPHU3 = struct_betas_safe['SAFEGUY_coef_IPHU3'] 
SAFEGUY_coef_RH2 = struct_betas_safe['SAFEGUY_coef_Ride Hailing Use = Once Week-RH'] 
SAFEGUY_coef_RH3 = struct_betas_safe['SAFEGUY_coef_Ride Hailing Use = Once Month-RH'] 
SAFEGUY_coef_CAR_OW0 = struct_betas_safe['SAFEGUY_coef_CAR_OW0']
SAFEGUY_coef_CAR_OW2 = struct_betas_safe['SAFEGUY_coef_CAR_OW2'] 


TECHGUY_coef_intercept = struct_betas_tech['TECHGUY_coef_intercept'] 
TECHGUY_coef_IWORK2 = struct_betas_tech['TECHGUY_coef_Occupation Employee Private'] 
TECHGUY_coef_IWORK3 = struct_betas_tech['TECHGUY_coef_Occupation Employee Public'] 
TECHGUY_coef_IWORK6 = struct_betas_tech['TECHGUY_coef_Occupation Unofficial'] 
TECHGUY_coef_IRTEH1 = struct_betas_tech['TECHGUY_coef_IRTEH1'] 
TECHGUY_coef_HINC3 = struct_betas_tech['TECHGUY_coef_Household Income 6 - 9'] 
TECHGUY_coef_HINC5 = struct_betas_tech['TECHGUY_coef_Household Income 14 - 20'] 
TECHGUY_coef_HINC6 = struct_betas_tech['TECHGUY_coef_Household Income 20 - 30'] 
TECHGUY_coef_RH1 = struct_betas_tech['TECHGUY_coef_Ride Hailing Use > Once Week-RH'] 
TECHGUY_coef_RH2 = struct_betas_tech['TECHGUY_coef_Ride Hailing Use = Once Week-RH'] 
TECHGUY_coef_CAR_OW1 = struct_betas_tech['TECHGUY_coef_CAR_OW1'] 

sigma_s_pt = Beta('sigma_s_pt', 1, None, None, 1)
error_component_pt = sigma_s_pt * bioDraws('EC1', 'NORMAL_MLHS')
sigma_s_safe = Beta('sigma_s_safe', 1, None, None, 0)
error_component_safe = sigma_s_safe * bioDraws('EC2', 'NORMAL_MLHS')
sigma_s_tech = Beta('sigma_s_tech', 1, None, None, 0)
error_component_tech = sigma_s_tech * bioDraws('EC3', 'NORMAL_MLHS')

PTGUY =   PTGUY_coef_intercept + \
          PTGUY_coef_IAGE5 * IAGE5 + \
          PTGUY_coef_IWORK4 * IWORK4 + \
          PTGUY_coef_IWORK5 * IWORK5 + \
          PTGUY_coef_IRTEH1 * IRTEH1 + \
          PTGUY_coef_HINC2 * HINC2 + \
          PTGUY_coef_HINC3 * HINC3 + \
          PTGUY_coef_HINC6 * HINC6 + \
          PTGUY_coef_IPHU3 * IPHU3 + \
          PTGUY_coef_RH2 * RH2 + \
          PTGUY_coef_RH3 * RH3 + \
          PTGUY_coef_RH4 * RH4 + \
          PTGUY_coef_CAR_OW2 * CAR_OW2 + error_component_pt

SAFEGUY = (  SAFEGUY_coef_intercept  
            +SAFEGUY_coef_IGN * IGN    
            +SAFEGUY_coef_IEDU3 * IEDU3  
            +SAFEGUY_coef_IWORK3 * IWORK3 
            +SAFEGUY_coef_IWORK6 * IWORK6 
            +SAFEGUY_coef_IRTEH1 * IRTEH1 
            +SAFEGUY_coef_IWTEH1 * IWTEH1 
            +SAFEGUY_coef_HINC2 * HINC2
            +SAFEGUY_coef_HINC5 * HINC5 
            +SAFEGUY_coef_IPHU1 * IPHU1 
            +SAFEGUY_coef_IPHU3 * IPHU3  
            +SAFEGUY_coef_RH2 * RH2 
            +SAFEGUY_coef_RH3 * RH3 
            +SAFEGUY_coef_CAR_OW0 * CAR_OW0  
            +SAFEGUY_coef_CAR_OW2 * CAR_OW2 + error_component_safe
            
)
        
TECHGUY = TECHGUY_coef_intercept + \
          TECHGUY_coef_IWORK2 * IWORK2 + \
          TECHGUY_coef_IWORK3 * IWORK3 + \
          TECHGUY_coef_IWORK6 * IWORK6 + \
          TECHGUY_coef_IRTEH1 * IRTEH1 + \
          TECHGUY_coef_HINC3 * HINC3 + \
          TECHGUY_coef_HINC5 * HINC5 + \
          TECHGUY_coef_HINC6 * HINC6 + \
          TECHGUY_coef_RH1 * RH1 + \
          TECHGUY_coef_RH2 * RH2 + \
          TECHGUY_coef_CAR_OW1 * CAR_OW1 + error_component_tech

B_PTGUY_AU = Beta("B_PTGUY_AU", 0, None, None, 1)
B_PTGUY_RH = Beta("B_PTGUY_RH", 0, None, None, 1)
B_PTGUY_AT = Beta("B_PTGUY_AT", 0, None, None, 1)
B_PTGUY_PT = Beta("B_PTGUY_PT", 0, None, None, 1)

B_SAFEGUY_AU = Beta("B_SAFEGUY_AU", 0, None, None, 1)
B_SAFEGUY_RH = Beta("B_SAFEGUY_RH", 0, None, None, 0)
B_SAFEGUY_AT = Beta("B_SAFEGUY_AT", 0, None, None, 0)
B_SAFEGUY_PT = Beta("B_SAFEGUY_PT", 0, None, None, 1)

B_TECHGUY_AU = Beta("B_TECHGUY_AU", 0, None, None, 1)
B_TECHGUY_RH = Beta("B_TECHGUY_RH", 0, None, None, 0)
B_TECHGUY_AT = Beta("B_TECHGUY_AT", 0, None, None, 1)
B_TECHGUY_PT = Beta("B_TECHGUY_PT", 0, None, None, 1)
 
V1 =ASC_AU +\
    B_TT      * (CAR_TT + CAR_WT)+\
    B_COST     * CAR_CO +\
    B_MM_AU_AU   * MM_AU +\
    B_MM_RH_AU   * MM_RH +\
    B_MM_PT_AU   * MM_PT +\
    B_IWORK4_AU  * IWORK4 +\
    B_IOPW1_AU   * IOPW1 +\
    B_TTSTATION1_AU * TTSTATION1 +\
    B_TTSTATION2_AU * TTSTATION2 +\
    B_IEMTR_AU    * IEMTR +\
    B_RHUSE1_AU   * RHUSE1 +\
    B_RHUSE2_AU   * RHUSE2 +\
    B_PTGUY_AU * PTGUY +\
    B_TECHGUY_AU * TECHGUY +\
    B_SAFEGUY_AU * SAFEGUY 
        

V2 =ASC_RH+\
    B_TT      * (T_TT + T_WT)+\
    B_COST     * T_CO +\
    B_IWORK2_RH * IWORK2 +\
    B_IWORK3_RH * IWORK3  +\
    B_IOPW1_RH  * IOPW1 +\
    B_HINC6_RH * HINC6  +\
    B_IPHU2_RH * IPHU2 +\
    B_IPHU3_RH * IPHU3 +\
    B_CAR_OW0_RH * CAR_OW0 +\
    B_CAR_OW1_RH * CAR_OW1 +\
    B_CAR_OW2_RH * CAR_OW2 +\
    B_IEMTR_RH    * IEMTR +\
    B_RHUSE6_RH   * RHUSE6 +\
    B_PTGUY_RH * PTGUY +\
    B_TECHGUY_RH * TECHGUY +\
    B_SAFEGUY_RH * SAFEGUY


V3 =ASC_AT +\
    B_AT_TT      * (AT_TT + AT_WT)+\
    B_AT_CO      * AT_CO  +\
    B_SM_RH_AT   * SM_RH +\
    B_IAGE2_AT   * IAGE2 +\
    B_IWORK3_AT  * IWORK3 +\
    B_RH1_AT * RH1 +\
    B_RH2_AT * RH2 +\
    B_RH3_AT * RH3 +\
    B_RH4_AT * RH4  +\
    B_PTGUY_AT * PTGUY +\
    B_TECHGUY_AT * TECHGUY +\
    B_SAFEGUY_AT * SAFEGUY


V4 =ASC_PT+\
    B_PT_TT      * (PT_TT + PT_WT) +\
    B_PT_CO      * PT_CO +\
    B_MM_RH_PT * MM_RH +\
    B_SM_AU_PT * SM_AU +\
    B_ITT2_PT * ITT2  +\
    B_HINC2_PT * HINC2 +\
    B_CAR_OW1_PT * CAR_OW1 +\
    B_RHUSE1_PT * RHUSE1 +\
    B_RHUSE4_PT * RHUSE4 +\
    B_PTGUY_PT * PTGUY +\
    B_TECHGUY_PT * TECHGUY +\
    B_SAFEGUY_PT * SAFEGUY

# Associate utility functions with the numbering of alternatives
V = {1: V1, 2: V2 ,3: V3, 4: V4 }

# Associate the availability conditions with the alternatives
av = {1: 1, 2: 1, 3: 1, 4:1}


'''
existing = MU, [1,2,4]
future = 1, [3]
nests = existing, future
logprob = models.logit(V, av, AirportToHotelCHOICE)
loglike = log(MonteCarlo(logprob))
biogeme = bio.BIOGEME(database,loglike)
biogeme.modelName = 'MNL_Air_Nested_Latent'
'''

'''
existing = MU, [1,2,4]
future = 1, [3]
nests = existing, future
logprob = models.lognested(V, av, nests, AirportToHotelCHOICE)
biogeme = bio.BIOGEME(database,logprob)
biogeme.modelName = 'MNL_Air_Nested'
'''


existing = OneNestForNestedLogit(nest_param=MU,list_of_alternatives=[1,2,4],name='existing')
future = OneNestForNestedLogit(nest_param=1,list_of_alternatives=[3],name='future')
nests = NestsForNestedLogit(choice_set=list(V),tuple_of_nests=(existing,future))

logprob = models.nested(V, av, nests, AirportToHotelCHOICE)
loglike = log(MonteCarlo(logprob))
biogeme = bio.BIOGEME(database,loglike)
biogeme.modelName = 'NL_Air'
'''

loglike = models.lognested(V, av, nests, AirportToHotelCHOICE)
biogeme = bio.BIOGEME(database,loglike)
biogeme.modelName = 'NL_Air'
'''

biogeme.calculateNullLoglikelihood(av)
results = biogeme.estimate()
pandasResults = results.getEstimatedParameters(onlyRobust=False)
print(pandasResults)
