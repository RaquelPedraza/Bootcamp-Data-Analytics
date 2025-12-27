query_db_creation ="CREATE SCHEMA IF NOT EXISTS `abc_corporation` DEFAULT CHARACTER SET utf8 ;"

query_table_creation_employee_personal_data = """
                                            CREATE TABLE IF NOT EXISTS `abc_corporation`.`employee_personal_data` (
                                            `Employee_ID` INT NOT NULL AUTO_INCREMENT,
                                            `Date_Birth` INT NOT NULL,
                                            `Gender` VARCHAR(255) NOT NULL,
                                            `Marital_Status` VARCHAR(255) NOT NULL,
                                            PRIMARY KEY (`Employee_ID`))
                                            ENGINE = InnoDB
                                            DEFAULT CHARACTER SET = utf8mb3;"""

query_table_creation_employee_profile = """
                                        CREATE TABLE IF NOT EXISTS `abc_corporation`.`employee_profile` (
                                        `Employee_Profile_ID` INT NOT NULL AUTO_INCREMENT,
                                        `Education` INT NOT NULL,
                                        `Education_Field` VARCHAR(255) NOT NULL,
                                        `Training_Times_Last_Year` INT NOT NULL,
                                        `Num_Companies_Worked` INT NOT NULL,
                                        `Employee_ID` INT NOT NULL,
                                        PRIMARY KEY (`Employee_Profile_ID`, `Employee_ID`),
                                        INDEX `fk_Employee_Profile_Employee_Personal_Data1_idx` (`Employee_ID` ASC) VISIBLE,
                                        CONSTRAINT `fk_Employee_Profile_Employee_Personal_Data`
                                            FOREIGN KEY (`Employee_ID`)
                                            REFERENCES `abc_corporation`.`employee_personal_data` (`Employee_ID`))
                                        ENGINE = InnoDB
                                        DEFAULT CHARACTER SET = utf8mb3;"""

query_table_creation_company_data = """
                                    CREATE TABLE IF NOT EXISTS `abc_corporation`.`company_data` (
                                    `Company_Data_ID` INT NOT NULL AUTO_INCREMENT,
                                    `Employee_Number` VARCHAR(255) NOT NULL,
                                    `Job_Level` INT NOT NULL,
                                    `Job_Role` VARCHAR(255) NOT NULL,
                                    `Hourly_Rate` FLOAT NOT NULL,
                                    `Daily_Rate` FLOAT NOT NULL,
                                    `Monthly_Rate` FLOAT NOT NULL,
                                    `Monthly_Income` FLOAT NOT NULL,
                                    `Percent_Salary_Hike` INT NOT NULL,
                                    `Stock_Option_Level` INT NOT NULL,
                                    `Total_Working_Years` FLOAT NOT NULL,
                                    `Years_At_Company` INT NOT NULL,
                                    `Years_with_Curr_Manager` INT NOT NULL,
                                    `Years_Since_Last_Promotion` INT NOT NULL,
                                    `Distance_From_Home` INT NOT NULL,
                                    `Business_Travel` VARCHAR(255) NOT NULL,
                                    `Remote_Work` VARCHAR(255) NOT NULL,
                                    `Employee_ID` INT NOT NULL,
                                    PRIMARY KEY (`Company_Data_ID`, `Employee_ID`),
                                    INDEX `fk_Company_Data_Employee_Personal_Data_idx` (`Employee_ID` ASC) VISIBLE,
                                    CONSTRAINT `fk_Company_Data_Employee_Personal_Data`
                                        FOREIGN KEY (`Employee_ID`)
                                        REFERENCES `abc_corporation`.`employee_personal_data` (`Employee_ID`))
                                    ENGINE = InnoDB
                                    DEFAULT CHARACTER SET = utf8mb3;"""

query_table_creation_satisfaction_survey = """
                                        CREATE TABLE IF NOT EXISTS `abc_corporation`.`satisfaction_survey` (
                                        `Survey_ID` INT NOT NULL AUTO_INCREMENT,
                                        `Attrition` VARCHAR(255) NOT NULL,
                                        `Environment_Satisfaction` INT NOT NULL,
                                        `Job_Involvement` INT NOT NULL,
                                        `Job_Satisfaction` INT NOT NULL,
                                        `Over_Time` VARCHAR(255) NOT NULL,
                                        `Performance_Rating` FLOAT NOT NULL,
                                        `Relationship_Satisfaction` INT NOT NULL,
                                        `Work_Life_Balance` FLOAT NOT NULL,
                                        `Employee_ID` INT NOT NULL,
                                        PRIMARY KEY (`Survey_ID`, `Employee_ID`),
                                        INDEX `fk_Satisfaction_Survey_employee_personal_data1_idx` (`Employee_ID` ASC) VISIBLE,
                                        CONSTRAINT `fk_Satisfaction_Survey_employee_personal_data`
                                            FOREIGN KEY (`Employee_ID`)
                                            REFERENCES `abc_corporation`.`employee_personal_data` (`Employee_ID`)
                                            ON DELETE NO ACTION
                                            ON UPDATE NO ACTION)
                                        ENGINE = InnoDB;"""
                                        
query_insert_employee_personal_data = "INSERT INTO employee_personal_data (Date_Birth, Gender, Marital_Status) VALUES (%s,%s,%s)"
query_insert_employee_profile = "INSERT INTO employee_profile (Education, Education_Field, Training_Times_Last_Year,Num_Companies_Worked) VALUES (%s,%s,%s,%s)"
query_insert_company_data = "INSERT INTO company_data (Employee_Number, Job_Level, Job_Role,Hourly_Rate,Daily_Rate,Monthly_Rate,Monthly_Income,Percent_Salary_Hike,Stock_Option_Level,Total_Working_Years,Years_At_Company,Years_with_Curr_Manager,Years_Since_Last_Promotion,Distance_From_Home,Business_Travel,Remote_Work) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query_insert_satisfaction_survey = "INSERT INTO satisfaction_survey (Attrition, Environment_Satisfaction, Job_Involvement,Job_Satisfaction,Over_Time,Performance_Rating,Relationship_Satisfaction,Work_Life_Balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"