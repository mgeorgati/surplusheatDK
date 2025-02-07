def rename_columns(df,renamed_columns):

    return df.rename(columns=renamed_columns)

def filter_columns(df, columns: list):
    existing_cols = [col for col in columns if col in df.columns]
    return df[existing_cols]

def filter_by_year(df, year):
    return df[df['year'] == year]



def process_data(df):
    # Group by year, municipality_code, and plant_type to sum heat_production_TJ
    df = (
        df.groupby(['year', 'municipality_code', 'plant_type'], as_index=False)
          ['heat_production_TJ']
          .sum()
    )

    # Calculate the total heat production per municipality (and year)
    df['total_municipality_heat_production_TJ'] = (
        df.groupby(['year', 'municipality_code'])['heat_production_TJ']
          .transform('sum')
    )

    # Calculate the share of each plant type in the total municipality heat production
    df['share_of_total_heat_production_TJ'] = (
        df['heat_production_TJ'] / df['total_municipality_heat_production_TJ'] * 100
    )

    # Filter to only the specified plant types
    #df = df[df['plant_type'].isin(['Overskudsvarme', 'Varmepumpe Oversku'])]
    df = [ (df ['Brændselsfrit_TJ']>0) & (df ['VrkTypeID']=='ER')]

    # Group by year and municipality_code again to sum the share
    df = (
        df.groupby(['year', 'municipality_code'], as_index=False)
          ['share_of_total_heat_production_TJ']
          .sum()
    )

    return df
