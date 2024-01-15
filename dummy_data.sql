-- Inserting dummy data into users table
INSERT INTO users (username, password, role, subscription_status, google_calendar_connected)
VALUES ('user1', 'password1', 'provider', 'active', true),
       ('user2', 'password2', 'seeker', 'inactive', false),
       ('user3', 'password3', 'provider', 'active', true),
       ('user4', 'password4', 'seeker', 'inactive', false),
       ('superadmin', 'superpassword', 'superadmin', 'active', true);

-- Inserting dummy data into bookings table
INSERT INTO bookings (provider_id, seeker_id, booking_type, booking_status, booking_fee, google_meet_link, google_maps_link)
VALUES (1, 2, 'online', 'confirmed', 100, 'meet.google.com/online-meeting', null),
       (1, 4, 'in-person', 'pending', 200, null, 'maps.google.com/in-person-location'),
       (3, 2, 'online', 'cancelled', 150, 'meet.google.com/another-online-meeting', null),
       (3, 4, 'in-person', 'confirmed', 250, null, 'maps.google.com/another-in-person-location');

-- Inserting dummy data into transactions table
INSERT INTO transactions (provider_id, seeker_id, booking_id, transaction_amount, transaction_status)
VALUES (1, 2, 1, 90, 'completed'),
       (1, 4, 2, 180, 'pending'),
       (3, 2, 3, 135, 'cancelled'),
       (3, 4, 4, 225, 'completed');

-- Inserting dummy data into reviews table
INSERT INTO reviews (booking_id, rating, review_text)
VALUES (1, 5, 'Great service!'),
       (2, 4, 'Good service, but could be better'),
       (4, 5, 'Excellent service!');