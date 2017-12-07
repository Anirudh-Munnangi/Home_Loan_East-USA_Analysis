import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
plt.style.use('ggplot')
loans_df=pd.read_csv('C:\\Python_Scripts\\Cap_One\\hmda_lar.csv')

def by_sum_by_state():
	# By Sum
	plt.figure(1)
	# State Delaware
	filtered_df=loans_df[loans_df['state_names']=='Delaware']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['sum_loan_amount']).tolist()
	plt.plot(valsx,valsy,'b',label='DE')
	# State District of Columbia
	filtered_df=loans_df[loans_df['state_names']=='District of Columbia']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['sum_loan_amount']).tolist()
	plt.plot(valsx,valsy,'g',label='DC')
	# State of Virginia
	filtered_df=loans_df[loans_df['state_names']=='Virginia']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['sum_loan_amount']).tolist()
	plt.plot(valsx,valsy,'r',label='VA')
	# State of West Virginia
	filtered_df=loans_df[loans_df['state_names']=='West Virginia']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['sum_loan_amount']).tolist()
	plt.plot(valsx,valsy,'c',label='WV')
	# State of Maryland
	filtered_df=loans_df[loans_df['state_names']=='Maryland']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['sum_loan_amount']).tolist()
	plt.plot(valsx,valsy,'m',label='MD')
	# Plot properties
	ax=plt.gca()
	ax.ticklabel_format(style='plain')
	plt.xlabel('Years')
	plt.ylabel('Sum of Loans')
	plt.legend()
	plt.title('Yearly Market Variation: By Sum of Loan Amount')
	plt.show()


def by_count_by_state():
	# By Count
	loans_df=pd.read_csv('C:\\Python_Scripts\\Cap_One\\hmda_lar.csv')
	plt.figure(2)
	# State Delaware
	filtered_df=loans_df[loans_df['state_names']=='Delaware']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	plt.plot(valsx,valsy,'b',label='DE')
	# State District of Columbia
	filtered_df=loans_df[loans_df['state_names']=='District of Columbia']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	plt.plot(valsx,valsy,'g',label='DC')
	# State of Virginia
	filtered_df=loans_df[loans_df['state_names']=='Virginia']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	plt.plot(valsx,valsy,'r',label='VA')
	# State of West Virginia
	filtered_df=loans_df[loans_df['state_names']=='West Virginia']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	plt.plot(valsx,valsy,'c',label='WV')
	# State of Maryland
	filtered_df=loans_df[loans_df['state_names']=='Maryland']
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	plt.plot(valsx,valsy,'m',label='MD')
	# Plot properties
	ax=plt.gca()
	ax.ticklabel_format(style='plain')
	plt.xlabel('Years')
	plt.ylabel('Count of Loans')
	plt.legend()
	plt.title('Yearly Market Variation: By Count of Number of Loans')
	plt.show()


def by_homepurchase_by_state():
	# NEW PART
	loans_df=pd.read_csv('C:\\Python_Scripts\\Cap_One\\hmda_lar2.csv')
	plt.figure(3)
	# Filtering on loan purpose
	filtered_df=loans_df[loans_df['loan_purpose']=='Home purchase']
	# State Delaware
	df=filtered_df[filtered_df['state_names']=='Delaware']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'b',label='DE')
	# State District of Columbia
	df=filtered_df[filtered_df['state_names']=='District of Columbia']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'g',label='DC')
	# State of Virginia
	df=filtered_df[filtered_df['state_names']=='Virginia']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'r',label='VA')
	# State of West Virginia
	df=filtered_df[filtered_df['state_names']=='West Virginia']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'c',label='WV')
	# State of Maryland
	df=filtered_df[filtered_df['state_names']=='Maryland']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'m',label='MD')
	# Plot properties
	ax=plt.gca()
	ax.ticklabel_format(style='plain')
	plt.xlabel('Years')
	plt.ylabel('Count of Loans')
	plt.legend()
	plt.title('Home Purchase Market Variation: By Count of Number of Loans')
	plt.show()


def by_refinancing_by_state():
	plt.figure(4)
	loans_df=pd.read_csv('C:\\Python_Scripts\\Cap_One\\hmda_lar2.csv')
	# Filtering on loan purpose
	filtered_df=loans_df[loans_df['loan_purpose']=='Refinancing']
	# State Delaware
	df=filtered_df[filtered_df['state_names']=='Delaware']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'b',label='DE')
	# State District of Columbia
	df=filtered_df[filtered_df['state_names']=='District of Columbia']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'g',label='DC')
	# State of Virginia
	df=filtered_df[filtered_df['state_names']=='Virginia']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'r',label='VA')
	# State of West Virginia
	df=filtered_df[filtered_df['state_names']=='West Virginia']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'c',label='WV')
	# State of Maryland
	df=filtered_df[filtered_df['state_names']=='Maryland']
	valsx=(df['Year']).tolist()
	valsy=(df['count']).tolist()
	plt.plot(valsx,valsy,'m',label='MD')
	# Plot properties
	ax=plt.gca()
	ax.ticklabel_format(style='plain')
	plt.xlabel('Years')
	plt.ylabel('Count of Loans')
	plt.legend()
	plt.title('Refinancing Market Variation: By Count of Number of Loans')
	plt.show()


def by_loan_density():
	# Division with population graph
	loans_df=pd.read_csv('C:\\Python_Scripts\\Cap_One\\hmda_lar.csv')
	pop_df=pd.read_excel('C:\\Python_Scripts\\Cap_One\\Census.xlsx')
	plt.figure(5)
	# State Delaware
	filtered_df=loans_df[loans_df['state_names']=='Delaware']
	filtered_pop_df=(pop_df.iloc[[0]])
	val_pops=[]
	for i in range(0,9):
		val_pops.append(filtered_pop_df.iloc[0,i])
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	ploty=list((a/b for (a,b) in zip(valsy,val_pops)))
	plt.plot(valsx,ploty,'b',label='DE')
	# State District of Columbia
	filtered_df=loans_df[loans_df['state_names']=='District of Columbia']
	filtered_pop_df=(pop_df.iloc[[1]])
	val_pops=[]
	for i in range(0,9):
		val_pops.append(filtered_pop_df.iloc[0,i])
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	ploty=list((a/b for (a,b) in zip(valsy,val_pops)))
	plt.plot(valsx,ploty,'g',label='DC')
	# State of Virginia
	filtered_df=loans_df[loans_df['state_names']=='Virginia']
	filtered_pop_df=(pop_df.iloc[[2]])
	val_pops=[]
	for i in range(0,9):
		val_pops.append(filtered_pop_df.iloc[0,i])
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	ploty=list((a/b for (a,b) in zip(valsy,val_pops)))
	plt.plot(valsx,ploty,'r',label='VA')
	# State of West Virginia
	filtered_df=loans_df[loans_df['state_names']=='West Virginia']
	filtered_pop_df=(pop_df.iloc[[3]])
	val_pops=[]
	for i in range(0,9):
		val_pops.append(filtered_pop_df.iloc[0,i])
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	ploty=list((a/b for (a,b) in zip(valsy,val_pops)))
	plt.plot(valsx,ploty,'c',label='WV')
	# State of Maryland
	filtered_df=loans_df[loans_df['state_names']=='Maryland']
	filtered_pop_df=(pop_df.iloc[[4]])
	val_pops=[]
	for i in range(0,9):
		val_pops.append(filtered_pop_df.iloc[0,i])
	valsx=(filtered_df['Year']).tolist()
	valsy=(filtered_df['count']).tolist()
	ploty=list((a/b for (a,b) in zip(valsy,val_pops)))
	plt.plot(valsx,ploty,'m',label='MD')
	# Plot properties
	ax=plt.gca()
	ax.ticklabel_format(style='plain')
	plt.xlabel('Years')
	plt.ylabel('Loan Density Percentage')
	plt.legend()
	plt.title('Loan Density: By count of loans')
	plt.show()

def cagr_plot():
	loans_df=pd.read_csv('yearly loan values.csv')
	loan_vals=(loans_df['Loan_Amount_Sum_Total']).tolist()
	year_vals=(loans_df['Year']).tolist()
	cagr_val=-0.0459 # Expressed as percentage/100 and calculated by values from 2008 to 2014 i.e. 6 years
	predicted_2016=(loan_vals[-1])*(1+cagr_val)
	predicted_2017=predicted_2016*(1+cagr_val)
	predicted_2018=predicted_2017*(1+cagr_val)
	loan_vals.append(predicted_2016)
	loan_vals.append(predicted_2017)
	loan_vals.append(predicted_2018)
	year_vals.append(2016)
	year_vals.append(2017)
	year_vals.append(2018)
	plt.figure(6)
	ax=plt.gca()
	ax.ticklabel_format(style='plain')
	plt.plot(year_vals,loan_vals)
	plt.title('Predication of Market by Sum of loans per year')
	plt.xlabel('Year Values')
	plt.ylabel('Sum of Loan Amounts')
	plt.show()
	
def main():
	by_sum_by_state()
	by_count_by_state()
	by_homepurchase_by_state()
	by_refinancing_by_state()
	by_loan_density()
	cagr_plot()
	
if __name__=="__main__":
	main()