from config import llm


def recommend_assets(state):

    allocation = state["allocation"]

    prompt = f"""
Role:
You are an investment research assistant specializing in low-cost,
diversified ETFs.

Your job is to map the target asset allocation to suitable ETF options.

Target Asset Allocation:
{allocation}

Task:

For each asset category:

1. Recommend one or two suitable low-cost ETFs.
2. Include the ETF ticker and fund name.
3. Briefly explain what the ETF provides.
4. Mention the approximate expense ratio when known.
5. Keep recommendations diversified.
6. Do not recommend individual stocks.

Output:

Return a simple table with:

- Asset Category
- Target Allocation
- ETF
- Fund Name
- Expense Ratio
- Reason

Keep the response concise and educational.

Do not present ETF choices as guaranteed or as personalized financial advice.
"""

    result = llm.invoke(prompt)

    state["recommendations"] = result.content

    return state