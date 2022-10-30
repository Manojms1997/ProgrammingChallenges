import pandas as pd
import time
import os

# accessories_df = pd.read_csv("./fixtures/accessories.csv")
# clothing_df = pd.read_csv("./fixtures/clothing.csv")
# accessories_df["filename"] = "accessories"
# clothing_df["filename"] = "clothing"
# combined = pd.concat([accessories_df,clothing_df])
# combined.to_csv('enrollment.csv',index=False,header=True)

# start_time = time.time()
# random_df = pd.read_csv("./fixtures/random.csv")
# random1_df = pd.read_csv("./fixtures/random-1.csv")
# random1_df["filename"] = "random"
# random1_df["filename"] = "random-1"
# combined = pd.concat([random_df,random1_df])
# combined.to_csv('rand.csv',index=False,header=True)
# to_time = time.time() - start_time
# print(to_time)

# using chunking method 1:
# start_time = time.time()
# files = ["./fixtures/random.csv","./fixtures/random-1.csv"]
# chunks = []
# for file in files:
#     for chunk in pd.read_csv(file,chunksize=10**4):
#         filename = os.path.basename(file)
#         chunk['filename'] = filename
#         chunks.append(chunk)
# for chunk in chunks:
#     print(chunk.to_csv(index=False, header=True, chunksize=10**4, line_terminator='\n'), end='')
# to_time = time.time() - start_time
# print(to_time)

# just pandas method:
# start_time = time.time()
# files = ["./fixtures/random.csv","./fixtures/random-1.csv"]
# chunks = []
# for file in files:
#     filename = os.path.basename(file)
#     chunk = pd.read_csv(file)
#     chunk['filename'] = filename
#     chunks.append(chunk)
# for chunk in chunks:
#     print(chunk.to_csv(index=False, line_terminator='\n'), end='')
# to_time = time.time() - start_time
# print(to_time)


# missing columns:
accessories_df = pd.read_csv("./fixtures/accessories.csv")
clothing_df = pd.read_csv("./fixtures/miss-clothing.csv")
accessories_df["filename"] = "accessories"
clothing_df["filename"] = "clothing"
combined = pd.concat([accessories_df,clothing_df])
combined.to_csv('enrollment.csv',index=False,header=True)