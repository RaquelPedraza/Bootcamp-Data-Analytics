-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema abc
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema abc_corporation
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema abc_corporation
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `abc_corporation` DEFAULT CHARACTER SET utf8 ;
USE `abc_corporation` ;

-- -----------------------------------------------------
-- Table `abc_corporation`.`employee_personal_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `abc_corporation`.`employee_personal_data` (
  `Employee_ID` INT NOT NULL AUTO_INCREMENT,
  `Date_Birth` INT NOT NULL,
  `Gender` VARCHAR(255) NOT NULL,
  `Marital_Status` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`Employee_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `abc_corporation`.`company_data`
-- -----------------------------------------------------
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
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `abc_corporation`.`employee_profile`
-- -----------------------------------------------------
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
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `abc_corporation`.`satisfaction_survey`
-- -----------------------------------------------------
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
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
