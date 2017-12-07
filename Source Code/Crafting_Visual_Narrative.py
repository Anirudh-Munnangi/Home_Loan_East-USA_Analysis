import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive
#interactive(True)
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

# Defining Auxillary Functions

def replaceNA(x):
	na_values=['NA ', 'NA ', 'NA ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '', 'NA  ','NA   ','NA      ']
	#if x in na_values:
	if pd.isnull(x):
		return(-5)
	else:
		return(x)

def complete_parent_names(row):
	if row['Parent_Name_TS']=='':
		return(row['Respondent_Name_TS'])
	else:
		return(row['Parent_Name_TS'])
    
def find_share(x):
	return(float((float(x))/1321158.0))

def filter_app_income(combined_df):
	combined_df['Applicant_Income_000'] =combined_df['Applicant_Income_000'].apply(replaceNA)
	return(combined_df)

def displayed_stacked_chart_2(combined_df,title_head):
	# bucketing loan amount
	buckets=[0,100,250,500,1000,100000]
	bucket_names=['(0-100k)','(101-250k)','(251-500k)','(501-1000k)','(>1000k)']
	combined_df['loan_bucket']=pd.cut(combined_df['Loan_Amount_000'],buckets,labels=bucket_names)
	# bucketing applicant income
	buckets=[-10,0,10,25,50,100,250,10000]
	bucket_names=['NA','(0-10k)','(11-25k)','(25-50k)','(50-100k)','(100-250k)','(>250k)']
	combined_df['income']=pd.cut(combined_df['Applicant_Income_000'].astype(int),buckets,labels=bucket_names)
	# Grouping by first Loan Amount Second applicant income
	new_attribute=combined_df.groupby(['loan_bucket','income'])
	values=((new_attribute[['Applicant_Income_000']]).count()).values
	#print('\n\n',values,'\n\n')
	arranged_values=np.reshape(values,(5,7))
	#print('\n\n',arranged_values,'\n\n')
	#arranged_values=np.transpose(arranged_values)
	
	# create plot
	fig, ax = plt.subplots()
	index = np.arange(5)
	bar_width = 0.1
	opacity = 0.8
	
	#Plot 1
	rects1 = plt.bar(index, arranged_values[:,0], bar_width,alpha=opacity,color='b',label='Applicant_Income(NA)')
	#Plot 2
	rects2 = plt.bar(index+1*bar_width, arranged_values[:,1], bar_width,alpha=opacity,color='g',label='Applicant_Income(0-10k)')
	#Plot 3
	rects3 = plt.bar(index+2*bar_width, arranged_values[:,2], bar_width,alpha=opacity,color='r',label='Applicant_Income(10k-25k)')
	#Plot 4
	rects4 = plt.bar(index+3*bar_width, arranged_values[:,3], bar_width,alpha=opacity,color='c',label='Applicant_Income(25k-50k)')
	#Plot 5
	rects5 = plt.bar(index+4*bar_width, arranged_values[:,4], bar_width,alpha=opacity,color='m',label='Applicant_Income(50k-100k)')
	#Plot 6
	rects6 = plt.bar(index+5*bar_width, arranged_values[:,5], bar_width,alpha=opacity,color='y',label='Applicant_Income(100k-250k)')
	#Plot 7
	rects7 = plt.bar(index+6*bar_width, arranged_values[:,6], bar_width,alpha=opacity,color='k',label='Applicant_Income(>250k)')
	
	plt.ylabel('Number of Loans')
	plt.xlabel('Loan Amount Value Categories')
	plt.xticks(index + bar_width, ('(0-100k)','(101-250k)','(251-500k)','(501-1000k)','(>1000k)'))
	plt.title(title_head)
	plt.legend()
	plt.tight_layout()
	plt.show()

def loan_type_top_lenders(Top_Parents,combined_df):
	# Top lender Purchase vs Refinance
	con=[]
	fha=[]
	fsa=[]
	va=[]
	names=[]
	for val in ((Top_Parents['Parent_Name_TS']).tolist()):
		filtered_df=combined_df[combined_df['Parent_Name_TS']==val]
		names.append(val)
		con.append(len((filtered_df[filtered_df['Loan_Type_Description']=='Conventional']).index))
		fha.append(len((filtered_df[filtered_df['Loan_Type_Description']=='FHA insured']).index))
		fsa.append(len((filtered_df[filtered_df['Loan_Type_Description']=='FSA/RHS guaranteed']).index))
		va.append(len((filtered_df[filtered_df['Loan_Type_Description']=='VA guaranteed']).index))
	fig, ax = plt.subplots()
	index = np.arange(10)
	bar_width = 0.15
	opacity = 0.8
	#Plot 1
	rects1 = plt.barh(index, con, bar_width,alpha=opacity,color='b',label='Conventional')
	#Plot 2
	rects2 = plt.barh(index+1*bar_width, fha, bar_width,alpha=opacity,color='r',label='FHA insured')
	#Plot 3
	rects3 = plt.barh(index+2*bar_width, fsa, bar_width,alpha=opacity,color='g',label='FSA/RHS guaranteed')
	#Plot 2
	rects4 = plt.barh(index+3*bar_width, va, bar_width,alpha=opacity,color='y',label='VA guaranteed')
	
	for i, v in enumerate(va):
		plt.text(v, i+0.25, str(names[va.index(v)]), color='blue',fontweight='bold')
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Lender Name')
	plt.xlabel('Number of Loans')
	plt.title('Loan Type Descrition for Top Lenders')
	plt.legend()
	plt.tight_layout()
	plt.show()


	
def conforming_status_top_lenders(Top_Parents,combined_df):
	# Top lender Purchase vs Refinance
	pur=[]
	ref=[]
	names=[]
	for val in ((Top_Parents['Parent_Name_TS']).tolist()):
		filtered_df=combined_df[combined_df['Parent_Name_TS']==val]
		names.append(val)
		pur.append(len((filtered_df[filtered_df['Conforming_Status']=='Conforming']).index))
		ref.append(len((filtered_df[filtered_df['Conforming_Status']=='Jumbo']).index))
	fig, ax = plt.subplots()
	index = np.arange(10)
	bar_width = 0.35
	opacity = 0.8
	#Plot 1
	rects1 = plt.barh(index, pur, bar_width,alpha=opacity,color='b',label='Conforming')
	#Plot 2
	rects2 = plt.barh(index+1*bar_width, ref, bar_width,alpha=opacity,color='r',label='Jumbo')
	for i, v in enumerate(ref):
		plt.text(v, i+0.25, str(names[ref.index(v)]), color='blue',fontweight='bold')
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Lender Name')
	plt.xlabel('Number of Loans')
	plt.title('Conforming VS Jumbo for Top Lenders')
	plt.legend()
	plt.tight_layout()
	plt.show()

def conventional_conforming_yes_vs_no(Top_Parents,combined_df):
	# Top lender Purchase vs Refinance
	pur=[]
	ref=[]
	names=[]
	for val in ((Top_Parents['Parent_Name_TS']).tolist()):
		filtered_df=combined_df[combined_df['Parent_Name_TS']==val]
		names.append(val)
		pur.append(len((filtered_df[filtered_df['Conventional_Conforming_Flag']=='Y']).index))
		ref.append(len((filtered_df[filtered_df['Conventional_Conforming_Flag']=='N']).index))
	fig, ax = plt.subplots()
	index = np.arange(10)
	bar_width = 0.35
	opacity = 0.8
	#Plot 1
	rects1 = plt.barh(index, pur, bar_width,alpha=opacity,color='b',label='CC: YES')
	#Plot 2
	rects2 = plt.barh(index+1*bar_width, ref, bar_width,alpha=opacity,color='r',label='CC: NO')
	for i, v in enumerate(ref):
		plt.text(v, i+0.25, str(names[ref.index(v)]), color='blue',fontweight='bold')
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Lender Name')
	plt.xlabel('Number of Loans')
	plt.title('Conventional Conforming: Yes/No for Top Lenders')
	plt.legend()
	plt.tight_layout()
	plt.show()

def pur_vs_ref(Top_Parents,combined_df):
	# Top lender Purchase vs Refinance
	pur=[]
	ref=[]
	names=[]
	for val in ((Top_Parents['Parent_Name_TS']).tolist()):
		filtered_df=combined_df[combined_df['Parent_Name_TS']==val]
		names.append(val)
		pur.append(len((filtered_df[filtered_df['Loan_Purpose_Description']=='Purchase']).index))
		ref.append(len((filtered_df[filtered_df['Loan_Purpose_Description']=='Refinance']).index))
	fig, ax = plt.subplots()
	index = np.arange(10)
	bar_width = 0.35
	opacity = 0.8
	#Plot 1
	rects1 = plt.barh(index, pur, bar_width,alpha=opacity,color='b',label='Purchase')
	#Plot 2
	rects2 = plt.barh(index+1*bar_width, ref, bar_width,alpha=opacity,color='r',label='Refinance')
	for i, v in enumerate(ref):
		if i==0:
			plt.text(v-9000, i+0.25, str(names[ref.index(v)]), color='blue',fontweight='bold')
		else:
			plt.text(v, i+0.25, str(names[ref.index(v)]), color='blue',fontweight='bold')
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Lender Name')
	plt.xlabel('Number of Loans')
	plt.title('Purchasing Vs Refinancing for Top Lenders')
	plt.legend()
	plt.tight_layout()
	plt.show()
	
def hindex(combined_df):
	# H index
	total_loans=len(combined_df.index)
	unique_lenders=set((combined_df['Parent_Name_TS']).tolist())
	hind=0.0
	for val in unique_lenders:
		hval=float((len((combined_df[combined_df['Parent_Name_TS']==val]).index))/(1321158.0))
		to_add=((hval*100)**2)
		hind+=to_add
	print(hind)

def hindex_ret(combined_df):
	# H index
	total_loans=len(combined_df.index)
	unique_lenders=set((combined_df['Parent_Name_TS']).tolist())
	hind=0.0
	for val in unique_lenders:
		hval=float((len((combined_df[combined_df['Parent_Name_TS']==val]).index))/(len(combined_df.index)))
		to_add=((hval*100)**2)
		hind+=to_add
	return(hind)
	
	
def hindex_by_msa(combined_df):
	msa_codes=set((combined_df['MSA_MD']).tolist())
	name=[]
	h_val=[]
	for code in msa_codes:
		if pd.isnull(code):
			continue
		filtered_df=combined_df[combined_df['MSA_MD']==code]
		descp=filtered_df['MSA_MD_Description']
		unique_descp=(descp.tolist())[0]
		name.append(unique_descp)
		h_val.append(hindex_ret(filtered_df))
	y_pos = np.arange(len(name))
	print("\n\n",h_val,"\n\n")
	print("\n\n",name,"\n\n")
	# Ordering the values as per index
	mix=zip(h_val,name)
	sorted_mix=sorted(mix)
	h_val=[val[0] for val in sorted_mix]
	name=[val[1] for val in sorted_mix]
	plt.barh(y_pos,h_val ,align='center')
	for i, v in enumerate(h_val):
		plt.text(v , i, str(name[h_val.index(v)]), color='blue', fontweight='bold') 
	plt.show()
	
def hindex_by_state(combined_df):
	state_vals=set((combined_df['State']).tolist())
	name=[]
	h_val=[]
	for code in state_vals:
		if pd.isnull(code):
			continue
		filtered_df=combined_df[combined_df['State']==code]
		name.append(code)
		h_val.append(hindex_ret(filtered_df))
	y_pos = np.arange(len(name))
	print("\n\n",h_val,"\n\n")
	print("\n\n",name,"\n\n")
	# Ordering the values as per index
	mix=zip(h_val,name)
	sorted_mix=sorted(mix)
	h_val=[val[0] for val in sorted_mix]
	name=[val[1] for val in sorted_mix]
	plt.barh(y_pos,h_val ,align='center')
	for i, v in enumerate(h_val):
		plt.text(v , i, str(name[h_val.index(v)]), color='blue', fontweight='bold') 
	plt.show()
	
def top_lender_counts(Top_Parents,title,year_type):
	values=(Top_Parents['count']).tolist()
	top_lenders=(Top_Parents['Parent_Name_TS']).tolist()
	y_pos = np.arange(len(top_lenders))
	plt.barh(y_pos,values ,align='center')
	for i, v in enumerate(values):
		if year_type=='all':
			plt.text(v - 7000, i, str(top_lenders[values.index(v)]), color='blue', fontweight='bold')
		elif year_type=='2012':
			plt.text(v - 4000, i, str(top_lenders[values.index(v)]), color='blue', fontweight='bold')
		elif year_type=='2013':
			plt.text(v - 2000, i, str(top_lenders[values.index(v)]), color='blue', fontweight='bold')
		else:
			plt.text(v - 500, i, str(top_lenders[values.index(v)]), color='blue', fontweight='bold')
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Bank Names')
	plt.xlabel('Count of Loans')
	plt.title(title)
	plt.show()

def merge_df(loans_df,ins_df):
	combined_df=loans_df.merge(ins_df,on=['Respondent_ID','Agency_Code','As_of_Year'],how='left')
	return(combined_df)

	
	
def main():
	#LOADING THE DATASETS
	loans_df=pd.read_csv('C:\\Users\\Deepthi Gopal\\Desktop\\2012_to_2014_loans_data.csv',dtype={
	'Agency_Code':str,
	'Applicant_Income_000':str,
	'As_of_Year':int,
	'Census_Tract_Number':str,
	'County_Code':str,
	'FFIEC_Median_Family_Income':str,
	'Loan_Amount_000':int,
	'MSA_MD':str,
	'Number_of_Owner_Occupied_Units':str,
	'Respondent_ID':str,
	'Sequence_Number':str,
	'State_Code':str,
	'Tract_to_MSA_MD_Income_Pct':str,
	'MSA_MD_Description':str,
	'Loan_Purpose_Description':str,
	'Agency_Code_Description':str,
	'Lien_Status_Description':str,
	'Loan_Type_Description':str,
	'State':str,
	'County_Name':str,
	'Conforming_Limit_000':np.float64,
	'Conventional_Status':str,
	'Conforming_Status':str,
	'Conventional_Conforming_Flag':str
	},na_values=['NA ', 'NA ', 'NA ', 'NA  ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '','NA   ','NA      '])

	#institutiondata
	ins_df=pd.read_csv('C:\\Users\\Deepthi Gopal\\Desktop\\2012_to_2014_institutions_data.csv',dtype={
	'As_of_Year':int,
	'Respondent_ID':str,
	'Agency_Code':str,
	'Respondent_Name_TS':str,
	'Respondent_City_TS':str,
	'Respondent_State_TS':str,
	'Respondent_ZIP_Code':str,
	'Parent_Name_TS':str,
	'Parent_City_TS':str,
	'Parent_State_TS':str,
	'Parent_ZIP_Code':str,
	'Assets_000_Panel':np.int64},na_values=['NA ', 'NA ', 'NA ', 'NA  ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '','NA   ','NA      '])

	# Merging the two data frames
	combined_df=merge_df(loans_df,ins_df)
	
    # Completing parent names
	combined_df['Parent_Name_TS']=combined_df.apply(lambda row: complete_parent_names(row),axis=1)
    
	#Create a new applicant income with NA values equal to -5
	combined_df=filter_app_income(combined_df)
	
    
	# Separate by years
	combined_df_2012=combined_df[combined_df['As_of_Year']==2012]
	combined_df_2013=combined_df[combined_df['As_of_Year']==2013]
	combined_df_2014=combined_df[combined_df['As_of_Year']==2014]
	
	# Displaying year wise stacked chart
	displayed_stacked_chart_2(combined_df,'Division of Money during Year: 2012-2014')
	displayed_stacked_chart_2(combined_df_2012,'Division of Money during Year: 2012')
	displayed_stacked_chart_2(combined_df_2013,'Division of Money during Year: 2013')
	displayed_stacked_chart_2(combined_df_2014,'Division of Money during Year: 2014')
	
	# Top lender analysis---
	# Finding top parents
	Largest_lender=combined_df.groupby(['Parent_Name_TS']).size().reset_index().rename(columns={0:'count'})
	Top_Parents=Largest_lender.sort_values(['count'], ascending=0).head(10)
	
	Largest_lender=combined_df_2012.groupby(['Parent_Name_TS']).size().reset_index().rename(columns={0:'count'})
	Top_Parents_2012=Largest_lender.sort_values(['count'], ascending=0).head(10)
	
	Largest_lender=combined_df_2013.groupby(['Parent_Name_TS']).size().reset_index().rename(columns={0:'count'})
	Top_Parents_2013=Largest_lender.sort_values(['count'], ascending=0).head(10)
	
	Largest_lender=combined_df_2014.groupby(['Parent_Name_TS']).size().reset_index().rename(columns={0:'count'})
	Top_Parents_2014=Largest_lender.sort_values(['count'], ascending=0).head(10)
	
	# Bar chart of top lenders and counts
	top_lender_counts(Top_Parents,'Top 10 lenders of 2012-2014','all')
	top_lender_counts(Top_Parents_2012,'Top 10 lenders of 2012','2012')
	top_lender_counts(Top_Parents_2013,'Top 10 lenders of 2013','2013')
	top_lender_counts(Top_Parents_2014,'Top 10 lenders of 2014','2014')
	
	
	# Bar chart of purchase vs refinancing  for top lenders
	pur_vs_ref(Top_Parents,combined_df)
	
	# Bar chart of Conventional_Conforming for top lenders
	conventional_conforming_yes_vs_no(Top_Parents,combined_df)
	
	# Bar chart of conforming status for top lenders
	conforming_status_top_lenders(Top_Parents,combined_df)
	
	# Bar chart of Loan type description for top lenders
	loan_type_top_lenders(Top_Parents,combined_df)
	
	# print H index all
	hindex(combined_df)
	# print H index comparison of MSA MD
	hindex_by_msa(combined_df)
	# print H index comparison of states
	hindex_by_state(combined_df)
	# #############################################
	
	#Viz market size by year and state 
	Market_size = combined_df.groupby(['As_of_Year', 'State'])
	(((Market_size.count())['Sequence_Number']).unstack()).plot(kind='bar', stacked=False)#bar
	state_market = Market_size.size().reset_index().rename(columns={0:'count'})
	print(state_market[(state_market['State'] =='DC') | (state_market['State']=='VA')])#print
	plt.title('Market Size by Year and State')
	plt.xlabel('Year')
	plt.ylabel('Number Of Applicants')
	plt.show()
	
	#Market based on year (sum of loan amount and number of applicants)
	year= loans_df.groupby(['As_of_Year'])
	print(year[['Sequence_Number']].count())#print 
	year[['Sequence_Number']].count().plot(kind='line') #bar
	print(year[['Loan_Amount_000']].sum()) #print
	plt.title('Loan Volume')
	plt.xlabel('Years')
	plt.ylabel('Number of Loans')
	plt.show()

	#Over all Market share for largest banks based on Asset value. Assuming asset value >200m to be a large bank.
	Largest_bank= (combined_df['Respondent_Name_TS'][combined_df['Assets_000_Panel']>=200000000]).unique()
	Overall_market_share_largest_banks= combined_df[combined_df['Assets_000_Panel']>=200000000].groupby(['State', 'As_of_Year'])
	print(Overall_market_share_largest_banks.count()['Sequence_Number'].unstack()) #print
	Overall_market_share_largest_banks.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Overall Market Share for Large Banks')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()

	#Over all Market shere for smallest banks based on Asset value. Assuming asset value <200m to be a large bank.
	Small_banks= (combined_df['Respondent_Name_TS'][combined_df['Assets_000_Panel']<200000000]).unique()
	Overall_market_share_Small_banks= combined_df[combined_df['Assets_000_Panel']<200000000].groupby(['State', 'As_of_Year'])
	print(Overall_market_share_Small_banks.count()['Sequence_Number'].unstack())#print
	Overall_market_share_Small_banks.count()['Sequence_Number'].unstack().plot(kind='bar')#bar
	plt.title('Overall Market Share for Small Banks')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()

	#Loan_purpose Lender     
	Loan_purpose=combined_df.groupby(['Loan_Purpose_Description', 'Parent_Name_TS']).size().reset_index().rename(columns={0:'count'})
	Loan_purpose_Refinance  = Loan_purpose[Loan_purpose['Loan_Purpose_Description'] =='Refinance']
	Loan_purpose_Refinance_sort=Loan_purpose_Refinance.sort_values(['count'], ascending=0).head(5) #print
	Loan_purpose_Refinance_sort=Loan_purpose_Refinance.sort_values(['count'], ascending=0).head(5) #print
	print(Loan_purpose_Refinance_sort)

	Loan_purpose_Purchase  = Loan_purpose[Loan_purpose['Loan_Purpose_Description'] =='Purchase']
	Loan_purpose_Purchase_sort=Loan_purpose_Purchase.sort_values(['count'], ascending=0).head(5) #print
	print(Loan_purpose_Purchase_sort) #print

	#Refinance Vs Purchase based on year 
	Loan_purpose=combined_df.groupby(['Loan_Purpose_Description', 'As_of_Year'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar')  #bar  
	plt.title('Refinance Vs Purchase based on year')
	plt.xlabel('Year')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Refinance Vs Purchase based on state
	Loan_purpose=combined_df.groupby([ 'State', 'Loan_Purpose_Description'])
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Refinance Vs Purchase based on state')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Refinance Vs Purchase based on state and year
	Loan_purpose=combined_df.groupby(['Loan_Purpose_Description', 'State', 'As_of_Year', 'Loan_Purpose_Description', ])
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Refinance Vs Purchase based on state and year')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Loan type description based on state
	Loan_purpose=combined_df.groupby([ 'State', 'Loan_Type_Description'])
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') 
	plt.title('Loan Type Based on State')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Loan type description based on Year
	Loan_purpose=combined_df.groupby([ 'As_of_Year', 'Loan_Type_Description'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Loan Type Based on Year')
	plt.xlabel('Year')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Coventional Conforming Loans based on year
	Loan_purpose=combined_df.groupby([ 'As_of_Year', 'Conventional_Conforming_Flag'])
	print(Loan_purpose.count()['Sequence_Number'].unstack())#print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Coventional Conforming Loans based on year')
	plt.xlabel('Year')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Coventional Conforming Loans based on state
	Loan_purpose=combined_df.groupby([ 'State', 'Conventional_Conforming_Flag'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Coventional Conforming Loans based on State')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()

	#Conforming vs Jumbo Loans based on state
	Loan_purpose=combined_df.groupby([ 'State', 'Conforming_Status'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Conforming vs Jumbo Loans based on state')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Conforming vs Jumbo Loans based on year
	Loan_purpose=combined_df.groupby([ 'As_of_Year', 'Conforming_Status'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Conforming vs Jumbo Loans based on year')
	plt.xlabel('Year')
	plt.ylabel('Number of Loans')
	plt.show()

	#Lien Status based on state
	Loan_purpose=combined_df.groupby([ 'State', 'Lien_Status_Description'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Lien Status based on state')
	plt.xlabel('State')
	plt.ylabel('Number of Loans')
	plt.show()
	
	#Lien Status based on year
	Loan_purpose=combined_df.groupby([ 'As_of_Year', 'Lien_Status_Description'])
	print(Loan_purpose.count()['Sequence_Number'].unstack()) #print
	Loan_purpose.count()['Sequence_Number'].unstack().plot(kind='bar') #bar
	plt.title('Lien Status based on year')
	plt.xlabel('Year')
	plt.ylabel('Number of Loans')
	plt.show()

	#Top 10 Institution based on Year
	Largest_lender=combined_df.groupby(['Respondent_Name_TS', 'As_of_Year']).size().reset_index().rename(columns={0:'count'})
	Top_Institution=Largest_lender.sort_values(['count'], ascending=0).head(10) #print
	print(Top_Institution)
	
	
	# #############################################
if __name__=="__main__":
	main()