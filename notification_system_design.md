# Campus Notifications Microservice Design

## Stage 1: API Design

### Send Notification

POST /notifications

Request:

```json
{
  "studentId": 1042,
  "type": "Placement",
  "message": "TCS Recruitment Drive",
  "priority": "High"
}
```

Response:

```json
{
  "status": "success",
  "notificationId": "N1001"
}
```

### Fetch Notifications

GET /notifications/{studentId}

Response:

```json
[
  {
    "notificationId": "N1001",
    "type": "Placement",
    "message": "TCS Recruitment Drive",
    "isRead": false
  }
]
```

### Real-Time Delivery

* WebSockets for instant updates
* Fallback to polling
* Push notifications for mobile devices

---

## Stage 2: Database Design

### Choice

SQL Database (PostgreSQL)

Reason:

* Structured data
* ACID compliance
* Efficient indexing

### Tables

#### Students

| Column    | Type    |
| --------- | ------- |
| studentId | INT     |
| name      | VARCHAR |
| email     | VARCHAR |

#### Notifications

| Column         | Type      |
| -------------- | --------- |
| notificationId | UUID      |
| studentId      | INT       |
| type           | VARCHAR   |
| message        | TEXT      |
| isRead         | BOOLEAN   |
| createdAt      | TIMESTAMP |

### Scaling

* Read replicas
* Table partitioning
* Connection pooling

---

## Stage 3: Query Optimization

### Original Query

```sql
SELECT * FROM notifications
WHERE studentID = 1042
AND isRead = false
ORDER BY createdAt DESC;
```

### Problem

Without indexes:

* Full table scan
* Slow sorting
* High latency

### Solution

```sql
CREATE INDEX idx_student_read_created
ON notifications(studentID,isRead,createdAt DESC);
```

### Placement Notifications in Last 7 Days

```sql
SELECT *
FROM notifications
WHERE type='Placement'
AND createdAt >= NOW() - INTERVAL '7 days';
```

---

## Stage 4: Performance Improvements

### Issues

* Large notification volume
* Repeated database hits
* Slow loading

### Improvements

#### Caching

Use Redis

Benefits:

* Faster reads
* Reduced database load

#### Pagination

```http
GET /notifications?page=1&limit=20
```

#### Real-Time Updates

* WebSockets
* Server-Sent Events (SSE)

---

## Stage 5: Notify All Redesign

### Problems

Current approach:

```text
Loop through every student
Send notification synchronously
```

Issues:

* Slow execution
* Failure stops processing
* Not scalable

### Improved Design

1. API receives request
2. Store notification job
3. Push message to Queue
4. Worker services process queue
5. Retry failed messages

### Queue Options

* RabbitMQ
* Kafka
* AWS SQS

### Benefits

* High throughput
* Fault tolerance
* Horizontal scaling

---

## Stage 6: Priority Inbox

### Priority Rules

| Type      | Score |
| --------- | ----- |
| Placement | 100   |
| Result    | 80    |
| Event     | 50    |
| General   | 20    |

### Algorithm

1. Fetch notifications
2. Assign score
3. Sort by score
4. Return Top 10

### Sample Output

```json
[
  {
    "type":"Placement",
    "message":"Amazon Hiring Drive",
    "priority":100
  },
  {
    "type":"Result",
    "message":"Semester Results Published",
    "priority":80
  }
]
```

### Complexity

Sorting:

```text
O(n log n)
```

### Future Improvements

* ML-based prioritization
* Personalized ranking
* User preference learning

---

## Conclusion

The proposed Campus Notifications Microservice is scalable, fault-tolerant, and optimized for large student populations. It supports real-time delivery, efficient querying, queue-based processing, and priority-based notification ranking.
