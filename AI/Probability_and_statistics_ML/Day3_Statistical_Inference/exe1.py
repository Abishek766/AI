import numpy as np
from scipy.stats import norm

#Generate random sample data
data = np.random.normal(loc=50,scale=10,size=100)

#Sample Statistics
mean = np.mean(data)
std  = np.std(data, ddof=1)
n=len(data)

#95% Confidence Interval
z_value=norm.ppf(0.95)
margin_of_error = z_value *(std/np.sqrt(n))
ci=(mean - margin_of_error,mean + margin_of_error)

print("Sample mean: ",mean)
print("95% Confidence Interval ",ci)

# Absolutely! Let's break down this line both **programmatically** and **mathematically**:

# ---

# ### 🧾 Code:

# ```python
# from scipy.stats import norm
# z_value = norm.ppf(0.95)
# ```

# This line is using **SciPy's `norm` distribution** to get the **z-score** for a **95% probability**.

# ---

# ### 📌 What does it do?

# The function `norm.ppf(0.95)` gives you the **z-score** (also called a *quantile* or *percent-point*) such that the **area under the standard normal curve to the left of it is 95%**.

# In simple words:

# > "**What z-value (standard deviation) corresponds to 95% of the data being below it on the normal distribution?**"

# ---

# ### 🔢 The Result:

# ```python
# z_value = norm.ppf(0.95)
# # Output ≈ 1.6449
# ```

# This means:

# > On a **standard normal distribution** (mean = 0, standard deviation = 1), about **95%** of values lie **below** **z = 1.6449**.

# ---

# ### 📐 Mathematically:

# Let $Z \sim N(0, 1)$ (a standard normal distribution).
# You're solving this:

# $$
# P(Z \leq z) = 0.95
# $$

# You are finding the value of $z$ such that the **cumulative probability** (area under the curve) is 0.95.

# This is the **inverse of the CDF (Cumulative Distribution Function)**:

# $$
# z = \Phi^{-1}(0.95)
# $$

# Where:

# * $\Phi(z)$ is the CDF of the standard normal distribution.
# * $\Phi^{-1}(p)$ is the inverse CDF, also called the **percent-point function (PPF)**.

# So, `norm.ppf(0.95)` ≈ **1.6449**

# ---

# ### 📊 Visualization:

# If you imagine the bell curve of a standard normal distribution:

# ```
# <--------|--------------|----------------|-------->
#         -1.96           0               1.6449

# Area to the left of 1.6449 ≈ 95%
# ```

# ---

# ### 🔁 Common Use Case:

# In statistics, we use this when constructing **confidence intervals**:

# * For a **one-tailed 95% confidence level**, the critical z-value is **1.6449**.
# * For a **two-tailed 95% confidence level**, you’d use $\pm 1.96$.

# ---

# Let me know if you'd like to see how this applies to confidence intervals or hypothesis testing!


# Great question!

# ### ✅ Why do we use `ppf` (Percent-Point Function)?

# We use **`ppf`** to find **threshold values (quantiles)** in a probability distribution.

# ---

# ### 🔁 Short Answer:

# > We use `ppf` to **find the value of a variable (like z or x)** such that the **probability of getting a value less than or equal to it is a given number** (like 0.95).

# This is the **inverse** of the **CDF**.

# ---

# ### 📌 More Clearly:

# #### - `CDF` (Cumulative Distribution Function):

# * Input: a value $x$
# * Output: probability that a random variable is **≤ x**
# * Example: `norm.cdf(1.64)` → returns \~0.95
#   → "There's a 95% chance a value is ≤ 1.64"

# #### - `PPF` (Percent-Point Function):

# * Input: a probability (like 0.95)
# * Output: the value $x$ such that **P(X ≤ x) = 0.95**
# * Example: `norm.ppf(0.95)` → returns \~1.64
#   → "What value cuts off the lowest 95% of data?"

# ---

# ### 🧠 Real-Life Use Cases of `ppf`:

# 1. **Confidence Intervals**

#    * To build a 95% confidence interval, you need the z-value where 95% of the data lies below it.
#    * → Use `ppf(0.975)` for two-tailed test (since each tail has 2.5%)

# 2. **Hypothesis Testing**

#    * To find the **critical value** at a given significance level (e.g. 5%)
#    * Use `ppf(1 - 0.05)` for one-tailed test → gives you critical z

# 3. **Simulation or Sampling**

#    * You generate uniform random numbers between 0 and 1, then use `ppf` to transform them into values that follow a **target distribution** (like normal, exponential, etc.)

# ---

# ### ✍️ In summary:

# | Function | You give...       | You get...                                | Use for...                       |
# | -------- | ----------------- | ----------------------------------------- | -------------------------------- |
# | `cdf(x)` | a value $x$       | the probability $P(X \leq x)$             | "How likely is a value below x?" |
# | `ppf(p)` | a probability $p$ | the value $x$ such that $P(X \leq x) = p$ | "What x gives this probability?" |

# So we use `ppf` whenever we want to **go from probability → value**, especially in statistical calculations like **confidence intervals**, **critical regions**, or **sampling**.

# Let me know if you want a visual or code example!

