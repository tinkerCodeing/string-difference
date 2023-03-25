a = "afdtyeywfDVTECFDTYGEFDTVYGYCGVYGYqazxswedcvfrfgbhgytujnjkiokjuhjkopolkml"
b = "afdtyeyufDVTECFDTYGEhDTVYGYCGVYGYqazxswedcvfrfgbhgytujnjkiokjuhjkopolkml"

for i , j in enumerate(zip(a,b)):
    if j[0] != j[1]:
        print(f'{i},{j}')