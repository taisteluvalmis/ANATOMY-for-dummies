
-- Users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    role INTEGER
);

-- Courses
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    topic TEXT,
    created_at TIMESTAMP
);

-- Lessons
CREATE TABLE lessons (
    lesson_id SERIAL PRIMARY KEY,
    lesson_name TEXT,
    content TEXT,
    course_id INTEGER REFERENCES courses(course_id),
    lesson_order INTEGER
);

-- Users sign ups for lessons
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    course_id INTEGER REFERENCES courses(course_id)
);

-- Choices
CREATE TABLE choices (
    choice_id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses(course_id),
    choice_text TEXT
);

-- Answers for choices
CREATE TABLE answers (
    answer_id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices(choice_id),
    sent_at TIMESTAMP
);

-- Rewievs
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    course_id INTEGER REFERENCES courses(course_id),
    stars INTEGER,
    comment TEXT
);

