import dask.dataframe as dd
import time

# accessories_df = dd.read_csv("./fixtures/accessories.csv")
# clothing_df = dd.read_csv("./fixtures/clothing.csv")
# accessories_df["filename"] = "accessories"
# clothing_df["filename"] = "clothing"
# combined = dd.concat([accessories_df,clothing_df])
# combined.to_csv('enrollment.csv',index=False,header=True,single_file=True)

start_time = time.time()
random_df = dd.read_csv("./fixtures/random.csv")
random1_df = dd.read_csv("./fixtures/random-1.csv")
random1_df["filename"] = "random"
random1_df["filename"] = "random-1"
combined = dd.concat([random_df,random1_df])
combined.to_csv('rand.csv',index=False,header=True,single_file=True)
to_time = time.time() - start_time
print(to_time)