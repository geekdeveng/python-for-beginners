USE address_book;

INSERT INTO label (name)
VALUES ('family'), ('friends'), ('company');

INSERT INTO contact (profile_picture_url, name, email, phone_number, company, position, memo)
VALUES
    ('https://example.com/profile1.jpg', 'geek', 'geek@example.com', '123-456-7890', 'ABC Corp', 'Manager', 'This is a test contact 1.'),
    ('https://example.com/profile2.jpg', 'pink', 'pink@example.com', '987-654-3210', 'XYZ Inc', 'Director', 'This is a test contact 2.'),
    ('https://example.com/profile3.jpg', 'red', 'red@example.com', '555-555-5555', '123 Industries', 'Engineer', 'This is a test contact 3.');

INSERT INTO contact_label (contact_id, label_id)
VALUES (1, 1), (2, 2), (3, 3); 

INSERT INTO additional_info (contact_id, address, birthday, website)
VALUES
    (1, '123 Main St, City1, Country1', '1989-03-15', 'https://geek.com'),
    (2, '456 Elm St, City2, Country2', '1990-07-22', 'https://pink.com'),
    (3, '789 Oak St, City3, Country3', '1980-12-05', 'https://red.com');
