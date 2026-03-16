//+------------------------------------------------------------------+
//| Script by D.S.                                                  |
//| Fractal indicator based on the trading strategy                 |
//| of Golden Cross and Death Cross                                |
//+------------------------------------------------------------------+

input period_short = 12; // Short-term moving average period
input period_long = 26; // Long-term moving average period
input price = close;    // Close prices are used by default

void OnTick()
{
    int shortMA = 0, longMA = 0;

    // Calculate the SMA for the short and long periods
    for (int i = 0; i < period_short; ++i)
        shortMA += Price(symbol(), timeframe(), i, PERIOD_CURRENT);
    for (int i = 0; i < period_long; ++i)
        longMA += Price(symbol(), timeframe(), i, PERIOD_CURRENT);

    // Divide the moving average values by their respective periods to get the averages
    shortMA /= period_short;
    longMA /= period_long;

    // Compare the two moving averages and print the result
    if (Price(symbol(), timeframe(), 0, PERIOD_CURRENT) < shortMA && Price(symbol(), timeframe(), 0, PERIOD_CURRENT) > longMA)
        Print("Golden Cross detected!");
    else if (Price(symbol(), timeframe(), 0, PERIOD_CURRENT) > shortMA && Price(symbol(), timeframe(), 0, PERIOD_CURRENT) < longMA)
        Print("Death Cross detected!");
}
