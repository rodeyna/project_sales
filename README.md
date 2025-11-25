# 📈 Monthly Sales Analysis (NumPy + Pandas + Matplotlib + Seaborn)

## 📌 Project Description
This project focuses on generating, analyzing, and visualizing one year of simulated monthly sales data for four distinct products (A, B, C, D). [cite_start]It uses core Python data science libraries to compute key business metrics, identify performance trends, and extract actionable insights[cite: 4].

[cite_start]The primary objective is to generate, analyze, and visualize monthly sales data for four products over one year, and extract key business insights using NumPy, Pandas, Matplotlib, and Seaborn[cite: 4].

## 📂 Project Structure
[cite_start]The project files are organized as follows[cite: 6, 7]:

* [cite_start]`notebook.ipynb`: Main notebook containing all the steps for data analysis, metric calculation, and visualization[cite: 7].
* [cite_start]`utils.py`: Contains functions necessary for data generation[cite: 7].
* [cite_start]`data/initial.csv`: The raw generated dataset[cite: 7].
* [cite_start]`data/final.csv`: The DataFrame containing calculated metrics[cite: 7].
* [cite_start]`data/output.csv`: The final results, including computed pivot tables and summaries[cite: 7].
* `conclusions.txt`: A text file dedicated to answering the conclusion questions and outlining the strategic insights.
* `README.md`: This file.

## 🛠️ Requirements and Setup

[cite_start]This project requires standard Python data science libraries like `NumPy`, `Pandas`, `Matplotlib`, and `Seaborn`[cite: 2, 4].

1.  **Install Dependencies:**
    It is recommended to use a virtual environment. To install all necessary packages, run the following command, assuming a `requirements.txt` file exists:
    ```bash
    pip install -r requirements.txt
    ```

## 📊 Key Findings and Results
The analysis successfully calculated several key metrics, which are summarized in the final output files. [cite_start]The key insights identified are[cite: 38]:

* [cite_start]**Best Month (Highest Total Sales):** Identified [cite: 39]
* [cite_start]**Best Product (Highest Cumulative Annual Sales):** Identified [cite: 40]
* [cite_start]**Best Quarter (Highest Total Sales):** Identified [cite: 41]

## 📝 Conclusion and Strategy
The strategic answers to the conclusion questions and recommendations for improving the next year's sales strategy are provided in the **`conclusions.txt`** file.

## 📈 Visualizations
[cite_start]The project includes the following visualizations to present the data effectively[cite: 42]:

* [cite_start]Line chart for each product across months[cite: 43].
* [cite_start]Stacked bar chart of total monthly sales by product (annotating best month)[cite: 44].
* [cite_start]Seaborn heatmap: monthly sales of each product[cite: 45].
* [cite_start]Seaborn boxplot: distribution of sales per product[cite: 46].