CREATE TABLE Students (
    studentId INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE Notifications (
    notificationId VARCHAR(50) PRIMARY KEY,
    studentId INT,
    type VARCHAR(50),
    message TEXT,
    isRead BOOLEAN DEFAULT FALSE,
    createdAt TIMESTAMP,
    FOREIGN KEY(studentId)
    REFERENCES Students(studentId)
);

CREATE INDEX idx_student_read_created
ON Notifications(studentId,isRead,createdAt);