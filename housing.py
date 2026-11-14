# %%
import pandas as pd
import  matplotlib.pyplot as plt

# %%
df = pd.read_csv("Mumbai_House_Prices_Clean.csv")
print(df.shape)
df.head()
df.info()
# %%
region_stats = df.groupby("region")["price_per_sq_ft"].agg(["mean", "median", "count"])
print (region_stats.head())

# %%
region_stats = region_stats[region_stats["count"] >= 30]
print(region_stats.shape)

# %%
region_stats = region_stats.sort_values("median", ascending=False)
print(region_stats.head(5))

# %%
print(region_stats.tail(5))


#plott for top 10 regions by median price per sq ft
# %%
top10 = region_stats.head(10)
top10["median"].plot(kind="bar")
plt.title("Top 10 Mumbai regions by median price per sqft")
plt.ylabel("Price per sqft (Rs" )
plt.tight_layout()
plt.savefig("top10_regions.png")
plt.show()


#plott for top 10 cheapest mumbai regions by median price persqft
# %%
bottom10 = region_stats.tail(10)
bottom10["median"].plot(kind="bar")
plt.title("10 cheapest Mumbai regions by median price per sqft")
plt.ylabel("Price per sqft (Rs)" )
plt.tight_layout()
plt.savefig("bottom10_regions.png")
plt.show()

# %%
bhk_stats = df[df["bhk"].between(1, 5)].groupby("bhk")["price_per_sq_ft"].median()
bhk_stats.plot(kind="bar")
plt.title("Median price per sqft by BHK")
plt.xlabel("BHK")
plt.ylabel("Pricer per sqft (Rs)")
plt.tight_layout()
plt.savefig("pricer_by_bhk.png")
plt.show()

# %%
df["price_per_sq_ft"].plot(kind="hist", bins=50)
plt.title("Distribution of price per sqft")
plt.xlabel("Price per sqft (Rs)")
plt.ylabel("Number of listings")
plt.tight_layout()
plt.savefig("price_histogram.png")
plt.show()

# %%
df_bhk = df[df["bhk"].between(1, 5)]
df_bhk.boxplot(column="price_per_sq_ft", by="bhk")
plt.title("Price per sqft by BHK")
plt.suptitle("")
plt.xlabel("BHK")
plt.ylabel("Price per sqft (Rs)")
plt.tight_layout()
plt.savefig("price_boxplot_bhk.png")
plt.show()