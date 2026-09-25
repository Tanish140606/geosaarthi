"""
GeoSaarthi - Member 2 (ML/Intelligence) - Day 1-2 Practice
=============================================================
GOAL: Get comfortable with the train -> predict -> evaluate loop
using XGBoost, BEFORE touching real Assam weather data.

We're using FAKE rainfall data here that mimics the structure
your real ERA5 data will eventually have:
    rainfall_t-1, rainfall_t-2, rainfall_t-3, temperature, humidity -> rainfall_t

Run this in Anaconda Prompt with:
    conda activate geosaarthi
    python member2_regression_practice.py
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb

# -------------------------------------------------------------
# STEP 1: Create fake historical weather data
# (In Week 1, Member 1 will hand you a REAL version of this
#  built from ERA5. For now we simulate it so you can practice.)
# -------------------------------------------------------------
np.random.seed(42)
n_samples = 500

# Simulate rainfall that has some memory (today depends a bit on
# yesterday) plus randomness - similar behavior to real rainfall.
rainfall = [10]
for _ in range(n_samples):
    next_val = max(0, rainfall[-1] * 0.6 + np.random.normal(15, 20))
    rainfall.append(next_val)

df = pd.DataFrame({"rainfall": rainfall})

# Create "lag features" - this is the CORE technique you'll reuse
# on real data. It reframes a time series as a supervised ML problem.
df["rainfall_t-1"] = df["rainfall"].shift(1)
df["rainfall_t-2"] = df["rainfall"].shift(2)
df["rainfall_t-3"] = df["rainfall"].shift(3)
df["temperature"] = 28 + np.random.normal(0, 3, len(df))
df["humidity"] = 70 + np.random.normal(0, 10, len(df))

df = df.dropna().reset_index(drop=True)

# -------------------------------------------------------------
# STEP 2: Split into features (X) and target (y)
# -------------------------------------------------------------
feature_cols = ["rainfall_t-1", "rainfall_t-2", "rainfall_t-3", "temperature", "humidity"]
X = df[feature_cols]
y = df["rainfall"]  # what we're trying to predict

# NOTE: for real time-series data later, you should NOT shuffle
# randomly - split chronologically instead (train on earlier dates,
# test on later ones). We use random split here just for practice.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------------------------------------
# STEP 3: Train the model
# -------------------------------------------------------------
model = xgb.XGBRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    random_state=42,
)
model.fit(X_train, y_train)

# -------------------------------------------------------------
# STEP 4: Predict and evaluate
# -------------------------------------------------------------
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)
print(f"MAE  (avg error in mm):        {mae:.2f}")
print(f"RMSE (penalizes big misses):   {rmse:.2f}")
print(f"R2   (0=bad fit, 1=perfect):   {r2:.3f}")

# -------------------------------------------------------------
# STEP 5: Which features mattered most?
# This is a preview of how you'll explain your model to evaluators.
# -------------------------------------------------------------
importance = pd.Series(model.feature_importances_, index=feature_cols)
importance = importance.sort_values(ascending=False)
print("\nFEATURE IMPORTANCE:")
print(importance)

# -------------------------------------------------------------
# STEP 6: THE WHAT-IF ENGINE, in miniature
# This tiny function is the seed of your Week 2 "what-if" feature.
# -------------------------------------------------------------
def what_if_rainfall_scenario(base_row: pd.Series, pct_change: float) -> float:
    """Given one row of features, bump rainfall inputs by pct_change
    and see what the model predicts. This is exactly the logic
    you'll expand into the real what-if engine later."""
    scenario_row = base_row.copy()
    for col in ["rainfall_t-1", "rainfall_t-2", "rainfall_t-3"]:
        scenario_row[col] = scenario_row[col] * (1 + pct_change)
    return model.predict(pd.DataFrame([scenario_row]))[0]

sample_row = X_test.iloc[0]
normal_pred = model.predict(pd.DataFrame([sample_row]))[0]
plus_20_pred = what_if_rainfall_scenario(sample_row, 0.20)

print("\nWHAT-IF DEMO:")
print(f"Normal scenario prediction:   {normal_pred:.1f} mm")
print(f"+20% rainfall scenario:       {plus_20_pred:.1f} mm")

print("\nDone. Next step: swap the fake `df` above for Member 1's real")
print("cleaned ERA5 dataset once it's ready, and re-run this same pipeline.")