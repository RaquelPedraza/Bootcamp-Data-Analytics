#%%
import functions as fun
import queries_db_creation as query
import db_acb_corporation as db
#%%
df_hr_raw = fun.read_file("../data/input/HR RAW DATA.csv")
print(df_hr_raw.head())
#%%
fun.explore_dataframe(df_hr_raw)
# %%
query.query_db_creation
query.query_table_creation_employee_profile
query.query_table_creation_employee_personal_data
query.query_table_creation_company_data
query.query_table_creation_satisfaction_survey
# %%
db.db_table_creation(query.query_db_creation,"AlumnaAdalab")
db.db_table_creation(query.query_table_creation_employee_personal_data,"AlumnaAdalab","abc_corporation")
db.db_table_creation(query.query_table_creation_employee_profile,"AlumnaAdalab","abc_corporation")
db.db_table_creation(query.query_table_creation_company_data,"AlumnaAdalab","abc_corporation")
db.db_table_creation(query.query_table_creation_satisfaction_survey,"AlumnaAdalab","abc_corporation")
# %%
df = fun.read_file("../data/output/df_imputada.csv")
df = fun.convert_int64_to_int(df)
#%%
datos_tabla_employee_personal = list(zip(df["DateBirth"].values,df["Gender"].values,df["MaritalStatus"].values))
datos_tabla_employee_profile = list(zip(df["Education"].values,df["EducationField"].values,df["TrainingTimesLastYear"].values,df["NumCompaniesWorked"].values))
datos_tabla_company_data = list(zip(df["EmployeeNumber"].values,df["JobLevel"].values,df["JobRole"].values,df["HourlyRate"].values,df["DailyRate"].values,df["MonthlyRate"].values,df["MonthlyIncome"].values,df["PercentSalaryHike"].values,df["StockOptionLevel"].values,df["TotalWorkingYears"].values,df["YearsAtCompany"].values,df["YearsWithCurrManager"].values,df["YearsSinceLastPromotion"].values,df["DistanceFromHome"].values,df["BusinessTravel"].values,df["RemoteWork"].values))
datos_tabla_satisfaction_survey = list(zip(df["Attrition"].values,df["EnvironmentSatisfaction"].values,df["JobInvolvement"].values,df["JobSatisfaction"].values,df["OverTime"].values,df["PerformanceRating"].values,df["RelationshipSatisfaction"].values,df["WorkLifeBalance"].values))
#%%
db.insert_data(query.query_insert_employee_personal_data,"AlumnaAdalab","abc_corporation", datos_tabla_employee_personal)
db.insert_data(query.query_insert_employee_profile,"AlumnaAdalab","abc_corporation", datos_tabla_employee_profile)
db.insert_data(query.query_insert_company_data,"AlumnaAdalab","abc_corporation", datos_tabla_company_data)
db.insert_data(query.query_insert_satisfaction_survey,"AlumnaAdalab","abc_corporation", datos_tabla_satisfaction_survey)
