import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(df, title, figsize=(18, 16), cmap='viridis'):
    """
    Generates and displays a heatmap of the correlation matrix for a given DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        title (str): The title for the correlation matrix plot.
        figsize (tuple): A tuple specifying the figure size (width, height).
        cmap (str): The colormap for the heatmap.
    """
    # Calculate the correlation matrix
    correlation_matrix = df.corr()

    # Create the heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(correlation_matrix, annot=False, cmap=cmap)
    plt.title(title, fontsize=20)
    plt.tight_layout()
    plt.show()

def load_data_from_github(url):
    """
    Loads a CSV file from a raw GitHub URL.

    Args:
        url (str): The raw GitHub URL to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    try:
        print(f"Loading data from: {url}")
        df = pd.read_csv(url)
        # Drop the 'Unnamed: 0' column if it exists
        if 'Unnamed: 0' in df.columns:
            df = df.drop('Unnamed: 0', axis=1)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data from {url}: {e}")
        return None

# --- Main script execution ---
if __name__ == "__main__":
    prices_url = "https://raw.githubusercontent.com/leofischer21/bonds/main/bonds/prices.csv"
    yields_url = "https://raw.githubusercontent.com/leofischer21/bonds/main/bonds/yields.csv"

    # Load both prices and yields data
    df_prices = load_data_from_github(prices_url)
    df_yields = load_data_from_github(yields_url)

    if df_prices is not None:
        # Plot the correlation matrix for prices
        plot_correlation_matrix(df_prices, "Correlation Matrix for prices.csv")

    if df_yields is not None:
        # Plot the correlation matrix for yields
        plot_correlation_matrix(df_yields, "Correlation Matrix for yields.csv")
