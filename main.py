import platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression


plt.close("all")
data = pd.read_csv("House_Info.csv")
data = data.reset_index()
data['Closing_Date'] = data['Closing_Date'].astype('datetime64[ns]')

def Menu():
    userInput = input("\n"
                      "\n"
                      "\nMain Menu: "
                      "\n(Please Type Your Selection and Hit Enter)"
                      "\n"
                      "\n1:\t\tMenu Selection Item Placeholder"
                      "\n2:\t\tMenu Selection Item Placeholder"
                      "\nE:\t\tExit the Program"
                      "\n"
                      "\n")

    if userInput.lower() == "1":
        MenuSelectionOne()
    if userInput.lower() == "2":
        MenuSelectionTwo()
    elif userInput.lower() == "exit" or userInput.lower() == "e":
        print("\nExiting")
        exit()
    else:
        print("\n" + userInput + " is an invalid input...Please reselect...\n")
        Menu()

def MenuSelectionOne():

    X = data.Closing_Year
    X = sm.add_constant(X)  # Add a constant term to the independent variable
    y = data.Sold_Price - data.List_Price

    model = sm.OLS(y, X)
    results = model.fit()
    #
    plt.scatter(data.Closing_Year, data.Sold_Price - data.List_Price, label='Data')
    plt.plot(data.Closing_Year, results.fittedvalues, 'r', label='Regression Line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.Closing_Year, y=data.Sold_Price - data.List_Price, mode='markers', name='Data'))
    fig.add_trace(go.Scatter(x=data.Closing_Year, y=results.fittedvalues, mode='lines', name='Regression Line'))
    fig.update_layout(title='House Sales', xaxis_title='Year', yaxis_title='Cost of House')
    fig.show()

    specific_x = 2300
    intercept = results.params[0]
    intercept_for_specific_x = intercept + results.params[1] * specific_x

    print(round(intercept_for_specific_x,2))

    fig1 = px.scatter(data, x="Closing_Date", y=data.Sold_Price - data.List_Price)
    fig1.update_layout(
    title="Listing and Closing Price Differentials",
    xaxis_title="Year",
    yaxis_title="Pricing Differential",
    paper_bgcolor="#fff",
    plot_bgcolor="#e3e3e3",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#000000"
        )
    )
    fig1.show()

    #print("\nYou selected #1.\n")
    #Menu()

def MenuSelectionTwo():
    # TODO: Program capabilities
    print("\nYou selected #2.\n")
    Menu()


def main():
    # print("Programmer:\t\t\t Zachary Zamiska")
    # print("Student Number:\t\t 003194341")
    # print("Email:\t\t\t\t zzamisk@wgu.edu")
    #
    # print("\nPython Version:\t\t " + platform.python_version())
    # print("Pandas Version:\t\t " + pd.__version__)

    #Menu()
    MenuSelectionOne()


if __name__ == "__main__":
    main()








