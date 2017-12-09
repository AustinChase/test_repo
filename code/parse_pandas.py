import pandas as pd

def pandas_csv():
    df = pd.read_csv("source_data_v2.csv", delimiter = ',')
    return df

    #import raw csv data into a pandas data series with first two rows as headers
def get_enrollment():
    print df[['Q63_1','Q63_2','Q63_3','Q63_4','Q63_6']].mean(skipna=True)
    #count self funded plans, and group them by size
def get_self_funded():
    print df['Q11_6'].apply(lambda x: x == 1 or x == 2).sum() / 58.0
    print df['Q11_7'] = df['Q11_6'].apply(lambda x: x == 1 or x == 2)
    print df.groupby(['Q4'])['Q11_7'].sum() / df.groupby(['Q4'])['Q4'].count()
    #count distribution of employees by state, graph the result in a bar chart
def get_enrollment_distribution():
    df2 = df.iloc[ :, 11:63].count() / 58.0
    n_groups = df2.count()
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.50
    rects1 = ax.bar(index, df2, bar_width, color = 'b')
    ax.set_xlabel('State')
    ax.set_ylabel('percentage')
    ax.set_title('percentage of firms with employees in the following states')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(df2.iloc[:,0])
    ax.legend()
    fig.tight_lagout()
    plt.show()    

    