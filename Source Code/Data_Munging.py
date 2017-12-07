import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

# Providing API of required two functions along with additional functions for reporting

class HMDA_API:
	loans_dtype={
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
	}
	ins_dtype={
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
	'Assets_000_Panel':np.int64}

	def replaceNA(self,x):
		na_values=['NA ', 'NA ', 'NA ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', '', 'NA  ']
		#if x in na_values:
		if pd.isnull(x):
			return(-5)
		else:
			return(x)
		
	def filter_app_income(self):
		self.combined_df['Applicant_Income_000'] =self.combined_df['Applicant_Income_000'].apply(self.replaceNA)

	def make_loan_buckets(self):
		buckets=[0,100,250,500,1000,100000]
		bucket_names=['(0-100k)','(101-250k)','(251-500k)','(501-1000k)','(>1000k)']
		self.combined_df['loan_bucket']=pd.cut(self.combined_df['Loan_Amount_000'],buckets,labels=bucket_names)
	
	def display_loan_buckets(self):
		# Grouping by loan bucket
		buckets=[0,100,250,500,1000,100000]
		bucket_names=['(0-100k)','(101-250k)','(251-500k)','(501-1000k)','(>1000k)']
		new_attribute=self.combined_df.groupby(['loan_bucket'])
		values=((new_attribute[['Loan_Amount_000']]).count()).values
		y_pos = np.arange(len(bucket_names))
		plt.bar(y_pos,values ,align='center')
		plt.xticks(y_pos, bucket_names)
		plt.ylabel('Loan Amount Count')
		plt.xlabel('Range of Loans Amounts')
		plt.title('Division of Loan Amounts')
		plt.show()

	def make_income_buckets(self):
		#print("# of NA values= \t",len((combined_df[combined_df['Applicant_Income_000']==-5]).index))
		buckets=[-10,0,10,25,50,100,250,10000]
		bucket_names=['NA','(0-10k)','(11-25k)','(25-50k)','(50-100k)','(100-250k)','(>250k)']
		self.combined_df['income']=pd.cut(self.combined_df['Applicant_Income_000'].astype(int),buckets,labels=bucket_names)
		
	def display_income_buckets(self):
		# Grouping by applicant income
		buckets=[-10,0,10,25,50,100,250,10000]
		bucket_names=['NA','(0-10k)','(11-25k)','(25-50k)','(50-100k)','(100-250k)','(>250k)']
		new_attribute=self.combined_df.groupby(['income'])
		values=((new_attribute[['Applicant_Income_000']]).count()).values
		y_pos = np.arange(len(bucket_names))
		plt.bar(y_pos,values ,align='center')
		plt.xticks(y_pos, bucket_names)
		plt.ylabel('Applicant Income Count')
		plt.xlabel('Range of Applicant Income')
		plt.title('Division of Applicant Income')
		plt.show()

	def displayed_stacked_chart_1(self):
		# Grouping by first Loan Amount Second applicant income
		new_attribute=self.combined_df.groupby(['loan_bucket','income'])
		values=((new_attribute[['Applicant_Income_000']]).count()).values
		print('\n\n',values,'\n\n')
		arranged_values=np.reshape(values,(5,7))
		print('\n\n',arranged_values,'\n\n')
		#arranged_values=np.transpose(arranged_values)
		
		# create plot
		fig, ax = plt.subplots()
		index = np.arange(7)
		bar_width = 0.1
		opacity = 0.8
		
		#Plot 1
		rects1 = plt.bar(index, arranged_values[0,:], bar_width,alpha=opacity,color='b',label='Loan_Amount(0-100k)')
		#Plot 2
		rects2 = plt.bar(index+1*bar_width, arranged_values[1,:], bar_width,alpha=opacity,color='g',label='Loan_Amount(101-250k)')
		#Plot 3
		rects3 = plt.bar(index+2*bar_width, arranged_values[2,:], bar_width,alpha=opacity,color='r',label='Loan_Amount(251-500k)')
		#Plot 4
		rects4 = plt.bar(index+3*bar_width, arranged_values[3,:], bar_width,alpha=opacity,color='c',label='Loan_Amount(501-1000k)')
		#Plot 5
		rects5 = plt.bar(index+4*bar_width, arranged_values[4,:], bar_width,alpha=opacity,color='m',label='Loan_Amount(>1000k)')
		
		plt.ylabel('Loan Application Counts')
		plt.xlabel('Applicant Income Categories')
		plt.xticks(index + bar_width, ('(NA)','(0-10k)','(11-25k)','(25-50k)','(50-100k)','(100-250k)','(>250k)'))
		plt.title('Division of Money')
		plt.legend()
		plt.tight_layout()
		plt.show()

		
	def displayed_stacked_chart_2(self):
		# Grouping by first Loan Amount Second applicant income
		new_attribute=self.combined_df.groupby(['loan_bucket','income'])
		values=((new_attribute[['Applicant_Income_000']]).count()).values
		print('\n\n',values,'\n\n')
		arranged_values=np.reshape(values,(5,7))
		print('\n\n',arranged_values,'\n\n')
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
		plt.title('Division of Money')
		plt.legend()
		plt.tight_layout()
		plt.show()

	def merge_df(self):
		self.combined_df=self.loans_df.merge(self.ins_df,on=['Respondent_ID','Agency_Code','As_of_Year'],how='left')
	
	def __init__(self,loans_path,ins_path,json_path):
		self.loans_path=loans_path
		self.ins_path=ins_path
		self.json_path=json_path

	def hmda_init(self):
		# Loading the files
		self.loans_df=pd.read_csv(self.loans_path,dtype=HMDA_API.loans_dtype,na_values=['NA ', 'NA ', 'NA ', 'NA  ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''])
		self.ins_df=pd.read_csv(self.ins_path,dtype=HMDA_API.loans_dtype,na_values=['NA ', 'NA ', 'NA ', 'NA  ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''])
		# Merging the files
		self.merge_df()
		# Bucketing the Loan_Amount_000
		self.make_loan_buckets()
		
	
	def hmda_to_json(self,states=None,conventional_conforming=None):
		filtered_data=self.combined_df[self.combined_df['State'].isin(states) & self.combined_df['Conventional_Conforming_Flag'].isin(conventional_conforming)]
		filtered_data.to_json(path_or_buf=self.json_path,orient='records',double_precision=10)

def main():
	#Defining Paths to files
	loans_path='C:\\Users\\Deepthi Gopal\\Desktop\\2012_to_2014_loans_data.csv'
	ins_path='C:\\Users\\Deepthi Gopal\\Desktop\\2012_to_2014_institutions_data.csv'
	json_path='C:\\Users\\Deepthi Gopal\\Desktop\\output.json'
	
	# Creating an Object of the HMDA API
	obj=HMDA_API(loans_path,ins_path,json_path)
	
	# Merging the two data frames and bucketing Loan_Anount_000	
	obj.hmda_init()
	# Filtering data frame and storing as json file in PWD
	obj.hmda_to_json(['VA'],['N'])
	
	#  -----------------END OF DATA MUNGING ------------------
	# THE FOLLOWING FUNCTIONAL EXECUTIONS ARE FOR VISUALIZATION PURPOSES.
	# FEEL FREE TO COMMENT OUT THE CODE
	
	#Create a new applicant income with NA values equal to -5
	obj.filter_app_income()
	
	# Bucket the Applicant_Income_000
	obj.make_income_buckets()
	
	# Display Loan Amount buckets
	obj.display_loan_buckets()
	
	# Display Applicant Income buckets
	obj.display_income_buckets()
	
	# Display the Stacked Bar chart of Applicant Income filtered by Loan Amount
	obj.displayed_stacked_chart_1()
	
	# Display the Stacked Bar chart of Loan Amount filtered by Applicant Income
	obj.displayed_stacked_chart_2()
	

if __name__=="__main__":
	main()
	



