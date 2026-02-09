CREATE TABLE IF NOT EXISTS players (

    player_id INT PRIMARY KEY,

    username VARCHAR(50) NOT NULL,

    email VARCHAR(100) NOT NULL,

    join_date DATE,

    country VARCHAR(50)

);



CREATE TABLE IF NOT EXISTS scores (

    score_id VARCHAR(36) PRIMARY KEY,

    player_id INT,

    game_name VARCHAR(100),

    score_value INT,

    session_date DATETIME,

    FOREIGN KEY (player_id) REFERENCES players(player_id)

);