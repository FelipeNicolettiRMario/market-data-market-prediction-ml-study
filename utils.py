from matplotlib import pyplot as plt
import yfinance as yf


def load_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date, interval="1wk")

        data.columns = data.columns.droplevel(0)
        data.columns = ["Close", "High", "Low", "Open", "Volume"]
        data.dropna(inplace=True)

        return data
    except Exception as e:
        print(f"Error loading data for {symbol}: {e}")
        return None


def add_labels(df):
    if df is None or df.empty:
        return None

    df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df.dropna(inplace=True)

    return df


def add_features(df):
    if df is None or df.empty:
        return None

    df["returns"] = df["Close"].pct_change()
    df["volatility"] = df["returns"].rolling(window=2).std()
    df["ma_4"] = df["Close"].rolling(window=4).mean()
    df["ma_12"] = df["Close"].rolling(window=12).mean()
    df["ma_ratio"] = df["ma_4"] / df["ma_12"]
    df.dropna(inplace=True)

    return df


def plot_cumulative_returns(
    data, real_column="cumulative_real_return", predicted_columns=None
):
    if predicted_columns is None:
        predicted_columns = []

    plt.figure(figsize=(14, 7))

    plt.plot(
        data.index, data[real_column], label="Cumulative Real Return", color="blue"
    )

    for column in predicted_columns:
        plt.plot(
            data.index,
            data[column],
            label=f"Cumulative Predicted Return ({column})",
            linestyle="--",
        )

    plt.title("Comparison of Cumulative Real Return vs Predicted Returns")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid()
    plt.show()


def split_data(X, y, split_ratio=0.7):

    split_index = int(len(X) * split_ratio)

    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    return X_train, X_test, y_train, y_test
