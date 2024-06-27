# prompt: In above code can we have a grid of 2 coluns

import pandas as pd
import matplotlib.pyplot as plt
from seaborn import kdeplot

def create_distribution_plots(df, filename):
  """
  Loads a DataFrame, creates kdeplots for each column, and saves them to a single PDF document.

  Args:
      df (pd.DataFrame): The DataFrame to analyze.
      filename (str): The filename (including path) to save the PDF document.
  """
  num_cols = len(df.columns)
  num_rows = (num_cols + 1) // 2  # Calculate number of rows for 2 columns

  # Create a figure with subplots to avoid overplotting
  fig, axes = plt.subplots(nrows=num_rows, ncols=2, figsize=(15, num_rows * 3))  # Adjust figsize as needed

  # Iterate through columns and create kdeplots
  for i, col in enumerate(df.columns):
    row = i // 2
    col_num = i % 2
    kdeplot(df[col], shade=True, ax=axes[row, col_num])
    axes[row, col_num].set_title(col)
    axes[row, col_num].set_xlabel(col)
    axes[row, col_num].set_ylabel('Density')

  # Turn off any unused subplots
  if num_cols % 2 == 1:
    fig.delaxes(axes[num_rows - 1, 1])

  # Tight layout to prevent overlapping labels
  plt.tight_layout()

  # Save the figure as a PDF document
  plt.savefig(filename, bbox_inches='tight')

  # Close the figure to avoid memory leaks
  plt.close(fig)

# Load your DataFrame (replace with your loading method)
df = pd.read_csv('/content/sample_data/mnist_train_small.csv')  # Example, replace with your actual loading logic

# Create the distribution plots
create_distribution_plots(df[['6', '0', '0.1', '0.2', '0.3']].head(100), 'distribution_plots.pdf')

print(f'Distribution plots saved to: distribution_plots.pdf')

