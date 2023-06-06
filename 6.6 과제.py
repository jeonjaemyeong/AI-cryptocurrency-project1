import pandas as pd

file_path = '/Users/jeonjaemyeong/Desktop/2023-05-07-upbit-btc-orderbook.csv'

df = pd.read_csv(file_path, encoding='CP949')

df = df.drop(['Unnamed: 4', 'Unnamed: 5'], axis=1)

df.columns = ['Type', 'Price', 'Quantity', 'Timestamp', 'AdditionalColumn1', 'AdditionalColumn2']

df = df.dropna()

def calculate_features(data):
    mid_price = data['Price']
    book_delta = data['Quantity']
    book_imbalance = data['Timestamp']
    result.append([mid_price, book_delta, book_imbalance])
result = []
for _, row in df.iterrows():
    features = calculate_features(row)
    result.append(list(features))

filtered_result_df = pd.DataFrame(result, columns=['mid_price', 'book_delta', 'book_imbalance'])
filtered_result_df.to_csv('calculated_features_filtered.csv', index=False)
