USE cyofgkwuvz6mathq;

CREATE TABLE user(
    user_id   INT (11) NOT NULL AUTO_INCREMENT,
    name  VARCHAR (30) NOT NULL,
    nick  VARCHAR (30) NOT NULL,
    rank  VARCHAR (11) NOT NULL,
    primary_role enum('AWP', 'Rifler', 'Lurker', 'Entry Fragger', 'Support') NOT NULL,
    secondary_role enum('AWP', 'Rifler', 'Lurker', 'Entry Fragger', 'Support') NOT NULL,
    
    CONSTRAINT USER_PK PRIMARY KEY ( user_id )
    
) ENGINE = InnoDB AUTO_INCREMENT = 1, DEFAULT CHARSET utf8;

CREATE TABLE statistic_kda(
    kda_id   INT (11) NOT NULL AUTO_INCREMENT,
    kda DECIMAL(4,2) NOT NULL,
    user_id   INT (11) NOT NULL,


    CONSTRAINT STATISTIC_KDA_PK PRIMARY KEY ( kda_id ),
    CONSTRAINT STATISTIC_KDA_UK UNIQUE (user_id), 

    CONSTRAINT  STATISTIC_KDA_USER_FK  FOREIGN KEY ( user_id )
        REFERENCES  user ( user_id )

) ENGINE = InnoDB AUTO_INCREMENT = 1, DEFAULT CHARSET utf8;

CREATE TABLE statistic_adr(
    adr_id   INT (11) NOT NULL AUTO_INCREMENT,
    adr DECIMAL(4,2) NOT NULL,
    user_id   INT (11) NOT NULL,


    CONSTRAINT STATISTIC_ADR_PK PRIMARY KEY ( adr_id ),
    CONSTRAINT STATISTIC_ADR_UK UNIQUE (user_id), 

    CONSTRAINT  STATISTIC_ADR_USER_FK  FOREIGN KEY ( user_id )
        REFERENCES  user ( user_id )

) ENGINE = InnoDB AUTO_INCREMENT = 1, DEFAULT CHARSET utf8;
