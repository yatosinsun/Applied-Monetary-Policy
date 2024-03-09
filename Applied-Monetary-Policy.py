
# 3. COURSECON International Summer Seminars - 2023 July & August

# Genç Ekonomistler Kulübü

# Lecture: Dr. Şencan Felek / Pamukkale University

# Create (Applied) : Yasin Tosun / Siegen University 

##############################################################
## APPLIED PROBLEM SETS OF MONETARY POLICY (MINI SETS)
##############################################################

#################################################
# A. Balance of Payments Equilibrium
#################################################

"""
Balance of Payments Equilibrium, a
     inflows (resources) to outflows in the country's foreign economic relations
     It refers to the situation where (uses) are equal. In this case, a country
     current account balance, capital account, financial account and net error and
     The total of the deficiencies account becomes zero.
"""
import matplotlib.pyplot as plt
# Balance of payments components
current_account_balance = 100 # Current account balance
capital_account = -80 # Capital account
financial_account = -20 # Financial account
net_error_omissions = 0 # Net errors and omissions calculation

current_account_dengesi = abs(current_account_balance) # Converting negative value to positive
capital_account = abs(capital_account)
financial_account = abs(financial_account)
net_error_deficiencies = abs(net_error_deficiencies)

# sum of components
total = current_account_balance + capital_account + financial_account + net_error_deficiencies
# Plot the chart
labels = ['Current Account', 'Capital Account', 'Financial Account', 'Net Errors and Omissions']
sizes = [current_account_balance, capital_account, financial_account, net_error_deficiencies]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Balance of Payments Components')
plt.show()
# Balance control
if total == 0:
     print("Balance of Payments is at Equilibrium.")
else:
     print("Balance of Payments is not at Balance Point.")

"""
In this example, the balance of payments components are the current account balance,
     capital account, financial account and net errors and omissions account
     A pie chart is created using the data. your chart
     Shows fractions as percentage values.
    
Then, the sum of the components is calculated and determined whether the sum is zero or not.
     It is checked whether there is If the total is zero, "Balance of Payments
     At Balance Point" message is printed; otherwise, "Balance of Payments
     Not at Balance Point" message is printed.
"""

#################################################
# B. Cross Rate & Cross Rate
#################################################

"""
Cross rate or cross rate is a third rate between two different currencies.
     It means the exchange rate calculated on the currency. This concept
     when there is no direct exchange rate between two currencies or
     A direct exchange rate for the currency desired to be traded
     It is used when it is not available.
"""

import numpy as np
import matplotlib.pyplot as plt
# Data
dates = ['01.01.2023', '02.01.2023', '03.01.2023', '04.01.2023', '05.01.2023']
usd_eur = [0.85, 0.84, 0.93, 0.78, 0.87] # USD/EUR exchange rate
usd_jpy = [110.0, 119.8, 109.7, 106.5, 112.3] # USD/JPY exchange rate
# Cross rate calculation
eur_jpy = [usd_jpy[i] / usd_eur[i] for i in range(len(usd_eur))]
# Plotting graphs
plt.plot(dates, eur_jpy)
plt.xlabel('Date')
plt.ylabel('EUR/JPY Cross Rate')
plt.title('EUR/JPY Cross Rate')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

"""
In this example, three lists named "dates", "usd_eur" and "usd_jpy"
     USD/EUR and USD/JPY exchange rates are represented using Cross
     To calculate rate, USD/JPY exchange rate USD/EUR for each date
     divided by the exchange rate (usd_jpy / usd_eur). Finally, the EUR/JPY cross
     A graph representing rate values is drawn.
"""

import numpy as np
import matplotlib.pyplot as plt
# Data
dates = ['01.01.2023', '02.01.2023', '03.01.2023', '04.01.2023', '05.01.2023']
market_1_price = [10, 11, 12, 11.5, 12.5] # Asset price in market 1
market_2_price = [9, 10.5, 11, 12, 13] # Asset price in market 2
# Arbitrage profit calculation
arbitrage_profit = [market_1_price[i] - market_2_price[i] for i in range(len(market_1_price))]
# Plotting graphs
plt.plot(dates, arbitrage_profit)
plt.xlabel('Date')
plt.ylabel('Arbitrage Profit')
plt.title('Arbitrage Profit')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#################################################
# C. Floating Arrangements (Free Exchange Rate Regime)
#################################################

"""
In international economics, "Floating Arrangements" (Free Exchange Rate Regime) is a
     the country's currency according to supply and demand under free market conditions
     a currency that allows it to fluctuate above a set exchange rate
     is the dry regime. In this regime, the central bank generally does not intervene
     and exchange rates are formed under free market conditions. Below, hypothetical
     free market exchange rate of the Euro (EUR) against the US Dollar (USD)
     Here is an example code where conditions fluctuate:
"""

import numpy as np
import matplotlib.pyplot as plt
# Years and exchange rate data
years = np.arange(1, 11)
initial_exchange_rate = 1.1 # Initial rate
exchange_rate_change = np.random.normal(0, 0.1, size=len(years))
# Calculation of exchange rate data
exchange_rate = initial_exchange_rate + np.cumsum(exchange_rate_change)
# Graphic drawing
plt.plot(years, exchange_rate, color='blue', marker='o', linestyle='-', linewidth=2)
plt.xlabel('Years')
plt.ylabel('Exchange Rate (USD/EUR)')
plt.title('Floating Exchange Rate: EUR to USD')
plt.grid(True)
plt.show()

"""
In this example, the Euro against the US Dollar under free market conditions.
     It is assumed to fluctuate. We set the starting rate as 1.1
     and as the years progress, exchange rate changes follow a normal distribution.
     It occurs as . Exchange rate data corresponding to years in the chart
     is displayed.
"""

#################################################
# D. Managed Floating
#################################################

"""
In international economics, "Managed Floating" is a
     The exchange rate of the country's currency is subject to a certain level of fluctuation
     It is an exchange rate regime in which it intervenes. In this regime, the central bank
     or the government controls the exchange rate through certain policies and interventions.
     tries to be effective. The central bank usually sets the exchange rate
     while trying to control market fluctuations
     also takes into account the conditions. Below, hypothetically, the Euro
     (EUR) exhibits managed volatility against the US Dollar (USD).
     There is sample code:
"""

import numpy as np
import matplotlib.pyplot as plt
# Years and exchange rate data
years = np.arange(1, 11)
initial_exchange_rate = 1.1 # Initial rate
target_exchange_rate = 1.3 # Target rate
exchange_rate_change = np.random.normal(0, 0.1, size=len(years))
# Targeted exchange rate and intervention factor
target_rate_diff = target_exchange_rate - initial_exchange_rate
intervention_factor = 0.2 # Intervention factor
# Calculation of exchange rate data
exchange_rate = initial_exchange_rate + np.cumsum(exchange_rate_change + target_rate_diff * intervention_factor)
# Graphic drawing
plt.plot(years, exchange_rate, color='blue', marker='o', linestyle='-', linewidth=2)
plt.axhline(y=target_exchange_rate, color='red', linestyle='--', linewidth=2, label='Target Rate')
plt.xlabel('Years')
plt.ylabel('Exchange Rate (USD/EUR)')
plt.title('Managed Floating: EUR to USD')
plt.legend()
plt.grid(True)
plt.show()


"""
In this example, the managed volatility of the Euro against the US Dollar
     is assumed to exhibit. We set the starting rate as 1.1 and
     As the years progress, exchange rate changes follow a normal distribution.
     It occurs as . In addition, the target exchange rate is determined and the intervention
     The impact on the exchange rate is adjusted using the factor. In the chart,
     Exchange rate data corresponding to years and the target exchange rate
     There is a line shown.
"""