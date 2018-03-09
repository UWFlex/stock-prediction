CREATE DATABASE stock_training_data;
USE stock_training_data;

CREATE TABLE daily_adjusted (
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
	symbol VARCHAR(6) NOT NULL,
	timestamp DATE NOT NULL,
	open FLOAT(10,4) NOT NULL,
	high FLOAT(10,4) NOT NULL,
	low FLOAT(10,4) NOT NULL,
	close FLOAT(10,4) NOT NULL,
	adjusted_close FLOAT(10,4) NOT NULL,
	volume INT UNSIGNED NOT NULL,
	dividend_amount FLOAT(10,4) NOT NULL,
	split_coefficient FLOAT(10,4) NOT NULL, 
	PRIMARY KEY (id)
);

