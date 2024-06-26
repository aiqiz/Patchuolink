USE DEMO2_0;

CREATE TABLE node_info (
    node_ID INT PRIMARY KEY,
    lat_coord FLOAT,
    long_coord FLOAT,
    time_initialized TIME
);


CREATE TABLE history_update (
	ID INT PRIMARY KEY,
    update_time DATETIME,
    node_ID INT,
    soil_temp_0 FLOAT,
    soil_temp_10 FLOAT,
    soil_temp_20 FLOAT,
    soil_moisture_0 FLOAT,
    soil_moisture_10 FLOAT,
    soil_moisture_20 FLOAT,
    ph_0 FLOAT,
    ph_10 FLOAT,
    ph_20 FLOAT,
    light_intensity_0 FLOAT
);

SELECT * FROM node_info;

SELECT * FROM home_chatgptbot;
DROP TABLE node_info;
DROP TABLE history_update;
DROP TABLE data;

INSERT INTO node_info (node_ID, lat_coord, long_coord, time_initialized) VALUES
(1, 43.6426, -79.3871, '2024-01-01 12:00:00'),
(2, 43.6532, -79.3832, '2024-01-01 12:00:00'),
(3, 43.6677, -79.3948, '2024-01-01 12:00:00');

INSERT INTO node_info (node_ID, lat_coord, long_coord, time_initialized, last_update_time) VALUES
(5, 43.6426, -79.3871, '2024-01-01 12:00:00', NULL);


INSERT INTO history_update (ID, update_time, node_ID, soil_temp_0, soil_temp_10, soil_temp_20, soil_moisture_0, soil_moisture_10, soil_moisture_20, ph_0, ph_10, ph_20, light_intensity_0)
VALUES
('1', '2024-03-23 12:00:00', 1, 31.1827, 26.91355, 16.26971, 514.08631, 696.279, 582.37625, 7.0703, 5.97188, 7.91996, 35498.67268),
('2', '2024-03-23 12:00:00', 2, 24.15897, 22.4982, 17.3584, 503.4123, 635.1802, 655.3217, 4.705, 6.39215, 4.8612, 25001.5643),
('3', '2024-03-23 12:00:00', 3, 18.3497, 23.9872, 34.512, 625.123, 688.521, 503.412, 5.9872, 7.321, 6.812, 98512.3),
('4', '2024-03-23 15:00:00', 1, 29.5123, 24.1234, 30.9876, 552.321, 589.213, 521.789, 6.789, 4.321, 5.123, 60000.1234),
('5', '2024-03-23 15:00:00', 2, 20.5123, 29.9876, 25.3214, 500.123, 640.789, 589.321, 4.123, 7.789, 5.321, 12345.6789),
('6', '2024-03-23 15:00:00', 3, 33.9876, 25.7891, 21.3456, 670.789, 521.123, 600.321, 7.456, 6.789, 4.321, 98765.4321),
('7', '2024-03-23 18:00:00', 1, 28.1235, 20.9876, 22.4567, 520.123, 598.765, 542.321, 6.234, 5.678, 7.890, 43210.6789),
('8', '2024-03-23 18:00:00', 2, 31.7654, 22.5432, 19.8765, 505.678, 635.214, 580.321, 5.678, 7.123, 4.987, 56789.1234),
('9', '2024-03-23 18:00:00', 3, 24.3210, 28.7654, 33.2145, 610.321, 690.123, 555.678, 4.321, 6.234, 5.678, 23456.7890),
('10', '2024-03-23 21:00:00', 1, 29.6543, 27.8901, 24.3210, 540.987, 580.123, 569.234, 6.890, 5.123, 7.456, 34567.8901),
('11', '2024-03-23 21:00:00', 2, 22.9876, 25.4321, 26.7890, 510.321, 650.789, 590.123, 4.567, 7.890, 5.432, 45678.9012),
('12', '2024-03-23 21:00:00', 3, 35.2109, 23.6784, 20.5432, 680.123, 530.789, 610.456, 7.123, 6.456, 4.789, 56789.0123),
('13', '2024-03-24 00:00:00', 1, 28.1234, 22.5678, 23.8901, 550.321, 590.678, 570.123, 5.890, 5.678, 6.789, 37890.1234),
('14', '2024-03-24 00:00:00', 2, 21.7890, 26.3214, 27.6543, 515.789, 645.123, 585.678, 4.123, 7.234, 5.890, 48901.2345),
('15', '2024-03-24 00:00:00', 3, 33.4567, 24.1235, 22.7896, 675.234, 525.678, 605.123, 7.456, 6.123, 4.321, 59012.3456),
('16', '2024-03-24 03:00:00', 1, 27.8901, 23.4567, 24.6789, 530.456, 580.789, 560.234, 6.123, 5.789, 7.012, 40123.4567),
('17', '2024-03-24 03:00:00', 2, 20.1234, 27.8901, 28.4567, 505.123, 640.456, 580.789, 4.789, 7.012, 5.123, 51234.5678),
('18', '2024-03-24 03:00:00', 3, 34.7890, 25.0123, 21.3456, 680.789, 520.456, 600.123, 7.234, 6.789, 4.567, 62345.6789),
('19', '2024-03-24 06:00:00', 1, 26.5432, 24.7890, 25.1234, 540.123, 570.456, 550.789, 5.456, 4.123, 6.234, 73456.7890),
('20', '2024-03-24 06:00:00', 2, 23.4567, 28.1234, 29.7890, 510.789, 635.123, 595.456, 4.567, 7.789, 5.456, 84567.8901),
('21', '2024-03-24 06:00:00', 3, 32.1234, 26.7890, 23.4567, 665.321, 530.789, 615.678, 7.567, 6.234, 4.789, 95678.9012),
('22', '2024-03-24 09:00:00', 1, 28.6543, 23.8901, 26.3214, 545.987, 575.123, 565.234, 6.345, 5.678, 6.789, 36789.0123),
('23', '2024-03-24 09:00:00', 2, 22.1234, 27.4567, 30.7891, 510.321, 650.789, 585.123, 4.890, 7.321, 5.654, 47890.1234),
('24', '2024-03-24 09:00:00', 3, 31.7890, 25.2345, 22.6789, 670.123, 530.456, 605.789, 7.012, 6.345, 4.567, 58901.2345),
('25', '2024-03-24 12:00:00', 1, 27.8901, 22.3456, 23.1234, 535.678, 580.789, 560.321, 5.234, 4.789, 7.456, 69012.3456),
('26', '2024-03-24 12:00:00', 2, 21.4567, 26.7890, 28.1234, 505.789, 645.321, 575.678, 4.567, 7.890, 5.321, 70123.4567),
('27', '2024-03-24 12:00:00', 3, 32.6789, 24.8901, 21.4567, 680.456, 525.123, 600.789, 7.789, 6.567, 4.234, 81234.5678);



INSERT INTO history_update (ID, update_time, node_ID, soil_temp_0, soil_temp_10, soil_temp_20, soil_moisture_0, soil_moisture_10, soil_moisture_20, ph_0, ph_10, ph_20, light_intensity_0)
VALUES
('28', '2024-03-24 15:00:00', 1, 29.1234, 21.6789, 24.8901, 540.321, 570.456, 550.123, 6.456, 5.123, 6.789, 92345.6789),
('29', '2024-03-24 15:00:00', 2, 20.7890, 27.1234, 29.4567, 515.456, 640.123, 580.321, 4.123, 7.456, 5.678, 103456.789),
('30', '2024-03-24 15:00:00', 3, 33.4567, 26.0123, 22.3456, 675.789, 520.321, 605.456, 7.321, 6.789, 4.890, 114567.89),
('31', '2024-03-24 18:00:00', 1, 26.7890, 23.4567, 25.6789, 530.123, 565.789, 555.321, 5.789, 4.456, 6.123, 125678.901),
('32', '2024-03-24 18:00:00', 2, 23.8901, 28.2345, 30.5678, 510.678, 635.456, 595.123, 4.321, 7.678, 5.789, 136789.012),
('33', '2024-03-24 18:00:00', 3, 32.3456, 27.1234, 24.5678, 665.321, 530.123, 610.789, 7.456, 6.123, 4.321, 147890.123);


INSERT INTO history_update (ID, update_time, node_ID, soil_temp_0, soil_temp_10, soil_temp_20, soil_moisture_0, soil_moisture_10, soil_moisture_20, ph_0, ph_10, ph_20, light_intensity_0)
VALUES
('34', '2024-03-24 21:00:00', 1, 26.5432, 24.7890, 25.1234, 540.123, 570.456, 550.789, 5.456, 4.123, 6.234, 73456.7890),
('35', '2024-03-24 21:00:00', 2, 23.4567, 28.1234, 29.7890, 510.789, 635.123, 595.456, 4.567, 7.789, 5.456, 84567.8901),
('36', '2024-03-24 21:00:00', 3, 32.1234, 26.7890, 23.4567, 665.321, 530.789, 615.678, 7.567, 6.234, 4.789, 95678.9012);

INSERT INTO history_update (ID, update_time, node_ID, soil_temp_0, soil_temp_10, soil_temp_20, soil_moisture_0, soil_moisture_10, soil_moisture_20, ph_0, ph_10, ph_20, light_intensity_0)
VALUES
('37', '2024-03-25 00:00:00', 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
('48', '2024-03-25 00:00:00', 2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
('49', '2024-03-25 00::00', 3, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10);

INSERT INTO history_update (ID, update_time, node_ID, soil_temp_0, soil_temp_10, soil_temp_20, soil_moisture_0, soil_moisture_10, soil_moisture_20, ph_0, ph_10, ph_20, light_intensity_0)
VALUES
('34', '2024-03-24 21:00:00', 1, 26.5432, 24.7890, 25.1234, 540.123, 570.456, 550.789, 5.456, 4.123, 6.234, 73456.7890),
('35', '2024-03-24 21:00:00', 2, 23.4567, 28.1234, 29.7890, 510.789, 635.123, 595.456, 4.567, 7.789, 5.456, 84567.8901),
('36', '2024-03-24 21:00:00', 3, 32.1234, 26.7890, 23.4567, 665.321, 530.789, 615.678, 7.567, 6.234, 4.789, 95678.9012);

INSERT INTO testing (id, moisture_0)
VALUES
('1', '100');


USE DEMO1_0;
SELECT * FROM auth_user_user_permissions;

CREATE TABLE testing (
    id INT PRIMARY KEY,
	moisture_0 FLOAT
);

SELECT * FROM testing;

DROP TABLE chatgptbot;
CREATE TABLE home_chatgptbot (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    messageInput TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    CONSTRAINT chatgptbot_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES auth_user (id) ON DELETE CASCADE
);

TRUNCATE TABLE home_chatgptbot;
TRUNCATE TABLE history_update;

SELECT * FROM history_update;
SELECT * FROM home_chatgptbot;