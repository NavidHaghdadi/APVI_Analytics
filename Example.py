import pandas as pd
import requests
from Token import token
from APIDataRead import api_data_extractor

# examples:

# specify the dates, the token needs to be imported as well
start_date = "2020-01-01"
end_date = "2020-01-03"

# get all data:
# [df_load_all, df_out_all, df_cap_all, df_per_all] = api_data_extractor(start_date, end_date, token)

# for specific field performance, capacity, load or output
[df_load_all2, df_out_all2, df_cap_all2, df_per_all2] = api_data_extractor(start_date, end_date, token, field="capacity")
# saving data to csv
df_cap_all2.to_csv("CapacityData_2019.csv", index=False)

# # for specific postcode add the postcode in text, for example: "31" or "3" (to have all postcodes starting with 3)
# [df_load_all, df_out_all, df_cap_all, df_per_all] = api_data_extractor(start_date, end_date, token, field="performance", postcode="31")

