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
df = pd.read_csv('REC_TRIP_DATA.txt' , sep='\t')
selected_df = df.iloc[::6]
database = db.Database('Example', selected_df)
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
RH1        = (TAXI  == 1)
RH2        = (TAXI  == 2)
RH3        = (TAXI  == 3)
RH4        = (TAXI  == 4)
CAR_OW0    = (HHCOW == 0)
CAR_OW1    = (HHCOW == 1)
CAR_OW2    = (HHCOW == 2)
IMEHTR     = (MEHTR == 0 or MEHTR == 1 or MEHTR == 2 or MEHTR == 3)
IEMTR      = (EMTR  == 0 or EMTR  == 1 or EMTR  == 2 or EMTR  == 3)

logger = blog.get_screen_logger(level=blog.INFO)
logger.info('Example m01_latent_variable.py')

TECHGUY_coef_intercept = Beta('TECHGUY_coef_intercept',0, None, None, 0)
TECHGUY_coef_HHM1 = Beta('TECHGUY_coef_Household Member123', 0, None, None, 1)
TECHGUY_coef_HHM2 = Beta('TECHGUY_coef_Household Member45', 0, None, None, 1)
TECHGUY_coef_IGN = Beta('TECHGUY_coef_Gender', 0, None, None, 1)
TECHGUY_coef_IAGE1 = Beta('TECHGUY_coef_Age < 18', 0, None, None, 1)
TECHGUY_coef_IAGE2 = Beta('TECHGUY_coef_Age 18 - 24', 0, None, None, 1)
TECHGUY_coef_IAGE3 = Beta('TECHGUY_coef_Age 25 - 34', 0, None, None, 1)
TECHGUY_coef_IAGE4 = Beta('TECHGUY_coef_Age 35 - 44', 0, None, None, 0)
TECHGUY_coef_IAGE5 = Beta('TECHGUY_coef_Age 45 - 54', 0, None, None, 0)
TECHGUY_coef_IAGE6 = Beta('TECHGUY_coef_Age 55 - 64', 0, None, None, 1)
TECHGUY_coef_IEDU1 = Beta('TECHGUY_coef_IEDU1', 0, None, None, 1)
TECHGUY_coef_IEDU2 = Beta('TECHGUY_coef_IEDU2', 0, None, None, 0)
TECHGUY_coef_IEDU3 = Beta('TECHGUY_coef_IEDU3', 0, None, None, 1)
TECHGUY_coef_IEDU4 = Beta('TECHGUY_coef_IEDU4', 0, None, None, 0)
TECHGUY_coef_IWORK1 = Beta('TECHGUY_coef_Occupation Owner', 0, None, None, 1)
TECHGUY_coef_IWORK2 = Beta('TECHGUY_coef_Occupation Employee Private', 0, None, None, 0)
TECHGUY_coef_IWORK3 = Beta('TECHGUY_coef_Occupation Employee Public', 0, None, None, 1)
TECHGUY_coef_IWORK4 = Beta('TECHGUY_coef_Occupation Student', 0, None, None, 1)
TECHGUY_coef_IWORK5 = Beta('TECHGUY_coef_Occupation Retired', 0, None, None, 0)
TECHGUY_coef_IWORK6 = Beta('TECHGUY_coef_Occupation Unofficial', 0, None, None, 1)
TECHGUY_coef_IOPW1 = Beta('TECHGUY_coef_IOPW1', 0, None, None, 1)
TECHGUY_coef_IOPW2 = Beta('TECHGUY_coef_IOPW2', 0, None, None, 1)
TECHGUY_coef_IRTEH1 = Beta('TECHGUY_coef_Res TEH', 0, None, None, 0)
TECHGUY_coef_IWTEH1 = Beta('TECHGUY_coef_Work TEH', 0, None, None, 0)
TECHGUY_coef_HINC1 = Beta('TECHGUY_coef_Household Income < 3.5', 0, None, None, 1)
TECHGUY_coef_HINC2 = Beta('TECHGUY_coef_Household Income 3.5 - 6', 0, None, None, 1)
TECHGUY_coef_HINC3 = Beta('TECHGUY_coef_Household Income 6 - 9', 0, None, None, 1)
TECHGUY_coef_HINC4 = Beta('TECHGUY_coef_Household Income 9 - 14', 0, None, None, 1)
TECHGUY_coef_HINC5 = Beta('TECHGUY_coef_Household Income 14 - 20', 0, None, None,1)
TECHGUY_coef_HINC6 = Beta('TECHGUY_coef_Household Income 20 - 30', 0, None, None, 1)
TECHGUY_coef_HINC7 = Beta('TECHGUY_coef_Household Income > 30', 0, None, None, 1)
TECHGUY_coef_IPHU1 = Beta('TECHGUY_coef_IPHU1', 0, None, None, 1)
TECHGUY_coef_IPHU2 = Beta('TECHGUY_coef_IPHU2', 0, None, None, 1)
TECHGUY_coef_IPHU3 = Beta('TECHGUY_coef_IPHU3', 0, None, None, 1)
TECHGUY_coef_RH1 = Beta('TECHGUY_coef_Ride Hailing Use > Once Week-RH', 0, None, None, 1)
TECHGUY_coef_RH2 = Beta('TECHGUY_coef_Ride Hailing Use = Once Week-RH', 0, None, None, 1)
TECHGUY_coef_RH3 = Beta('TECHGUY_coef_Ride Hailing Use = Once Month-RH', 0, None, None, 1)
TECHGUY_coef_RH4 = Beta('TECHGUY_coef_Ride Hailing Use < Once Month-RH', 0, None, None, 1)
TECHGUY_coef_RH5 = Beta('TECHGUY_coef_Ride Hailing Use = Never', 0, None, None, 0)
TECHGUY_coef_RHUSE111 = Beta('TECHGUY_coef_RH FOR 01AIRPORT', 0, None, None, 0)
TECHGUY_coef_RHUSE211 = Beta('TECHGUY_coef_RH FOR 02WORK ALWAYS', 0, None, None, 0)
TECHGUY_coef_RHUSE311 = Beta('TECHGUY_coef_RH FOR 03WORK OCCASIONLY', 0, None, None, 0)
TECHGUY_coef_RHUSE411 = Beta('TECHGUY_coef_RH FOR 04NIGHT OUT', 0, None, None, 0)
TECHGUY_coef_RHUSE511 = Beta('TECHGUY_coef_RH FOR 05REC', 0, None, None, 0)
TECHGUY_coef_RHUSE611 = Beta('TECHGUY_coef_RH FOR 06OTHERS', 0, None, None, 0)
TECHGUY_coef_CAR_OW0 = Beta('TECHGUY_coef_CAR_OW0', 0, None, None, 1)
TECHGUY_coef_CAR_OW1 = Beta('TECHGUY_coef_CAR_OW1', 0, None, None, 1)
TECHGUY_coef_CAR_OW2 = Beta('TECHGUY_coef_CAR_OW2', 0, None, None, 1)

'''
omega = RandomVariable('omega')
density = dist.normalpdf(omega) 
sigma_s = Beta('sigma_s',1,None,None,0)
'''
TECHGUY = TECHGUY_coef_intercept + \
          TECHGUY_coef_HHM1 * HHM1 + \
          TECHGUY_coef_HHM2 * HHM2 + \
          TECHGUY_coef_IGN * IGN + \
          TECHGUY_coef_IAGE1 * IAGE1 + \
          TECHGUY_coef_IAGE2 * IAGE2 + \
          TECHGUY_coef_IAGE3 * IAGE3 + \
          TECHGUY_coef_IAGE4 * IAGE4 + \
          TECHGUY_coef_IAGE5 * IAGE5 + \
          TECHGUY_coef_IAGE6 * IAGE6 + \
          TECHGUY_coef_IEDU1 * IEDU1 + \
          TECHGUY_coef_IEDU2 * IEDU2 + \
          TECHGUY_coef_IEDU3 * IEDU3 + \
          TECHGUY_coef_IWORK1 * IWORK1 + \
          TECHGUY_coef_IWORK2 * IWORK2 + \
          TECHGUY_coef_IWORK3 * IWORK3 + \
          TECHGUY_coef_IWORK4 * IWORK4 + \
          TECHGUY_coef_IWORK5 * IWORK5 + \
          TECHGUY_coef_IWORK6 * IWORK6 + \
          TECHGUY_coef_IOPW1 * IOPW1 + \
          TECHGUY_coef_IOPW2 * IOPW2 + \
          TECHGUY_coef_IRTEH1 * IRTEH1 + \
          TECHGUY_coef_IWTEH1 * IWTEH1 + \
          TECHGUY_coef_HINC1 * HINC1 + \
          TECHGUY_coef_HINC2 * HINC2 + \
          TECHGUY_coef_HINC3 * HINC3 + \
          TECHGUY_coef_HINC4 * HINC4 + \
          TECHGUY_coef_HINC5 * HINC5 + \
          TECHGUY_coef_HINC6 * HINC6 + \
          TECHGUY_coef_HINC7 * HINC7 + \
          TECHGUY_coef_IPHU1 * IPHU1 + \
          TECHGUY_coef_IPHU2 * IPHU2 + \
          TECHGUY_coef_IPHU3 * IPHU3 + \
          TECHGUY_coef_RH1 * RH1 + \
          TECHGUY_coef_RH2 * RH2 + \
          TECHGUY_coef_RH3 * RH3 + \
          TECHGUY_coef_RH4 * RH4 + \
          TECHGUY_coef_CAR_OW0 * CAR_OW0 + \
          TECHGUY_coef_CAR_OW1 * CAR_OW1 + \
          TECHGUY_coef_CAR_OW2 * CAR_OW2 

 # %%
# Measurement equations
indicators = [
'TrustAutoDrive', 
'UsingSiriORAlexa', 
'TrustCruise',   
'UseGoogleMas',   
'UsingTimeINAuto',   
'PreferHybridAuto'
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
models = {k: inter[k] + coefficients[k] * TECHGUY for k in indicators}

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
the_biogeme = bio.BIOGEME(database,loglike,parameter_file='biogeme copy.toml')
the_biogeme.modelName = 'Rec_TECHGUY'

# %%
# Estimate the parameters
results = the_biogeme.estimate()
'''
html = results.getHtml(onlyRobust=False)
filename = "Business_TECHGUY.html"
with open(filename, 'w') as file:
    file.write(html)
'''
# %%
print(f'Estimated betas: {len(results.data.betaValues)}')
print(f'final log likelihood: {results.data.logLike:.3f}')
print(f'Output file: {results.data.htmlFileName}')

# %%
results.getEstimatedParameters()
