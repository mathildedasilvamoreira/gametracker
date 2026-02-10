CREATE TABLE IF NOT EXISTS players (

    player_id INT PRIMARY KEY,

    username VARCHAR(50) NOT NULL,

    email VARCHAR(100),

    registration_date DATE,

    country VARCHAR(50),


    level INT 

);



CREATE TABLE IF NOT EXISTS scores (

    score_id VARCHAR(36) PRIMARY KEY,

    player_id INT,

    game VARCHAR(100),

    score INT,

    duration_minutes INT,

    played_at DATETIME,

    platform VARCHAR(50),

    FOREIGN KEY (player_id) REFERENCES players(player_id)

);