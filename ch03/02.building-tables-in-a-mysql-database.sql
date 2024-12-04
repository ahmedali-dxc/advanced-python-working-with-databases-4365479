CREATE TABLE projects (
    project_id INT(11) NOT NULL AUTO_INCREMENT,
    title VARCHAR(30),
    description VARCHAR(255),
    PRIMARY KEY(project_id)
);

show tables;

CREATE TABLE tasks (
    task_id INT(11) NOT NULL AUTO_INCREMENT,
    project_id INT(11) NOT NULL,
    description VARCHAR(255),
    PRIMARY KEY(task_id),
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

show tables;