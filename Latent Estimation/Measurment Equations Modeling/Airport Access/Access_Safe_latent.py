import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio
import biogeme.models as models
import biogeme.distributions as dist
from biogeme.expressions import Beta, bioDraws, PanelLikelihoodTrajectory, MonteCarlo, log, bioNormalCdf, Elem, RandomVariable, Integrate
import biogeme.logging as blog
import biogeme.biogeme as bio
from biogeme.expressions import (
    Beta,
    log,
    Elem,
    bioNormalCdf,
    Variable,
    bioMultSum,
)
# Read the data
from Data import (
    database,
    HHM,
    GN, 
    AGE,
    EDU,
    IWORK,
    IOPW,
    IRTEH, 
    IWTEH,
    IRTEH,
    ITT,
    HHINC,
    PHU,
    MAIN_MODE,
    SEC_MODE,
    TTSTA,
    TAXI,
    HHCOW,
    MEHTR,
    EMTR,
    RHUSE1,
    RHUSE2,
    RHUSE3,
    RHUSE4,
    RHUSE5,
    RHUSE6,
    PreferElectricAuto,
    PreferHybridAuto,
    TrustAutoDrive,
    UsingSiriORAlexa,
    TrustCruise,
    UseGoogleMas,
    UsingTimeINAuto,
    SharedApp,
    HHM1,
    HHM2,
    IGN,
    IAGE1,
    IAGE2,
    IAGE3,
    IAGE4,
    IAGE5,
    IAGE6,
    IEDU1,
    IEDU2,
    IEDU3,
    IWORK1,
    IWORK2,
    IWORK3,
    IWORK4,
    IWORK5,
    IWORK6,
    IOPW1,
    IOPW2,
    IRTEH1,
    IWTEH1,
    ITT1,
    ITT2,
    ITT3,
    HINC1,
    HINC2,
    HINC3,
    HINC4,
    HINC5,
    HINC6,
    HINC7,
    IPHU1,
    IPHU2,
    IPHU3,
    IPHU4,
    MM_AU,
    MM_PT,
    MM_RH,
    MM_BK,
    MM_WA,
    SM_AU,
    SM_PT,
    SM_RH,
    SM_BK,
    SM_WA,
    TTSTATION1,
    TTSTATION2,
    RH1,
    RH2,
    RH3,
    RH4,
    RH5,
    CAR_OW0,
    CAR_OW1,
    CAR_OW2,
    IMEHTR,
    IEMTR,
    RHUSE111,
    RHUSE211,
    RHUSE311,
    RHUSE411,
    RHUSE511,
    RHUSE611
)

logger = blog.get_screen_logger(level=blog.INFO)
logger.info('Example m01_latent_variable.py')


SAFEGUY_coef_intercept = Beta('SAFEGUY_coef_intercept',0, None, None, 0)
SAFEGUY_coef_HHM1 = Beta('SAFEGUY_coef_HHM1', 0, None, None, 1)
SAFEGUY_coef_HHM2 = Beta('SAFEGUY_coef_HHM2', 0, None, None, 1)
SAFEGUY_coef_IGN = Beta('SAFEGUY_coef_IGN', 0, None, None, 0)
SAFEGUY_coef_IAGE1 = Beta('SAFEGUY_coef_Age < 18', 0, None, None, 1)
SAFEGUY_coef_IAGE2 = Beta('SAFEGUY_coef_Age 18 - 24', 0, None, None, 1)
SAFEGUY_coef_IAGE3 = Beta('SAFEGUY_coef_Age 25 - 34', 0, None, None, 1)
SAFEGUY_coef_IAGE4 = Beta('SAFEGUY_coef_Age 35 - 44', 0, None, None, 1)
SAFEGUY_coef_IAGE5 = Beta('SAFEGUY_coef_Age 45 - 54', 0, None, None, 1)
SAFEGUY_coef_IAGE6 = Beta('SAFEGUY_coef_Age 55 - 64', 0, None, None, 1)
SAFEGUY_coef_IEDU1 = Beta('SAFEGUY_coef_IEDU1', 0, None, None, 1)
SAFEGUY_coef_IEDU2 = Beta('SAFEGUY_coef_IEDU2', 0, None, None, 1)
SAFEGUY_coef_IEDU3 = Beta('SAFEGUY_coef_IEDU3', 0, None, None, 0)
SAFEGUY_coef_IWORK1 = Beta('SAFEGUY_coef_Occupation Owner', 0, None, None, 1)
SAFEGUY_coef_IWORK2 = Beta('SAFEGUY_coef_Occupation Employee Private', 0, None, None, 1)
SAFEGUY_coef_IWORK3 = Beta('SAFEGUY_coef_Occupation Employee Public', 0, None, None, 0)
SAFEGUY_coef_IWORK4 = Beta('SAFEGUY_coef_Occupation Student', 0, None, None, 1)
SAFEGUY_coef_IWORK5 = Beta('SAFEGUY_coef_Occupation Retired', 0, None, None, 1)
SAFEGUY_coef_IWORK6 = Beta('SAFEGUY_coef_Occupation Unofficial', 0, None, None, 0)
SAFEGUY_coef_IOPW1 = Beta('SAFEGUY_coef_IOPW1', 0, None, None, 1)
SAFEGUY_coef_IOPW2 = Beta('SAFEGUY_coef_IOPW2', 0, None, None,1)
SAFEGUY_coef_IRTEH1 = Beta('SAFEGUY_coef_IRTEH1', 0, None, None, 0)
SAFEGUY_coef_IWTEH1 = Beta('SAFEGUY_coef_IWTEH1', 0, None, None, 0)
SAFEGUY_coef_HINC1 = Beta('SAFEGUY_coef_Household Income < 3.5', 0, None, None, 1)
SAFEGUY_coef_HINC2 = Beta('SAFEGUY_coef_Household Income 3.5 - 6', 0, None, None, 0)
SAFEGUY_coef_HINC3 = Beta('SAFEGUY_coef_Household Income 6 - 9', 0, None, None, 1)
SAFEGUY_coef_HINC4 = Beta('SAFEGUY_coef_Household Income 9 - 14', 0, None, None, 1)
SAFEGUY_coef_HINC5 = Beta('SAFEGUY_coef_Household Income 14 - 20', 0, None, None, 0)
SAFEGUY_coef_HINC6 = Beta('SAFEGUY_coef_Household Income 20 - 30', 0, None, None, 1)
SAFEGUY_coef_HINC7 = Beta('SAFEGUY_coef_Household Income > 30', 0, None, None, 1)
SAFEGUY_coef_IPHU1 = Beta('SAFEGUY_coef_IPHU1', 0, None, None, 0)
SAFEGUY_coef_IPHU2 = Beta('SAFEGUY_coef_IPHU2', 0, None, None, 1)
SAFEGUY_coef_IPHU3 = Beta('SAFEGUY_coef_IPHU3', 0, None, None, 0)
SAFEGUY_coef_RH1 = Beta('SAFEGUY_coef_Ride Hailing Use > Once Week-RH', 0, None, None, 1)
SAFEGUY_coef_RH2 = Beta('SAFEGUY_coef_Ride Hailing Use = Once Week-RH', 0, None, None, 0)
SAFEGUY_coef_RH3 = Beta('SAFEGUY_coef_Ride Hailing Use = Once Month-RH', 0, None, None, 0)
SAFEGUY_coef_RH4 = Beta('SAFEGUY_coef_Ride Hailing Use < Once Month-RH', 0, None, None, 1)
SAFEGUY_coef_RH5 = Beta('SAFEGUY_coef_Ride Hailing Use = Never', 0, None, None, 1)
SAFEGUY_coef_RHUSE111 = Beta('SAFEGUY_coef_RH FOR 01AIRPORT', 0, None, None, 1)
SAFEGUY_coef_RHUSE211 = Beta('SAFEGUY_coef_RH FOR 02WORK ALWAYS', 0, None, None, 1)
SAFEGUY_coef_RHUSE311 = Beta('SAFEGUY_coef_RH FOR 03WORK OCCASIONLY', 0, None, None, 1)
SAFEGUY_coef_RHUSE411 = Beta('SAFEGUY_coef_RH FOR 04NIGHT OUT', 0, None, None, 1)
SAFEGUY_coef_RHUSE511 = Beta('SAFEGUY_coef_RH FOR 05REC', 0, None, None, 1)
SAFEGUY_coef_RHUSE611 = Beta('SAFEGUY_coef_RH FOR 06OTHERS', 0, None, None, 1)
SAFEGUY_coef_CAR_OW0 = Beta('SAFEGUY_coef_CAR_OW0', 0, None, None, 0)
SAFEGUY_coef_CAR_OW1 = Beta('SAFEGUY_coef_CAR_OW1', 0, None, None, 1)
SAFEGUY_coef_CAR_OW2 = Beta('SAFEGUY_coef_CAR_OW2', 0, None, None, 0)
'''
omega = RandomVariable('omega')
density = dist.normalpdf(omega) 
sigma_s = Beta('sigma_s',1,None,None,0)
'''
SAFEGUY = SAFEGUY_coef_intercept + \
          SAFEGUY_coef_HHM1 * HHM1 + \
          SAFEGUY_coef_HHM2 * HHM2 + \
          SAFEGUY_coef_IGN * IGN + \
          SAFEGUY_coef_IAGE1 * IAGE1 + \
          SAFEGUY_coef_IAGE2 * IAGE2 + \
          SAFEGUY_coef_IAGE3 * IAGE3 + \
          SAFEGUY_coef_IAGE4 * IAGE4 + \
          SAFEGUY_coef_IAGE5 * IAGE5 + \
          SAFEGUY_coef_IAGE6 * IAGE6 + \
          SAFEGUY_coef_IEDU1 * IEDU1 + \
          SAFEGUY_coef_IEDU2 * IEDU2 + \
          SAFEGUY_coef_IEDU3 * IEDU3 + \
          SAFEGUY_coef_IWORK1 * IWORK1 + \
          SAFEGUY_coef_IWORK2 * IWORK2 + \
          SAFEGUY_coef_IWORK3 * IWORK3 + \
          SAFEGUY_coef_IWORK4 * IWORK4 + \
          SAFEGUY_coef_IWORK5 * IWORK5 + \
          SAFEGUY_coef_IWORK6 * IWORK6 + \
          SAFEGUY_coef_IOPW1 * IOPW1 + \
          SAFEGUY_coef_IOPW2 * IOPW2 + \
          SAFEGUY_coef_IRTEH1 * IRTEH1 + \
          SAFEGUY_coef_IWTEH1 * IWTEH1 + \
          SAFEGUY_coef_HINC1 * HINC1 + \
          SAFEGUY_coef_HINC2 * HINC2 + \
          SAFEGUY_coef_HINC3 * HINC3 + \
          SAFEGUY_coef_HINC4 * HINC4 + \
          SAFEGUY_coef_HINC5 * HINC5 + \
          SAFEGUY_coef_HINC6 * HINC6 + \
          SAFEGUY_coef_HINC7 * HINC7 + \
          SAFEGUY_coef_IPHU1 * IPHU1 + \
          SAFEGUY_coef_IPHU2 * IPHU2 + \
          SAFEGUY_coef_IPHU3 * IPHU3 + \
          SAFEGUY_coef_RH1 * RH1 + \
          SAFEGUY_coef_RH2 * RH2 + \
          SAFEGUY_coef_RH3 * RH3 + \
          SAFEGUY_coef_RH4 * RH4 + \
          SAFEGUY_coef_RH5 * RH5 + \
          SAFEGUY_coef_RHUSE111 * RHUSE111 + \
          SAFEGUY_coef_RHUSE211 * RHUSE211 + \
          SAFEGUY_coef_RHUSE311 * RHUSE311 + \
          SAFEGUY_coef_RHUSE411 * RHUSE411 + \
          SAFEGUY_coef_RHUSE511 * RHUSE511 + \
          SAFEGUY_coef_RHUSE611 * RHUSE611 + \
          SAFEGUY_coef_CAR_OW0 * CAR_OW0 + \
          SAFEGUY_coef_CAR_OW1 * CAR_OW1 + \
          SAFEGUY_coef_CAR_OW2 * CAR_OW2 

""" 

#TAXIGUY = 
#SAFEGUY = 

TaxiMoreComfortableThanAuto                      0.444263
PreferNotToDrive                                  0.42436
PreferToUsePT                                    0.485313
PreferToRenACar                                  0.497794
PreferTaxi                                       0.675008

PreferElectricAuto           0.576702                    
PreferHybridAuto             0.577097                    
TrustAutoDrive               0.623502                    
UsingSiriORAlexa             0.679897                    
TrustCruise                  0.709201                    
UseGoogleMas                 0.462281                    
UsingTimeINAuto               0.41177                    
SharedApp                    0.497011                    

ATUsingCamera                          0.596168          
TalkingToOperator                      0.670262          
LandOperatorControl                    0.444441          
ATWorkWithTaxi                         0.505619          
MobileIsImportant                      0.431334          
TechnologyMatter             0.416707   0.41375          

 """

# %%
# Measurement equations
indicators = [
    'ATUsingCamera',                            
    'TalkingToOperator',                             
    'LandOperatorControl',                           
    'ATWorkWithTaxi',                                
    'MobileIsImportant',                              
    'TechnologyMatter'
]

# %%
# We define the intercept parameters. The first one is normalized to 0.
inter = {k: Beta(f'inter_{k}', 0, None, None, 0) for k in indicators[1:]}
inter[indicators[0]] = Beta(f'INTER_{indicators[0]}', 0, None, None, 1)

# %%
# We define the coefficients. The first one is normalized to 1.
coefficients = {k: Beta(f'coeff_{k}', 0, None, None, 0) for k in indicators[1:]}
coefficients[indicators[0]] = Beta(f'B_{indicators[0]}', 1, None, None, 1)

# %%
# We define the measurement equations for each indicator
models = {k: inter[k] + coefficients[k] * SAFEGUY for k in indicators}

# %%
# We define the scale parameters of the error terms.
sigma_star = {k: Beta(f'sigma_star_{k}', 1, 1.0e-5, None, 0) for k in indicators[1:]}
sigma_star[indicators[0]] = Beta(f'sigma_star_{indicators[0]}', 1, None, None, 1)

# %%
# Symmetric threshold.
delta_1 = Beta('delta_1', 0.1, 1.0e-5, None, 0)
delta_2 = Beta('delta_2', 0.2, 1.0e-5, None, 0)
tau_1 = -delta_1 - delta_2
tau_2 = -delta_1
tau_3 = delta_1
tau_4 = delta_1 + delta_2

# %%
# Ordered probit models.
tau_1_residual = {k: (tau_1 - models[k]) / sigma_star[k] for k in indicators}
tau_2_residual = {k: (tau_2 - models[k]) / sigma_star[k] for k in indicators}
tau_3_residual = {k: (tau_3 - models[k]) / sigma_star[k] for k in indicators}
tau_4_residual = {k: (tau_4 - models[k]) / sigma_star[k] for k in indicators}
dict_prob_indicators = {
    k: {
        1: bioNormalCdf(tau_1_residual[k]),
        2: bioNormalCdf(tau_2_residual[k]) - bioNormalCdf(tau_1_residual[k]),
        3: bioNormalCdf(tau_3_residual[k]) - bioNormalCdf(tau_2_residual[k]),
        4: bioNormalCdf(tau_4_residual[k]) - bioNormalCdf(tau_3_residual[k]),
        5: 1 - bioNormalCdf(tau_4_residual[k]),
    }
    for k in indicators
}

# %%
log_proba = {k: log(Elem(dict_prob_indicators[k], Variable(k))) for k in indicators}
loglike = bioMultSum(log_proba)

# %%
# Create the Biogeme object
the_biogeme = bio.BIOGEME(database,loglike)
the_biogeme.modelName = 'Access_SAFEGUY_latent'

# %%
# Estimate the parameters

results = the_biogeme.estimate()
'''
html = results.getHtml(onlyRobust=False)
filename = "Access_SAFEGUY.html"
with open(filename, 'w') as file:
    file.write(html)
'''
# %%
results.getEstimatedParameters()
