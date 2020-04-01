import json, os 
import pandas as pd

def test_notepad():
    cmd = 'notepad'
    os.system(cmd)

def run_cmd(city, city_id):
    # print(city, city_id)
    command = 'twitterscraper "statefarm near:{} within:30mi" -l  100000 --csv --lang en --begindate 2015-01-01 --enddate 2020-01-01 --output {}.csv'.format(city, city_id)
    os.system(command)

def main():
    world_cities_df = pd.read_csv('worldcities.csv')
    us_df = world_cities_df[world_cities_df.country == 'United States']
    ca_df = us_df[us_df.admin_name == 'California']

    for index, row in ca_df.iterrows():
        run_cmd(row['city'], row['id'])

main()