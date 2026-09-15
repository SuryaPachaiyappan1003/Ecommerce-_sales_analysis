import pandas as pd

df = pd.read_csv("ecommerce_products.csv")

print(df.head())

import pandas as pd

df = pd.read_csv("ecommerce_products.csv")

# 1. First 5 rows
print("FIRST 5 ROWS")
print(df.head())

# 2. Number of rows and columns
print("\nSHAPE")
print(df.shape)

# 3. Column names and data types
print("\nDATA INFORMATION")
print(df.info())

# 4. Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 5. Duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# DATA CLEANING

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Remove extra spaces from text columns
text_columns = [
    "Product_Name",
    "Category",
    "Sub_Category",
    "Brand"
]

for column in text_columns:
    df[column] = df[column].str.strip()

# Check invalid values
print("\nCLEANED DATA")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning")
print(df.duplicated().sum())


# STEP 3 - EXPLORATORY DATA ANALYSIS

print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())

print("\n--- CATEGORIES ---")
print(df["Category"].unique())

print("\n--- CATEGORY COUNT ---")
print(df["Category"].value_counts())

print("\n--- BRAND COUNT ---")
print(df["Brand"].value_counts())

print("\n--- TOP 10 MOST REVIEWED PRODUCTS ---")

top_reviewed = df.sort_values(
    by="Review_Count",
    ascending=False
).head(10)

print(top_reviewed[
    ["Product_Name", "Category", "Rating", "Review_Count"]
])

print("\n--- TOP 10 RATED PRODUCTS ---")

top_rated = df.sort_values(
    by="Rating",
    ascending=False
).head(10)

print(top_rated[
    ["Product_Name", "Category", "Rating", "Review_Count"]
])


# STEP 4 - PRICE ANALYSIS

print("\n--- PRICE ANALYSIS ---")

print("Average Price:", df["Price"].mean())
print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())
print("Average Selling Price:", df["Selling_Price"].mean())

print("\n--- TOP 10 MOST EXPENSIVE PRODUCTS ---")

expensive_products = df.sort_values(
    by="Price",
    ascending=False
).head(10)

print(expensive_products[
    ["Product_Name", "Category", "Brand", "Price", "Discount_Percent", "Selling_Price"]
])


print("\n--- CATEGORY WISE PRICE ANALYSIS ---")

category_price = df.groupby("Category")["Price"].agg(
    ["mean", "min", "max"]
).round(2)

print(category_price)

# STEP 5 - RATING AND REVIEW ANALYSIS

print("\n--- RATING ANALYSIS ---")

print("Average Rating:", round(df["Rating"].mean(), 2))
print("Highest Rating:", df["Rating"].max())
print("Lowest Rating:", df["Rating"].min())


print("\n--- CATEGORY WISE RATING ---")

category_rating = df.groupby("Category")["Rating"].agg(
    ["mean", "min", "max"]
).round(2)

print(category_rating)


print("\n--- TOP 10 MOST REVIEWED PRODUCTS ---")

top_reviewed = df.sort_values(
    by="Review_Count",
    ascending=False
).head(10)

print(top_reviewed[
    ["Product_Name", "Category", "Rating", "Review_Count"]
])


print("\n--- TOP 10 PRODUCTS BY RATING AND REVIEWS ---")

high_performing = df[
    (df["Rating"] >= 4.5) &
    (df["Review_Count"] >= 2000)
].sort_values(
    by="Review_Count",
    ascending=False
).head(10)

print(high_performing[
    ["Product_Name", "Category", "Rating", "Review_Count"]
])

(df["Rating"] >= 4.5) & (df["Review_Count"] >= 2000)

# STEP 6 - CATEGORY ANALYSIS

print("\n--- CATEGORY ANALYSIS ---")

category_analysis = df.groupby("Category").agg(
    Product_Count=("Product_ID", "count"),
    Average_Price=("Price", "mean"),
    Average_Rating=("Rating", "mean"),
    Total_Reviews=("Review_Count", "sum")
).round(2)

print(category_analysis)

print("\n--- MOST POPULAR CATEGORIES ---")

popular_categories = df["Category"].value_counts()

print(popular_categories)

print("\n--- HIGHEST RATED CATEGORY ---")

highest_rated_category = (
    df.groupby("Category")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

print(highest_rated_category)

print("\n--- CUSTOMER INTEREST BY CATEGORY ---")

customer_interest = (
    df.groupby("Category")["Review_Count"]
    .sum()
    .sort_values(ascending=False)
)

print(customer_interest)

import matplotlib.pyplot as plt
# STEP 7 - CATEGORY PRODUCT COUNT CHART

category_counts = df["Category"].value_counts()

plt.figure(figsize=(10, 6))

category_counts.plot(kind="bar")

plt.title("Number of Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# STEP 8 - PRICE DISTRIBUTION

plt.figure(figsize=(10, 6))

plt.hist(df["Price"], bins=20)

plt.title("Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.show()

# RATING DISTRIBUTION

plt.figure(figsize=(10, 6))

plt.hist(df["Rating"], bins=10)

plt.title("Product Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.show()

# STEP 9 - RATING DISTRIBUTION

plt.figure(figsize=(10, 6))

plt.hist(df["Rating"], bins=10)

plt.title("Product Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.show()

# STEP 10 - DISCOUNT ANALYSIS

print("\n--- DISCOUNT ANALYSIS ---")

print("Average Discount:", round(df["Discount_Percent"].mean(), 2))
print("Highest Discount:", df["Discount_Percent"].max())
print("Lowest Discount:", df["Discount_Percent"].min())

print("\n--- TOP 10 PRODUCTS WITH HIGHEST DISCOUNT ---")

top_discount = df.sort_values(
    by="Discount_Percent",
    ascending=False
).head(10)

print(top_discount[
    ["Product_Name", "Category", "Price", "Discount_Percent", "Selling_Price"]
])

# STEP 11 - SELLING PRICE ANALYSIS

print("\n--- SELLING PRICE ANALYSIS ---")

print("Average Selling Price:", round(df["Selling_Price"].mean(), 2))
print("Minimum Selling Price:", df["Selling_Price"].min())
print("Maximum Selling Price:", df["Selling_Price"].max())

print("\n--- TOP 10 PRODUCTS BY SELLING PRICE ---")

top_selling_price = df.sort_values(
    by="Selling_Price",
    ascending=False
).head(10)

print(top_selling_price[
    ["Product_Name", "Category", "Price", "Discount_Percent", "Selling_Price"]
])

# STEP 12 - CATEGORY WISE SELLING PRICE

category_selling_price = df.groupby("Category")["Selling_Price"].agg(
    ["mean", "min", "max"]
).round(2)

print("\n--- CATEGORY WISE SELLING PRICE ---")
print(category_selling_price)

# STEP 13 - STOCK ANALYSIS

print("\n--- STOCK ANALYSIS ---")

print("Average Stock:", round(df["Stock"].mean(), 2))
print("Minimum Stock:", df["Stock"].min())
print("Maximum Stock:", df["Stock"].max())

print("\n--- TOP 10 PRODUCTS WITH HIGHEST STOCK ---")

top_stock = df.sort_values(
    by="Stock",
    ascending=False
).head(10)

print(top_stock[
    ["Product_Name", "Category", "Stock", "Price", "Selling_Price"]
])

# STEP 14 - CATEGORY WISE STOCK ANALYSIS

category_stock = df.groupby("Category")["Stock"].agg(
    ["mean", "min", "max"]
).round(2)

print("\n--- CATEGORY WISE STOCK ---")
print(category_stock)

# STEP 15 - DISCOUNT VS SELLING PRICE

df["Discount_Amount"] = df["Price"] - df["Selling_Price"]

print("\n--- DISCOUNT AMOUNT ANALYSIS ---")

print("Average Discount Amount:",
      round(df["Discount_Amount"].mean(), 2))

print("Maximum Discount Amount:",
      round(df["Discount_Amount"].max(), 2))

print("\n--- TOP 10 PRODUCTS BY DISCOUNT AMOUNT ---")

top_discount_amount = df.sort_values(
    by="Discount_Amount",
    ascending=False
).head(10)

print(top_discount_amount[
    ["Product_Name", "Category", "Price",
     "Discount_Percent", "Discount_Amount", "Selling_Price"]
])

# STEP 16 - CORRELATION ANALYSIS

print("\n--- CORRELATION ANALYSIS ---")

correlation = df[
    ["Price", "Discount_Percent", "Rating",
     "Review_Count", "Stock", "Selling_Price"]
].corr().round(2)

print(correlation)

# STEP 17 - RATING VS REVIEW COUNT

plt.figure(figsize=(10, 6))

plt.scatter(df["Rating"], df["Review_Count"])

plt.title("Rating vs Review Count")
plt.xlabel("Rating")
plt.ylabel("Review Count")

plt.tight_layout()
plt.show()


# STEP 18 - CATEGORY WISE AVERAGE RATING

category_rating = df.groupby("Category")["Rating"].mean()

plt.figure(figsize=(10, 6))

category_rating.plot(kind="bar")

plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# STEP 19 - CATEGORY WISE REVIEW COUNT

category_reviews = df.groupby("Category")["Review_Count"].sum()

plt.figure(figsize=(10, 6))

category_reviews.plot(kind="bar")

plt.title("Total Reviews by Category")
plt.xlabel("Category")
plt.ylabel("Total Review Count")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# STEP 20 - CATEGORY WISE AVERAGE SELLING PRICE

category_selling = df.groupby("Category")["Selling_Price"].mean()

plt.figure(figsize=(10, 6))

category_selling.plot(kind="bar")

plt.title("Average Selling Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Selling Price")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# STEP 21 - TOP 10 PRODUCTS BY SELLING PRICE

top_selling = df.sort_values(
    by="Selling_Price",
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY SELLING PRICE ---")

print(top_selling[
    ["Product_Name", "Category", "Brand",
     "Price", "Discount_Percent", "Selling_Price"]
])

# STEP 22 - TOP 10 PRODUCTS BY REVIEW COUNT

top_reviews = df.sort_values(
    by="Review_Count",
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY REVIEW COUNT ---")

print(top_reviews[
    ["Product_Name", "Category", "Brand",
     "Rating", "Review_Count", "Selling_Price"]
])

# STEP 23 - BEST PERFORMING PRODUCTS

best_products = df[
    (df["Rating"] >= 4.5) &
    (df["Review_Count"] >= 2000)
].sort_values(
    by="Review_Count",
    ascending=False
)

print("\n--- BEST PERFORMING PRODUCTS ---")

print(best_products[
    ["Product_Name", "Category", "Brand",
     "Rating", "Review_Count", "Selling_Price"]
].head(10))

# STEP 24 - LOW STOCK PRODUCTS

low_stock = df.sort_values(
    by="Stock",
    ascending=True
).head(10)

print("\n--- LOW STOCK PRODUCTS ---")

print(low_stock[
    ["Product_Name", "Category", "Brand",
     "Stock", "Price", "Selling_Price"]
])

# STEP 25 - HIGH STOCK PRODUCTS

high_stock = df.sort_values(
    by="Stock",
    ascending=False
).head(10)

print("\n--- HIGH STOCK PRODUCTS ---")

print(high_stock[
    ["Product_Name", "Category", "Brand",
     "Stock", "Price", "Selling_Price"]
])

# STEP 26 - PRICE VS SELLING PRICE

plt.figure(figsize=(10, 6))

plt.scatter(df["Price"], df["Selling_Price"])

plt.title("Price vs Selling Price")
plt.xlabel("Original Price")
plt.ylabel("Selling Price")

plt.tight_layout()
plt.show()

# STEP 27 - CATEGORY WISE DISCOUNT ANALYSIS

category_discount = df.groupby("Category")["Discount_Percent"].agg(
    ["mean", "min", "max"]
).round(2)

print("\n--- CATEGORY WISE DISCOUNT ---")
print(category_discount)

# STEP 28 - CATEGORY WISE AVERAGE REVIEW COUNT

category_avg_reviews = df.groupby("Category")["Review_Count"].mean().round(2)

print("\n--- CATEGORY WISE AVERAGE REVIEW COUNT ---")
print(category_avg_reviews)

# STEP 29 - BRAND WISE PRODUCT COUNT

brand_count = df["Brand"].value_counts().head(10)

print("\n--- TOP 10 BRANDS BY PRODUCT COUNT ---")
print(brand_count)

# STEP 30 - BRAND WISE AVERAGE RATING

brand_rating = df.groupby("Brand")["Rating"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- TOP 10 BRANDS BY AVERAGE RATING ---")
print(brand_rating.head(10))

# STEP 31 - BRAND WISE TOTAL REVIEWS

brand_reviews = df.groupby("Brand")["Review_Count"].sum().sort_values(
    ascending=False
)

print("\n--- TOP 10 BRANDS BY TOTAL REVIEWS ---")
print(brand_reviews.head(10))

# STEP 32 - BRAND WISE AVERAGE SELLING PRICE

brand_selling_price = df.groupby("Brand")["Selling_Price"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- TOP 10 BRANDS BY AVERAGE SELLING PRICE ---")
print(brand_selling_price.head(10))

# STEP 33 - BRAND WISE AVERAGE DISCOUNT

brand_discount = df.groupby("Brand")["Discount_Percent"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- TOP 10 BRANDS BY AVERAGE DISCOUNT ---")
print(brand_discount.head(10))

# STEP 34 - SUB-CATEGORY ANALYSIS

subcategory_analysis = df.groupby("Sub_Category").agg(
    Product_Count=("Product_ID", "count"),
    Average_Price=("Price", "mean"),
    Average_Rating=("Rating", "mean"),
    Total_Reviews=("Review_Count", "sum")
).round(2)

print("\n--- SUB-CATEGORY ANALYSIS ---")
print(subcategory_analysis)

# STEP 35 - TOP SUB-CATEGORIES BY PRODUCT COUNT

subcategory_count = df["Sub_Category"].value_counts().head(10)

print("\n--- TOP 10 SUB-CATEGORIES BY PRODUCT COUNT ---")
print(subcategory_count)

# STEP 36 - SUB-CATEGORY WISE AVERAGE RATING

subcategory_rating = df.groupby("Sub_Category")["Rating"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- TOP 10 SUB-CATEGORIES BY AVERAGE RATING ---")
print(subcategory_rating.head(10))

# STEP 37 - SUB-CATEGORY WISE TOTAL REVIEWS

subcategory_reviews = df.groupby("Sub_Category")["Review_Count"].sum().sort_values(
    ascending=False
)

print("\n--- TOP 10 SUB-CATEGORIES BY TOTAL REVIEWS ---")
print(subcategory_reviews.head(10))

# STEP 38 - SUB-CATEGORY WISE AVERAGE SELLING PRICE

subcategory_selling = df.groupby("Sub_Category")["Selling_Price"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- TOP 10 SUB-CATEGORIES BY AVERAGE SELLING PRICE ---")
print(subcategory_selling.head(10))

# STEP 39 - SUB-CATEGORY WISE AVERAGE DISCOUNT

subcategory_discount = df.groupby("Sub_Category")["Discount_Percent"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- TOP 10 SUB-CATEGORIES BY AVERAGE DISCOUNT ---")
print(subcategory_discount.head(10))

# STEP 40 - BEST VALUE PRODUCTS

best_value = df.sort_values(
    by="Discount_Percent",
    ascending=False
).copy()

best_value["Value_Score"] = (
    best_value["Rating"] * best_value["Discount_Percent"]
)

best_value = best_value.sort_values(
    by="Value_Score",
    ascending=False
).head(10)

print("\n--- TOP 10 BEST VALUE PRODUCTS ---")

print(best_value[
    ["Product_Name", "Category", "Rating",
     "Discount_Percent", "Selling_Price", "Value_Score"]
])


# STEP 41 - SALES POTENTIAL ANALYSIS

df["Sales_Potential"] = df["Selling_Price"] * df["Stock"]

top_sales_potential = df.sort_values(
    by="Sales_Potential",
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY SALES POTENTIAL ---")

print(top_sales_potential[
    ["Product_Name", "Category", "Selling_Price",
     "Stock", "Sales_Potential"]
])

# STEP 42 - CATEGORY WISE SALES POTENTIAL

category_sales = df.groupby("Category")["Sales_Potential"].sum().sort_values(
    ascending=False
).round(2)

print("\n--- CATEGORY WISE SALES POTENTIAL ---")
print(category_sales)


# STEP 43 - CATEGORY WISE SALES POTENTIAL CHART

category_sales = df.groupby("Category")["Sales_Potential"].sum()

plt.figure(figsize=(10, 6))

category_sales.plot(kind="bar")

plt.title("Sales Potential by Category")
plt.xlabel("Category")
plt.ylabel("Sales Potential")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# STEP 44 - CATEGORY WISE AVERAGE SALES POTENTIAL

category_avg_sales = df.groupby("Category")["Sales_Potential"].mean().sort_values(
    ascending=False
).round(2)

print("\n--- CATEGORY WISE AVERAGE SALES POTENTIAL ---")
print(category_avg_sales)

# STEP 45 - TOP 10 PRODUCTS BY SALES POTENTIAL

top_sales = df.sort_values(
    by="Sales_Potential",
    ascending=False
).head(10)

print("\n--- TOP 10 PRODUCTS BY SALES POTENTIAL ---")

print(top_sales[
    ["Product_Name", "Category",
     "Selling_Price", "Stock", "Sales_Potential"]
])

# STEP 46 - OVERALL PROJECT SUMMARY

print("\n--- E-COMMERCE PROJECT SUMMARY ---")

print("Total Products:", len(df))
print("Total Categories:", df["Category"].nunique())
print("Total Brands:", df["Brand"].nunique())

print("Average Price:", round(df["Price"].mean(), 2))
print("Average Selling Price:", round(df["Selling_Price"].mean(), 2))
print("Average Rating:", round(df["Rating"].mean(), 2))
print("Average Discount:", round(df["Discount_Percent"].mean(), 2))
print("Average Stock:", round(df["Stock"].mean(), 2))

print("\nHighest Rated Category:")
print(df.groupby("Category")["Rating"].mean().idxmax())

print("\nMost Reviewed Category:")
print(df.groupby("Category")["Review_Count"].sum().idxmax())

print("\nHighest Sales Potential Category:")
print(df.groupby("Category")["Sales_Potential"].sum().idxmax())


# STEP 47 - SAVE FINAL DATASET

df.to_csv("ecommerce_products_final.csv", index=False)

print("\nFinal dataset saved successfully!")
print("File: ecommerce_products_final.csv")

# STEP 48 - EXPORT ANALYSIS RESULTS

summary = df.describe().round(2)

summary.to_csv("ecommerce_analysis_summary.csv")

print("\nAnalysis summary exported successfully!")
print("File: ecommerce_analysis_summary.csv")




