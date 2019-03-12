# pandas is a
    # Python library 
    # providing high-performance, easy-to-use data structures and 
    # data analysis tools


# Pandas deals with the following three data structures −
    # Series
    # DataFrame
    # Panel
# These data structures are built on top of Numpy array, which means they are fast.

# Data Structure        Dimensions        Homo/hetro            value-mutable         size-mutable
 Series                    1            homogeneous array       Yes                    No
 Data Frames               2            hetro                   Yes                    Yes
 Panel                     3            hetro                   Yes                    yes

# All Pandas data structures are value mutable (can be changed)
# All pandas ds except Series all are size mutable. Series is size immutable.
____________________________________________________________________________
#pandas.Series
pandas.Series( data, index, dtype, copy)	# data source can be array, list, constant, dictionary

s = pd.Series()								# creates empty series
s = pd.Series(5, index=[0, 1, 2, 3])
											# 0  5
											# 1  5
											# 2  5
											# 3  5
											# dtype: int64
											
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print s['a']								# retrieve a single element
____________________________________________________________________________
# pandas.DataFrame
pandas.DataFrame( data, index, columns, dtype, copy)
											# data source can be lists,dict,series,numpy ndarrays, another dataframe
											# index - For the row labels, the Index to be used for the resulting frame is Optional 
											# 		   Default np.arrange(n) if no index is passed.
											# columns- For column labels, the optional default syntax is - np.arrange(n). 
											#	This is only true if no index is passed.
											# dtype - Data type of each column.
											# copy - used for copying of data, if the default is False.
											
df = pd.DataFrame()							# empty dataframe

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
														 Age    Name
												rank1    28      Tom
												rank2    34     Jack
												rank3    29    Steve
												rank4    42    Ricky

# column selection, addition, and deletion
df['Name']													# selection
df['Sex']=pd.Series(['m','f', 'm'],index=['a','b','c'])		# column addition
del df['Name']												# column deletion

# Row Selection, Addition, and Deletion
print df.loc['b'] 											# Rows can be selected by passing row label to a loc function.
print df.iloc[2]											# Rows can be selected by passing integer location to an iloc function.
print df[2:4]												# slice rows
df = df.append(df2)											# row addition
df = df.drop(0)												# row deletion
____________________________________________________________________________
# pandas.panel

pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
		# data	Data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame
		# items	axis=0
		# major_axis	axis=1
		# minor_axis	axis=2
		# dtype	Data type of each column
		# copy	Copy data. Default, false

pd.Panel() 													# empty Panel
____________________________________________________________________________
# Basic Functionality	
T						# Transposes rows and columns.
axes 					# Returns a list with the row axis labels and column axis labels as the only members.
dtypes 					# Returns the dtypes in this object.
empty 					# True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.	
ndim 					# Number of axes / array dimensions.
shape 					# Returns a tuple representing the dimensionality of the DataFrame.
size 					# Number of elements in the NDFrame.
values 					# Numpy representation of NDFrame.
head() 					# Returns the first n rows.
tail()					# Returns last n rows
____________________________________________________________________________
# statistics
count()		Number of non-null observations
sum()		Sum of values
mean()		Mean of Values
median()	Median of Values
mode()		Mode of values
std()		Standard Deviation of the Values
min()		Minimum Value
max()		Maximum Value
abs()		Absolute Value
prod()		Product of Values
cumsum()	Cumulative Sum
cumprod()	Cumulative Product
____________________________________________________________________________
# Function Application
To apply your own or another library’s functions to Pandas objects, you should be aware of the three important methods.
Custom operations can be performed by passing the function and the appropriate number of parameters

pipe() 		# Table wise Function Application
apply()		# Row or Column Wise Function Application
applymap()  # Element wise Function Application

def adder(ele1,ele2):
   return ele1+ele2
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
____________________________________________________________________________
#pandas IO tools
read_csv() and read_table()
# They both use the same parsing code to intelligently convert tabular data into a DataFrame object

pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',

df = pd.read_csv("temp.csv")
df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})			# change data type for salary column
df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e']) 			# gives header names

# If the header is in a row other than the first, pass the row number to header. This will skip the preceding rows.
import pandas as pd 
df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
print df

# skiprows skips the number of rows specified.
df=pd.read_csv("temp.csv", skiprows=2)
____________________________________________________________________________
# Visualization
This functionality on Series and DataFrame is just a simple wrapper around the matplotlib libraries plot() method.

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))
df.plot()

# These methods can be provided as the kind keyword argument to plot(). These include −
	'bar' or barh for bar plots
	'hist' for histogram
	'box' for boxplot
	'area' for area plots
	'scatter' for scatter plots
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d')
df.plot.bar()

df.diff.hist(bins=20)
df.plot.barh(stacked=True)
df.plot.scatter(x='a', y='b')
df.plot.pie(subplots=True)
