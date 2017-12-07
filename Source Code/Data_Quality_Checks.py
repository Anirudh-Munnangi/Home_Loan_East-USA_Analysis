import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

def replaceNA(x):
	na_values=['NA', 'NA  ', 'NA ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '','NA      ']
	#if x in na_values:
	if pd.isnull(x):
		return(-5)
	else:
		return(x)

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
	},na_values=['NA', 'NA  ', 'NA ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '','NA      '])

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
	'Assets_000_Panel':np.int64},na_values=['NA', 'NA  ', 'NA ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '','NA      '])

	#MERGING the datasets
	combined_df=loans_df.merge(ins_df,on=['Respondent_ID','Agency_Code','As_of_Year'],how='left')

	# Respondent_Name_TS: NA values
	ins_df['na_of_respondent_name']=ins_df['Respondent_Name_TS'].apply(replaceNA)
	print('NAs in Respondent_Name_TS:\t',len((ins_df[ins_df['na_of_respondent_name']==-5]).index))
   # Parent_Name_TS: NA values
	ins_df['na_of_parent_name']=ins_df['Parent_Name_TS'].apply(replaceNA)
	print('NAs in Parent_Name_TS:\t',len((ins_df[ins_df['na_of_parent_name']==-5]).index))
	# Applicant_Income_000: NA values
	loans_df['na_of_applicant_income']=loans_df['Applicant_Income_000'].apply(replaceNA)
	print('NAs in Applicant_Income_000:\t',len((loans_df[loans_df['na_of_applicant_income']==-5]).index))
	# MSA_MD: NA values
	loans_df['na_of_msd_codes']=loans_df['MSA_MD'].apply(replaceNA)
	print('NAs in MSA_MD codes:\t',len((loans_df[loans_df['na_of_msd_codes']==-5]).index))
	# FFIEC_Median_Family_Income: NA values
	loans_df['na_of_ffiec']=loans_df['FFIEC_Median_Family_Income'].apply(replaceNA)
	print('NAs in FFIEC_Median_Family_Income:\t',len((loans_df[loans_df['na_of_ffiec']==-5]).index))
   # Conforming_Limit_000 : NA values
	loans_df['na_of_conforming']=loans_df['Conforming_Limit_000'].apply(replaceNA)
	print('NAs in Conforming_Limit_000:\t',len((loans_df[loans_df['na_of_conforming']==-5]).index))
	# Proof of repetition in Respondent_Name_TS
	print('Repeated Elements in Respondent_Name_TS:\t',len((ins_df['Respondent_Name_TS']).index)-len(set((ins_df['Respondent_Name_TS']).tolist())))
	# Count of Loans which are greater than 2500,000 ~2.5 million
	print('Count of Loan_Amount_000 > 2500:\t',len((loans_df[loans_df['Loan_Amount_000']>2500]).index))
	# Plot of Loan_Amount_000 VS Applicant_Income_000
	loan_values=(loans_df['Loan_Amount_000']).values
	income_values=(loans_df['Applicant_Income_000']).values
	plt.scatter(income_values,loan_values)
	plt.xlabel('Applicant Income values')
	plt.ylabel('Loan Amount values')
	plt.show()
	# Data quality checks 
	# Check:   Identifying if there is a mismatch and existence of duplicate records
	print('Unique count of Respondent ID:\t',combined_df['Respondent_ID'].nunique())
	print('Unique count of Respondent Name:\t',combined_df['Respondent_Name_TS'].nunique())
	# Check:   check for duplicate records in the passed institution dataframe
	ins_quality_check=ins_df.groupby(['Respondent_Name_TS','Respondent_ID', 'Agency_Code', 'As_of_Year']).size().reset_index().rename(columns={0:'count'})
	ins_quality_check[ins_quality_check['count']>1]
	print('Number of records in the combined data frame:\t',len((combined_df).index))
	# Check:   check for duplicate records in the passed loan dataframe
	loans_quality_check=loans_df.groupby(['Respondent_ID', 'Agency_Code', 'As_of_Year','Sequence_Number']).size().reset_index().rename(columns={0:'count'})
	loans_quality_check[loans_quality_check['count']>1]
	print('Number of records in the loans data frame:\t',len((loans_df).index))
	# Check:   checking for 1:1 mapping to identify duplicates in MSA_MD
	print('Unique count of MSA_MD:\t',combined_df['MSA_MD'].nunique())
	print('Unique count of MSA_MD_Description:\t',combined_df['MSA_MD_Description'].nunique())
	combined_df.groupby(['MSA_MD','MSA_MD_Description']).size().reset_index().rename(columns={0:'count'})

if __name__=="__main__":
	main()