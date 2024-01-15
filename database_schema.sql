CREATE DATABASE chatbot_platform;

USE chatbot_platform;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    UserName VARCHAR(255),
    Email VARCHAR(255),
    Password VARCHAR(255),
    Role ENUM('Seeker', 'Provider', 'SuperAdmin'),
    GoogleCalendarConnected BOOLEAN,
    PRIMARY KEY (UserID)
);

CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT,
    ProviderID INT,
    ServiceName VARCHAR(255),
    ServiceDescription TEXT,
    PRIMARY KEY (ServiceID),
    FOREIGN KEY (ProviderID) REFERENCES Users(UserID)
);

CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT,
    ServiceID INT,
    SeekerID INT,
    ProviderID INT,
    BookingType ENUM('Online', 'In-Person'),
    GoogleMeetLink VARCHAR(255),
    GoogleMapsLink VARCHAR(255),
    BookingTime DATETIME,
    PRIMARY KEY (BookingID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID),
    FOREIGN KEY (SeekerID) REFERENCES Users(UserID),
    FOREIGN KEY (ProviderID) REFERENCES Users(UserID)
);

CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT,
    BookingID INT,
    Amount DECIMAL(10,2),
    TransactionTime DATETIME,
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT,
    BookingID INT,
    Rating INT,
    ReviewText TEXT,
    PRIMARY KEY (ReviewID),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

CREATE TABLE Subscriptions (
    SubscriptionID INT AUTO_INCREMENT,
    ProviderID INT,
    StartDate DATE,
    EndDate DATE,
    PRIMARY KEY (SubscriptionID),
    FOREIGN KEY (ProviderID) REFERENCES Users(UserID)
);