teachercourses_teacher= "SELECT teacher.name,teacher.phone,teacher_courses.course_id FROM teacher full JOIN teacher_courses on teacher_courses.teacher_id = teacher.id;"

teachercourses_courses= "SELECT teacher_courses.teacher_id,courses.course_name,courses.credits FROM teacher_courses full JOIN courses on courses.course_id = teacher_courses.course_id;"

teacher_courses = "select teacher.id, teacher.name, teacher.phone ,courses.credits,courses.course_name from teacher full join courses on teacher.course_name = courses.course_name;"
