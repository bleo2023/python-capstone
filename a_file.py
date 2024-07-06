import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Read CSV and filter data
    df = pd.read_csv('ViewingActivity.csv')
    df = df[df['Profile Name'] == 'B']

    # Drop unnecessary columns
    df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type',
                  'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

    if 'Duration' in df.columns:
        df['Duration'] = pd.to_timedelta(df['Duration'])

        # Group by 'Title' and aggregate total watch time or count of views
    most_watched = df.groupby('Title').size().sort_values(ascending=False)
    most_watched_show = most_watched.index[0]
    print(f"The most watched show is {most_watched_show}")
    # Filter by Title containing 'Roman Empire' and Duration > '0 days 00:01:00'
    roman_empire = df[df['Title'].str.contains('One Piece', regex=False)]
    roman_empire = roman_empire[(roman_empire['Duration'] > '0 days 00:01:00')]

    # Ensure 'Start Time' is datetime format
    roman_empire['Start Time'] = pd.to_datetime(roman_empire['Start Time'])

    # Calculate weekday and hour using .dt.weekday and .dt.hour
    roman_empire['weekday'] = roman_empire['Start Time'].dt.weekday
    roman_empire['hour'] = roman_empire['Start Time'].dt.hour

    # Count occurrences by hour
    roman_empire['hour'] = pd.Categorical(roman_empire['hour'], categories=
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                                    ordered=True)
    roman_empire_by_hour = roman_empire['hour'].value_counts()
    roman_empire_by_hour = roman_empire_by_hour.sort_index()

    # Plot as a bar chart
    plt.figure(figsize=(20, 10))
    roman_empire_by_hour.plot(kind='bar', title='Roman Empire Episodes Watched by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    main()

