import pandas as pd
import plotly.express as px

df = pd.read_excel(
    "Library_Management_System-Dataset.xlsx",
    sheet_name="Books"
)
print(df.head())

# Create a histogram
fig1 = px.histogram(
    df,
    x="Total_Copies",
    title="Distribution of Total Book Copies",
    labels={"Total_Copies": "Total Copies"}
)
fig1.update_traces(
    xbins=dict(start=0, end=400, size=25)
)

fig1.update_layout(
    yaxis_title="Number of Books",
    bargap=0.05,
    xaxis=dict(
        rangeslider=dict(visible=True, thickness=0.12),
        dtick=50
    )
)
fig1.show()



# Scatter Plot
fig2 = px.scatter(
    df,
    x="Total_Copies",
    y="Issued_Copies",
    color="Category",
    title="Relationship Between Total Copies and Issued Copies",
    labels={
        "Total_Copies": "Total Copies",
        "Issued_Copies": "Issued Copies",
        "Category": "Book Category"
    },
    hover_data=["Category"]
)
fig2.update_layout(
    xaxis_title="Total Copies",
    yaxis_title="Issued Copies"
)
fig2.show()



# Box Plot
fig3 = px.box(
    df,
    x="Category",
    y="Issued_Copies",
    color="Category",
    title="Distribution of Issued Copies by Book Category",
    labels={
        "Category": "Book Category",
        "Issued_Copies": "Issued Copies"
    },
    points="outliers"
)
fig3.update_layout(
    xaxis_title="Book Category",
    yaxis_title="Issued Copies",
    showlegend=False
)
fig3.show()


# Violin Plot
fig4 = px.violin(
    df,
    x="Category",
    y="Total_Copies",
    color="Category",
    title="Distribution of Total Copies by Book Category",
    labels={
        "Category": "Book Category",
        "Total_Copies": "Total Copies"
    },
    box=True,
    points="outliers"
)
fig4.update_layout(
    xaxis_title="Book Category",
    yaxis_title="Total Copies",
    showlegend=False
)
fig4.show()
