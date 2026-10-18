DROP TABLE IF EXISTS activities;
CREATE TABLE IF NOT EXISTS activities(
    activity_id INTEGER PRIMARY KEY,
    activity_name TEXT,
    activity_type TEXT,
    participants INTEGER,
    fee REAL,
    duration_hours REAL
);

INSERT INTO activities(activity_id, activity_name, activity_type, participants, fee, duration_hours) VALUES
(1, 'Yoga', 'Fitness', 20, 300, 1.5),
(2, 'Dance', 'Fitness', 25, 400, 2),
(3, 'Painting', 'Art', 15, 250, 2),
(4, 'Music', 'Art', 18, 350, 1.5),
(5, 'Chess', 'Games', 12, 150, 1),
(6, 'Carrom', 'Games', 16, 100, 1),
(7, 'Zumba', 'Fitness', 30, 500, 1),
(8, 'Craft', 'Art', 10, 200, 2),
(9, 'Badminton', 'Sports', 22, 350, 2),
(10, 'Football', 'Sports', 28, 450, 2.5);
SELECT * FROM activities;
SELECT * FROM activities ORDER BY fee ASC;
SELECT activity_name, participants FROM activities WHERE participants>20;
SELECT activity_type, COUNT(*) AS total_activities FROM activities GROUP BY activity_type;
SELECT SUM(participants) AS total_participants FROM activities;
SELECT AVG(fee) AS average_fee FROM activities;
SELECT activity_type, SUM(participants) AS total_participants, AVG(fee) as average_fee FROM activities GROUP BY activity_type;
SELECT activity_type, SUM(participants) AS total_participants FROM activites GROUP BY activity_type HAVING SUM(participants)>40;
