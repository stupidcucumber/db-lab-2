CREATE TABLE users (
    telegram_id INT NOT NULL,
    username VARCHAR(32),
    about TEXT,

    PRIMARY KEY (telegram_id)
);

CREATE TABLE groups (
    group_id SERIAL PRIMARY KEY,
    admin_id INT NOT NULL,

    FOREIGN KEY (admin_id)
        REFERENCES users(telegram_id)
);

CREATE TABLE members (
    entry_id SERIAL PRIMARY KEY,
    group_id INT NOT NULL,
    recipient_id INT NOT NULL,
    santa_id INT,
    desired TEXT,

    FOREIGN KEY (group_id)
        REFERENCES groups(group_id),
    FOREIGN KEY (recipient_id)
        REFERENCES users(telegram_id),
    FOREIGN KEY (santa_id)
        REFERENCES users(telegram_id)
);