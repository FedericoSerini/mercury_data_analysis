import math
import pandas as pd

store = pd.read_csv('../data/cnn_result.csv', delimiter=';')
store.rename(columns={0: 'prediction', 1: 'test_label', 2: 'test_price'}, inplace=True)

money = 10000.0
money_BAH = 10000.0
maximum_money = 0
minimum_money = 10000
maximum_profit_percent = 0.0
maximum_lost_percent = 0.0
maximum_gain = 0.0
maximum_lost = 0.0
total_gain = 0.0
success_transaction_count = 0
failed_transaction_count = 0
total_transaction_length = 0
transaction_count = 0
total_percent_profit = 0.0
data = []
daily_profit = [0.0] * (len(store)-1)
counter = 0

print("Start Capital: $" + str(money))

while counter < len(store):
    elem = store.iloc[counter]

    if elem.prediction == 1:
        buy_point = float(elem.test_price)
        buy_point = buy_point * 100
        share_number = (money - 1.0) / buy_point
        force_sell = False

        for j in range(counter, len(store) - 1, 1):
            elem2 = store.iloc[j]
            sell_point = float(elem2.test_price)
            sell_point = sell_point * 100
            money_temp = (share_number * sell_point) - 1.0

            if elem2.prediction == 2 | force_sell:
                sell_point = float(elem2.test_price)
                sell_point = sell_point * 100
                gain = sell_point - buy_point
                if gain > 0:
                    success_transaction_count += 1
                else:
                    failed_transaction_count += 1

                if gain >= maximum_gain:
                    maximum_gain = gain
                    maximum_profit_percent = maximum_gain / buy_point * 100

                if gain <= maximum_lost:
                    maximum_lost = gain
                    maximum_lost_percent = maximum_lost / buy_point * 100

                money_temp = (share_number * sell_point) - 1.0
                money = money_temp
                if money > maximum_money:
                    maximum_money = money

                if money < minimum_money:
                    minimum_money = money

                transaction_count += 1

                prof = gain * share_number / (money - (gain * share_number))
                number_of_day = j - counter
                one_day_prof = prof / number_of_day

                m = counter + 1
                while m <= j:
                    daily_profit[m] = one_day_prof
                    m += 1

                total_percent_profit = total_percent_profit + (gain / buy_point)

                total_transaction_length = total_transaction_length + (j - counter)
                counter = j + 1

                totalGain = total_gain + gain
                break
    counter += 1



def sharpe_ratio(daily_profit):

    summ = 0
    sd = 0

    for i in range(0, len(daily_profit), 1):
        summ = summ + daily_profit[i]

    print("sum is : " + str(summ))
    average = summ / len(daily_profit)
    print("Average value is : " + str(average))

    for i in range(0, len(daily_profit), 1):
        sd += ((daily_profit[i] - average) * (daily_profit[i] - average)) / len(daily_profit)

    standard_deviation = math.sqrt(sd)
    print("standardDeviation is : " + str(standard_deviation))

    sharpe_ratio_val = average / standard_deviation

    return sharpe_ratio_val

sharpaR = sharpe_ratio(daily_profit)

print("Sharpa Ratio of Our System=>" + str(sharpaR))

print("Our System => totalMoney = $" + str(money))


buy_point_BAH = store.loc[0].test_price
share_number_BAH = (money_BAH - 1.0) / buy_point_BAH
money_BAH = store.loc[len(store) - 1][2] * share_number_BAH - 1.0

print("BAH => totalMoney = $" + str(money_BAH))


number_of_days = len(store) - 1
number_of_years = number_of_days / 365


print("Our System Annualized return % => " + str(((math.exp(math.log(money/10000.0)/number_of_years)-1)*100))+"%")  # 5 years 0.2
print("BaH Annualized return % => " + str(((math.exp(math.log(money_BAH/10000.0)/number_of_years)-1)*100))+"%")
print("Annualized number of transaction => " + str(transaction_count) + "#")
print("Percent success of transaction => " + str((success_transaction_count / transaction_count) * 100) + "%")
print("Average percent profit per transaction => " + str((total_percent_profit / transaction_count) * 100) + "%")
print("Average transaction length => " + str(total_transaction_length / transaction_count) + "#")
print("Maximum profit percent in transaction=> " + str(maximum_profit_percent) + "%")
print("Maximum loss percent in transaction=> " + str(maximum_lost_percent) + "%")
print("Maximum capital value=> " + "$" + str(maximum_money))
print("Minimum capital value=> " + "$" + str(minimum_money))
print("Idle Ratio %=>  " + str((len(store) - total_transaction_length) / len(store) * 100) + "%")