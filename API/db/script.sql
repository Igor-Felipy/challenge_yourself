CREATE TABLE IF NOT EXISTS tb_profile(
    id INT(11) AUTO_INCREMENT NOT_NULL,
    profile_name VARCHAR(255) NOT_NULL,
    profile_description VARCHAR(255),
    email VARCHAR(255) NOT_NULL,
    pass VARCHAR(255) NOT_NULL,
    nick VARCHAR(255) NOT_NULL,
    active INT(1) NOT_NULL,
    image_link VARCHAR(300),
    born_date DATE,
    cell_phone VARCHAR(20),
    adrress VARCHAR(350),
    lang VARCHAR(5)
);

CREATE TABLE IF NOT EXISTS challenge (
    id INT(11) AUTO_INCREMENT NOT_NULL,
    title VARCHAR(255) NOT_NULL,
    answer VARCHAR(255) NOT_NULL,
    lang VARCHAR(5) NOT_NULL,
    active INT(1) NOT_NULL,
    PRIMARY KEY (id)
);
