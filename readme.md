# Parquet File Converter

1. In Case of **EQUITY** Open python file and Change ticker_type to "EQUITY"
2. In Case of **FOREX** Open python file and Change ticker_type to "FOREX"

Data should contain following columns:
1. "Date"
2. "Time"
3. "Open"
4. "High"
5. "Low"
6. "Close"
7. "Tick volume"

File shiould be named using following format:
1. For Bid Data > TICKER_TIMEINTERVAL.csv 
2. For Ask Data > TICKER_ask_TIMEINTERVAL.csv, Only needed when ticker_type is "EQUITY"