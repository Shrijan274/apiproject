CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    address VARCHAR(255)
);
INSERT INTO Students (student_id, first_name, last_name, phone, address)
VALUES
  (1, 'abc', 'abc', '123', 'Hyd'),
  (2, 'def', 'def', '456', 'Delhi'),
  (3, 'xyz', 'xyz', '789', 'Mumbai');
select * from students


CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    credits INT NOT NULL
);
INSERT INTO Courses (course_id, course_name, credits)
VALUES
  (1, 'Mathematics', 3),
  (2, 'English', 3),
  (3, 'Computer Science', 4);
select * from courses;

CREATE TABLE teacher (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  phone VARCHAR(20)
);
INSERT INTO teacher (id, name, phone)
VALUES
  (1, 'teacher1', '1234567890'),
  (2, 'teacher2', '9876543210'),
  (3, 'teacher3', '5551234567');
select * from teacher;

CREATE TABLE teacher_courses (
  teacher_id INT,
  course_id INT,
  FOREIGN KEY (teacher_id) REFERENCES teacher(id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id),
  PRIMARY KEY (teacher_id, course_id)
);
INSERT INTO teacher_courses (teacher_id, course_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 2),
  (2, 3),
  (3, 1),
  (3, 3);
SELECT * FROM teacher_courses;