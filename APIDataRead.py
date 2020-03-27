import pandas as pd
import requests

def api_data_extractor(start_date,end_date,token, field="all",postcode="all"):

    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    df_cap_all = pd.DataFrame()
    df_per_all = pd.DataFrame()
    df_out_all = pd.DataFrame()
    df_load_all = pd.DataFrame()

    for date in date_range.values.astype('<M8[D]').astype(str):
        response = requests.get("https://pv-map.apvi.org.au/api/v2/2-digit/{}.json?access_token={}".format(date, token))
        print(date + " started")

        data = response.json()

        if field == "all" or field == "capacity":
            df_cap = pd.DataFrame.from_dict(data['capacity'], orient='index')
            df_cap.reset_index(inplace=True)
            df_cap['Date'] = date
            df_cap.columns = ['Postcode', 'Capacity_MW', 'Date']
            df_cap = df_cap[['Date', 'Postcode', 'Capacity_MW']]
            if postcode != "all":
                df_cap = df_cap[df_cap['Postcode'].str.startswith(str(postcode))].copy()
            df_cap_all = df_cap_all.append(df_cap)

        if field == "all" or field == "performance":
            df_per = pd.DataFrame.from_dict(data['performance'], orient='index')
            df_per.reset_index(inplace=True)
            df_per = pd.melt(df_per, id_vars=['index'])
            df_per.columns = ['Postcode', 'Timestamp', 'Performance']
            if postcode != "all":
                df_per = df_per[df_per['Postcode'].str.startswith(str(postcode))].copy()
            df_per_all = df_per_all.append(df_per)

        if field == "all" or field == "output":
            df_out = pd.DataFrame.from_dict(data['output'], orient='index')
            df_out.reset_index(inplace=True)
            df_out = pd.melt(df_out, id_vars=['index'])
            df_out.columns = ['Postcode', 'Timestamp', 'Output']
            if postcode != "all":
                df_out = df_out[df_out['Postcode'].str.startswith(str(postcode))].copy()
            df_out_all = df_out_all.append(df_out)

        if field == "all" or field == "load":
            df_load = pd.DataFrame.from_dict(data['load'], orient='index')
            df_load.reset_index(inplace=True)
            df_load.rename(columns={'index': 'Timestamp'}, inplace=True)
            df_load_all = df_load_all.append(df_load)
    return [df_load_all, df_out_all, df_cap_all, df_per_all]


