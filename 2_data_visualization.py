import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_dashboard(input_file):
    # Load and prep data
    df = pd.read_csv(input_file)
    df['first_air_date'] = pd.to_datetime(df['first_air_date'])
    df['year'] = df['first_air_date'].dt.year

    # Set visual style
    sns.set_theme(style='darkgrid')
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Top Rated TV Shows: Data Insights Dashboard', fontsize=24, fontweight='bold', y=0.98)

    # 1. Top 10 by Popularity
    top_10_pop = df.nlargest(10, 'popularity')
    sns.barplot(ax=axes[0, 0], x='popularity', y='name', data=top_10_pop, palette='viridis')
    axes[0, 0].set_title('Top 10 Most Popular Shows', fontsize=16)

    # 2. Rating Distribution
    sns.histplot(ax=axes[0, 1], x='vote_average', data=df, bins=30, kde=True, color='skyblue')
    axes[0, 1].set_title('Distribution of Vote Ratings', fontsize=16)

    # 3. Shows per Year
    yearly_counts = df.groupby('year').size().reset_index(name='count')
    sns.lineplot(ax=axes[1, 0], x='year', y='count', data=yearly_counts, color='salmon', linewidth=2)
    axes[1, 0].set_title('Content Growth Over Time (Shows Released)', fontsize=16)

    # 4. Popularity vs Rating
    sns.scatterplot(ax=axes[1, 1], x='vote_average', y='popularity', data=df, alpha=0.5, color='purple')
    axes[1, 1].set_title('Popularity vs. Rating Correlation', fontsize=16)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    output_img = 'tv_show_insights.png'
    plt.savefig(output_img, dpi=300)
    print(f"Dashboard saved as {output_img}")

if __name__ == "__main__":
    create_dashboard('top_rated_tv_cleaned.csv')
