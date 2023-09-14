CREATE DATABASE address_book;

USE address_book;

CREATE TABLE contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    profile_picture_url VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(20),
    company VARCHAR(255),
    position VARCHAR(255),
    memo TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE label (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE contact_label (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contact_id INT,
    label_id INT,
    FOREIGN KEY (contact_id) REFERENCES contact(id),
    FOREIGN KEY (label_id) REFERENCES label(id)
);

CREATE TABLE additional_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contact_id INT,
    address VARCHAR(255),
    birthday DATE,
    website VARCHAR(255),
    FOREIGN KEY (contact_id) REFERENCES contact(id)
);
