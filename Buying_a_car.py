''''Let us begin with an example:

A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car until he can buy the secondhand one.

He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.

Can you help him?

How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?'''



def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    month, saving_money = 0, 0
    price_old = startPriceOld
    price_new = startPriceNew
    available = saving_money + price_old - price_new
    result = []
    while available < 0:
        month += 1
        if month % 2 == 0:
            percentLossByMonth += 0.5
        saving_money += savingperMonth
        price_old -= (price_old * percentLossByMonth/100)
        price_new -= (price_new * percentLossByMonth/100)
        available = saving_money + price_old - price_new
    result.append(month)
    result.append(int(available))
    return result


print(nbMonths(12000, 8000, 1000, 1.5))



