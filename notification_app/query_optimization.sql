SELECT *
FROM Notifications
WHERE studentId = 1042
AND isRead = FALSE
ORDER BY createdAt DESC;

CREATE INDEX idx_student_read_created
ON Notifications(studentId,isRead,createdAt);

SELECT *
FROM Notifications
WHERE type='Placement'
AND createdAt >= NOW() - INTERVAL '7 DAYS';